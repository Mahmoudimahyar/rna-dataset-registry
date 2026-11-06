"""Summaries only; never exports RNA sequence values."""
import argparse,collections,csv,gzip,io,json,pathlib,sys,tarfile,zipfile,zlib
sys.stdout.reconfigure(encoding='utf-8')
a=argparse.ArgumentParser();a.add_argument('--download-dir',required=True);a.add_argument('--out',required=True);a=a.parse_args();d=pathlib.Path(a.download_dir);o={}
for n in ['sci_datasets_legacy','sci_projects_legacy']:
 x=json.loads((d/(n+'.bin')).read_bytes());print(n,type(x).__name__,len(x),str(x)[:1800])
for n in ['charge_tar','charge188_tar']:
 files=[]
 with tarfile.open(d/(n+'.bin')) as t:
  for m in t.getmembers():
   b=t.extractfile(m).read(); b=gzip.decompress(b) if m.name.endswith('.gz') else b;lines=b.decode().splitlines()
   files.append(dict(member=m.name,rows=len(lines),first_lines=lines[:2],delimiter=':' if ':' in lines[0] else '\t',field_width_counts=dict(collections.Counter(len(s.split(':')) for s in lines))))
 o[n]=files;print(n,json.dumps(files[:2]))
for n in ['m6a_conditions','m6a_sites']:
 with gzip.open(d/(n+'.bin'),'rt') as f:
  reader=csv.DictReader(f,delimiter='\t');counts=collections.Counter();null=collections.Counter();cells=collections.Counter();tech=collections.Counter();gse=set();idset=set();nr=0
  for r in reader:
   nr+=1
   for k,v in r.items():
    if v in {'','NA','NaN','NULL',None}:null[k]+=1
   if n=='m6a_conditions':cells[r['CellLine']]+=1;tech[r['Technique']]+=1;gse.add(r['GSE']);idset.add(r['ID'])
  o[n]=dict(header=reader.fieldnames,data_rows=nr,missing_counts=dict(null),cell_support_rows=dict(cells),tech_support_rows=dict(tech),unique_gse=len(gse) if gse else None,unique_site_ids=len(idset) if idset else None)
 print(n,json.dumps(o[n])[:3500])
p=d/'m6a_quantification.bin';b=zlib.decompressobj(16+zlib.MAX_WBITS).decompress(p.read_bytes(),1024*1024);lines=b.decode().splitlines();o['m6a_quantification_prefix']=dict(scope='First 1MiB uncompressed from bounded 32MiB compressed prefix; last line omitted',header=lines[0],complete_sample_rows=len(lines)-2,example_fields=lines[1].split('\t')[:8]);print('m6a_quantification_prefix',o['m6a_quantification_prefix'])
with zipfile.ZipFile(d/'modomics_positions.bin') as z:
 tables=[]
 for n in z.namelist():
  ls=z.read(n).decode().splitlines(); rs=[r.split('\t') for r in ls if not r.startswith('#') and r.strip()];sp=collections.Counter(r[4] for r in rs if len(r)==9)
  tables.append(dict(member=n,line_count=len(ls),noncomment_rows=len(rs),field_width_counts=dict(collections.Counter(map(len,rs))),schema_for_9fields=['RNA_type','RNA_name','anticodon_or_subtype','compartment','organism','native_position','aligned_position_or_missing','modification','source_annotation'],human_rows=sp.get('Homo sapiens',0),cell_line_column_present=False,numerical_output_column_present=False))
 o['modomics_positions']=tables;print('modomics',json.dumps(tables))
entries=json.loads((d/'tmod_dataset_entries.bin').read_bytes())['data']['all_dataset_entries']['items'];matches=[x for x in entries if x['sample'].lower() in {'hepg2','hek293t','hct116'}];o['tmod_matched_cell_entries']=matches;print('tmod_matches',json.dumps(matches)[:4500])
en=json.loads((d/'tmod_selected_entities.bin').read_bytes())['data']['dataset_entities']['items'];o['tmod_entity_numeric_summary']=dict(rows=len(en),count_positive_rows=sum(x['counts']>0 for x in en),total_positive_rows=sum(x['total']>0 for x in en),per_counts_range=[min(x['per_counts'] for x in en),max(x['per_counts'] for x in en)],cov_nonzero_rows=sum(any(v>0 for v in x['cov'] if isinstance(v,(int,float))) for x in en));print('tmod_entity_numeric_summary',o['tmod_entity_numeric_summary'])
pathlib.Path(a.out).write_text(json.dumps(o,indent=2),encoding='utf-8')
