# ALL-tRNAseq tissue and cell-line study

Registry ID: `all-trnaseq-gse186736` · study · **curated** · verification: **schema**

Dedicated assay retains full-length and fragmented tRNA signals to profile abundance together with sample integrity.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Human clinical glioblastoma and diffuse large B-cell lymphoma tissues, comparison tissues, cell lines and hESC differentiation examples.
- Assays: ALL-tRNAseq
- Accessions: GSE186736
- Scale: value: 58; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| anticodon RPM: all tRNA | Relative abundance including tRNA-derived fragments | computed | RPM | transcript |
| anticodon RPM: full-length tRNA | Separate abundance table restricted to full-length species | computed | RPM | transcript |
| read length | Integrity/fragmentation-associated distribution, not abundance alone | computed | nucleotides | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tRNA_readlength_cell-lines.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tissues_anticodon_RPM_all_tRNA.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tissues_anticodon_RPM_full-length_tRNA.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tRNA_readlength_cell-lines.csv.gz (CSV header only); https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tissues_anticodon_RPM_all_tRNA.csv.gz (CSV header only); https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tissues_anticodon_RPM_full-length_tRNA.csv.gz (CSV header only).

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Header discrepancy preserved: one all-tRNA column is GBM_55 while full-length table uses GBM_VU55; sample equivalence was not established.

- All-tRNA and full-length tables use distinct definitions; do not merge their values.
- GtRNAdb hg38 nuclear references and mitochondrial references; assay handling and clinical RNA quality affect fragmentation.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE186736&targ=self&form=text&view=quick
- https://doi.org/10.1101/gad.350233.122

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE186736&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://doi.org/10.1101/gad.350233.122; supports: Assay and biological measurement interpretation
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tRNA_readlength_cell-lines.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tissues_anticodon_RPM_all_tRNA.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186736/suppl/GSE186736_tissues_anticodon_RPM_full-length_tRNA.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected

Related models: not established. Related resources: gtrnadb.
