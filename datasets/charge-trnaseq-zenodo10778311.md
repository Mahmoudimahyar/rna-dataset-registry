# Charge tRNA-Seq validation and aminoacylation-decay study

Registry ID: `charge-trnaseq-zenodo10778311` · study · **curated** · verification: **metadata**

Dedicated aminoacylation assay validation with baseline charging and ex-vivo aminoacylation half-life measurements.

## What the data contains

- Observation unit: tRNA transcript charge by sample/timepoint
- RNA scope: tRNA
- Biological context: Human H1299 baseline samples and purified-RNA decay time course; assay calibration controls.
- Assays: charge tRNA-Seq
- Accessions: Zenodo:10778311; Zenodo:8200906
- Scale: value: unknown; unit: unknown; basis: No sample-level manifest counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| charge | Source charged fraction or percentage | computed | fraction / percent | transcript |
| aminoacylation half-life | Fit to charge decay in purified RNA; not cellular tRNA turnover | computed | source time units | transcript |

## Access and reuse

- Access: open
- Formats: split tar.gz archive listed; not downloaded
- Source license: CC-BY-4.0 (Zenodo record metadata)
- Redistribution: Permitted under CC-BY-4.0 subject to attribution and source terms

- https://zenodo.org/records/10778311

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Only Zenodo metadata inspected; archive parts and processed table schemas were not downloaded.
- Cited identifier 8200906 resolves to version DOI 10778311 in repository metadata; preserve version.

- Polymerase and reference masking affect relative-expression recovery; charge validation does not establish absolute abundance accuracy.
- Ex-vivo charge decay is not in-vivo cell-state regulation.

## Cell specificity

evidence: context_only; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://elifesciences.org/articles/91554
- https://zenodo.org/api/records/10778311
- https://doi.org/10.5281/zenodo.8200906

- url: https://elifesciences.org/articles/91554; supports: H1299 context, charging and purified-RNA decay endpoints; source reference uses deduplicated hg38 GtRNAdb plus mitochondrial/control entries
- url: https://zenodo.org/api/records/10778311; supports: Repository title, version DOI, open access and CC-BY-4.0 metadata; split archive file listing

Related models: not established. Related resources: charged-trnaseq-gse97259; gtrnadb.
