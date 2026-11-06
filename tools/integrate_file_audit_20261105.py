"""Integrate the bounded 20-resource file audit without redistributing source data."""
from pathlib import Path
import collections, copy, json
B=Path(__file__).resolve().parents[1]; E=B/'evidence/file-audit-20261105'; D='2026-11-05'
def read(p): return json.loads((B/p).read_text(encoding='utf-8'))
def save(p,o):
    p=B/p
    if p.exists() and json.loads(p.read_text(encoding='utf-8'))==o:return
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def unique(xs): return list(dict.fromkeys(xs))
fragments={p.name:json.loads(p.read_text(encoding='utf-8')) for p in (B/'catalog/fragments').glob('*.json')}
existing={r['id']:r for rr in fragments.values() for r in rr}
new=[]; summary=[]; payloads=[]
def label(n,m,t='annotation',u='category',res='sample'):return dict(name=n,meaning=m,label_type=t,unit=u,resolution=res)
def base(i,n,k,desc,urls,labels,rna=('mRNA',)):
    return dict(id=i,name=n,kind=k,topics=['cell_context','source_provenance'],rna_scope=list(rna),description=desc,source_urls=urls,paper_doi=[],accessions=[],organisms=[],biological_context='See selected-file audit; not matched to reporter assay conditions.',assays=[],observation_unit='Source-specific record',labels=labels,scale=dict(value=None,unit='unknown',basis='Selected inspection scope is recorded separately; no database-wide recount',as_of=D),access=dict(level='open',data_urls=[],formats=[],license='unknown',redistribution='not established; metadata only redistributed'),verification=dict(level='metadata',checked_on=D,evidence=[dict(url=u,supports='Primary resource documentation and file routes') for u in urls],files_inspected=[],limitations=[]),ml_tasks=['context_annotation'],cell_specificity=dict(evidence='context_only',notes='Not a matched synthetic RNA protein-output experiment'),integration_caveats=[],related_model_ids=[],related_resource_ids=[],priority='context',status='curated')
def get(i,template=None):
    if i in existing:return existing[i]
    assert template is not None,i
    r=copy.deepcopy(template); new.append(r); existing[i]=r; return r
def add_payload(i,f,scope='selected source file'):
    u=f.get('url',f.get('source_url')); sha=f.get('sha256'); partial=f.get('full_file_sha256','absent') is None or 'byte_prefix_sha256' in f
    if not u:return
    payloads.append(dict(resource_id=i,url=u,scope=f.get('scope',f.get('checksum_scope',f.get('hash_scope',f.get('sha256_scope',scope)))),download_complete=not partial,sha256=None if partial else sha,partial_sha256=f.get('byte_prefix_sha256') if partial else None,bytes=f.get('bytes',f.get('bytes_saved',f.get('bytes_inspected'))),verification='selected payload inspected; see resource audit',request_note='For query APIs, response hashes depend on the exact request. See the request/provenance audit.'))
def annotate(i,verified,level,files,evidence_path,role,limits,template=None):
    r=get(i,template); r['verification']['checked_on']=D
    if level=='file_sample':
        r['verification']['level']='file_sample'
        stale={'No biological data file was inspected; this record establishes resource metadata and documented endpoints only.','No downloadable profile was opened.','Schema documentation was inspected, not an exported dataset.','Metadata/schema review is not inspection of every underlying dataset file.'}
        r['verification']['limitations']=[x for x in r['verification'].get('limitations',[]) if x not in stale]
    r['verification']['limitations']=unique(r['verification'].get('limitations',[])+limits+[f'Bounded file audit: {evidence_path}; selected coverage only.'])
    inspected=[f.get('url',f.get('source_url')) for f in files if f.get('url',f.get('source_url'))]
    if level=='file_sample':r['verification']['files_inspected']=unique(r['verification'].get('files_inspected',[])+inspected)
    r['access']['data_urls']=unique(r['access'].get('data_urls',[])+inspected)
    r['file_audit_20261105']=dict(selected_payload_inspected=verified,verification_level=level,evidence_path=evidence_path,integration_role=role,scope='Selected files/API responses, not all source holdings')
    summary.append(dict(resource_id=i,name=r['name'],selected_data_or_reference_payload_inspected=verified,verification_level=level,evidence_path=evidence_path,integration_role=role,limitations=limits))
    for f in files:add_payload(i,f)
    return r

