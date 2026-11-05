"""One-time migration of the earlier audit, preserving its evidence limits.

Run with --audit-root pointing at the earlier report folder. Local paths are never
included in generated public records. This is an import, not new verification.
"""
from pathlib import Path
import argparse,json,re,hashlib
P=argparse.ArgumentParser();P.add_argument('--audit-root',required=True);a=P.parse_args()
SRC=Path(a.audit_root);B=Path(__file__).resolve().parents[1]
d=json.loads((SRC/'dataset_audit.json').read_text(encoding='utf-8'))
c=json.loads((SRC/'rna_coverage_gaps.json').read_text(encoding='utf-8'))
methods={r['review_id']:r for r in json.loads((SRC.parent/'review.json').read_text(encoding='utf-8'))['reviews']}
wanted={r['review_id'] for r in c['models']};gaps={r['review_id']:r for r in c['models']}
models=[];assets=[];queue={}
for r in d['model_reviews']:
    i=r['review_id']
    if i not in wanted:continue
    p=methods[i];g=gaps[i];sp=g.get('second_pass') or {}
    repos=list(r['repository_urls'])
    if i=='P006':repos=['https://github.com/castillohair/paper-5utr-design',*repos,'https://github.com/johli/genesis']
    if i=='P010':repos.append('https://github.com/CenikLab/TE_classic_ML')
    repos=list(dict.fromkeys(repos))
    official=sp.get('official_repo_verification',r['repository_status'])
    if isinstance(official,dict):official={k:v for k,v in official.items() if k in ['status','notes','repository_urls','live_evidence']}
    model=dict(id=i,name=r['model'],paper_title=r['paper_title'],paper_doi=p.get('doi') or None,area=r['area'],task=p.get('task',''),method_summary=p.get('mechanism',''),inputs=p.get('input',''),outputs=p.get('output',''),repository_urls=repos,repository_provenance=official,dataset_ids=[i.lower()+'-asset-'+str(j) for j in range(1,len(r['datasets'])+1)],paper_inventory_complete=bool(sp.get('paper_inventory_complete',False)),all_dataset_files_inspected=False,remaining_gaps=sp.get('missing_or_unverified',['Original access/schema audit does not establish an exhaustive inventory of paper datasets.']),inventory_source='Imported earlier paper and repository audit; evidence remains nonexhaustive.',checked_on='2026-11-04')
    if i=='P012':
        model['inputs']='RNA sequence and sequence-derived possible-base-pair compatibility arrays; not experimentally measured or thermodynamic pairing-probability structure labels.'
        model['remaining_gaps']=['All upstream source files and Supplementary Data1-5 have not been fully reconciled and validated.','The384-member aptaswitch library now has a distinct curated record; full values, normalization formulas and replicate/missingness audit remain incomplete.','Generated optimization traces and synthetic scores must remain separate from experimental validation.']
    models.append(model)
    for u in repos:
        m=re.match(r'https://github.com/([^/]+/[^/#?]+)',u)
        if m:
            q='https://github.com/'+m.group(1).removesuffix('.git')
            queue.setdefault(q,[]).append(i)
    for j,x in enumerate(r['datasets'],1):
        urls=list(dict.fromkeys([x.get('url',''),*x.get('evidence_urls',[])]));urls=[u for u in urls if u.startswith('http')]
        if not urls:urls=list(r['evidence_urls'])
        acc=list(dict.fromkeys(re.findall(r'\b(?:GSE|GSM|SRP|PRJNA|PRJEB|OMIX)\d+\b',' '.join(urls)+' '+x['name'])))
        assets.append(dict(id=i.lower()+'-asset-'+str(j),name=x['name'],kind='model_release',topics=[r['area']],rna_scope=['RNA; exact type varies by source'],description=x.get('unit','')+' '+x.get('inputs',''),source_urls=urls,paper_doi=[p['doi']] if p.get('doi') else [],accessions=acc,organisms=[],biological_context=x.get('context','unknown'),assays=[],observation_unit=x.get('unit','unknown'),labels=[dict(name=x.get('labels','unknown'),meaning=x.get('label_meaning','unknown'),label_type='unknown',unit='unknown',resolution='unknown')],scale=dict(value=None,unit='unknown',basis='Not independently recounted; see prior evidence note',as_of='2026-11-04'),access=dict(level='unknown',data_urls=[x['url']] if x.get('url','').startswith('http') else [],formats=[],license='unknown',redistribution='not established'),verification=dict(level='unverified',checked_on='2026-11-04',evidence=[dict(url=u,supports='Previously recorded audit source; fresh dataset reconciliation pending') for u in urls],files_inspected=[],limitations=[x.get('limitations',''), 'Imported candidate. Prior evidence level: '+x.get('access_status','unknown')+'. Import is not a new file inspection or certification of labels.']),ml_tasks=[],cell_specificity=dict(evidence='unknown',notes=x.get('cell_specificity_use','unknown')),integration_caveats=['May group multiple datasets or overlap other model assets; do not count as an independent experimental dataset.'],related_model_ids=[i],related_resource_ids=[],priority='context',status='candidate',provenance=dict(origin='earlier_nonexhaustive_model_audit',prior_access_level=x.get('access_status','unknown'),prior_fields_observed=x.get('fields_observed',[]))))
for x in assets:
    if x['id'] in {'p002-asset-1','p007-asset-1','p018-asset-2'}:
        x['related_resource_ids']=['sample2019-chemistry-reporters']
        x['integration_caveats'].append('Known reuse of Sample2019 / GSE114002 source family; not an independent new study.')
    if x['id'] in {'p002-asset-2','p012-asset-1'}:
        x['related_resource_ids']=['sample2019-chemistry-reporters',*(['p012-asset-1'] if x['id']=='p002-asset-2' else ['p002-asset-2'])]
        x['integration_caveats'].append('Both imported entries reference GSM3130443; they share an upstream source, not independent experimental replication.')
(B/'catalog/models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'catalog/fragments/legacy_model_assets.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'evidence/repository-check-queue.json').write_text(json.dumps([dict(url=k,model_ids=v) for k,v in queue.items()],indent=2),encoding='utf-8')
print(json.dumps(dict(model_records=len(models),candidate_asset_records=len(assets),repository_urls=len(queue))))
