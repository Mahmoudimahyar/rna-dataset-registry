# Five-cell-line hydro-tRNAseq / small-RNA-seq comparison

Registry ID: `hydro-smallrna-comparison-gse137834` · study · **curated** · verification: **schema**

Matched assay comparison testing tRNA estimates from ordinary small-RNA sequencing against a dedicated hydrolysis assay.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: HEK293, HCT116, HeLa, MDA-MB-231 and BJ fibroblasts.
- Assays: hydro-tRNAseq; ordinary small RNA-seq
- Accessions: GSE137834
- Scale: value: 30; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RPM matrix | Source tRNA estimates for both methods; retain assay suffix | computed | RPM | transcript |
| assay / cell line / replicate | Explicitly encoded sample-column labels | annotation | unknown | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE137nnn/GSE137834/suppl/GSE137834_rpm_matrix.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE137nnn/GSE137834/suppl/GSE137834_rpm_matrix.csv.gz (CSV header only).

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- CSV header verifies 30 assay-labelled columns; exact mapping reference/version was not rechecked.

- Paired assay agreement in these cell lines does not eliminate fragment and modification biases in all small-RNA studies.
- Hydrolysis fragments and naturally occurring tRNA fragments must remain distinguished.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE137834&targ=self&form=text&view=quick
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7061310/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE137834&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7061310/; supports: Assay and biological measurement interpretation
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE137nnn/GSE137834/suppl/GSE137834_rpm_matrix.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected

Related models: not established. Related resources: gtrnadb.
