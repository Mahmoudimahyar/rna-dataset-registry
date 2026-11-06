"""Read bounded official source files; write private response bodies and public retrieval metadata.

Usage: python probe_sources.py --download-dir PRIVATE_DIRECTORY --out PUBLIC_METADATA_JSON
No biological sequence values are emitted in metadata.
"""
import argparse, concurrent.futures, hashlib, json, pathlib, requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

SOURCES = {
 'sci_modom_frontend':'https://scimodom.dieterichlab.org/',
 'm6a_conditions':'https://rnamd.org/m6a/download/high/hg38/Condition_hg38.txt.gz',
 'm6a_quantification':'https://rnamd.org/m6a/download/high/hg38/human_all_logFC.txt.gz',
 'm6a_sites':'https://rnamd.org/m6a/download/high/hg38/hg38_CL_Tech.txt.gz',
 'modomics_positions':'https://genesilico.pl/modomics/download/modified_positions/',
 'tmodbase_frontend':'http://www.tmodbase2.com/',
 'tpsic_index':'https://tpsic.igcz.poznan.pl/trna-sequencing/all/',
 'charge_gse239867':'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE239nnn/GSE239867/suppl/',
 'charge_gse188855':'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE188nnn/GSE188855/suppl/'
}

def fetch(item, d):
 name,url=item
 try:
  r=requests.get(url, timeout=(20,55), stream=True)
  b=bytearray(); complete=True
  for c in r.iter_content(65536):
   b.extend(c)
   if len(b)>32*1024*1024: complete=False;break
  p=d/(name+'.bin');p.write_bytes(b)
  x=dict(id=name,url=url,resolved_url=r.url,status=r.status_code,content_type=r.headers.get('Content-Type'),bytes_read=len(b),complete=complete,sha256=hashlib.sha256(b).hexdigest(),hash_scope='full_response' if complete else 'bounded_prefix')
  if 'html' in r.headers.get('Content-Type',''):
   s=BeautifulSoup(bytes(b),'html.parser')
   x['links']=[dict(text=a.get_text(' ',strip=True)[:100],url=urljoin(r.url,a['href'])) for a in s.select('a[href]')]
   x['scripts']=[urljoin(r.url,a['src']) for a in s.select('script[src]')]
  return x
 except Exception as e:return dict(id=name,url=url,error=str(e))

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--download-dir',required=True);a.add_argument('--out',required=True);a=a.parse_args()
 d=pathlib.Path(a.download_dir);d.mkdir(parents=True,exist_ok=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: rows=list(ex.map(lambda item:fetch(item,d),SOURCES.items()))
 pathlib.Path(a.out).write_text(json.dumps(rows,indent=2),encoding='utf-8')
 print(json.dumps([{k:v for k,v in x.items() if k not in {'links','scripts'}} for x in rows]))
