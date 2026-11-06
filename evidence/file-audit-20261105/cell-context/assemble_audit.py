"""Summarize inspection, counts, joins and proposed updates without copying bulk data."""
from audit_fetch import *
import pandas as pd

def meta(name): return json.loads((M/name).read_text())
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return {'artifact_name':p.name,'bytes':p.stat().st_size,'sha256':h.hexdigest(),'sha256_scope':'complete local artifact'}
def read_table(name,sep='\t',skiprows=0):
    f=pd.read_csv(D/name,sep=sep,skiprows=skiprows)
    return {'artifact_name':name,'full_rows_counted':len(f),'columns':list(f.columns),'sample_rows':f.head(2).fillna('unknown').to_dict('records')}

models=pd.read_csv(D/'depmap_Model_24Q4.csv'); profiles=pd.read_csv(D/'depmap_OmicsProfiles_24Q4.csv')
target_ids=['CVCL_1058','CVCL_0023','CVCL_0139','CVCL_0291','CVCL_0027','CVCL_0065','CVCL_0019','CVCL_0006','CVCL_0022','CVCL_0336','CVCL_2478','CVCL_0042','CVCL_0063']
matched=models[models['RRID'].isin(target_ids)].copy(); model_ids=set(matched['ModelID'])
full_count=0; all_ids=[]; slices=[]; headers=None
for chunk in pd.read_csv(D/'depmap_Expression_24Q4.csv',chunksize=100):
    headers=list(chunk.columns); full_count+=len(chunk); all_ids.extend(chunk.iloc[:,0].tolist())
    cols=[headers[0]]+[x for x in headers if x.startswith(('TSPAN6 (','YTHDF3 (','EIF4G2 (','PABPC1 (','HNRNPU (','ADAR (','METTL3 ('))]
    sub=chunk[chunk.iloc[:,0].isin(model_ids)][cols]
    if len(sub): slices.append(sub)
slice_df=pd.concat(slices,ignore_index=True); slice_df.to_csv(D/'depmap_requested_numeric_slice.tsv',sep='\t',index=False)
matched['numeric_expression_present']=matched['ModelID'].isin(all_ids)
dm_rows=matched[['ModelID','CellLineName','StrippedCellLineName','RRID','numeric_expression_present','GrowthPattern','OnboardedMedia','ModelTreatment','EngineeredModel']].fillna('unknown').to_dict('records')
save_meta('depmap_file_inspection',{'source_url':'https://api.figshare.com/v2/articles/27993248','release':'DepMap Public 24Q4','latest_release_claim':False,'full_expression_rows_counted':full_count,'gene_columns_counted':len(headers)-1,'identifier_column':headers[0],'identifier_type':'ModelID ACH-*','gene_header_examples':headers[1:6],'models_metadata_rows':len(models),'profiles_metadata_rows':len(profiles),'matched_requested_models':dm_rows,'numeric_slice_rows':len(slice_df),'numeric_slice_columns':list(slice_df.columns),'sample_rows':slice_df.head(2).to_dict('records'),'numeric_slice_artifact':'depmap_requested_numeric_slice.tsv','readout':'log2(TPM+1) protein-coding-gene RNA expression, computed from measured RNA-seq','replicates':'one aggregate/model matrix row; profile metadata may include multiple RNA profiles; not independently matched to source-study replicate','condition':'ModelTreatment and media available in Model.csv; not same-batch evidence for reporter studies','license':'CC BY 4.0 from release Figshare metadata','latest_download_endpoint_status':'200 HTML challenge, not biological CSV','limitations':['Human cancer cell line reference; mouse lines C2C12/Neuro-2a/RAW264.7/N2A not represented by this table.','HEK293T absent among exact requested RRID candidates in this Model.csv.','U87 source shorthand requires identity validation; CVCL_0022 is U-87 MG and must not be silently assigned.','HPA incorporates CCLE-derived RNA; HPA and DepMap are not necessarily independent evidence.']})
dm_report=meta('depmap_file_inspection.json')
dm_report['requested_model_metadata_matches']=len(dm_rows)
dm_report['requested_model_numeric_matches']=sum(x['numeric_expression_present'] for x in dm_rows)
dm_report['limitations'].append('HCT-8 ACH-001084 exists in Model.csv but has no row in this selected expression matrix; metadata availability is not numeric expression coverage.')
save_meta('depmap_file_inspection',dm_report)

