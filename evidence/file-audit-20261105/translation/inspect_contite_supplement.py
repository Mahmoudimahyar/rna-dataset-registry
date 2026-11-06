"""Inspect the source-atlas links in the public ContiTE supplement."""
import argparse,requests,zipfile,io,pypdf,pathlib,json,hashlib,re,sys
sys.stdout.reconfigure(encoding='utf8')
URL='https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13591282/supplementaryFiles'
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--download-dir',required=True);args=p.parse_args();d=pathlib.Path(args.download_dir);d.mkdir(parents=True,exist_ok=True)
 archive=d/'ContiTE_supplementaryFiles.zip'
 if archive.exists():data=archive.read_bytes()
 else:
  r=requests.get(URL,timeout=(15,50));r.raise_for_status();data=r.content;archive.write_bytes(data)
 z=zipfile.ZipFile(io.BytesIO(data));name='si-contite_final_bbag518.pdf';pdf=z.read(name);(d/name).write_bytes(pdf);reader=pypdf.PdfReader(io.BytesIO(pdf));pages=[p.extract_text() or '' for p in reader.pages]
 selected=[{'page':i+1,'text':t} for i,t in enumerate(pages) if any(q in t.lower() for q in ['dataset sources','accessibility','supplementary table s1'])]
 result={'source_url':URL,'archive_bytes':len(data),'archive_sha256':hashlib.sha256(data).hexdigest(),'supplement_pdf':name,'pdf_bytes':len(pdf),'pdf_sha256':hashlib.sha256(pdf).hexdigest(),'pages':len(pages),'selected_pages':selected}
 # Source PDF remains outside the repository; evidence stores supported source links and short descriptions separately.
 (d/'contite_supplement_inspection_private.json').write_text(json.dumps(result,indent=2),encoding='utf8')
 print(json.dumps({k:v for k,v in result.items() if k!='selected_pages'}))
 for x in selected:print('PAGE '+str(x['page'])+'\n'+x['text'][:15000])
