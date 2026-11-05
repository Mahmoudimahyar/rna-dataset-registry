# Rfam riboswitch-family reference subset

Registry ID: `rfam-riboswitch-families` · reference · **curated** · verification: **metadata**

Family alignments and covariance-model annotations searchable as riboswitches; a reference rather than a reporter-activity dataset.

## What the data contains

- Observation unit: Family alignment or genomic family hit
- RNA scope: riboswitch
- Biological context: Taxonomically varied natural families; genome hits depend on family and release.
- Assays: comparative sequence annotation
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| family accession; consensus structure | Family identity and alignment annotation | annotation | categorical | unknown |
| score; E-value | Covariance-model hit support | computed | source score / E-value | interval |

## Access and reuse

- Access: open
- Formats: Stockholm; covariance models; genome-hit tables; JSON/XML
- Source license: CC0 (Rfam downloads page)
- Redistribution: Rfam data stated CC0; retain release and provenance

- https://ftp.ebi.ac.uk/pub/databases/Rfam/
- https://www.ebi.ac.uk/ebisearch/ws/rest/rfam?query=riboswitch&format=json&fields=num_seed,description

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Release page observed 15.1; subset not enumerated or downloaded.
- Family membership is not measured switching activity.

- Pin a versioned release.
- Seed/full hits and Ribocentre/RiboD overlap are not independent.
- Use family/phylogenetic splits for generalization.

## Cell specificity

evidence: none; notes: No cellular reporter response labels.

## Sources

- https://rfam.org/downloads
- https://docs.rfam.org/en/latest/searching-rfam.html
- https://docs.rfam.org/en/latest/api.html

- url: https://rfam.org/downloads; supports: Primary source supports resource or study identity and the described context.
- url: https://docs.rfam.org/en/latest/searching-rfam.html; supports: Primary source supports resource or study identity and the described context.
- url: https://docs.rfam.org/en/latest/api.html; supports: Primary source supports resource or study identity and the described context.

Related models: not established. Related resources: ribocentre-switch; ribod; tbdb.
