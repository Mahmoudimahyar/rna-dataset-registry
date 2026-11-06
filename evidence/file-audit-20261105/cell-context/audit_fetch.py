"""Bounded public-source file audit. Biological files stay in --data-dir outside repo."""
import argparse, concurrent.futures, csv, gzip, hashlib, io, json, pathlib, requests, zipfile, time

P=argparse.ArgumentParser(); P.add_argument('--data-dir',required=True); P.add_argument('--metadata-dir',required=True); A=P.parse_args()
D=pathlib.Path(A.data_dir); M=pathlib.Path(A.metadata_dir); D.mkdir(parents=True,exist_ok=True); M.mkdir(parents=True,exist_ok=True)
S=requests.Session(); S.headers['User-Agent']='PublicResearchDatasetAudit/1.0'

def save_meta(name,obj):
    (M/(name+'.json')).write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
def fetch(name,url,cap=300_000_000):
    rec={'name':name,'source_url':url,'checked_on':'2026-11-05','complete':False}
    try:
        with S.get(url,stream=True,timeout=(20,90)) as r:
            rec.update(status=r.status_code,content_type=r.headers.get('Content-Type'),content_length=r.headers.get('Content-Length'))
            r.raise_for_status(); p=D/name; total=0; h=hashlib.sha256()
            with p.open('wb') as f:
                for b in r.iter_content(1048576):
                    if total+len(b)>cap: rec['limit_reached']=cap; break
                    f.write(b); h.update(b); total+=len(b)
                else: rec['complete']=True
            rec.update(bytes_saved=total,sha256=h.hexdigest(),sha256_scope='entire downloaded response body' if rec['complete'] else 'saved prefix only',artifact_name=name)
    except Exception as e: rec['error']=str(e)[:600]
    save_meta(name.replace('.','_')+'_fetch',rec); return rec

jobs={
 'hpa_rna_celline.tsv.zip':'https://www.proteinatlas.org/download/rna_celline.tsv.zip',
 'depmap_download_files.csv':'https://depmap.org/portal/api/download/files',
 'depmap_24q4_article.json':'https://api.figshare.com/v2/articles/27993248',
 'mirtarbase_release.html':'https://awi.cuhk.edu.cn/miRTarBase/downloads/releases/v11.0/',
 'postar3_download.html':'http://postar.ncrnalab.org/download.html',
 'encode_rbns.json':'https://www.encodeproject.org/search/?type=File&assay_title=RNA+Bind-N-Seq&output_type=enrichment&format=json&limit=5',
 'encode_eclip.json':'https://www.encodeproject.org/search/?type=File&assay_title=eCLIP&file_format=bed&status=released&format=json&limit=5',
 'encode_knockdown.json':'https://www.encodeproject.org/search/?type=File&assay_title=shRNA+RNA-seq&file_format=tsv&status=released&format=json&limit=5',
 'census_release.json':'https://census.cellxgene.cziscience.com/cell-census/v1/release.json'
}
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(lambda kv:fetch(*kv),jobs.items()): print(json.dumps(r),flush=True)
