"""Inspect publicly served application/documentation route references only."""
import argparse,json,pathlib,re,tarfile,gzip,zipfile,sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup
a=argparse.ArgumentParser();a.add_argument('--download-dir',required=True);a=a.parse_args();d=pathlib.Path(a.download_dir)
for name in ['sci_js','tmod_js']:
 s=(d/(name+'.bin')).read_text(encoding='utf-8')
 paths=sorted(set(re.findall(r'[\"\x27`]([^\"\x27`\n]{0,180}(?:api/|/api|download|baseURL)[^\"\x27`\n]{0,180})[\"\x27`]',s,re.I)))
 print(name,json.dumps(paths[:150]))
 for token in (['const Pxt','/datasets/','/projects','/browse','/download'] if name=='sci_js' else ['graphql','/api/v1','async function','http://www.tmodbase2']):
  print('route_context',token,[s[max(0,m.start()-100):m.end()+180] for m in list(re.finditer(re.escape(token),s))[-6:]])
 if name=='tmod_js': print('tmod_data_assets',json.dumps(sorted(set(re.findall(r'[\"\x27`]([^\"\x27`\n]{1,160}\.(?:json|csv|txt|tsv|xlsx|gz))',s)))[:100]))
 if name=='sci_js':
  print('api_routes',json.dumps(sorted(set(x for x in re.findall(r'[\"\x27]([^\"\x27\n]{1,80})[\"\x27]',s) if any(w in x.lower() for w in ['dataset','metadata','bedrmod','api/v','project']) and ' ' not in x))))
  print('Pxt_definition',[s[max(0,m.start()-80):m.end()+150] for m in list(re.finditer('Pxt=',s))])
s=(d/'sci_api_doc.bin').read_text(encoding='utf-8'); bs=BeautifulSoup(s,'html.parser');print('doc_scripts',[(x.get('src'),x.get_text()[:300]) for x in bs.select('script')][-8:]);print('doc_refs',re.findall(r'.{0,70}(?:openapi|spec-url|spec_url|swagger|json).{0,150}',s,re.I)[-20:])
with tarfile.open(d/'charge_tar.bin') as t:
 print('tar_members',[(x.name,x.size) for x in t.getmembers()]); x=t.getmembers()[0]; b=gzip.decompress(t.extractfile(x).read());print('charge_first_lines',b.decode().splitlines()[:3])
with zipfile.ZipFile(d/'modomics_positions.bin') as z:
 for n in z.namelist():
  lines=z.read(n).decode().splitlines();print('mods',n,'lines',len(lines),'linefirst',lines[:2])
