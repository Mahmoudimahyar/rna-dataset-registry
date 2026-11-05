# RMBase v3.0

Registry ID: `rmbase-v3` · database · **curated** · verification: **paper**

Integrated modification maps and functional context assembled from heterogeneous epitranscriptomic assays and curated sources.

## What the data contains

- Observation unit: A source-supported modification site or enrichment region, with assay and reference assembly attached.
- RNA scope: mRNA; tRNA; rRNA; other RNA
- Biological context: Multiple source studies; context must be retained per source record.
- Assays: MeRIP-seq/m6A-seq; single-base modification profiling; curated MODOMICS and publication annotations
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RNA modification call | Assay-derived or curated modification annotation; resolution follows its source. | computed | unknown | position |
| m6A enriched region | Enrichment call from lower-resolution profiling, not a uniquely measured modified base. | computed | unknown | interval |

## Access and reuse

- Access: open
- Formats: download tables (documented; files not inspected)
- Source license: unknown
- Redistribution: not established

- https://bioinformaticsscience.cn/rmbase/download.php

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Direct page fetch timed out; indexed primary documentation and original paper were inspected, but current file delivery was not verified.

- A missing call is unobserved under a source assay, not a confirmed unmodified base.
- Retain assay, genome assembly, evidence provenance and interval-versus-position resolution.
- Shares source studies and curated annotations with other modification databases; sizes must not be added.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://academic.oup.com/nar/article/52/D1/D273/7416807
- https://bioinformaticsscience.cn/rmbase/download.php

- url: https://academic.oup.com/nar/article/52/D1/D273/7416807; supports: Original v3 paper describes multi-species integration and distinguishes approximate 200-nt m6A maps from single-nucleotide annotations.
- url: https://bioinformaticsscience.cn/rmbase/download.php; supports: Indexed primary download documentation describes downloadable modification records and linked annotations.

Related models: not established. Related resources: modomics; m6a-atlas-v2.
