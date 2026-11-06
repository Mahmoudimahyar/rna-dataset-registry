# MODOMICS (2025 update)

Registry ID: `modomics` · database · **curated** · verification: **file_sample**

Reference catalog of modified residues, modification machinery and annotated RNA positions; includes natural and synthetic residue chemistry rather than a synthetic-mRNA expression screen.

## What the data contains

- Observation unit: A chemical-residue record, machinery record, or annotated modification position in an RNA reference; these tables have different units.
- RNA scope: mRNA; lncRNA; tRNA; rRNA; other RNA
- Biological context: Cross-species reference chemistry and RNA annotations; new long-RNA annotations draw from Sci-ModoM.
- Assays: literature curation; structure-supported annotation; integrated high-throughput modification mapping
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| modification identity | Curated identity and nomenclature of a modified residue. | annotation | category | position |
| annotated RNA modification position | Evidence-filtered modification annotation on an RNA reference. | annotation | unknown | position |

## Access and reuse

- Access: open
- Formats: MOL2; SDF; OWL Lite; N3; downloadable tables (paper-described)
- Source license: unknown
- Redistribution: not established

- https://genesilico.pl/modomics/download
- https://genesilico.pl/modomics/download/modified_positions/

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://genesilico.pl/modomics/download/modified_positions/.

- Dataset license was not established from the download page; paper states free research access.
- Audited three legacy .mods files within one download archive, not every current MODOMICS endpoint
- No cell-line or protein-output fields in inspected tables
- Reference positions do not imply modification stoichiometry or actual presence in a new synthetic RNA
- Bounded file audit: evidence/file-audit-20261105/modification-trna/audit.json; selected coverage only.

- The latest paper marks only sites passing cross-dataset evidence filters; other displayed bases are not verified unmodified negatives.
- Do not pool residue chemistry records with position annotations or treat either as measured expression.
- Sci-ModoM-derived annotations overlap the upstream resource.

## Cell specificity

evidence: none; notes: Reference identities and pooled annotations are not a cell-selectivity assay.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC12807697/
- https://genesilico.pl/modomics/download

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12807697/; supports: 2025 update describes chemistry, evidence framework, Sci-ModoM-derived long-RNA annotations and research access.
- url: https://genesilico.pl/modomics/download; supports: Current download page lists chemistry, ontology and modified-position exports.

## Selected-file audit

Use as chemical/reference vocabulary and site annotation only; cannot join by cell to predict output.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/modification-trna/audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: sci-modom.
