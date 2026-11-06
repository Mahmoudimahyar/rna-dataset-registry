"""Inspect bounded primary-source files; publish metadata only, never raw rows.

Usage: python inspect_auxiliary.py --cache OUTSIDE_REPOSITORY --output audit.json
Requires requests; cache location is supplied by the caller.
"""
from pathlib import Path
import argparse, collections, concurrent.futures, csv, gzip, hashlib, io, json, sys, tarfile, zipfile
from urllib.parse import urlencode
import requests

sys.stdout.reconfigure(encoding='utf-8')
P=argparse.ArgumentParser(); P.add_argument('--cache',required=True); P.add_argument('--output',required=True); args=P.parse_args()
C=Path(args.cache); C.mkdir(parents=True,exist_ok=True)
DATE='2026-11-05'

def fetch(url,name,cap=120_000_000):
    dest=C/name
    if dest.exists():
        b=dest.read_bytes()
        return dest,dict(url=url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),checksum_scope='full cached response body downloaded earlier in this audit',download_complete=True,cache_reused=True)
    r=requests.get(url,timeout=(20,60),stream=True)
    info=dict(url=url,http_status=r.status_code,content_type=r.headers.get('Content-Type'),last_modified=r.headers.get('Last-Modified'))
    r.raise_for_status(); dest=C/name; n=0; h=hashlib.sha256()
    with dest.open('wb') as f:
        for chunk in r.iter_content(1<<18):
            n+=len(chunk)
            if n>cap: raise ValueError('Download exceeds explicit byte cap; no full-file checksum claimed')
            f.write(chunk); h.update(chunk)
    info.update(bytes=n,sha256=h.hexdigest(),checksum_scope='full response body',download_complete=True)
    return dest,info

def inspect_rnalocate(kind):
    u='https://www.rnalocate.org/static/download/'+requests.utils.quote(kind+' subcellular localization information.zip')
    path,info=fetch(u,'rnalocate_'+kind+'.zip')
    members=[]
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if name.endswith('/') or name.startswith('__MACOSX/'): continue
            with z.open(name) as f:
                txt=io.TextIOWrapper(f,encoding='utf-8-sig',errors='replace')
                header=txt.readline().rstrip('\r\n').split('\t')
                n=0; widths=collections.Counter(); missing=collections.Counter(); species=collections.Counter(); cellcol=[i for i,x in enumerate(header) if 'cell' in x.lower() or 'tissue' in x.lower()]
                cellvalues={header[i]:set() for i in cellcol}
                for line in txt:
                    if not line.strip(): continue
                    row=line.rstrip('\r\n').split('\t'); n+=1; widths[len(row)]+=1
                    for i,v in enumerate(row):
                        if not v or v.lower() in {'na','n/a','none','null','-'}: missing[header[i] if i<len(header) else str(i)]+=1
                    for i in cellcol:
                        if i<len(row): cellvalues[header[i]].add(row[i])
                    for i,x in enumerate(header):
                        if 'species' in x.lower() and i<len(row): species[row[i]]+=1
                members.append(dict(member=name,rows=n,header=header,row_width_counts=dict(widths),missing_or_sentinel_counts=dict(missing),species_counts=dict(species),cell_context_fields={k:dict(distinct_count=len(v),example_labels=sorted(v)[:30]) for k,v in cellvalues.items()}))
    return dict(resource_id='rnalocate',file_kind=kind,verification='full_selected_archive_parsed',file=info,members=members,interpretation='Localization annotation, not protein-output or translation-rate labels. Missing or coarse context cannot be silently assigned to reporter cells.',license='Official page permits noncommercial use with attribution; sources retain their own terms.')

def inspect_rnalocate_export():
    params=dict(dataset='Symbol',Keyword='ACTB',category='mRNA',species='Homo sapiens',subcellular_loc='All',page='1',score1='0.0',score2='1.0',sources='experiment',sortBy='None',last_id='',download='yes')
    u='https://www.rnalocate.org/show_search?'+urlencode(params)
    fp,fi=fetch(u,'rnalocate_ACTB_experiment.csv')
    reader=csv.DictReader(io.StringIO(fp.read_text(encoding='utf-8-sig'),newline=''))
    rows=[x for x in reader if x.get('RNA Symbol')]
    assert rows and 'Score' in reader.fieldnames
    numeric=[float(x['Score']) for x in rows]
    return dict(resource_id='rnalocate',verification='full_selected_query_csv_parsed',file=fi,columns=reader.fieldnames,query=params,selected_rows=len(rows),distinct_localizations=sorted({x['Localization'] for x in rows}),cell_or_tissue_labels=sorted({x['Tissue/Cell Line'] for x in rows}),missing_cell_or_tissue_rows=sum(not x['Tissue/Cell Line'] for x in rows),score_range=[min(numeric),max(numeric)],interpretation='Experimental-source localization annotations with computed confidence score, not measured translation. This targeted ACTB export is a schema/data sample; it does not verify the full database.',license='Official download page permits noncommercial use with attribution. Bulk mRNA/circRNA ZIP links returned404 in this audit.')

