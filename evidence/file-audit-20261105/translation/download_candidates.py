import requests, pathlib, hashlib, json, concurrent.futures,argparse
TASKS=[
('circAtlas_human_bed_v3.0.zip','https://ngdc.cncb.ac.cn/circatlas/analysis/bed/human_bed_v3.0.zip',None),
('CircTarget_A549.rar','https://circtarget.cn/static/download/A549.rar',None),
('RDP_A549_metadata.csv','https://rdp.ucc.ie/sample_select_form/',{'download-metadata':'Cell-Line=A549'}),
('riboCIRC2_context.rar','http://www.ribocirc.com/download/All_context-specific_ribo-circRNAs.rar',None),
('riboCIRC2_literature.rar','http://www.ribocirc.com/download/literature-reported_trans-circRNAs.rar',None),
]
def get(t):
 name,url,params=t
 try:
  r=requests.get(url,params=params,timeout=(15,90));r.raise_for_status()
  f=OUT/name;f.write_bytes(r.content)
  return {'name':name,'url':r.url,'status':r.status_code,'bytes':len(r.content),'sha256':hashlib.sha256(r.content).hexdigest(),'type':r.headers.get('Content-Type'),'prefix_hex':r.content[:10].hex()}
 except Exception as e:return {'name':name,'url':url,'error':str(e)}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--download-dir',required=True);parser.add_argument('--only-ribocirc',action='store_true')
 args=parser.parse_args();OUT=pathlib.Path(args.download_dir);OUT.mkdir(parents=True,exist_ok=True)
 if args.only_ribocirc:TASKS=[t for t in TASKS if t[0].startswith('riboCIRC2')]
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
  for a in ex.map(get,TASKS):print(json.dumps(a),flush=True)
