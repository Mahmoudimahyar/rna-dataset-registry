# riboCIRC v2

Registry ID: `ribocirc2` · database · **curated** · verification: **file_sample**

Context-specific inferred endogenous translation evidence and literature-curated evidence; not a quantitative synthetic circRNA-by-cell output matrix

## What the data contains

- Observation unit: context-specific circRNAs in inspected archive
- RNA scope: circRNA
- Biological context: Can annotate endogenous circRNA coding/interaction evidence and reconcile coordinates with circAtlas; direct overlap with synthetic reporter sequences not established
- Assays: Ribo-seq
- Accessions: not established
- Scale: value: 86; unit: context-specific circRNAs in inspected archive; basis: Recounted fully inspected relevant table; other source files and partial signal inspect scopes are detailed in evidence/file-audit-20261105/translation/translation_file_audit.json; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Footprints / Footprints_unique | Total and unique footprints supporting inferred circRNA association | computed | read count | construct |
| Translation_Evidences | Combined source evidence categories; not a uniform quantitative output | annotation | category | construct |
| cORFs | Predicted circRNA coding regions | prediction | genomic/transcript coordinate | construct |

## Access and reuse

- Access: open
- Formats: RAR
- Source license: unknown
- Redistribution: not established; metadata only is cataloged

- http://www.ribocirc.com/download/All_context-specific_ribo-circRNAs.rar
- http://www.ribocirc.com/download/literature-reported_trans-circRNAs.rar

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: http://www.ribocirc.com/download/All_context-specific_ribo-circRNAs.rar; http://www.ribocirc.com/download/literature-reported_trans-circRNAs.rar.

- Two complete downloadable archives inspected, not all riboCIRC datasets
- Context-specific means source-context evidence, not a calibrated cell-selectivity score
- Source_ is heterogeneous text and often only an SRX identifier; explicit cell mapping still needed
- Footprints and unique footprints are counts of supporting evidence, not RNA-normalized protein output
- Predicted ORFs, m6A/IRES/RBP annotations and literature evidence must retain their evidence types
- HTTP official site works; HTTPS timed out; legacy sysbio human ZIP links return404 through web tool
- Bounded file audit: evidence/file-audit-20261105/translation/translation_file_audit.json; selected coverage only.

- Two complete downloadable archives inspected, not all riboCIRC datasets
- Context-specific means source-context evidence, not a calibrated cell-selectivity score
- Source_ is heterogeneous text and often only an SRX identifier; explicit cell mapping still needed
- Footprints and unique footprints are counts of supporting evidence, not RNA-normalized protein output
- Predicted ORFs, m6A/IRES/RBP annotations and literature evidence must retain their evidence types
- HTTP official site works; HTTPS timed out; legacy sysbio human ZIP links return404 through web tool

## Cell specificity

evidence: context_only; notes: Can annotate endogenous circRNA coding/interaction evidence and reconcile coordinates with circAtlas; direct overlap with synthetic reporter sequences not established

## Sources

- http://www.ribocirc.com/download.html
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12807610/

- url: http://www.ribocirc.com/download.html; supports: Primary source, file route and evidence definitions; file-level details in assigned audit JSON
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12807610/; supports: Primary source, file route and evidence definitions; file-level details in assigned audit JSON

## Selected-file audit

Context-specific inferred endogenous translation evidence and literature-curated evidence; not a quantitative synthetic circRNA-by-cell output matrix

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/translation/translation_file_audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
