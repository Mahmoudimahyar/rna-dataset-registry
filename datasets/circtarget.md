# CircTarget

Registry ID: `circtarget` · database · **curated** · verification: **file_sample**

Read-supported RNA-RNA interaction evidence with computed significance

## What the data contains

- Observation unit: A549 RNA-RNA interaction rows
- RNA scope: circRNA
- Biological context: A549 cell identity overlaps LAMAR, but endogenous circRNA interaction IDs do not establish matching synthetic reporter constructs
- Assays: KARR-seq
- Accessions: not established
- Scale: value: 1677; unit: A549 RNA-RNA interaction rows; basis: Recounted fully inspected relevant table; other source files and partial signal inspect scopes are detailed in evidence/file-audit-20261105/translation/translation_file_audit.json; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Chimeric read count | Sequencing reads supporting the detected RNA-RNA interaction | computed | read count | construct |
| P-value | Monte Carlo interaction-support significance | computed | probability | construct |
| Interaction type | BSJ-supported versus nonBSJ-supported evidence category | annotation | category | construct |

## Access and reuse

- Access: open
- Formats: RAR
- Source license: unknown
- Redistribution: not established; metadata only is cataloged

- https://circtarget.cn/static/download/A549.rar

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://circtarget.cn/static/download/A549.rar.

- Only the A549 archive was inspected
- BSJ supported and nonBSJ supported interactions must remain distinct
- Chimeric read counts and P-values are not activation, leakage or protein-output labels
- No causal effect on translation established by an interaction
- Bounded file audit: evidence/file-audit-20261105/translation/translation_file_audit.json; selected coverage only.

- Only the A549 archive was inspected
- BSJ supported and nonBSJ supported interactions must remain distinct
- Chimeric read counts and P-values are not activation, leakage or protein-output labels
- No causal effect on translation established by an interaction

## Cell specificity

evidence: context_only; notes: A549 cell identity overlaps LAMAR, but endogenous circRNA interaction IDs do not establish matching synthetic reporter constructs

## Sources

- https://circtarget.cn/download/

- url: https://circtarget.cn/download/; supports: Primary source, file route and evidence definitions; file-level details in assigned audit JSON

## Selected-file audit

Read-supported RNA-RNA interaction evidence with computed significance

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/translation/translation_file_audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
