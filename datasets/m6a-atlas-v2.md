# m6A-Atlas v2.0

Registry ID: `m6a-atlas-v2` · database · **curated** · verification: **file_sample**

m6A atlas with high-resolution sites, lower-resolution MeRIP regions, condition-specific profiles and separate single-cell modules.

## What the data contains

- Observation unit: A modification site or MeRIP interval within an experimental context; single-cell profiles remain a separate observation family.
- RNA scope: mRNA
- Biological context: Multiple species and experimental conditions; human and mouse single-cell modules are explicitly documented.
- Assays: base-resolution modification profiling; MeRIP-seq; scDART-seq; scm6A-seq
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| high-resolution m6A site | Site supported by a documented base-resolution assay. | computed | unknown | position |
| MeRIP m6A region | m6A-enriched interval; cannot be promoted to single-base ground truth. | computed | unknown | interval |
| condition-specific quantitative profile | Assay-derived methylation profile with source-specific normalization. | computed | unknown | position |
| single-cell m6A profile | Human scDART-seq or mouse scm6A-seq profile; preserve technology and cell identity. | computed | unknown | cell |

## Access and reuse

- Access: open
- Formats: CSV (documented DMR exports)
- Source license: unknown
- Redistribution: not established

- https://rnamd.org/m6a/help.php
- https://rnamd.org/m6a/download/high/hg38/Condition_hg38.txt.gz
- https://rnamd.org/m6a/download/high/hg38/hg38_CL_Tech.txt.gz
- https://www.rnamd.org/m6a/apiHighResolution.php?species=HomoSapiens&gene=EIF4G2

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://rnamd.org/m6a/download/high/hg38/Condition_hg38.txt.gz; https://rnamd.org/m6a/download/high/hg38/hg38_CL_Tech.txt.gz; https://www.rnamd.org/m6a/apiHighResolution.php?species=HomoSapiens&gene=EIF4G2.

- Help page gives inconsistent MeRIP sample totals in different sections; no single exact scale is asserted.
- 843678 support rows refer to427760 unique sites; do not treat support rows as independent modified positions
- High-resolution support and bulk quantification have different assay interpretations
- Quantification file read as bounded compressed prefix only; no full-file count or checksum claimed
- No full measured synthetic-RNA modification-to-protein output matrix
- Reported logFC values must not be interpreted as calibrated occupancy fractions
- Bounded file audit: evidence/file-audit-20261105/modification-trna/audit.json; selected coverage only.

- High-resolution sites, MeRIP intervals and single-cell profiles cannot share a single resolution label.
- Absent calls are not confirmed unmodified controls.
- Quantitative profiles from distinct assays and conditions require compatible normalization.

## Cell specificity

evidence: direct_multi_context; notes: Multiple contexts and a single-cell module are documented; this does not establish general cell-selective expression.

## Sources

- https://academic.oup.com/nar/article/52/D1/D194/7243455
- https://rnamd.org/m6a/help.php

- url: https://academic.oup.com/nar/article/52/D1/D194/7243455; supports: Original v2 study describes integrated high-resolution and MeRIP data.
- url: https://rnamd.org/m6a/help.php; supports: Current help separates sites, enriched regions, quantitative contexts, single-cell modules and CSV differential-region export.

## Selected-file audit

Useful endogenous annotation and exploratory context evidence after genome/condition reconciliation; cannot mark the corresponding position as modified in an engineered reporter.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/modification-trna/audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: rmbase-v3; m5c-atlas.
