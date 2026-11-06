"""Check provenance, source-role and publication invariants for the file audit."""
from pathlib import Path
import collections, json, re
B=Path(__file__).resolve().parents[1]
def read(p):return json.loads((B/p).read_text(encoding='utf-8'))
s=read('evidence/file-audit-20261105/summary.json');registry=read('catalog/registry.json');rs={r['id']:r for r in registry['resources']}
assert len(s['resources'])==20==len({r['resource_id'] for r in s['resources']})
assert all(r['resource_id'] in rs for r in s['resources'])
assert sum(r['selected_data_or_reference_payload_inspected'] for r in s['resources'])==16
assert {r['resource_id'] for r in s['resources'] if not r['selected_data_or_reference_payload_inspected']}==set(s['numeric_data_access_gaps'])
for r in s['resources']:
    assert (B/r['evidence_path']).is_file(),r['resource_id']
    assert r['integration_role'] and r['limitations']
    if not r['selected_data_or_reference_payload_inspected']:
        assert rs[r['resource_id']]['verification']['level']!='file_sample'
    elif r['verification_level']=='file_sample':
        limits=' '.join(rs[r['resource_id']]['verification']['limitations'])
        assert 'No biological data file was inspected;' not in limits
        assert 'No downloadable profile was opened.' not in limits
        assert 'Schema documentation was inspected, not an exported dataset.' not in limits
for f in read('evidence/file-audit-20261105/verified_payloads.json')['files']:
    assert f['resource_id'] in rs and f['url'].startswith(('http://','https://'))
    if not f['download_complete']:assert f['sha256'] is None and f['partial_sha256']
    if f['sha256']:assert re.fullmatch('[0-9a-f]{64}',f['sha256'])
j=read('catalog/cell_context_join_manifest.json')['joins']
assert len(j)==19 and all(x['matched_assay_condition'] is False for x in j)
assert all('source_label_raw' in x for x in j)
assert all(not x['hpa_numeric_cell_name'] for x in j if x['study']=='Albatross' and x['source_label']=='HEK293T')
assert all(not x['depmap_numeric_model_id'] for x in j if x['source_label']=='HCT8')
rb=read('evidence/file-audit-20261105/benchmarks/ribonn_human_original.json')
assert rb['numeric_te_observations']==sum(rb['numeric_per_context'].values())
assert rb['rows']*rb['te_contexts']==rb['numeric_te_observations']+sum(rb['missing_or_nonnumeric_per_context'].values())
assert rs['p010-asset-2']['status']=='curated'
assert all(x['label_type']=='synthetic' for x in rs['p010-asset-1']['labels'])
assert read('catalog/combination_plan.json')['reliability_demonstrated'] is False
files=0
for p in (B/'evidence/file-audit-20261105').rglob('*'):
    if p.suffix not in {'.json','.py','.md'}:continue
    if p==B/'evidence/file-audit-20261105/validation.json':continue
    text=p.read_text(encoding='utf-8'); files+=1
    if p.suffix=='.json':json.loads(text)
    assert not re.search(r'(?<![A-Za-z0-9])[A-Z]:[\\/]|file://',text),str(p.relative_to(B))
    assert not re.search(r'[ACGTUacgtu]{80,}',text),str(p.relative_to(B))
    assert not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]+|[?&](?:token|signature|credential|api_key)=',text,re.I),str(p.relative_to(B))
report=dict(status='PASS',audited_resources=20,selected_payload_resources=16,explicit_numeric_access_gaps=s['numeric_data_access_gaps'],text_evidence_files_checked=files,limits='Checks establish audit consistency and publication hygiene, not predictive reliability or complete database coverage.')
(B/'evidence/file-audit-20261105/validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