encode=[]
for key,fn in [('eclip','ENCFF593RED.bed.gz'),('eclip','ENCFF897MSA.bed.gz'),('knockdown','ENCFF644GCJ.tsv'),('knockdown','ENCFF060HYJ.tsv'),('rbns','ENCFF335XEM.tsv')]:
    search=json.loads((D/('encode_'+({'rbns':'rbns_files'}.get(key,key))+'.json')).read_text())
    accession=fn.split('.')[0]
    f=next((x for x in search['@graph'] if x['accession']==accession),{})
    if key=='rbns':
        ex=json.loads((D/'encode_rbns_experiment.json').read_text());f=next(x for x in ex['files'] if isinstance(x,dict) and x['accession']==accession)
    rec={k:f.get(k) for k in ['accession','dataset','assembly','biological_replicates','technical_replicates','output_type','file_format','genome_annotation']}
    bio=f.get('biosample_ontology',{})
    rec.update(target=f.get('target',{}).get('label') if isinstance(f.get('target'),dict) else None,source_url='https://www.encodeproject.org'+f.get('href',''),context=bio.get('term_name') if isinstance(bio,dict) else bio)
    if fn.endswith('.gz'):
        with gzip.open(D/fn,'rt') as b: rows=[line.rstrip('\n').split('\t') for line in b]
        rec.update(full_rows_counted=len(rows),header_in_file=False,column_count=len(rows[0]),sample_rows=rows[:2],column_semantics='BED6+4; numeric score/signal fields retained; exact extra-field semantics not inferred from values alone',readout='RBP-binding peak interval, not translation output')
    else:
        rec.update(read_table(fn));rec['readout']='in vitro YBX2 k-mer enrichment ratio at listed nM concentrations' if key=='rbns' else 'RNA-seq transcript/gene quantification after DDX24 shRNA, not differential expression by itself'
    if key=='rbns':rec.update(context='cell-free sample',target='YBX2',biological_replicates=[1],concentrations_nM=[5,80,1300])
    rec.update(digest(D/fn));encode.append(rec)
save_meta('encode_file_inspection',{'verification_level':'file_sample','sample_scope':'five complete selected files; not entire ENCODE collection','files':encode,'license':'not independently verified; primary policy URL attempted returned 404','limitation':'K562 peak/RNA perturbation examples are not matched to the requested reporter-cell contexts; cell-free RBNS cannot establish cell-specific binding or translation.'})

z=zipfile.ZipFile(D/'postar3_ALKBH1.binding.sites.zip'); member=z.namelist()[0]
with z.open(member) as f: rows=[x.decode().rstrip('\n').split('\t') for x in f]
save_meta('postar3_file_inspection',{'source_url':'http://111.198.139.65/download/human_RBP/ALKBH1.binding.sites.zip','redirect_provenance':'https://postar.ncrnalab.org/ publishes canonical/meta-refresh link to http://111.198.139.65','archive_member':member,'full_selected_file_rows_counted':len(rows),'unique_site_ids':len(set(r[3] for r in rows)),'column_count':sorted(set(map(len,rows))),'header_in_file':False,'sample_rows':rows[:2],'rbps':sorted(set(r[6] for r in rows)),'cell_contexts':sorted(set(r[8] for r in rows)),'assay_pipeline_labels':sorted(set(r[7] for r in rows)),'source_accessions':sorted(set(r[9] for r in rows)),'identifiers':'genomic intervals, POSTAR binding-site ID, Ensembl gene|transcript, gene symbol, GEO source accessions','readout':'processed CLIP binding-site/transcript-overlap rows; not expression, affinity or translation','replicates':'not explicit in selected table; source GEO records needed','assembly':'not established from headerless selected table','condition':'HeLa label; culture/treatment not explicit','license':'unknown; accessibility is not redistribution permission','limitations':['One ALKBH1 file only; not full POSTAR3.','Multiple rows may repeat one binding site across transcript overlaps; site IDs and row counts must remain distinct.','22 columns observed but exact definitions of extra scores and assembly unresolved.']})

manifest=[]
for f in sorted(M.glob('*_fetch.json')):
    x=json.loads(f.read_text()); manifest.append(x)
