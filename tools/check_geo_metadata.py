"""Fetch a bounded public GEO series metadata snapshot; no sample sequences."""
from pathlib import Path
import urllib.request,concurrent.futures,json,re,sys
B=Path(__file__).resolve().parents[1]
ids=sys.argv[1:]
def get(acc):
    url='https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='+acc+'&targ=self&form=text&view=brief'
    keep={};status='unknown'
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'RNA-dataset-registry-metadata/0.1'}),timeout=40) as f:
            text=f.read(400000).decode('utf-8','replace');status=f.status
        for line in text.splitlines():
            if line.startswith('!Series_') and ' = ' in line:
                k,v=line.split(' = ',1)
                if any(s in k.lower() for s in ['title','summary','overall_design','sample_id','supplementary_file','pubmed_id','relation','type','status','last_update','submission_date']):keep.setdefault(k[1:],[]).append(v)
        return dict(accession=acc,url=url,http_status=status,metadata=keep,checked_on='2026-11-04',error=None if keep else 'No series metadata parsed; verify record manually')
    except Exception as e:return dict(accession=acc,url=url,http_status=status,metadata={},checked_on='2026-11-04',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(get,ids))
dest=B/'evidence/geo-metadata-root.json'
prior={r['accession']:r for r in json.loads(dest.read_text(encoding='utf-8'))} if dest.exists() else {}
prior.update({r['accession']:r for r in rows})
dest.write_text(json.dumps(list(prior.values()),ensure_ascii=False,indent=2),encoding='utf-8')
for r in rows:print(r['accession'],r['http_status'],'; '.join(r['metadata'].get('Series_title',[])),len(r['metadata'].get('Series_sample_id',[])),'samples',r['error'] or '')