# Six translation/circRNA resources. Preserve broader existing records.
tr=read('evidence/file-audit-20261105/translation/translation_file_audit.json')['resources']
suggest={r['id']:r for r in read('evidence/file-audit-20261105/translation/proposed_resources.json')}
for a in tr:
    i=a['resource_id']; good=a['verification_level']=='file_sample'
    r=annotate(i,good,a['verification_level'],a.get('files',[]) if good else [],'evidence/file-audit-20261105/translation/translation_file_audit.json',a['data_role'],a['limitations'],suggest[i])
    if not good and i not in {'rpfdb3'}: r['status']='candidate'

# Five modification/tRNA resources: index metadata remains metadata, even when
# the independently linked studies have inspected numerical files.
mods=read('evidence/file-audit-20261105/modification-trna/audit.json')['resources']
for a in mods:
    i=a['id']; urls=[x['url'] for x in a['files']]
    if i=='tmodbase2':
        template=base(i,'tModBase v2.0','database','tRNA sequencing datasets and condition-specific abundance/modification-associated signals.',['https://doi.org/10.1093/nar/gkag1092','https://www.tmodbase2.com/'],[label('counts / per_counts / mismatch / stop / coverage','Assay-derived numerical signals; not interchangeable with charging or calibrated modification fractions','computed','source-specific','transcript')],('tRNA',))
        template['paper_doi']=['10.1093/nar/gkag1092']; template['assays']=['tRNA sequencing; method varies by dataset']
    elif i=='t-psi-c-sequencing-index':
        template=base(i,'T-psi-C tRNA sequencing study index','reference','Method/source index; linked charging experiments audited separately.',urls,[label('Study/method/accession','Reference discovery metadata')],('tRNA',))
        template['cell_specificity']['evidence']='none'
    else:template=None
    r=annotate(i,True,a['verification_level'],a['files'],'evidence/file-audit-20261105/modification-trna/audit.json',a['integration_decision'],a['limits'],template)
    if i=='tmodbase2':r['biological_context']='Selected numerical sample: HepG2, DAMM-seq, ALKBH7-mutant rescue; not untreated reporter context. Other dataset contexts were inspected as metadata only.'
    for study in a.get('linked_numerical_studies',[]):
        add_payload(i,study['file'],'linked study; not index-native numerical data')
        r['access']['data_urls']=unique(r['access']['data_urls']+[study['file']['url']])

