# Charged tRNA-seq aminoacylation study

Registry ID: `charged-trnaseq-gse97259` · study · **curated** · verification: **metadata**

Dedicated charged-fraction sequencing, derived from the DM-tRNA-seq assay family.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: HEK293T; three biological replicates each represented with and without demethylase treatment.
- Assays: Charged DM-tRNA-seq
- Accessions: GSE97259
- Scale: value: 6; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| charging fraction | Fraction of source end-state read counts attributed to charged tRNA; separate from total abundance | computed | fraction | transcript |
| demethylase treatment | Assay condition affecting recoverability | annotation | unknown | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE97nnn/GSE97259/suppl/GSE97259_Aggregate_Ratios.xlsx
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE97nnn/GSE97259/suppl/GSE97259_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Aggregate-ratio workbook schema and measurement cells were not inspected.

- GEO lists Aggregate_Ratios.xlsx and per-sample processed files.
- Charging depends on preservation and assay end-state definitions; a high total count does not imply high charged fraction.

## Cell specificity

evidence: context_only; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE97259&targ=self&form=text&view=quick
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5737633/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE97259&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5737633/; supports: Assay and biological measurement interpretation

Related models: not established. Related resources: dm-trnaseq-gse66550.
