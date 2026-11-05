# hydro-tRNAseq and SSB/La PAR-CLIP atlas

Registry ID: `hydro-trnaseq-gse95683` · study · **curated** · verification: **metadata**

Dedicated hydrolysis-based tRNA profiling paired with precursor-binding information.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: HEK293 cells; four hydro-tRNAseq and two SSB/La PAR-CLIP samples in the source design.
- Assays: hydro-tRNAseq; SSB/La PAR-CLIP
- Accessions: GSE95683
- Scale: value: 6; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| mature / precursor abundance | Source transcript counts or expression estimates; processing classes must remain separate | computed | source-specific | transcript |
| processing and modification sites | Source sequence/RT-based annotation | annotation | unknown | position |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE95nnn/GSE95683/suppl/GSE95683_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Exact processed table schema and reference version not inspected.

- Hydrolysis generates technical fragments; these are not automatically endogenous tRNA-derived fragments.
- PAR-CLIP binding and pre-tRNA transcription are not equivalent to mature total tRNA abundance. Reference curation is study-specific.

## Cell specificity

evidence: context_only; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE95683&targ=self&form=text&view=quick
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5564215/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE95683&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5564215/; supports: Assay and biological measurement interpretation

Related models: not established. Related resources: gtrnadb.
