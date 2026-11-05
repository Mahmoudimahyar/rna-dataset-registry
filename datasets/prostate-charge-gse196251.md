# Prostate-cell GCN2 CHARGE-seq study

Registry ID: `prostate-charge-gse196251` · study · **curated** · verification: **schema**

Dedicated tRNA-charging measurements in a prostate-cancer treatment context.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: LNCaP WT cells: DMSO, GCN2iB and GCN2iB plus essential amino acids; four samples per group.
- Assays: CHARGE-seq
- Accessions: GSE196251
- Scale: value: 12; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| unnormalized end-state read counts | Input counts for charge estimation; not itself a validated charged fraction | computed | reads | transcript |
| charged fraction | Derived charged-to-total tRNA endpoint described by the paper | computed | fraction | transcript |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE196nnn/GSE196251/suppl/GSE196251_LNCaP_WT_CHARGEseq_readcounts_unnormalized.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE196nnn/GSE196251/suppl/GSE196251_LNCaP_WT_CHARGEseq_readcounts_unnormalized.csv.gz (CSV header only).

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- No numeric charge values or secondary header rows were inspected.

- Treatment-specific charging changes are distinct from total tRNA-abundance changes.
- CSV uses grouped multirow headers; only its first grouping line was inspected, so subordinate columns remain unresolved.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE196251&targ=self&form=text&view=quick
- https://elifesciences.org/articles/81083

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE196251&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://elifesciences.org/articles/81083; supports: Assay and biological measurement interpretation
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE196nnn/GSE196251/suppl/GSE196251_LNCaP_WT_CHARGEseq_readcounts_unnormalized.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected

Related models: not established. Related resources: charged-trnaseq-gse97259.
