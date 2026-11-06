# ENCODE RNA experiments

Registry ID: `encode` · database · **curated** · verification: **file_sample**

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
- https://www.encodeproject.org/files/ENCFF593RED/@@download/ENCFF593RED.bed.gz
- https://www.encodeproject.org/files/ENCFF897MSA/@@download/ENCFF897MSA.bed.gz
- https://www.encodeproject.org/files/ENCFF644GCJ/@@download/ENCFF644GCJ.tsv
- https://www.encodeproject.org/files/ENCFF060HYJ/@@download/ENCFF060HYJ.tsv
- https://www.encodeproject.org/files/ENCFF335XEM/@@download/ENCFF335XEM.tsv

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://www.encodeproject.org/files/ENCFF593RED/@@download/ENCFF593RED.bed.gz; https://www.encodeproject.org/files/ENCFF897MSA/@@download/ENCFF897MSA.bed.gz; https://www.encodeproject.org/files/ENCFF644GCJ/@@download/ENCFF644GCJ.tsv; https://www.encodeproject.org/files/ENCFF060HYJ/@@download/ENCFF060HYJ.tsv; https://www.encodeproject.org/files/ENCFF335XEM/@@download/ENCFF335XEM.tsv.

- five complete selected files; not entire ENCODE collection
- K562 peak/RNA perturbation examples are not matched to the requested reporter-cell contexts; cell-free RBNS cannot establish cell-specific binding or translation.
- Knockdown quantification without matched controls is not an effect estimate.
- Bounded file audit: evidence/file-audit-20261105/cell-context/encode_file_inspection.json; selected coverage only.

- Preserve size-matched input, RBP identity, replicate, audit flags and assay.
- RBP binding and perturbation effects are not direct translation-efficiency labels.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.encodeproject.org/data-standards/

- url: https://www.encodeproject.org/data-standards/; supports: Resource identity, available label types and access route described in primary source documentation

## Selected-file audit

RBP-binding and cell-free motif evidence; selected knockdown RNA quantifications are not matched translation labels.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/cell-context/encode_file_inspection.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
