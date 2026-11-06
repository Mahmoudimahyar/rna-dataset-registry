# CZ CELLxGENE Census

Registry ID: `cellxgene-census` · derived_resource · **curated** · verification: **metadata**

Versioned single-cell corpus with standardized cell/gene metadata and queryable slices.

## What the data contains

- Observation unit: Cell-by-gene count plus cell/dataset metadata
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| counts | Molecule or full-gene read counts depending on assay; preserve assay | measured | unknown | transcript |
| cell_type / tissue / disease | Source cell-state annotations | annotation | unknown | cell |

## Access and reuse

- Access: open
- Formats: TileDB-SOMA; AnnData; Arrow
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://chanzuckerberg.github.io/cellxgene-census/

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.
- Release manifest inspected; native TileDB-SOMA runtime unavailable on supplied Windows Python.
- Do not promote metadata or a release listing to expression-file validation.
- Bounded file audit: evidence/file-audit-20261105/cell-context/census_access_audit.json; selected coverage only.

- Filter duplicate cells using is_primary_data; retain original dataset citations.
- UMI and full-length read counts are not directly interchangeable.
- Dataset licenses and donor/project splits remain source-specific.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://chanzuckerberg.github.io/cellxgene-census/

- url: https://chanzuckerberg.github.io/cellxgene-census/; supports: Resource identity, available label types and access route described in primary source documentation

## Selected-file audit

Potential primary-cell context; no numeric data slice verified in this environment.

Selected payload inspected: False. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/cell-context/census_access_audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: human-cell-atlas.
