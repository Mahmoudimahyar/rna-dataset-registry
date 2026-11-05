# tRNAmod: MODOMICS-derived uridine-modification reference and predictor

Registry ID: `trnamod-reference-derived` · derived_resource · **curated** · verification: **metadata**

Prediction resource trained from MODOMICS annotations; retained to document its reference relationship, not as a measured cellular tRNA distribution.

## What the data contains

- Observation unit: Predicted uridine position in a reference tRNA
- RNA scope: tRNA
- Biological context: Kingdom-level reference-derived predictions; no tissue or cell-state abundance labels.
- Assays: SVM-based prediction from curated modification references
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| uridine modification class | Predicted pseudouridine, dihydrouridine, methyluridine or other uridine modification | prediction | unknown | position |
| probability score | Server confidence category; not an experimental probability calibration | prediction | 0-9 server score | position |

## Access and reuse

- Access: open
- Formats: not established
- Source license: unknown
- Redistribution: not established

- Not established.

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Training downloads and split membership were not inspected; no model was run.

- Overlaps underlying MODOMICS annotations; do not count as independent modification evidence.
- Absence of an annotated modification is not a verified unmodified negative.

## Cell specificity

evidence: none; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://webs.iiitd.edu.in/raghava/trnamod/index.html
- https://webs.iiitd.edu.in/raghava/trnamod/help.html
- https://doi.org/10.1186/1471-2105-15-326

- url: https://webs.iiitd.edu.in/raghava/trnamod/index.html; supports: tRNAmod predicts modifications using annotations obtained from MODOMICS
- url: https://webs.iiitd.edu.in/raghava/trnamod/help.html; supports: Prediction categories and source-defined 0-9 confidence score

Related models: not established. Related resources: modomics.