save_meta('download_manifest',{'checked_on':'2026-11-05','entries':manifest,'note':'Each SHA refers only to the complete downloaded body or explicitly described prefix. A complete HTML/JSON response is not biological data.'})
save_meta('derived_slice_manifest',{'entries':[digest(D/x) for x in ['hpa_requested_numeric_slice.tsv','depmap_requested_numeric_slice.tsv']],'scope':'SHA values cover complete local derived slice artifacts only; full source file SHA values are separate in download_manifest.json.'})
release=json.loads((D/'census_release_correct.json').read_text())
save_meta('census_access_audit',{'resource':'CELLxGENE Census','verification_level':'metadata','source_url':'https://census.cellxgene.cziscience.com/cellxgene-census/v1/release.json','resolved_stable':release.get('stable'),'numeric_expression_rows_inspected':0,'sdk_attempt':'cellxgene-census installation attempted with bundled Windows Python; tiledbsoma had to build from source and native build failed.','unavailable_gap':'No actual numeric Census slice obtained; metadata does not meet file_sample verification.','license':'per-dataset/collection terms not inspected; API code license is not data license','recommended_next_step':'Use supported Linux/macOS environment and export a bounded real 10-cell x 3-gene slice with dataset_id, donor/assay/condition and raw-layer provenance.'})
save_meta('mirtarbase_access_audit',{'resource':'miRTarBase','verification_level':'metadata','source_url':'https://awi.cuhk.edu.cn/miRTarBase/downloads/releases/v11.0/','data_url':'https://awi.cuhk.edu.cn/miRTarBase/downloads/files/11.0/miRTarBase_MTI.csv','numeric_or_interaction_rows_inspected':0,'requests_result':'TLS handshake failure on current CSV and legacy official mirror; Windows native TLS request reached HTTP 403.','web_tool_result':'official release page inspected; direct CSV HTTP403','license':'unknown; linked LICENSE could not be fetched','unavailable_gap':'No actual MTI CSV rows inspected. Do not upgrade to file_sample.','semantic_caveat':'Validated interactions do not establish miRNA abundance/activity, a translation-gating dose-response, or identical activity across cell states.'})

hpa=meta('hpa_file_inspection.json');dep=meta('depmap_file_inspection.json');enc=meta('encode_file_inspection.json');post=meta('postar3_file_inspection.json')
requested={'LAMAR13':['A204','A549','AGS','C2C12','HCT116','HepG2','HFF1','JURKAT','Neuro-2a','RAW264.7','SH-SY5Y','THP-1','U87'],'Albatross':['HEK293T','HCT8','Huh7','SH-SY5Y','U2OS','mouse N2A']}
hpa_ids=set(meta('hpa_requested_cell_metadata.json')['requested_candidates_by_rrid'].values()); hm=meta('hpa_requested_cell_metadata.json')['rows']; hpa_cv={x['Cellosaurus ID']:x['Cell line'] for x in hm}; dm_cv={x['RRID']:x for x in dm_rows}
alias={'A204':'CVCL_1058','A549':'CVCL_0023','AGS':'CVCL_0139','HCT116':'CVCL_0291','HepG2':'CVCL_0027','JURKAT':'CVCL_0065','SH-SY5Y':'CVCL_0019','THP-1':'CVCL_0006','U87':'CVCL_0022','Huh7':'CVCL_0336','HCT8':'CVCL_2478','U2OS':'CVCL_0042','HEK293T':'CVCL_0063'}
cross=[]
for study,lines in requested.items():
    for line in lines:
        rid=alias.get(line); d=dm_cv.get(rid,{})
        cross.append({'study':study,'source_label':line,'candidate_rrid':rid,'hpa_numeric_cell_name':hpa_cv.get(rid),'depmap_numeric_model_id':d.get('ModelID') if d.get('numeric_expression_present') else None,'depmap_cell_name':d.get('CellLineName'),'identity_status':'U87 shorthand unresolved; candidate only' if line=='U87' else 'name-to-RRID mapping requires source identity confirmation; source variants preserved','source_label_notes':'LAMAR13 original typo Neruo-2a; no silent normalization to mouseN2A' if line=='Neuro-2a' else 'LAMAR13 source SY5Y; SH-SY5Y mapping needs identity confirmation' if study=='LAMAR13' and line=='SH-SY5Y' else 'mouse line; absent from human references' if line in ['C2C12','RAW264.7','mouse N2A'] else None,'matched_assay_condition':False})
