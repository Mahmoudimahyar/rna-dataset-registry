# DepMap/CCLE protein-coding expression reference

Registry ID: `depmap-ccle-expression` · database · **curated** · verification: **file_sample**

Versioned cancer-cell expression and identity metadata.

## What the data contains

- Observation unit: Source-specific record
- RNA scope: mRNA
- Biological context: See selected-file audit; not matched to reporter assay conditions.
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Selected inspection scope is recorded separately; no database-wide recount; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| log2(TPM+1) | RNA-seq-derived protein-coding gene abundance | computed | log2(TPM+1) | transcript |
| ModelID / RRID | Cell-model identity and context metadata | annotation | category | sample |

## Access and reuse

- Access: open
- Formats: CSV
- Source license: CC BY4.0 (inspected24Q4 Figshare release)
- Redistribution: not established; metadata only redistributed

- https://ndownloader.figshare.com/files/51065489
- https://ndownloader.figshare.com/files/51065297
- https://ndownloader.figshare.com/files/51065723

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://ndownloader.figshare.com/files/51065489; https://ndownloader.figshare.com/files/51065297; https://ndownloader.figshare.com/files/51065723.

- Human cancer cell line reference; mouse lines C2C12/Neuro-2a/RAW264.7/N2A not represented by this table.
- HEK293T absent among exact requested RRID candidates in this Model.csv.
- U87 source shorthand requires identity validation; CVCL_0022 is U-87 MG and must not be silently assigned.
- HPA incorporates CCLE-derived RNA; HPA and DepMap are not necessarily independent evidence.
- HCT-8 ACH-001084 exists in Model.csv but has no row in this selected expression matrix; metadata availability is not numeric expression coverage.
- Bounded file audit: evidence/file-audit-20261105/cell-context/depmap_file_inspection.json; selected coverage only.

- Not established.

## Cell specificity

evidence: context_only; notes: Not a matched synthetic RNA protein-output experiment

## Sources

- https://api.figshare.com/v2/articles/27993248
- https://depmap.org/portal/data_page/

- url: https://api.figshare.com/v2/articles/27993248; supports: Primary resource documentation and file routes
- url: https://depmap.org/portal/data_page/; supports: Primary resource documentation and file routes

## Selected-file audit

External expression features:1673 models by19193 genes; inspect24Q4 rather than assume latest.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/cell-context/depmap_file_inspection.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
