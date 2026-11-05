# MSR-seq stress and polysome-associated tRNA study

Registry ID: `msr-stress-gse198441` · study · **curated** · verification: **metadata**

Specialized multiplex small-RNA assay with tRNA abundance and modification signals, alongside separate mRNA libraries.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA; mRNA
- Biological context: Human HEK293T total and polysome-associated RNA under control, heat, peroxide and arsenite stresses; MCF7 modification controls.
- Assays: MSR-seq; paired mRNA-seq
- Accessions: GSE198441
- Scale: value: 64; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| tRNA abundance | Mapped tRNA counts/relative abundance by cellular fraction | computed | source-specific | transcript |
| RT stop / mismatch fractions | Modification-associated signals, assay-treatment dependent | computed | fraction | position |
| fraction / stress / RT condition | Separate total versus polysome and assay labels | annotation | unknown | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE198nnn/GSE198441/suppl/GSE198441_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Large processed TSV archive was not downloaded; per-position schema and charging outputs not verified.

- 64 series records include assay optimization and mRNA samples; not 64 comparable tRNA biological samples.
- Source sample lists hg19/hg38 usage; total, fragment and polysome-associated tRNA populations are distinct.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198441&targ=self&form=text&view=quick
- https://www.nature.com/articles/s41467-022-30261-3

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198441&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://www.nature.com/articles/s41467-022-30261-3; supports: Assay and biological measurement interpretation

Related models: not established. Related resources: gtrnadb; modomics.