save_meta('reporter_cell_intersections',{'joins':cross,'explicit_non_equivalences':['HEK293 is not HEK293T','HCT116 is not HCT8','JURKAT is not Jurkat E6.1','Neuro-2a/Neruo-2a/N2A require source/Cellosaurus confirmation','U87 must not be silently resolved as U-87 MG ATCC','A study cell-name overlap does not establish matched treatment, culture, passage, differentiation or batch'],'numeric_sources_verified':True})

updates=[
 {'id':'human-protein-atlas-rna','proposed_verification_level':'file_sample','scale':{'value':hpa['full_rows_counted'],'unit':'gene-cell-line rows in complete selected v25.1 file','basis':'counted all rows'},'files_inspected':['rna_celline.tsv.zip member rna_celline.tsv'],'limitations':['Full selected RNA cell-line matrix validated, not all HPA modalities.','HPA may contain CCLE-derived profiles; avoid double-counting independent biological evidence.']},
 {'id':'depmap-ccle-expression','record_action':'new candidate resource record; coordinator resolve existing ID','proposed_verification_level':'file_sample','scale':{'value':dep['full_expression_rows_counted'],'unit':'model rows in complete 24Q4 expression file','basis':'counted; gene columns separately counted'},'files_inspected':['Model.csv','OmicsProfiles.csv','OmicsExpressionProteinCodingGenesTPMLogp1.csv'],'limitations':['24Q4 inspected, not latest release.','Current endpoint returned HTML; exact no-newer-release claim not made.']},
 {'id':'encode','proposed_verification_level':'file_sample','scale':{'value':5,'unit':'selected biological files inspected','basis':'2 eCLIP BED + 2 knockdown quantifications + 1 RBNS enrichment'},'limitations':['File-sample scope only.','RBNS PWM files share enrichment output_type; inspect contents to distinguish PWM versus k-mer R tables.','Knockdown quantification alone is not a perturbational effect estimate.']},
 {'id':'postar3','proposed_verification_level':'file_sample','scale':{'value':post['full_selected_file_rows_counted'],'unit':'transcript-overlap rows in selected ALKBH1 file','basis':'complete selected archive member counted'},'limitations':['Do not report this as full database scale.','Assembly, extra scores, replicate provenance and redistribution terms remain unknown.']},
 {'id':'cellxgene-census','proposed_verification_level':'metadata','files_inspected':[],'limitations':['Actual small numeric slice not obtained; Windows TileDB-SOMA installation blocked.']},
 {'id':'mirtarbase','record_action':'new blocked/candidate resource record; coordinator resolve existing ID','proposed_verification_level':'metadata','files_inspected':[],'limitations':['Release webpage reachable, actual interactionCSV HTTP403/TLS failure.','License and row schema not verified.']}
]
save_meta('proposed_record_updates',{'not_applied':True,'updates':updates})
save_meta('audit_summary',{'checked_on':'2026-11-05','resources_investigated':6,'resources_with_actual_numeric_or_interval_rows':4,'resources_with_access_gaps':2,'hpa_rows':hpa['full_rows_counted'],'depmap_model_rows':dep['full_expression_rows_counted'],'encode_files':len(encode),'postar_selected_rows':len(rows),'combination_feasibility':{'feasible':'Build baseline cell-context features by Ensembl/Entrez mapping and validated cell identities; retain original study reporter translation labels separately.','not_supported':'A matched causal training table joining these context references to LAMAR13/Albatross conditions; miRNA activity labels from miRTarBase; direct protein-factor activity inferred from RNA abundance.','must_preserve':['species and cell lineage','cell stock/RRID and ambiguous aliases','release/version and gene annotation','RNA units vs protein/translation readouts','perturbation vs baseline','biological/technical replicate identity','missingness','overlapping upstream CCLE provenance']},'metadata_only_in_repo':True,'bulk_download_location':'external user-designated audit directory; no absolute paths stored'})
print(json.dumps({'hpa_rows':hpa['full_rows_counted'],'depmap_rows':full_count,'depmap_genes':len(headers)-1,'depmap_matches':len(dm_rows),'encode_file_rows':[(x['accession'],x['full_rows_counted']) for x in encode],'postar_rows':len(rows),'postar_unique_sites':len(set(r[3] for r in rows))}),flush=True)
