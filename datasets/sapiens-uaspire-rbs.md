# uASPIre/SAPIENs bacterial RBS data

Registry ID: `sapiens-uaspire-rbs` · study · **curated** · verification: **metadata**

RBS strength data from DNA-based phenotypic recording; upstream benchmark reused by SANDSTORM.

## What the data contains

- Observation unit: RBS variant with source activity target
- RNA scope: mRNA
- Biological context: Bacterial expression assay; no mammalian cell panel.
- Assays: uASPIre DNA-based phenotypic recording
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RBS strength / IFP0-480 min | Activity target from integrated DNA flipping profile | computed | source-defined activity scale | construct |

## Access and reuse

- Access: open
- Formats: NPY; figure source data
- Source license: CC BY-NC-ND 4.0 for data directory; code has separate terms
- Redistribution: Noncommercial unadapted data sharing with attribution; assess derivatives separately

- https://github.com/BorgwardtLab/SAPIENs/tree/main/data

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://raw.githubusercontent.com/BorgwardtLab/SAPIENs/main/data/Readme.md; https://raw.githubusercontent.com/BorgwardtLab/SAPIENs/main/data/LICENSE.md.

- Binary arrays not inspected/count-validated.
- Exact target transform requires source ML annex.
- Paper's raw-sample list repeats an identifier; not silently repaired.

- Preserve Split0 and sample-subset identities.
- SANDSTORM reuse is not independent data.

## Cell specificity

evidence: context_only; notes: Bacterial RBS output is not human cap-dependent translation.

## Sources

- https://github.com/BorgwardtLab/SAPIENs
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7363850/

- url: https://github.com/BorgwardtLab/SAPIENs; supports: Train/validation/test arrays; documented Split0.
- url: https://raw.githubusercontent.com/BorgwardtLab/SAPIENs/main/data/LICENSE.md; supports: Data-specific CC BY-NC-ND 4.0.
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7363850/; supports: Measured assay identity and activity endpoint.

Related models: P012. Related resources: gardn-sandstorm-release.
