"""Summarize locally downloaded biological payloads without publishing sequences."""
import argparse,collections,csv,gzip,io,json,pathlib,re,tarfile,zipfile
from bs4 import BeautifulSoup
a=argparse.ArgumentParser();a.add_argument('--download-dir',required=True);a.add_argument('--out',required=True);a=a.parse_args();d=pathlib.Path(a.download_dir)
out={}
for n in ['m6a_conditions','m6a_sites','m6a_quantification']:
 p=d/(n+'.bin')
 if not p.exists():continue
 try:
  b=gzip.decompress(p.read_bytes()); lines=b.decode('utf-8-sig').splitlines(); rows=list(csv.reader(lines,delimiter='\t'))
  out[n]={'full_decompression':True,'total_lines':len(lines),'header':rows[0],'row_width_counts':dict(collections.Counter(map(len,rows))),'first_rows_no_sequences':rows[1:3] if n=='m6a_conditions' else [],'unique_cell_labels':None}
  if n=='m6a_conditions':
   # The file schema is inspected before deciding which columns contain context.
   out[n]['sample_rows_for_schema']=rows[1:6]
 except Exception as e:out[n]={'error':str(e)}
p=d/'modomics_positions.bin'
if p.exists():
 try:
  with zipfile.ZipFile(p) as z:
   out['modomics_positions']={'members':[{ 'name':i.filename,'bytes':i.file_size} for i in z.infolist()]}
   for i in z.infolist():
    if i.filename.endswith(('.txt','.csv','.tsv')):
     b=z.read(i);text=b.decode('utf-8-sig');lines=text.splitlines()
     out['modomics_positions'].setdefault('tables',[]).append({'name':i.filename,'line_count':len(lines),'header':lines[0][:1000],'first_row_field_count':len(lines[1].split('\t')) if len(lines)>1 else None})
 except Exception as e:out['modomics_positions']={'error':str(e)}
pathlib.Path(a.out).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
