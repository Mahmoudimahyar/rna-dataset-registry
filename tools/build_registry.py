"""Build machine-readable exports, individual cards and an offline browser."""
from pathlib import Path
import json,csv,collections,html,hashlib,re
B=Path(__file__).resolve().parents[1]
rows=[]
for f in sorted((B/'catalog/fragments').glob('*.json')):
    rr=json.loads(f.read_text(encoding='utf-8'))
    assert isinstance(rr,list),f
    for r in rr:r['curation_fragment']=f.name
    rows+=rr
rows.sort(key=lambda r:(r['status']!='curated',r['name'].casefold()))
models=json.loads((B/'catalog/models.json').read_text(encoding='utf-8'))
repos=json.loads((B/'evidence/repositories.json').read_text(encoding='utf-8'))
readmes=json.loads((B/'evidence/model-readme-data-pointers.json').read_text(encoding='utf-8'))
for m in models:
    m['repository_live_checks']=[r for r in repos if m['id'] in r['model_ids']]
    m['readme_pointer_checks']=[r for r in readmes if m['id'] in r.get('model_ids',[])]
    m['curated_resource_ids']=[r['id'] for r in rows if m['id'] in r.get('related_model_ids',[]) and r['status']=='curated']
    m['complete_dataset_audit']=False
date='2026-11-05'
summary=dict(release='0.2.0',built_on=date,research_window=['2026-11-04','2026-11-05'],resource_records=len(rows),curated_records=sum(r['status']=='curated' for r in rows),candidate_records=sum(r['status']=='candidate' for r in rows),blocked_records=sum(r['status']=='blocked' for r in rows),model_family_records=len(models),repository_urls_checked=len(repos),repositories_reachable=sum(r['accessible'] for r in repos),readmes_scanned=sum(r['status']=='readme_data_pointers_scanned' for r in readmes),kind_counts=dict(collections.Counter(r['kind'] for r in rows if r['status']=='curated')),verification_counts=dict(collections.Counter(r['verification']['level'] for r in rows if r['status']=='curated')),limits=['Record counts mix database/reference/study/benchmark levels and are not counts of unique independent datasets or biological observations.','Curated means source-backed metadata, with verification level stated. It does not mean full data-file validation.','Imported assets remain candidates unless explicitly reconciled with inspected original data.','Neither global exhaustiveness nor world-largest status is established.'])
audit_path=B/'evidence/file-audit-20261105/summary.json'
if audit_path.exists():
    audit=json.loads(audit_path.read_text(encoding='utf-8'))
    summary['bounded_file_audit']={k:audit[k] for k in ['resources_investigated','selected_data_or_reference_payload_inspected','numeric_data_access_gaps','coverage_limit']}
registry=dict(schema_version='1.0.0',summary=summary,resources=rows)
for f,x in [('catalog/registry.json',registry),('catalog/model_coverage.json',models),('catalog/summary.json',summary)]:
    (B/f).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
def st(x):
    if x is None:return 'unknown'
    if isinstance(x,str):return x.strip()
    if isinstance(x,list):return '; '.join(st(y) for y in x) or 'not established'
    if isinstance(x,dict):return '; '.join(str(k)+': '+st(v) for k,v in x.items())
    return str(x)
def line(x):return st(x).replace('|','\\|').replace('\n',' ')
def bullet(xs):return '\n'.join('- '+st(x) for x in xs) or '- Not established.'
cards=B/'datasets';cards.mkdir(exist_ok=True)
for r in rows:
    s=f'# {r["name"]}\n\nRegistry ID: `{r["id"]}` · {r["kind"]} · **{r["status"]}** · verification: **{r["verification"]["level"]}**\n\n{r["description"]}\n\n'
    s+='## What the data contains\n\n'+f'- Observation unit: {st(r["observation_unit"])}\n- RNA scope: {st(r["rna_scope"])}\n- Biological context: {st(r["biological_context"])}\n- Assays: {st(r["assays"])}\n- Accessions: {st(r["accessions"])}\n- Scale: {st(r["scale"])}\n\n'
    s+='## Labels\n\n| Label | Meaning | Evidence type | Unit | Resolution |\n|---|---|---|---|---|\n'
    for x in r['labels']:s+='| '+' | '.join(line(x[k]) for k in ['name','meaning','label_type','unit','resolution'])+' |\n'
    s+='\n## Access and reuse\n\n'+f'- Access: {r["access"]["level"]}\n- Formats: {st(r["access"]["formats"])}\n- Source license: {st(r["access"]["license"])}\n- Redistribution: {st(r["access"]["redistribution"])}\n\n'+bullet(r['access']['data_urls'])+'\n\n'
    s+='## Verification and remaining gaps\n\n'+f'Checked: {r["verification"]["checked_on"]}. Actual files/headers inspected: {st(r["verification"]["files_inspected"])}.\n\n'+bullet(r['verification']['limitations'])+'\n\n'+bullet(r['integration_caveats'])+'\n\n'
    s+='## Cell specificity\n\n'+st(r['cell_specificity'])+'\n\n## Sources\n\n'+bullet(r['source_urls'])+'\n\n'+bullet([st(x) for x in r['verification']['evidence']])+'\n\n'
    if r.get('file_audit_20261105'):
        a=r['file_audit_20261105'];s+='## Selected-file audit\n\n'+st(a['integration_role'])+'\n\nSelected payload inspected: '+str(a['selected_payload_inspected'])+'. Coverage: '+a['scope']+'.\n\n[Inspection evidence](../'+a['evidence_path']+'). [Combination assessment](../docs/cell-specific-model-feasibility.md).\n\n'
    s+='Related models: '+st(r['related_model_ids'])+'. Related resources: '+st(r['related_resource_ids'])+'.\n'
    (cards/(r['id']+'.md')).write_text('\n'.join(x.rstrip() for x in s.splitlines())+'\n',encoding='utf-8')
