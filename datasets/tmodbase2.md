# tModBase v2.0

Registry ID: `tmodbase2` · database · **curated** · verification: **file_sample**

tRNA sequencing datasets and condition-specific abundance/modification-associated signals.

## What the data contains

- Observation unit: Source-specific record
- RNA scope: tRNA
- Biological context: Selected numerical sample: HepG2, DAMM-seq, ALKBH7-mutant rescue; not untreated reporter context. Other dataset contexts were inspected as metadata only.
- Assays: tRNA sequencing; method varies by dataset
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Selected inspection scope is recorded separately; no database-wide recount; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| counts / per_counts / mismatch / stop / coverage | Assay-derived numerical signals; not interchangeable with charging or calibrated modification fractions | computed | source-specific | transcript |

## Access and reuse

- Access: open
- Formats: not established
- Source license: unknown
- Redistribution: not established; metadata only redistributed

- https://www.tmodbase2.com/graphql

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://www.tmodbase2.com/graphql.

- 650 tRNA entities but only81 with nonzero counts/coverage in inspected response
- total field is zero in every inspected entity despite positive counts in81; interpretation remains unresolved
- No per-replicate entity dimension; metadata can aggregate multiple GSMs
- Cell labels alone do not establish preparation or biological-condition equivalence
- One numerical condition verified, not all528 datasets
- Bounded file audit: evidence/file-audit-20261105/modification-trna/audit.json; selected coverage only.

- Not established.

## Cell specificity

evidence: context_only; notes: Not a matched synthetic RNA protein-output experiment

## Sources

- https://doi.org/10.1093/nar/gkag1092
- https://www.tmodbase2.com/

- url: https://doi.org/10.1093/nar/gkag1092; supports: Primary resource documentation and file routes
- url: https://www.tmodbase2.com/; supports: Primary resource documentation and file routes

## Selected-file audit

Exploratory functional tRNA context only after selecting comparable assays and treatments. Inspected numerical condition is perturbed and cannot be assigned to untreated HepG2 reporter output.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/modification-trna/audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
