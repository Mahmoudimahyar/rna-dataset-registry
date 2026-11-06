"""Bounded BigWig inspection of a public normal-condition A549 Ribo-seq sample.

Inspects genuine numerical signal records without publishing sequence data.
The byte-prefix hash is explicitly not a full-source checksum.
"""
import requests,struct,zlib,json,hashlib,pathlib
URL='https://rdp.ucc.ie/static2/bigwig/SRR328/SRR3286544.forward.bw'
if __name__=='__main__':
 r=requests.get(URL,headers={'Range':'bytes=0-1048575'},stream=True,timeout=(15,40))
 r.raise_for_status()
 data=b''
 for chunk in r.iter_content(65536):
  data+=chunk
  if len(data)>=1048576:break
 r.close()
 info={'url':URL,'status':r.status_code,'content_range':r.headers.get('Content-Range'),'content_length_header':r.headers.get('Content-Length'),'bytes_inspected':len(data),'byte_prefix_sha256':hashlib.sha256(data).hexdigest(),'full_file_sha256':None,'scope':'First 1 MiB of source; only first compressed data section parsed'}
 if len(data)<64:raise ValueError('Insufficient binary header')
 h=struct.unpack('<IHHQQQHHQQIQ',data[:64])
 info['bigwig_header']={'magic_hex':hex(h[0]),'version':h[1],'zoom_levels':h[2],'chrom_tree_offset':h[3],'full_data_offset':h[4],'full_index_offset':h[5],'uncompress_buffer_size':h[10]}
 assert h[0]==0x888FFC26,'Not a BigWig payload'
 pos=h[4]
 info['section_count_header']=struct.unpack_from('<Q',data,pos)[0]
 block=zlib.decompressobj().decompress(data[pos+8:]) if h[10] else data[pos+8:]
 sec=struct.unpack_from('<IIIIIBBH',block,0)
 info['first_section']={'chrom_id':sec[0],'start':sec[1],'end':sec[2],'step':sec[3],'span':sec[4],'type':sec[5],'items':sec[7]}
 typ,n=sec[5],sec[7];p=24;items=[]
 for i in range(n):
  if typ==1: start,end,val=struct.unpack_from('<IIf',block,p);p+=12
  elif typ==2:start,val=struct.unpack_from('<If',block,p);end=start+sec[4];p+=8
  elif typ==3:val=struct.unpack_from('<f',block,p)[0];start=sec[1]+i*sec[3];end=start+sec[4];p+=4
  else:raise ValueError('Unknown section type')
  items.append((start,end,val))
 info['signal_records_parsed']=len(items)
 info['signal_min_max']=[min(x[2] for x in items),max(x[2] for x in items)]
 info['signal_fields']=['chrom_id','start','end','numeric coverage value']
 info['biology']={'run':'SRR3286544','study':'PRJNA316125','geo':'GSE79539','cell_line':'A549','condition':'Grown under normal condition','inhibitor':'Cycloheximide','library_type':'Ribo-Seq','meaning':'Genome-aligned footprint coverage, not completed protein production or a direct circRNA-specific signal'}
 info['integration_limits']=['Requires transcript/reference annotation and independently verified matched RNA-seq to derive endogenous TE','Ribo-seq genomic reads do not uniquely establish circRNA translation','Not an independent dataset from other portals that index SRR3286544']
 dest=pathlib.Path(__file__).parent/'rdp_signal_sample.json';dest.write_text(json.dumps(info,indent=2)+'\n',encoding='utf8')
 print(json.dumps(info))
