# OpenProt

Registry ID: `openprot` · reference · **curated** · verification: **metadata**

Canonical and alternative ORF/protein annotations with separable experimental-support filters.

## What the data contains

- Observation unit: ORF/protein annotation linked to transcript
- RNA scope: mRNA; ncRNA coding potential
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ORF identity / support | Predicted coding potential and evidence flags; selected mass-spectrometry support is distinct | annotation | unknown | transcript |

## Access and reuse

- Access: open
- Formats: TSV; FASTA; BED
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://api.openprot.org/downloads

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- All predicted ORFs are not all translated proteins.
- Use explicit ribosome/MS support categories and transcript/assembly versions.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://api.openprot.org/downloads

- url: https://api.openprot.org/downloads; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: not established.
