# m7GHub V2.0

Registry ID: `m7ghub-v2` · database · **curated** · verification: **metadata**

m7G collection with distinct base-resolution NGS, enrichment-region, nanopore and predicted variant-effect modules.

## What the data contains

- Observation unit: A source m7G site/region or a separately predicted m7G-associated variant.
- RNA scope: mRNA; tRNA; rRNA; other RNA
- Biological context: Multiple source studies; context must be retained per source record.
- Assays: m7G-seq; m7G-MeRIP-seq; m7G-miCLIP-seq; m7G-MaP-seq; nanopore direct RNA sequencing
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| NGS base-resolution m7G annotation | Source-identified base-level annotation. | computed | unknown | position |
| NGS m7G region | Enrichment interval rather than a resolved modified nucleotide. | computed | unknown | interval |
| ONT putative m7G site | Nanopore-derived putative annotation; retain tool and evidence. | prediction | unknown | position |
| m7G-associated variant | Model-derived potential modification gain/loss annotation. | prediction | category | position |

## Access and reuse

- Access: open
- Formats: CSV
- Source license: unknown
- Redistribution: not established

- https://www.rnamd.org/m7GHub2/download.html

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.

- Do not collapse intervals, base-level sites and ONT predictions into one ground-truth label.
- Internal m7G annotations are not equivalent to cap identity or cap efficiency measurements.
- Absence from a source assay is not proof of an unmodified guanosine.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.rnamd.org/m7GHub2/
- https://www.rnamd.org/m7GHub2/help.html
- https://www.rnamd.org/m7GHub2/download.html

- url: https://www.rnamd.org/m7GHub2/; supports: Primary homepage identifies release and separate source/prediction modules.
- url: https://www.rnamd.org/m7GHub2/help.html; supports: Help identifies ONT annotations as putative and separates variant predictions.
- url: https://www.rnamd.org/m7GHub2/download.html; supports: Download page separates base-resolution, region and nanopore exports.

Related models: not established. Related resources: rmbase-v3; directrmdb.
