# ARCHS4

Registry ID: `archs4` · derived_resource · **curated** · verification: **metadata**

Uniformly processed public RNA-seq expression with GEO/SRA metadata; current portal moved to archs4.org.

## What the data contains

- Observation unit: Gene/transcript by source sample
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| gene/transcript counts | Quantified RNA abundance; pipeline and release determine identifier and scaling | measured | unknown | transcript |

## Access and reuse

- Access: open
- Formats: HDF5; TSV
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://archs4.org/
- https://maayanlab.cloud/archs4/download.html

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Old download page lists older releases; do not call its version the current global release.
- Overlaps raw GEO/SRA and other reanalyses; source sample is the deduplication key.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://maayanlab.cloud/archs4/

- url: https://maayanlab.cloud/archs4/; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: geo; sra; recount3.
