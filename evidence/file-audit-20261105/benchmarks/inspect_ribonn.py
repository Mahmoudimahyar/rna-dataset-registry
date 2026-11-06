"""Audit the original human RiboNN experimental-label supplement, not examples.
Usage: python inspect_ribonn.py --source downloaded.xlsx --output audit.json
Requires read-only openpyxl. No transcript sequences are written to the evidence.
"""
from pathlib import Path
import argparse, collections, hashlib, json, math
import openpyxl

p=argparse.ArgumentParser(); p.add_argument('--source',required=True); p.add_argument('--output',required=True); a=p.parse_args()
source=Path(a.source)
w=openpyxl.load_workbook(source,read_only=True,data_only=True)
s=w['Human']; it=s.iter_rows(values_only=True); header=list(next(it)); ti=[i for i,x in enumerate(header) if str(x).startswith('TE_')]
rows=0; ids=collections.Counter(); txs=collections.Counter(); folds=collections.Counter(); valid=collections.Counter(); nulls=collections.Counter(); ranges={header[i]:[math.inf,-math.inf] for i in ti}; lengths=[]; all_rows_numeric=0
for row in it:
    if not any(v is not None for v in row): continue
    rows+=1; d=dict(zip(header,row)); ids[str(d['gene_id'])]+=1; txs[str(d['tx_id'])]+=1; folds[str(d['fold'])]+=1
    if d['tx_sequence'] is not None: lengths.append(len(str(d['tx_sequence'])))
    n=0
    for i in ti:
        v=row[i]; k=header[i]
        if isinstance(v,(int,float)) and math.isfinite(v):
            valid[k]+=1; n+=1; ranges[k][0]=min(ranges[k][0],v); ranges[k][1]=max(ranges[k][1],v)
        else: nulls[k]+=1
    if n==len(ti): all_rows_numeric+=1
assert rows>0 and len(ids)==rows and len(txs)==rows
out=dict(audit_date='2026-11-05',source_url='https://static-content.springer.com/esm/art%3A10.1038%2Fs41587-025-02712-x/MediaObjects/41587_2025_2712_MOESM3_ESM.xlsx',source_filename='41587_2025_2712_MOESM3_ESM.xlsx',bytes=source.stat().st_size,sha256=hashlib.sha256(source.read_bytes()).hexdigest(),checksum_scope='complete original publisher workbook',scope='All nonempty Human sheet rows and all TE columns parsed; sequences used only for length/identity audit and not redistributed.',sheet='Human',rows=rows,columns=header,te_context_columns=[header[i] for i in ti],te_contexts=len(ti),unique_genes=len(ids),unique_transcripts=len(txs),numeric_te_observations=sum(valid.values()),complete_across_all_contexts_rows=all_rows_numeric,numeric_per_context=dict(valid),missing_or_nonnumeric_per_context=dict(nulls),fold_counts=dict(folds),transcript_length_min_max=[min(lengths),max(lengths)],te_value_ranges=ranges,endpoint='Study-derived endogenous mRNA translation-efficiency estimates; retain source-specific processing and normalization. Not measured completed protein output or synthetic reporter labels.',provenance_cautions=['GitHub example training table is explicitly fake TE in README; not used as biological labels.','ContiTE reuses the RiboNN atlas; it is not an independent experimental dataset.','ContiTE article states different counts from this inspected original Human supplement; reconcile exact input versions before reproducing or comparing.','Publisher Supplementary Tables3/4 contain predicted TEs and must not be treated as measured labels.','Same gene across contexts is a repeated observation, not a new independent sequence.','No uniformly matched external HPA/DepMap assay condition established.'])
out['endpoint']='Endogenous TE defined by the original paper as residuals from compositional linear regression of centered-log-ratio CDS RPF/RNA counts, then averaged within cell context. Not raw Ribo/RNA ratios, completed protein output, or synthetic reporter labels.'
out['endpoint_source']='https://www.nature.com/articles/s41587-025-02712-x'
out['endpoint_source_section']='Methods: calculation of cell-type-specific translation efficiencies'
out['context_identity_caution']='The Human sheet is a human-transcript benchmark, not independent verification of every context species or stock. In particular, TE_Vero_6 requires source-metadata reconciliation before assigning a human cell identity.'
Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:out[k] for k in ['rows','unique_genes','te_contexts','numeric_te_observations','complete_across_all_contexts_rows','fold_counts']},indent=2))
