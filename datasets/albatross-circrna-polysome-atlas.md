# Albatross synthetic circRNA polysome-loading atlas

Registry ID: `albatross-circrna-polysome-atlas` · study · **curated** · verification: **file_sample**

96IRES IDs across six cell lines;576ID-cell point estimates and SDs.

## What the data contains

- Observation unit: Source-specific record
- RNA scope: circRNA
- Biological context: Synthetic IVT circRNA library across five human lines and mouseN2A; preprint.
- Assays: Polysome fractionation and barcode sequencing
- Accessions: GSE347508
- Scale: value: 576; unit: IRES-ID-cell rows; basis: 96IDs by6cells; repeated/discordant sequence identities require reconciliation.; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Ribosomal_Loading | Weighted polysome-derived average ribosomes per RNA; not completed protein output | computed | ribosomes per RNA | construct |
| SD | Released variability of ribosome-loading measurement | computed | ribosomes per RNA | construct |

## Access and reuse

- Access: open
- Formats: XLSX
- Source license: unknown
- Redistribution: not established; metadata only redistributed

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE347nnn/GSE347508/suppl/GSE347508_Supplement_S1.xlsx

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE347nnn/GSE347508/suppl/GSE347508_Supplement_S1.xlsx.

- Preprint functional atlas is distinct from the Albatross structure model.
- FiveIRES IDs have discordant sequence fields across sheets andDNA_IRES requires alias reconciliation; do not silently join all rows.
- IRES reference has95unique sequences for96IDs; endpoint sequence fields have92unique sequences.
- Two biological by two technical replicates are not four independent biological replicates.
- Ribosome loading can reflect elongation or stalling; cannot directly validate protein-output accuracy.
- Publisher/PMC and GEO workbook bytes differ; source versions and digests must remain explicit.

- Preprint functional atlas is distinct from the Albatross structure model.
- FiveIRES IDs have discordant sequence fields across sheets andDNA_IRES requires alias reconciliation; do not silently join all rows.
- IRES reference has95unique sequences for96IDs; endpoint sequence fields have92unique sequences.
- Two biological by two technical replicates are not four independent biological replicates.
- Ribosome loading can reflect elongation or stalling; cannot directly validate protein-output accuracy.
- Publisher/PMC and GEO workbook bytes differ; source versions and digests must remain explicit.

## Cell specificity

evidence: direct_multi_context; notes: Same reporter library across six named cells; loading endpoint only.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC13228543/
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE347508
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE347nnn/GSE347508/suppl/GSE347508_Supplement_S1.xlsx

- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE347nnn/GSE347508/suppl/GSE347508_Supplement_S1.xlsx; supports: Full processed workbook, headers, loading and SD columns inspected

Related models: not established. Related resources: not established.
