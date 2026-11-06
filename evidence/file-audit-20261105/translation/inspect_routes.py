import requests,bs4,json,concurrent.futures,re
from urllib.parse import urljoin
URLS=[
'https://ngdc.cncb.ac.cn/circatlas/links1.php',
'https://rdp.ucc.ie/samples?Cell-Line=A549',
'https://rdp.ucc.ie/Sample/SRR19749681/',
'http://sysbio.gzzoc.com/rpfdb/download.html',
'http://sysbio.gzzoc.com/ribocirc/download.html',
'https://sysbio.gzzoc.com/ribocirc2/download.html',
'https://sysbio.gzzoc.com/ribocirc/download/Human-condition-dependent%20translatable%20circRNAs.zip',
'https://circtarget.cn/static/download/A549.rar',
]
def get(u):
 try:
  r=requests.get(u,timeout=30);s=bs4.BeautifulSoup(r.text,'html.parser')
  forms=[str(f)[:2500] for f in s.select('form') if ('human' in str(f).lower() or 'download' in str(f).lower() or 'selection' in str(f).lower())]
  links=[{'text':a.get_text(' ',strip=True)[:70],'url':urljoin(r.url,a['href'])} for a in s.select('a[href]') if re.search('download|\\.bw|\\.bigWig|\\.sqlite|\\.zip|\\.gz|Sample/',a['href'])]
  return {'url':u,'status':r.status_code,'bytes':len(r.content),'type':r.headers.get('Content-Type'),'forms':forms[:3],'links':links[:35]}
 except Exception as e:return {'url':u,'error':str(e)}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  for a in ex.map(get,URLS):print(json.dumps(a))
