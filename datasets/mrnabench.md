# mRNABench dataset collection

Registry ID: `mrnabench` · benchmark · **curated** · verification: **schema**

Reusable dataset catalog and split logic for evaluating mRNA representations, with a linked Hugging Face collection.

## What the data contains

- Observation unit: Task-specific transcript/sequence example
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| target | Task-specific label; semantics differ across dataset cards | unknown | unknown | transcript |

## Access and reuse

- Access: open
- Formats: Hugging Face datasets; tables
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://huggingface.co/collections/morrislab/mrnabench-6825747c0b9253c3226078d9

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Code AGPL does not define every source dataset license.
- Redistributions overlap original studies; retain original papers and split definitions.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://github.com/morrislab/mRNABench

- url: https://github.com/morrislab/mRNABench; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: saluki-half-life; rnalocate.