mcards=B/'models';mcards.mkdir(exist_ok=True)
for m in models:
    s=f'# {m["name"]}\n\n{m["id"]} · {m["area"]}\n\n**Paper:** {m["paper_title"]}\n\n'
    if m['paper_doi']:s+='https://doi.org/'+m['paper_doi']+'\n\n'
    s+=f'**Task:** {m["task"]}\n\n**Method:** {m["method_summary"]}\n\n**Inputs:** {m["inputs"]}\n\n**Outputs:** {m["outputs"]}\n\n'
    s+='## Repository provenance\n\n'+st(m['repository_provenance'])+'\n\n'+bullet(m['repository_urls'])+'\n\n'
    s+='## Dataset coverage\n\n**A complete dataset audit is not established.** Model families/algorithms are not necessarily individual trained networks. Imported assets are candidates, distinct from newly curated records.\n\n'
    s+=bullet(['['+i+'](../datasets/'+i+'.md)' for i in m['dataset_ids']])+'\n\nCurated related resources:\n\n'+bullet(['['+i+'](../datasets/'+i+'.md)' for i in m['curated_resource_ids']])+'\n\n## Remaining gaps\n\n'+bullet(m['remaining_gaps'])+'\n'
    (mcards/(m['id']+'.md')).write_text('\n'.join(x.rstrip() for x in s.splitlines())+'\n',encoding='utf-8')
with (B/'catalog/registry.csv').open('w',encoding='utf-8',newline='') as f:
    keys=['id','name','kind','status','topics','observation_unit','labels','biological_context','access_level','license','verification_level','accessions','source_urls']
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for r in rows:w.writerow({k:st(r[k]) if k in r else r['access']['level'] if k=='access_level' else st(r['access']['license']) if k=='license' else r['verification']['level'] for k in keys})
# Access manifest includes file links and landing pages, explicitly marked.
manifest=[]
payload_path=B/'evidence/file-audit-20261105/verified_payloads.json'
payload_rows=json.loads(payload_path.read_text(encoding='utf-8'))['files'] if payload_path.exists() else []
for r in rows:
    for u in r['access']['data_urls']:
        proofs=[p for p in payload_rows if p['resource_id']==r['id'] and p['url']==u]
        digests={p['sha256'] for p in proofs if p.get('sha256') and p.get('download_complete')}
        checksum=next(iter(digests)) if len(digests)==1 else None
        manifest.append(dict(resource_id=r['id'],url=u,link_kind='file' if re.search(r'\.(?:gz|zip|csv|tsv|xlsx|bw|h5|hdf5|7z|rar|txt|json|rdat)(?:\?|$)',u,re.I) else 'landing_or_api',access=r['access']['level'],source_license=st(r['access']['license']),redistribution=st(r['access']['redistribution']),checksum=checksum,checksum_status='SHA256 of complete selected response; see request/scope evidence' if checksum else 'Multiple request-specific response hashes; see verification records' if len(digests)>1 else 'Partial-file inspection only; full checksum not established' if proofs else 'Not established in this registry; obtain source checksum before download/use',downloaded=any(p.get('download_complete') for p in proofs),sample_inspected=bool(proofs),verification_records=proofs))
(B/'catalog/access_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
topic_counts=collections.Counter(t for r in rows if r['status']=='curated' for t in r['topics'])
idx='# Dataset index\n\nCounts are catalog records at mixed levels, not unique biological datasets.\n\n'
for status in ['curated','candidate','blocked']:
    idx+='## '+status.title()+'\n\n| Resource | Kind | Verification | Topics |\n|---|---|---|---|\n'
    for r in rows:
        if r['status']==status:idx+=f'| [{line(r["name"])}](../datasets/{r["id"]}.md) | {r["kind"]} | {r["verification"]["level"]} | {line(r["topics"])} |\n'
    idx+='\n'
(B/'docs/dataset-index.md').write_text(idx.rstrip()+'\n',encoding='utf-8')
mi='# Models in the source collection\n\nAll52 paper-level model/family records are mapped; no record is certified as an exhaustive audit of every paper dataset. Repository reachability does not prove official provenance or reproducibility.\n\n| Model/family | Area | Curated related resources | Imported candidate assets |\n|---|---|---|---|\n'
for m in models:mi+=f'| [{line(m["name"])}](../models/{m["id"]}.md) | {line(m["area"])} | {len(m["curated_resource_ids"])} | {len(m["dataset_ids"])} |\n'
(B/'docs/model-index.md').write_text(mi.replace('All52','All 52'),encoding='utf-8')
payload=json.dumps(dict(resources=rows,models=models),ensure_ascii=False).replace('</','<\\/')
template=(B/'web/index.template.html').read_text(encoding='utf-8')
(B/'index.html').write_text(template.replace('__REGISTRY_DATA__',payload).replace('__SUMMARY__',html.escape(json.dumps(summary,ensure_ascii=False))),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))