# Six context/RBP resources.
cp='evidence/file-audit-20261105/cell-context/'
hpa=read(cp+'hpa_file_inspection.json'); hm=read(cp+'hpa_rna_celline_v25_tsv_zip_fetch.json')
annotate('human-protein-atlas-rna',True,'file_sample',[hm],cp+'hpa_file_inspection.json','External baseline RNA-expression features; 1206 cell lines and20162 genes in inspected25.1 file.',['No replicate column or matched reporter condition; RNA expression does not establish protein activity.','HPA can reuse CCLE profiles; HPA and DepMap are not independent cohorts.'])
dm=read(cp+'depmap_file_inspection.json'); manifest=read(cp+'download_manifest.json')['entries']; df=[f for f in manifest if f['name'] in ['depmap_Expression_24Q4.csv','depmap_Model_24Q4.csv','depmap_OmicsProfiles_24Q4.csv']]
template=base('depmap-ccle-expression','DepMap/CCLE protein-coding expression reference','database','Versioned cancer-cell expression and identity metadata.',['https://api.figshare.com/v2/articles/27993248','https://depmap.org/portal/data_page/'],[label('log2(TPM+1)','RNA-seq-derived protein-coding gene abundance','computed','log2(TPM+1)','transcript'),label('ModelID / RRID','Cell-model identity and context metadata')])
template['access']['license']='CC BY4.0 (inspected24Q4 Figshare release)'; template['access']['formats']=['CSV']; template['organisms']=['Homo sapiens']
annotate('depmap-ccle-expression',True,'file_sample',df,cp+'depmap_file_inspection.json','External expression features:1673 models by19193 genes; inspect24Q4 rather than assume latest.',dm['limitations'],template)
en=read(cp+'encode_file_inspection.json'); annotate('encode',True,'file_sample',en['files'],cp+'encode_file_inspection.json','RBP-binding and cell-free motif evidence; selected knockdown RNA quantifications are not matched translation labels.',[en['sample_scope'],en['limitation'],'Knockdown quantification without matched controls is not an effect estimate.'])
po=read(cp+'postar3_file_inspection.json'); pf=read(cp+'postar3_ALKBH1_binding_sites_zip_fetch.json'); annotate('postar3',True,'file_sample',[pf],cp+'postar3_file_inspection.json','Endogenous binding-site annotation; coordinate joins require resolving assembly and score meanings.',po['limitations'])
annotate('cellxgene-census',False,'metadata',[],cp+'census_access_audit.json','Potential primary-cell context; no numeric data slice verified in this environment.',['Release manifest inspected; native TileDB-SOMA runtime unavailable on supplied Windows Python.','Do not promote metadata or a release listing to expression-file validation.'])
mt=base('mirtarbase','miRTarBase','database','Experiment-supported miRNA-target interaction resource; current data file unavailable during this audit.',['https://awi.cuhk.edu.cn/miRTarBase/downloads/'],[label('Interaction support','Evidence-specific interaction records; actual current schema unverified','unknown')],('miRNA','mRNA'))
mt['status']='candidate'; mt['access']['level']='unavailable'
annotate('mirtarbase',False,'metadata',[],cp+'mirtarbase_access_audit.json','Potential miRNA mechanism evidence; not cleared for numerical integration.',['Current CSV returned403 or TLS failure; no interaction rows inspected.','Schema and source redistribution terms unresolved.'],mt)

# Three auxiliary resources, each with actual reference/numerical records.
aux=read('evidence/file-audit-20261105/auxiliary/audit.json')['results']
ra=aux['rasp2']; annotate('rasp2',True,'file_sample',[ra['metadata_file'],ra['file']],'evidence/file-audit-20261105/auxiliary/audit.json','Measured structure features:7732882 six-column raw HepG2 icSHAPE BED rows in selected track.',['Human API lists124 raw and54 imputed tracks; only one raw track inspected.','Native genomic structure need not transfer to synthetic reporters; match assembly, condition and sequence.'])
rn=aux['rnalocate_export']; annotate('rnalocate',True,'file_sample',[rn['file']],'evidence/file-audit-20261105/auxiliary/audit.json','Localization annotation with computed confidence;55ACTB mRNA query-export rows.',['Bulk mRNA and circRNA ZIP links returned404; selected query CSV works.','Localization does not establish translation rate; RNALocate noncommercial terms apply.'])
ce=aux['cellosaurus']; ct=base('cellosaurus','Cellosaurus cell-line identities','reference','Stable cell-line identifiers, synonyms, species and cross-references.',['https://api.cellosaurus.org/','https://api.cellosaurus.org/api-fields'],[label('Cellosaurus accession / recommended name / synonyms / species','Cell-line identity annotations')],('RNA context',)); ct['cell_specificity']['evidence']='none'
annotate('cellosaurus',True,'file_sample',[x['file'] for x in ce['entries']],'evidence/file-audit-20261105/auxiliary/audit.json','Identity reconciliation only;18selected reference entries inspected.',['Do not substituteHEK293 forHEK293T, equateJurkat sublines or resolve unspecifiedU87 silently.'],ct)

assert len(summary)==20 and len({x['resource_id'] for x in summary})==20
save('evidence/file-audit-20261105/summary.json',dict(audit_date=D,resources_investigated=20,selected_data_or_reference_payload_inspected=sum(r['selected_data_or_reference_payload_inspected'] for r in summary),numeric_data_access_gaps=[r['resource_id'] for r in summary if not r['selected_data_or_reference_payload_inspected']],coverage_limit='Selected files/queries only. Reference and index records are not experimental training observations; T-psi-C includes independently audited linked studies.',resources=summary))

