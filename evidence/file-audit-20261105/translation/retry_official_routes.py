"""Bounded retries of publisher-documented alternate official routes."""
import requests,concurrent.futures,json,pathlib
URLS=['https://www.ribocirc.com/','https://ribocirc.com/','http://www.ribocirc.com/','https://biosino.org/transcirc-v1/download','https://www.biosino.org/transcirc-v1/download']
def get(u):
 try:
  r=requests.get(u,timeout=(5,10));return {'url':u,'status':r.status_code,'bytes':len(r.content)}
 except Exception as e:return {'url':u,'error_type':type(e).__name__}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rows=list(ex.map(get,URLS))
 (pathlib.Path(__file__).parent/'official_route_retries.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
 print(json.dumps(rows))
