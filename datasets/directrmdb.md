# DirectRMDB

Registry ID: `directrmdb` · database · **curated** · verification: **metadata**

Integrated direct-RNA-sequencing modification calls with isoform/context annotations and accompanying transcript expression estimates.

## What the data contains

- Observation unit: A putative modification position supported by a specified ONT analysis tool/sample, linked to transcript context.
- RNA scope: mRNA; other RNA
- Biological context: Multiple source studies; context must be retained per source record.
- Assays: nanopore direct RNA sequencing; cross-technology annotation
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| putative modification site | Computational call from nanopore direct-RNA data; support from other technologies is separately annotated. | prediction | unknown | position |
| transcript expression level | Computational abundance estimate from the associated DRS context, distinct from modification frequency. | computed | unknown | transcript |

## Access and reuse

- Access: open
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://www.rnamd.org/directRMDB/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.

- Predicted chemistry/site identity must retain caller, controls and independent evidence.
- Abundance and modification are separate endpoints with different units.
- Isoform assignment is not equivalent to single-cell specificity; uncalled bases remain unobserved.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC9825532/
- https://www.rnamd.org/directRMDB/

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9825532/; supports: Original paper describes isoform distribution, expression estimates and tool/sample evidence, and warns of false-positive sites.
- url: https://www.rnamd.org/directRMDB/; supports: Current landing page was accessible; no data table/file was opened.

Related models: not established. Related resources: rmpore; rmbase-v3.
