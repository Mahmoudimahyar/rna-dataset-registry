"""Fetch official JS/API documentation and a small processed charging archive."""
import argparse,concurrent.futures,json,pathlib
from probe_sources import fetch
a=argparse.ArgumentParser();a.add_argument('--download-dir',required=True);a.add_argument('--out',required=True);a=a.parse_args();d=pathlib.Path(a.download_dir)
urls={
 'sci_datasets_legacy':'https://scimodom.dieterichlab.org/api/v0/dataset/list_all',
 'sci_projects_legacy':'https://scimodom.dieterichlab.org/api/v0/project/list_all',
 'charge239_human_sample':'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7675803&targ=self&form=text&view=full',
 'charge188_sample':'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5687544&targ=self&form=text&view=full'
}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:rows=list(ex.map(lambda item:fetch(item,d),urls.items()))
pathlib.Path(a.out).write_text(json.dumps(rows,indent=2),encoding='utf-8');print(json.dumps([{k:v for k,v in x.items() if k not in {'links','scripts'}} for x in rows]))
