# MapUTR rare and cancer 3-prime UTR variant screen

Registry ID: `maputr-2024` · study · **curated** · verification: **paper**

Two-cell reporter study with processed public results and raw GEO data; external patient/genotype resources have separate terms.

## What the data contains

- Observation unit: Reference/alternate pair by cell line
- RNA scope: mRNA
- Biological context: Human HEK293 and HeLa; rare and cancer-associated UTR variants.
- Assays: MapUTR RNA/DNA reporter assay
- Accessions: GSE232573
- Scale: value: 17301; unit: rare variants in primary screen; basis: Paper-reported subset; excludes separate somatic/follow-up collections; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| activity score | Source reporter abundance effect | computed | source-normalized score | construct |
| variant effect | Allelic abundance effect and significance | computed | source effect scale / p-value | construct |

## Access and reuse

- Access: open
- Formats: processed repository data; GEO/SRA reads
- Source license: unknown
- Redistribution: not established

- https://github.com/gxiaolab/mapUTR
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE232573

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Processed headers and GEO samples not inspected.
- Primary assay GSE232573 differs from follow-up prime-editing GSE232570.
- Controlled external cancer/genotype data not accessed.

- Retain rare/somatic libraries, allele pairing, QC and cell identity.
- Reporter splicing and normalization may influence output.
- Public reporter tables do not authorize controlled patient-data redistribution.

## Cell specificity

evidence: direct_multi_context; notes: Two-cell relative abundance effects, not broad tissue selectivity.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11026479/
- https://github.com/gxiaolab/mapUTR
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE232573

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11026479/; supports: Two-cell assay; rare screen, processed repository and raw GSE232573.

Related models: not established. Related resources: griesemer2021-mprau.
