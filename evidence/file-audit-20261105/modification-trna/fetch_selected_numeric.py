"""Inspect representative read-only numeric endpoints from documented public routes."""
import argparse,concurrent.futures,json,pathlib
from probe_sources import fetch
a=argparse.ArgumentParser();a.add_argument('--download-dir',required=True);a.add_argument('--out',required=True);a=a.parse_args();d=pathlib.Path(a.download_dir)
ds=json.loads((d/'sci_datasets_legacy.bin').read_bytes());sel=[x for x in ds if x['cto']=='HEK293T' and x['tech']=='BID-seq'];sel=sel[:1] or ds[:1]
urls={f'sci_bedrmod_{x["dataset_id"]}':f'https://scimodom.dieterichlab.org/api/v0/transfer/dataset/{x["dataset_id"]}' for x in sel}
urls['charge188_correct_sample']='https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5691036&targ=self&form=text&view=full'
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows=list(ex.map(lambda item:fetch(item,d),urls.items()))
out=dict(selected_dataset_metadata=sel,retrievals=rows)
pathlib.Path(a.out).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
