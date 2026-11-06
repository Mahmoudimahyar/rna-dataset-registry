"""Inspect public download pages; bulk payloads stay outside the repository."""
import requests, concurrent.futures, json, re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

URLS=[
 'https://sysbio.gzzoc.com/rpfdb/download.html',
 'https://rdp.ucc.ie/',
 'https://ngdc.cncb.ac.cn/circatlas/',
 'https://ngdc.cncb.ac.cn/circatlas/download.php',
 'https://sysbio.gzzoc.com/ribocirc/download.html',
 'https://circtarget.cn/download/',
 'https://www.biosino.org/transcirc/download',
 'https://www.biosino.org/transcirc-v1/download',
]
def get(u):
 try:
  r=requests.get(u,timeout=35);s=BeautifulSoup(r.text,'html.parser')
  links=[{'text':a.get_text(' ',strip=True)[:90],'url':urljoin(r.url,a.get('href',''))} for a in s.select('a[href]')]
  scripts=[urljoin(r.url,a.get('src')) for a in s.select('script[src]')]
  interesting=[l for l in links if re.search('download|\\.(?:csv|txt|tsv|zip|gz|rar|xlsx)|data/',l['url'],re.I)]
  return {'url':u,'status':r.status_code,'final_url':r.url,'length':len(r.content),'links':interesting,'scripts':scripts,'inline_urls':re.findall(r'''["']([^"']*(?:\\.php|\\.csv|\\.json|\\.gz|\\.zip|\\.txt)[^"']*)["']''',r.text)[:60]}
 except Exception as e:return {'url':u,'error':str(e)}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:
  for x in e.map(get,URLS): print(json.dumps(x))
