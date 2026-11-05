# recount3

Registry ID: `recount3` · derived_resource · **curated** · verification: **metadata**

Uniformly processed human/mouse RNA-seq gene, exon and exon-junction counts plus coverage.

## What the data contains

- Observation unit: Sample by gene/exon/junction or genomic coverage bin
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| coverage/count | Processed sequence evidence; package-specific scaling is required | measured | unknown | transcript |
| junction count | Splice junction support | measured | count | interval |

## Access and reuse

- Access: open
- Formats: bigWig; TSV; RangedSummarizedExperiment
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://rna.recount.bio/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Gene/exon/junction units differ; retain reference and normalization.
- Many source studies overlap other portals.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://rna.recount.bio/

- url: https://rna.recount.bio/; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: geo; sra; archs4.
