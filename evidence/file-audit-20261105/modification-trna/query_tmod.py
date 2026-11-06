"""Read-only GraphQL queries matching the public tModBase download view."""
import argparse,hashlib,json,pathlib,requests
a=argparse.ArgumentParser();a.add_argument('--download-dir',required=True);a.add_argument('--out',required=True);a=a.parse_args();d=pathlib.Path(a.download_dir)
url='https://www.tmodbase2.com/graphql'
q='query GetDatasetEntries { all_dataset_entries { __typename ... on DatasetEntryList { total_count items { id gse gsm technology species sample treatment dataset under_construction srr } } ... on ErrorMessage { message code } } }'
rows=[]
for name,payload in [('tmod_dataset_entries',dict(query=q))]:
 try:
  r=requests.post(url,json=payload,timeout=45);b=r.content;(d/(name+'.bin')).write_bytes(b)
  record=dict(id=name,url=url,request=payload,status=r.status_code,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),hash_scope='full_response')
  obj=r.json(); data=obj.get('data',{}).get('all_dataset_entries',{});items=data.get('items',[])
  record.update(total_count=data.get('total_count'),actual_rows=len(items),schema=list(items[0]) if items else [],cell_sample_labels=sorted(set(x.get('sample','') for x in items)),under_construction_count=sum(bool(x.get('under_construction')) for x in items),species=sorted(set(x.get('species','') for x in items)))
  print(json.dumps(record));rows.append(record)
  selected=[x for x in items if x.get('sample','').lower() in {'hek293t','hek293','hepg2','a549','hela','hct116'} and not x.get('under_construction')]
  if not selected:selected=[x for x in items if not x.get('under_construction')]
  if selected:
   ds=selected[0]['dataset'];q2='query GetDatasetEntities($ds: String!) { dataset_entities(dataset: $ds) { __typename ... on EntityList { total_count items { id name raw_name dataset cov stop mismatch per_mismatch total counts per_counts cov_ng stop_ng mismatch_ng per_mismatch_ng } } ... on ErrorMessage { message code } } }'
   p2=dict(query=q2,variables={'ds':ds});r2=requests.post(url,json=p2,timeout=45);b2=r2.content;(d/'tmod_selected_entities.bin').write_bytes(b2);obj2=r2.json();en=obj2.get('data',{}).get('dataset_entities',{});it=en.get('items',[])
   rec2=dict(id='tmod_selected_entities',url=url,request=p2,selected_dataset_metadata=selected[0],status=r2.status_code,bytes=len(b2),sha256=hashlib.sha256(b2).hexdigest(),hash_scope='full_response',actual_rows=len(it),total_count=en.get('total_count'),schema=list(it[0]) if it else [],non_null_by_field={k:sum(x.get(k) is not None for x in it) for k in it[0]} if it else {},array_lengths_first_entity={k:len(v) for k,v in it[0].items() if isinstance(v,(list,dict))} if it else {},sample_numeric_or_summary={k:v if isinstance(v,(int,float)) else dict(type=type(v).__name__,length=len(v)) if isinstance(v,(list,dict,str)) else None for k,v in it[0].items() if k not in {'name','raw_name','dataset'}} if it else {},errors=obj2.get('errors'))
   print(json.dumps(rec2));rows.append(rec2)
 except Exception as e:rows.append(dict(id=name,url=url,error=str(e)));print(json.dumps(rows[-1]))
pathlib.Path(a.out).write_text(json.dumps(rows,indent=2),encoding='utf-8')
