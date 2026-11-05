"""Validate catalog semantics, provenance requirements and publication hygiene."""
from pathlib import Path
import json,re,sys,collections
B=Path(__file__).resolve().parents[1];issues=[];warnings=[]
doc=json.loads((B/'catalog/registry.json').read_text(encoding='utf-8'));rows=doc['resources']
required={'id','name','kind','topics','rna_scope','description','source_urls','paper_doi','accessions','organisms','biological_context','assays','observation_unit','labels','scale','access','verification','ml_tasks','cell_specificity','integration_caveats','related_model_ids','related_resource_ids','priority','status'}
enums={'kind':{'database','archive','reference','study','benchmark','model_release','software_example','derived_resource'},'status':{'curated','candidate','blocked'},'priority':{'high','medium','context'}}
ids=[r['id'] for r in rows];idset=set(ids)
if len(ids)!=len(idset):issues.append('Duplicate resource IDs')
models=json.loads((B/'catalog/model_coverage.json').read_text(encoding='utf-8'));mids={m['id'] for m in models}
def url(u):return isinstance(u,str) and re.match(r'^https?://[^\s/]+',u) and not re.search(r'[?&](token|signature|credential|api_key|password)=',u,re.I)
def local_path(x):return bool(re.search(r'''(?<![A-Za-z0-9])[A-Z]:[\\/]|file://|["']/(?:Users|home)/''',json.dumps(x),re.I))
assert not local_path({'url':'https://example.org/home/downloads'})
assert local_path({'path':'G:/private/file.txt'})
assert local_path({'path':r'C:\Users\example\file.txt'})
for r in rows:
    prefix=r['id']+': '
    for k in required-r.keys():issues.append(prefix+'missing '+k)
    if not re.fullmatch('[a-z0-9][a-z0-9._-]*',r['id']):issues.append(prefix+'invalid ID')
    for k,vals in enums.items():
        if r[k] not in vals:issues.append(prefix+'invalid '+k+' '+str(r[k]))
    if r['verification']['level'] not in {'file_sample','schema','metadata','paper','unverified'}:issues.append(prefix+'invalid verification level')
    if r['access']['level'] not in {'open','mixed','controlled','request','unavailable','unknown'}:issues.append(prefix+'invalid access level')
    if not r['source_urls'] or not all(url(u) for u in r['source_urls']):issues.append(prefix+'invalid primary source URLs')
    if not all(url(u) for u in r['access']['data_urls']):issues.append(prefix+'invalid access URLs')
    if r['status']=='curated' and (r['verification']['level']=='unverified' or not r['verification']['evidence']):issues.append(prefix+'curated without evidence')
    if not r['labels']:issues.append(prefix+'no label description')
    for l in r['labels']:
        if not {'name','meaning','label_type','unit','resolution'}<=l.keys():issues.append(prefix+'incomplete label schema')
        if l['label_type'] not in {'measured','computed','annotation','prediction','synthetic','unknown'}:issues.append(prefix+'invalid label evidence type')
    if r['verification']['level']=='file_sample' and not r['verification']['files_inspected']:issues.append(prefix+'file_sample without inspected file evidence')
    for i in r['related_model_ids']:
        if i not in mids:warnings.append(prefix+'model link outside original collection: '+i)
    for i in r['related_resource_ids']:
        if i not in idset:warnings.append(prefix+'unresolved related resource '+i)
    if local_path(r):issues.append(prefix+'local path in public metadata')
for m in models:
    for i in m['dataset_ids']+m['curated_resource_ids']:
        if i not in idset:issues.append(m['id']+' missing resource '+i)
    if m['complete_dataset_audit']:issues.append(m['id']+' unsupported exhaustive audit claim')
    if local_path(m):issues.append(m['id']+' local path in public model metadata')
summary=doc['summary']
if len(rows)!=summary['resource_records']:issues.append('Resource summary mismatch')
if sum(r['status']=='curated' for r in rows)!=summary['curated_records']:issues.append('Curated summary mismatch')
report=dict(status='PASS' if not issues else 'FAIL',records=len(rows),models=len(models),errors=issues,warnings=warnings,limits='Structural/semantic validation does not independently establish scientific correctness or full file coverage.')
(B/'evidence/validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False));sys.exit(bool(issues))
