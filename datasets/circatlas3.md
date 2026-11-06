# circAtlas v3

Registry ID: `circatlas3` · database · **curated** · verification: **file_sample**

Reference coordinates and identifier reconciliation, not measured expression or translation labels

## What the data contains

- Observation unit: human coordinate rows
- RNA scope: circRNA
- Biological context: Can reconcile endogenous circRNA identifiers; no direct join to arbitrary synthetic IRES sequences established
- Assays: RNA-seq
- Accessions: not established
- Scale: value: 768986; unit: human coordinate rows; basis: Recounted fully inspected relevant table; other source files and partial signal inspect scopes are detailed in evidence/file-audit-20261105/translation/translation_file_audit.json; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Chro / Start / End / Strand | RNA-seq-derived circRNA coordinate annotation | computed | genomic coordinate | interval |
| circAltas_ID | Database-assigned circRNA identity | annotation | identifier | interval |

## Access and reuse

- Access: open
- Formats: ZIP
- Source license: unknown
- Redistribution: not established; metadata only is cataloged

- https://ngdc.cncb.ac.cn/circatlas/analysis/bed/human_bed_v3.0.zip

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://ngdc.cncb.ac.cn/circatlas/analysis/bed/human_bed_v3.0.zip.

- Full human coordinate file was inspected, not the entire database
- Coordinate download contains no tissue/cell expression or protein-output columns
- Do not infer full-length isoform identity from a BSJ coordinate alone
- Genome assembly and coordinate conventions must be independently preserved
- Bounded file audit: evidence/file-audit-20261105/translation/translation_file_audit.json; selected coverage only.

- Full human coordinate file was inspected, not the entire database
- Coordinate download contains no tissue/cell expression or protein-output columns
- Do not infer full-length isoform identity from a BSJ coordinate alone
- Genome assembly and coordinate conventions must be independently preserved

## Cell specificity

evidence: context_only; notes: Can reconcile endogenous circRNA identifiers; no direct join to arbitrary synthetic IRES sequences established

## Sources

- https://ngdc.cncb.ac.cn/circatlas/links1.php
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10767913/

- url: https://ngdc.cncb.ac.cn/circatlas/links1.php; supports: Primary source, file route and evidence definitions; file-level details in assigned audit JSON
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10767913/; supports: Primary source, file route and evidence definitions; file-level details in assigned audit JSON

## Selected-file audit

Reference coordinates and identifier reconciliation, not measured expression or translation labels

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/translation/translation_file_audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