def inspect_rasp():
    mu='https://rasp2.zhanglab.net/api/query_bwfiles/?species=hg38'
    mp,mi=fetch(mu,'rasp_human_tracks.json')
    tracks=json.loads(mp.read_text())['bw_files']
    raw=[x for x in tracks if x.get('tracktype')=='raw' and x.get('cellline') in {'HepG2','HCT116','HEK293T','Huh7','U2OS','SH-SY5Y'}]
    if not raw: raw=[x for x in tracks if x.get('tracktype')=='raw' and x.get('cellline')=='HEK293']
    chosen=raw[0]; bed=chosen['bed_file_path'].strip()
    u='https://rasp2.zhanglab.net/api/downloadfile/?'+urlencode(dict(filetype='bed',filelist=bed))
    fp,fi=fetch(u,'rasp_selected.bed.gz')
    b=fp.read_bytes()
    if tarfile.is_tarfile(fp):
        with tarfile.open(fp) as t:
            members=[x for x in t.getmembers() if x.isfile()]; member=members[0].name; b=t.extractfile(members[0]).read()
    elif b[:2]==b'PK':
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            names=[x for x in z.namelist() if not x.endswith('/')]; member=names[0]; b=z.read(member)
    else: member=None
    stream=gzip.GzipFile(fileobj=io.BytesIO(b)) if b[:2]==b'\x1f\x8b' else io.BytesIO(b)
    widths=collections.Counter(); n=0; headers=[]; numeric=0; valid_coords=0
    for line in io.TextIOWrapper(stream,encoding='utf-8',errors='strict'):
        if line.startswith(('#','track','browser')): headers.append(line[:200]); continue
        if not line.strip(): continue
        row=line.rstrip('\r\n').split('\t'); n+=1; widths[len(row)]+=1
        if len(row)>4:
            try: float(row[4]); numeric+=1
            except ValueError: pass
        if len(row)>=3:
            try:
                if int(row[2])>int(row[1]): valid_coords+=1
            except ValueError: pass
    assert n>0 and widths=={6:n} and numeric==n and valid_coords==n, 'Selected file did not validate as six-column numerical BED'
    return dict(resource_id='rasp2',verification='full_selected_structure_track_parsed',metadata_file=mi,human_metadata_tracks=len(tracks),human_raw_tracks=sum(x.get('tracktype')=='raw' for x in tracks),human_imputed_tracks=sum(x.get('tracktype')=='imputed' for x in tracks),selected_track=chosen,file=fi,archive_member=member,selected_track_rows=n,row_width_counts=dict(widths),numeric_fifth_column_rows=numeric,valid_coordinate_rows=valid_coords,header_lines=headers,schema=['chromosome','start','end','name_placeholder','reactivity','strand'],interpretation='Raw chemical-probing signal is structure evidence. Cell identity and condition are source-specific; no synthetic reporter sequence/output pairing established.')

def inspect_cellosaurus():
    ids=['CVCL_1058','CVCL_0023','CVCL_0139','CVCL_0291','CVCL_0027','CVCL_0065','CVCL_0367','CVCL_0019','CVCL_0006','CVCL_0022','CVCL_0336','CVCL_0045','CVCL_0063','CVCL_2478','CVCL_0042','CVCL_0470','CVCL_0188','CVCL_0493']
    entries=[]
    for ac in ids:
        u='https://api.cellosaurus.org/cell-line/'+ac+'?fields=id,sy,ac,ox,dr,hi,problematic,caution&format=json'
        path,info=fetch(u,'cellosaurus_'+ac+'.json',cap=2_000_000)
        obj=json.loads(path.read_text())['Cellosaurus']['cell-line-list']
        for line in obj:
            names=line.get('name-list',[])
            entries.append(dict(requested_accession=ac,primary_accessions=[x['value'] for x in line.get('accession-list',[]) if x.get('type')=='primary'],recommended_names=[x['value'] for x in names if x.get('type')=='identifier'],synonyms=[x['value'] for x in names if x.get('type')=='synonym'],species=line.get('species-list',[]),parent_information=line.get('derived-from',line.get('derived-from-list',None)),comment_fields=[k for k in line if 'comment' in k or 'problem' in k or 'caution' in k],file=info))
    return dict(resource_id='cellosaurus',verification='selected_reference_records_parsed',entries=entries,interpretation='Reference identity only. Source stock/subline must be reconciled; name similarity and shared parentage do not establish condition equivalence. HEK293 must not replace HEK293T; unspecified U87/JURKAT stocks remain ambiguous.')

jobs={'rnalocate_mRNA':lambda:inspect_rnalocate('mRNA'),'rnalocate_circRNA':lambda:inspect_rnalocate('circRNA'),'rnalocate_export':inspect_rnalocate_export,'rasp2':inspect_rasp,'cellosaurus':inspect_cellosaurus}
out=dict(audit_date=DATE,scope='Selected data files and reference API records; no raw rows or molecular sequences redistributed.',results={})
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    fs={pool.submit(fn):name for name,fn in jobs.items()}
    for f in concurrent.futures.as_completed(fs):
        name=fs[f]
        try: out['results'][name]=f.result(); print(name,'OK',flush=True)
        except Exception as e: out['results'][name]=dict(status='access_or_parse_failed',error=type(e).__name__+': '+str(e)); print(name,'FAILED',str(e),flush=True)
Path(args.output).parent.mkdir(parents=True,exist_ok=True)
Path(args.output).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
