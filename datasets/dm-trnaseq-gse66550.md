# DM-tRNA-seq method study

Registry ID: `dm-trnaseq-gse66550` · study · **curated** · verification: **metadata**

Original dedicated tRNA-sequencing study comparing demethylase-treated and untreated human material.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: HEK293T; tRNA versus total-RNA input and assay-treatment comparisons.
- Assays: DMTRT-tRNA-seq / DM-tRNA-seq
- Accessions: GSE66550
- Scale: value: 8; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| raw read count | Mapped tRNA read count in source processed files | computed | reads | transcript |
| demethylase condition | Assay-treatment label, not a biological cell state | annotation | unknown | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE66nnn/GSE66550/suppl/GSE66550_GEO_Processing.txt.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE66nnn/GSE66550/suppl/GSE66550_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- GSE66550 is a method-development dataset, not a multi-tissue atlas.

- Selected sample declares hg19 and tab-delimited gene-ID/raw-count files.
- Demethylation changes recoverability; treated and untreated counts are not interchangeable. Identical mature sequences cannot resolve genomic origin.

## Cell specificity

evidence: context_only; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE66550&targ=self&form=text&view=quick
- https://www.nature.com/articles/nmeth.3478

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE66550&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://www.nature.com/articles/nmeth.3478; supports: Assay and biological measurement interpretation

Related models: not established. Related resources: gtrnadb.
