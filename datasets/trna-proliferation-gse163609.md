# tRNA-pool proliferation and cell-cycle-arrest study

Registry ID: `trna-proliferation-gse163609` · study · **curated** · verification: **metadata**

Dedicated tRNA profiling within a study of tRNA-family dependence during cellular growth and arrest.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Induced HeLa iCas9 control and tRNA-family perturbation backgrounds over time.
- Assays: tRNA-seq
- Accessions: GSE163609
- Scale: value: 40; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| mature-tRNA abundance | Source relative expression/count matrix; normalization requires file-level follow-up | computed | unknown | transcript |
| indel signal | Separate mutation-associated matrix; not a tRNA-abundance label | computed | source-specific | transcript |
| condition | Perturbation identity and collection day | annotation | unknown | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE163nnn/GSE163609/suppl/GSE163609_maturetRNA_Indel_tRNAtargetedHeLa_rep1.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE163nnn/GSE163609/suppl/GSE163609_maturetRNA_Indel_tRNAtargetedHeLa_rep2.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE163nnn/GSE163609/suppl/GSE163609_maturetRNA_tRNAtargetedHeLa_rep1.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE163nnn/GSE163609/suppl/GSE163609_maturetRNA_tRNAtargetedHeLa_rep2.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- No perturbation sequences, implementation details or processed measurement rows were retrieved. Exact tRNA reference and normalization not established.

- GSE163609 is tRNA-seq within GSE163611; cellular-growth/arrest phenotypes are distinct endpoints.
- Perturbed cell populations do not establish normal tissue distributions. Preserve condition, time and replicate keys.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE163609&targ=self&form=text&view=quick
- https://elifesciences.org/articles/58461

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE163609&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://elifesciences.org/articles/58461; supports: Assay and biological measurement interpretation

Related models: not established. Related resources: gtrnadb.
