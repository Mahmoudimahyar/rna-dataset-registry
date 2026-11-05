# REDIportal (2025 publication)

Registry ID: `rediportal` · database · **curated** · verification: **paper**

A-to-I RNA-editing reference with site annotations, sample-level editing levels and aggregated tissue/disease context.

## What the data contains

- Observation unit: An editing position with sample-specific RNA-seq support or a sample-level editing index.
- RNA scope: mRNA; other RNA
- Biological context: Human GTEx and TCGA RNA-seq contexts plus mouse tissue data; source-project provenance must be retained.
- Assays: RNA-seq reanalysis; known-site annotation; selected proteomic support
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| A-to-I editing site | Known editing annotation and genomic context. | annotation | unknown | position |
| sample editing level | RNA-seq-derived edited-read proportion at a covered site. | computed | proportion | position |
| AEI/REI | Aggregated editing indices; not site-level labels. | computed | unknown | sample |

## Access and reuse

- Access: mixed
- Formats: not established
- Source license: unknown
- Redistribution: not established

- http://srv00.recas.ba.infn.it/atlas/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Portal endpoint could not be fetched in this inspection; current export format unverified.
- Derived annotations are public; access conditions for upstream human raw data must be checked independently.

- A-to-G RNA evidence requires genomic-variant and mapping controls; not every mismatch proves editing.
- A noncalled site can reflect insufficient expression/coverage rather than absence of editing.
- Aggregated tissue support is not per-cell resolution; newer ONT modules discussed as future work in this publication are not assumed available.

## Cell specificity

evidence: direct_multi_context; notes: Sample/tissue context is documented across projects; pooled tissue labels do not imply cell-specific causality.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11701558/

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11701558/; supports: Original update describes GTEx/TCGA contexts, site and sample tables, editing indices and mouse coverage.

Related models: not established. Related resources: radar-editing; darned-editing.
