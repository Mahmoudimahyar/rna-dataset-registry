# m5C-Atlas

Registry ID: `m5c-atlas` · database · **curated** · verification: **metadata**

Integrated RNA m5C site annotations and condition-specific RNA-bisulfite profiles with downloadable contextual metadata.

## What the data contains

- Observation unit: A candidate m5C position in a reference assembly and its source assay/condition.
- RNA scope: mRNA; tRNA; rRNA
- Biological context: Multiple source studies; context must be retained per source record.
- Assays: RNA bisulfite-seq; miCLIP; RBS-seq; m5C MeRIP; Aza-IP
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| m5C site | Candidate site annotation from base-resolution assay sources; enrichment-only intervals are separate. | computed | unknown | position |
| condition-specific methylation level | Coverage-dependent methylation estimate from RNA-bisulfite sequencing. | computed | unknown | position |
| m5C enrichment interval | MeRIP/enrichment-based interval; cannot be treated as a resolved single-base call without supporting evidence | computed | source enrichment/support | interval |

## Access and reuse

- Access: open
- Formats: CSV; ZIP
- Source license: unknown
- Redistribution: not established

- https://rnamd.org/m5c-atlas/download.html

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Homepage/paper and help use differing species totals; no single exact scale is asserted.
- Download page lists surprising assembly labels for some plants; reference identity requires file-level checking before use.

- Incomplete bisulfite conversion and RNA structure can create false positives; noncalls are not verified unmodified negatives.
- Source quality and mRNA coverage differ by organism and experiment.
- tRNA mapping ambiguity and duplicate input studies require separate handling.
- The integrated assay collection includes enrichment measurements; preserve interval versus base resolution and do not assign every source a single-position label.

## Cell specificity

evidence: direct_multi_context; notes: Condition-specific profiles span multiple cell lines/tissues; assay and coverage confounding remain.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC8728298/
- https://rnamd.org/m5c-atlas/help.html
- https://rnamd.org/m5c-atlas/download.html

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8728298/; supports: Original paper describes integrated assays, quantitative conditions and conversion/structure limitations.
- url: https://rnamd.org/m5c-atlas/help.html; supports: Primary help defines candidate sites and metadata export.
- url: https://rnamd.org/m5c-atlas/download.html; supports: Download page separately lists sites, assays, contexts and reference assemblies.

Related models: not established. Related resources: rbs-seq-gse90963; ubs-seq-gse225614.
