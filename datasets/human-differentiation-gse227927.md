# Selective gene expression maintains human tRNA anticodon pools during differentiation

Registry ID: `human-differentiation-gse227927` · study · **curated** · verification: **schema**

Dedicated human differentiation tRNA subseries; the broader study also has distinct ChIP, ATAC, RNA and ribosome-profiling subseries.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: WT hiPSC, neural progenitor cells, mature neurons and cardiomyocytes; two transcript-count columns per state.
- Assays: mim-tRNAseq
- Accessions: GSE227927
- Scale: value: 8; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Unique tRNA transcript counts | Source count matrix indexed by unique tRNA rather than guaranteed unique gene locus | computed | reads | transcript |
| differentiation state | hiPSC, NPC, neurons, CM | annotation | unknown | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE227nnn/GSE227927/suppl/GSE227927_mimtRNAseq_transcriptCounts.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE227nnn/GSE227927/suppl/GSE227927_mimtRNAseq_transcriptCounts.csv.gz (CSV header only).

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Header verifies WT_k_hiPSC/NPC/neurons/CM rep1/rep2. Exact mapping-reference release not independently inspected.

- GSE227927 is the tRNA subseries of GSE227928; do not add counts across assay subseries as independent subjects.
- Near-identical transcripts differing at modification-sensitive sites may remain unresolved. Transcript shifts must not be equated with anticodon-pool shifts.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE227927&targ=self&form=text&view=quick
- https://www.nature.com/articles/s41556-023-01317-3

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE227927&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://www.nature.com/articles/s41556-023-01317-3; supports: Assay and biological measurement interpretation
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE227nnn/GSE227927/suppl/GSE227927_mimtRNAseq_transcriptCounts.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected

Related models: not established. Related resources: gtrnadb.
