from audit_fetch import *
import pandas as pd, re
from bs4 import BeautifulSoup

for name in ['postar3_redirect_download.html']:
    soup=BeautifulSoup((D/name).read_text(),'html.parser')
    links=[{'label':a.get_text(' ',strip=True),'href':a.get('href')} for a in soup.find_all('a',href=True)]
    save_meta('postar3_download_links',{'links':links})
    print('POSTAR',links[:35],flush=True)
for name in ['ENCFF356YQN.tsv','ENCFF957CWU.tsv','ENCFF644GCJ.tsv']:
    if (D/name).exists(): print(name,(D/name).read_text()[:1000],flush=True)
print('BED',gzip.open(D/'ENCFF593RED.bed.gz','rt').readline(),flush=True)
for name in ['encode_eclip.json','encode_knockdown.json','encode_rbns_files.json']:
    j=json.loads((D/name).read_text()); print(name,[{k:x.get(k) for k in ['accession','dataset','target','assembly','biological_replicates','biosample_ontology','output_type']} for x in j['@graph'][:2]],flush=True)
print('DEPHEADER',(D/'depmap_Expression_24Q4.csv').open().readline()[:400],flush=True)

hpa_tables=pd.read_html(io.StringIO((D/'hpa_cell_metadata.html').read_text()))
hpa_meta=next(t for t in hpa_tables if 'Cellosaurus ID' in t.columns)
targets={'A204':'CVCL_1058','A549':'CVCL_0023','AGS':'CVCL_0139','HCT116':'CVCL_0291','HepG2':'CVCL_0027','JURKAT':'CVCL_0065','SH-SY5Y':'CVCL_0019','THP-1':'CVCL_0006','U87':'CVCL_0022','Huh7':'CVCL_0336','HCT8':'CVCL_2478','U2OS':'CVCL_0042','HEK293T':'CVCL_0063'}
hm=hpa_meta[hpa_meta['Cellosaurus ID'].isin(targets.values())].fillna('unknown')
save_meta('hpa_requested_cell_metadata',{'source_url':'https://www.proteinatlas.org/humanproteome/cell+line/data','release':'25.1','total_cell_metadata_rows':len(hpa_meta),'requested_candidates_by_rrid':targets,'rows':hm.to_dict('records'),'caveat':'Candidate name-to-RRID harmonization requires source-study provenance; U87 not silently resolved beyond source name.'})
print('HPACELLS',hm[['Cell line','Cellosaurus ID']].to_dict('records'),flush=True)
z=zipfile.ZipFile(D/'hpa_rna_celline_v25.tsv.zip'); names=z.namelist(); count=0; genes=set(); cells=set(); selected=[]
with z.open(names[0]) as f:
    for chunk in pd.read_csv(f,sep='\t',chunksize=500000):
        headers=list(chunk.columns); count+=len(chunk); genes.update(chunk['Gene']); cells.update(chunk['Cell line'])
        take=chunk[chunk['Cell line'].isin(hm['Cell line']) & chunk['Gene'].isin(['ENSG00000000003','ENSG00000198793','ENSG00000125347','ENSG00000105255'])]
        if not take.empty: selected.extend(take.to_dict('records'))
pd.DataFrame(selected).to_csv(D/'hpa_requested_numeric_slice.tsv',sep='\t',index=False)
save_meta('hpa_file_inspection',{'source_url':'https://www.proteinatlas.org/download/tsv/rna_celline.tsv.zip','release':'25.1','archive_member':names[0],'full_rows_counted':count,'genes_counted':len(genes),'cells_counted':len(cells),'columns':headers,'numeric_slice_rows':len(selected),'numeric_slice_artifact':'hpa_requested_numeric_slice.tsv','cell_names_present':sorted(cells),'sample_rows':selected[:2],'readout':'gene expression, TPM/pTPM/nTPM; not protein abundance or translation efficiency','replicates':'aggregate file has no replicate column','condition':'cell-line profile; culture/batch/perturbation matching to LAMAR13 and Albatross not established','license':'HPA copyrightable parts CC BY 4.0; third-party constraints may apply','license_url':'https://www.proteinatlas.org/about/licence'})
print('HPACOUNT',count,len(genes),len(cells),len(selected),flush=True)
