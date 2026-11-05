# ENCODE RNA experiments

Registry ID: `encode` · database · **curated** · verification: **metadata**

Released RNA-seq, long-read RNA, eCLIP, RNA Bind-n-Seq and perturbation data with assay standards and audits.

## What the data contains

- Observation unit: Experiment/file, gene expression estimate or RBP peak
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: RNA-seq; eCLIP; RBNS; perturbation RNA-seq
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| counts / abundance | RNA expression quantification; source normalization applies | measured | unknown | transcript |
| eCLIP peak / IDR | RBP binding evidence with replicate/control provenance | annotation | unknown | interval |

## Access and reuse

- Access: open
- Formats: FASTQ; BAM; BED; bigWig; TSV; JSON
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.encodeproject.org/data-standards/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Preserve size-matched input, RBP identity, replicate, audit flags and assay.
- RBP binding and perturbation effects are not direct translation-efficiency labels.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.encodeproject.org/data-standards/

- url: https://www.encodeproject.org/data-standards/; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: not established.
