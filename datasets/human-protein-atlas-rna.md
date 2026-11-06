# Human Protein Atlas RNA expression downloads

Registry ID: `human-protein-atlas-rna` · database · **curated** · verification: **file_sample**

Tissue, cell-line and cell-type RNA expression tables alongside distinct protein modalities.

## What the data contains

- Observation unit: Gene by tissue/cell context
- RNA scope: mRNA
- Biological context: Human tissue, immune, cell-line and single-cell reference contexts
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RNA abundance | RNA expression quantification; source table defines normalization | measured | source normalized abundance | gene |
| specificity score / class | Derived expression specificity score or classification; not a directly measured response | computed | score/category | gene |

## Access and reuse

- Access: open
- Formats: TSV; JSON; XML
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.proteinatlas.org/about/download
- https://www.proteinatlas.org/download/tsv/rna_celline.tsv.zip

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://www.proteinatlas.org/download/tsv/rna_celline.tsv.zip.

- No replicate column or matched reporter condition; RNA expression does not establish protein activity.
- HPA can reuse CCLE profiles; HPA and DepMap are not independent cohorts.
- Bounded file audit: evidence/file-audit-20261105/cell-context/hpa_file_inspection.json; selected coverage only.

- Keep RNA and protein evidence separate.
- Reference cell-type expression does not establish physical mRNA delivery or response to a regulatory design.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.proteinatlas.org/about/download

- url: https://www.proteinatlas.org/about/download; supports: Resource identity, available label types and access route described in primary source documentation

## Selected-file audit

External baseline RNA-expression features; 1206 cell lines and20162 genes in inspected25.1 file.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/cell-context/hpa_file_inspection.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
