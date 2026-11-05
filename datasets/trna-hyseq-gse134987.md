# tRNA-HySeq yeast PAF1/Rtf1 study

Registry ID: `trna-hyseq-gse134987` · study · **curated** · verification: **metadata**

Dedicated hydrolysis-based tRNA-pool profiling in transcription-complex mutants.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Log-phase wild-type, paf1 deletion and rtf1 deletion Saccharomyces cerevisiae.
- Assays: tRNA-HySeq
- Accessions: GSE134987
- Scale: value: 6; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| tRNA pool read count | Source processed tRNA counts; exact normalization not established | computed | unknown | transcript |
| genotype | WT, paf1 deletion or rtf1 deletion | annotation | unknown | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE134nnn/GSE134987/suppl/GSE134987_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.

- Six sample records represent two replicates per genotype.
- Hydrolysis-derived read fragments and endogenous tRNA fragments are different entities. Reference release and table schema require follow-up.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE134987&targ=self&form=text&view=quick
- https://www.nature.com/articles/s41598-019-49316-5

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE134987&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://www.nature.com/articles/s41598-019-49316-5; supports: Assay and biological measurement interpretation

Related models: not established. Related resources: gtrnadb.