# Original measured/assay-derived benchmark: upgrade the existing stable ID.
rb=read('evidence/file-audit-20261105/benchmarks/ribonn_human_original.json'); r=get('p010-asset-2')
r.update(name='RiboNN original human endogenous mRNA TE atlas',kind='derived_resource',status='curated',description='Original publisher Human supplement with transcript identities/sequences, cross-validation folds and78 context-specific TE estimates.',organisms=['Homo sapiens'],observation_unit='One gene/transcript row with repeated context-specific TE estimates',biological_context='78 source human transcriptome contexts; labels include cell lines, primary populations and tissues.',assays=['Matched Ribo-seq and RNA-seq; study-derived TE residuals'],labels=[label('TE_*',rb['endpoint'],'computed','source compositional-regression residual','transcript'),label('fold','Original gene-level cross-validation fold','annotation','fold','transcript')],scale=dict(value=rb['rows'],unit='gene/transcript rows in original Human sheet',basis=f"All rows parsed; {rb['numeric_te_observations']} numeric TE values across78 columns. Not that many independent sequences.",as_of=D),source_urls=['https://www.nature.com/articles/s41587-025-02712-x','https://github.com/Sanofi-Public/RiboNN',rb['source_url']],paper_doi=['10.1038/s41587-025-02712-x'])
r['access'].update(level='open',data_urls=[rb['source_url']],formats=['XLSX'],license='Original paper states processed supplements available without restriction; preserve publisher/source terms',redistribution='Source remains with publisher; metadata only here')
r['verification']=dict(level='file_sample',checked_on=D,evidence=[dict(url=rb['source_url'],supports='Entire original Human table parsed; exact counts/hash in benchmark audit'),dict(url='https://www.nature.com/articles/s41587-025-02712-x',supports='Methods define TE as compositional-regression residuals averaged within context')],files_inspected=[rb['source_url']],limitations=rb['provenance_cautions'])
r['cell_specificity']=dict(evidence='direct_multi_context',notes='Repeated endogenous transcripts across contexts; not synthetic-RNA cell-selective protein output.')
r['biological_context']='Original Human transcript table with78context columns spanning source cell lines, primary populations and tissues; stock/species/condition metadata must be reconciled, including the TE_Vero_6 label.'
r['integration_caveats']=unique(r.get('integration_caveats',[])+rb['provenance_cautions']+[rb['endpoint'],rb['context_identity_caution']]); add_payload(r['id'],dict(url=rb['source_url'],bytes=rb['bytes'],sha256=rb['sha256'],checksum_scope=rb['checksum_scope']))
fake=get('p010-asset-1'); fake['kind']='software_example'; fake['description']='Author-provided example training schema with explicitly FAKE TE values; not biological training labels.'
fake['labels']=[label('example TE','Synthetic/example labels explicitly described as fake by author README','synthetic','example value','transcript')]
fake['integration_caveats']=unique(fake.get('integration_caveats',[])+['Never use this example as measured translation ground truth.'])

