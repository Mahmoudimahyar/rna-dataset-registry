# Saluki half-life corpus

Registry ID: `saluki-half-life` · benchmark · **curated** · verification: **paper**

Human/mouse half-life collections with raw sparse matrices, processed matrices and aggregate consensus targets.

## What the data contains

- Observation unit: Gene/transcript with per-study half-life and consensus score
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| individual half-life | Study-specific decay estimate; original units/method required | measured | unknown | transcript |
| PC1 consensus | First principal component of filtered/transformed/imputed/normalized half-life matrix; not literal hours | computed | unitless | transcript |

## Access and reuse

- Access: open
- Formats: XLSX; ZIP; HDF5
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://zenodo.org/records/6326409
- https://github.com/vagarwal87/saluki_paper

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Do not relabel PCA consensus as half-life in hours.
- Retain missingness/imputation and individual assay provenance; aggregate can hide context differences.

## Cell specificity

evidence: none; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://link.springer.com/article/10.1186/s13059-022-02811-x

- url: https://link.springer.com/article/10.1186/s13059-022-02811-x; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: not established.
