# POSTAR3

Registry ID: `postar3` · database · **curated** · verification: **file_sample**

Integrated CLIP-derived RBP interaction data and other post-transcriptional annotations.

## What the data contains

- Observation unit: RBP-site interaction or annotated RNA region
- RNA scope: mRNA; ncRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: CLIP variants
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RBP binding interval | CLIP-derived binding evidence; protocol and support vary | annotation | unknown | interval |

## Access and reuse

- Access: open
- Formats: BED; tables
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- http://postar.ncrnalab.org/
- http://111.198.139.65/download/human_RBP/ALKBH1.binding.sites.zip

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: http://111.198.139.65/download/human_RBP/ALKBH1.binding.sites.zip.

- One ALKBH1 file only; not full POSTAR3.
- Multiple rows may repeat one binding site across transcript overlaps; site IDs and row counts must remain distinct.
- 22 columns observed but exact definitions of extra scores and assembly unresolved.
- Bounded file audit: evidence/file-audit-20261105/cell-context/postar3_file_inspection.json; selected coverage only.

- Different CLIP technologies and callers have different resolution/background.
- Database integrates source datasets; interaction counts are not independent experiments.

## Cell specificity

evidence: none; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://doi.org/10.1093/nar/gkab702

- url: https://doi.org/10.1093/nar/gkab702; supports: Resource identity, available label types and access route described in primary source documentation

## Selected-file audit

Endogenous binding-site annotation; coordinate joins require resolving assembly and score meanings.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/cell-context/postar3_file_inspection.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