# Companion synthetic reporter studies audited earlier in the same research
# session; kept outside the denominator of the requested20-database audit.
la=read('evidence/file-audit-20261105/benchmarks/lamar.json')
i='lamar-circrna-multicell-output'
lr=base(i,'LAMAR multicell circRNA reporter-output panel','study','305IRES inserts in a shared synthetic circRNA reporter;3915observed sequence-cell pairs across13cell lines.',[la['article_url'],la['source']['url']],[label('Raw Activity','Reporter luminescence relative to modified linear mRNA control after mock subtraction','computed','relative activity','construct'),label('Predicted probability','LAMAR classification score; not experimental activity','prediction','probability','construct')],('circRNA',))
lr['topics']=['translation','cell_context','reporter_expression'];lr['paper_doi']=[la['doi']];lr['biological_context']='Shared Fluc circRNA reporter; mixed human/mouse cell lines;24-hour output; source-selected IRES candidates.'
lr['assays']=['Reporter luminescence'];lr['observation_unit']='IRES insert by cell line in shared reporter';lr['scale']=dict(value=3915,unit='observed sequence-cell pairs;305unique insert sequences',basis='All activity and metadata rows inspected; complete280-by13or305-by11subsets.',as_of=D)
lr['access'].update(data_urls=[la['source']['url']],formats=['XLSX']);lr['verification']=dict(level='file_sample',checked_on=D,evidence=[dict(url=la['source']['url'],supports='Full metadata/activity workbook joined byIRESID and counted')],files_inspected=[la['source']['url']],limitations=la['scope_limits']+['Methods report two replicates, but workbook contains one scalar per pair and no replicate uncertainty.','Cell-specific reference-mRNA normalization limits interpretation to relative reporter advantage.','Shared FlucCDS cannot identify a varying-CDS codon by tRNA-context interaction.'])
lr['cell_specificity']=dict(evidence='direct_multi_context',notes='Same inserts across named cells; relative output only, not intrinsic translation rate or arbitrary unseen-cell generalization.')
lr['integration_caveats']=lr['verification']['limitations'];lr['priority']='high'; r=get(i,lr);r.update(lr);add_payload(i,dict(url=la['source']['url'],bytes=la['source']['bytes'],sha256=la['source']['sha256'],checksum_scope='complete publisher source workbook'))
al=read('evidence/file-audit-20261105/benchmarks/albatross.json');i='albatross-circrna-polysome-atlas'
ar=base(i,'Albatross synthetic circRNA polysome-loading atlas','study','96IRES IDs across six cell lines;576ID-cell point estimates and SDs.',[al['sources']['paper'],al['sources']['geo_series'],al['sources']['processed_xlsx']],[label('Ribosomal_Loading','Weighted polysome-derived average ribosomes per RNA; not completed protein output','computed','ribosomes per RNA','construct'),label('SD','Released variability of ribosome-loading measurement','computed','ribosomes per RNA','construct')],('circRNA',))
ar['topics']=['translation','cell_context','polysome_loading']; ar['paper_doi']=[al['paper']['doi']];ar['accessions']=['GSE347508'];ar['assays']=['Polysome fractionation and barcode sequencing'];ar['biological_context']='Synthetic IVT circRNA library across five human lines and mouseN2A; preprint.'
ar['scale']=dict(value=576,unit='IRES-ID-cell rows',basis='96IDs by6cells; repeated/discordant sequence identities require reconciliation.',as_of=D);ar['access'].update(data_urls=[al['sources']['processed_xlsx']],formats=['XLSX'])
ar['verification']=dict(level='file_sample',checked_on=D,evidence=[dict(url=al['sources']['processed_xlsx'],supports='Full processed workbook, headers, loading and SD columns inspected')],files_inspected=[al['sources']['processed_xlsx']],limitations=['Preprint functional atlas is distinct from the Albatross structure model.','FiveIRES IDs have discordant sequence fields across sheets andDNA_IRES requires alias reconciliation; do not silently join all rows.','IRES reference has95unique sequences for96IDs; endpoint sequence fields have92unique sequences.','Two biological by two technical replicates are not four independent biological replicates.','Ribosome loading can reflect elongation or stalling; cannot directly validate protein-output accuracy.','Publisher/PMC and GEO workbook bytes differ; source versions and digests must remain explicit.'])
ar['cell_specificity']=dict(evidence='direct_multi_context',notes='Same reporter library across six named cells; loading endpoint only.');ar['integration_caveats']=ar['verification']['limitations'];ar['priority']='high';r=get(i,ar);r.update(ar)
add_payload(i,dict(url=al['sources']['processed_xlsx'],bytes=al['download_verified']['geo_xlsx_bytes'],sha256=al['download_verified']['geo_xlsx_sha256'],checksum_scope='complete GEO source workbook'))

if new:
    additions=fragments.setdefault('file_audit_additions.json',[])
    present={r['id'] for r in additions}
    additions.extend(r for r in new if r['id'] not in present)
for name,rows in fragments.items():save('catalog/fragments/'+name,rows)
save('evidence/file-audit-20261105/verified_payloads.json',dict(audit_date=D,scope='Selected successful source bodies. API hashes are request-specific; partial hashes never certify entire files.',files=payloads))
joins=read(cp+'reporter_cell_intersections.json')
raw_lamar={'HepG2':'Hepg2','Neuro-2a':'Neruo-2a ','SH-SY5Y':'SY5Y'}
raw_albatross={'HEK293T':'293t','SH-SY5Y':'SHSY5Y','mouse N2A':'N2A'}
for j in joins['joins']:
    mapping=raw_lamar if j['study']=='LAMAR13' else raw_albatross
    j['source_label_raw']=mapping.get(j['source_label'],j['source_label'])
    j['permitted_use']='candidate external baseline proxy only; no matched assay-condition claim'
joins['audit_date']=D
joins['source_provenance']=['evidence/file-audit-20261105/cell-context/reporter_cell_intersections.json','evidence/file-audit-20261105/benchmarks/lamar.json','evidence/file-audit-20261105/benchmarks/albatross.json','evidence/file-audit-20261105/auxiliary/audit.json']
save('catalog/cell_context_join_manifest.json',joins)
plan=dict(audit_date=D,model_trained=False,reliability_demonstrated=False,task_contracts=[
    dict(task='endogenous_mrna_te',label_resource='p010-asset-2',endpoint=rb['endpoint'],feature_resources=['human-protein-atlas-rna','depmap-ccle-expression'],status='scoped supervised benchmark feasible; external context remains a proxy',required_tests=['sequence/gene-family holdout','cell holdout','joint sequence/cell holdout','increment over cell/sequence/additive baselines','upstream study deduplication']),
    dict(task='synthetic_circrna_relative_output',label_resource='lamar-circrna-multicell-output',feature_resources=['human-protein-atlas-rna','depmap-ccle-expression','cellosaurus'],status='assay-specific benchmark feasible; candidate cell identities need review',endpoint='Relative reporter luminescence against a cell-specific linear mRNA reference',limits=['few independent contexts','reference normalization','no released replicate uncertainty','fixed Fluc CDS','no matched RNA persistence']),
    dict(task='synthetic_circrna_loading',label_resource='albatross-circrna-polysome-atlas',status='separate loading task; sequence joins need reconciliation',endpoint='polysome-derived ribosomes per RNA',limits=['not direct protein-output validation','preprint','conflicting sequence fields']),
    dict(task='functional_trna_by_cds',status='not supported by inspected matched data',limits=['circ reporter shared CDS','tRNA condition/schema conflicts','no matched CDS-varying protein-output panel']),
    dict(task='endogenous_rna_sensor_performance',status='not supported by these databases alone',limits=['no paired sensor activation/leakage/protein-output table','expression/accessibility are component evidence'])],forbidden_pools=['protein output with ribosome loading or endogenousTE residuals','predicted coding potential with experimental translation output','HPA and DepMap as independent biological replicates','tRNA abundance with charging or gene copy number','cell-name overlaps as exact condition matches'])
save('catalog/combination_plan.json',plan)

# Review corrections for original model cards; model inventory membership is unchanged.
models=read('catalog/models.json')
for m in models:
    if m['id']=='P010':
        m['inputs']='Full mRNA sequence plus coding-frame annotations; standard multitask inference does not require a measured cell-state vector.'
        m['outputs']='Context-specific endogenous TE residual predictions through output heads for contexts represented during training.'
        m['remaining_gaps']=[x for x in m['remaining_gaps'] if x!='Actual supplementary workbooks not inspected in this pass.']
        note='All original Human-table rows and TE columns were parsed; mouse and predicted-TE supplements were not inspected. Source-context/species metadata and ContiTE preprocessing remain to reconcile.'
        m['remaining_gaps']=unique(m['remaining_gaps']+[note])
    if m['id']=='P029':
        m['inputs']='UTR sequence, explicit cell-line identity and sequence annotations; original training panel covers six cell lines.'
        m['outputs']='Post-transcriptional reporter activity and deviation from across-cell mean, plus candidate UTR designs; activity includes RNA stability effects.'
    if m['id']=='P032':
        m['inputs']='CDS sequence, target mRNA abundance and RNA-seq cellular-expression profile; measured tRNA supply is not an explicit standard input.'
        m['outputs']='ln(5 * Ribo-seq RPKM + 1) prediction, MFE surrogate and synonymous candidate designs; not RNA-normalized TE or direct protein production per RNA.'
save('catalog/models.json',models)
print(json.dumps(dict(audited_resources=len(summary),selected_payloads_inspected=sum(x['selected_data_or_reference_payload_inspected'] for x in summary),new_resource_records=len(new),verified_payload_records=len(payloads))))
