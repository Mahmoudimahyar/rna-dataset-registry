# GTEx

Registry ID: `gtex` · database · **curated** · verification: **metadata**

Tissue-context gene/transcript expression and QTL resources, with open processed data and controlled donor/raw data.

## What the data contains

- Observation unit: Gene/transcript by donor/tissue sample
- RNA scope: mRNA
- Biological context: Normal human tissue cohorts; donor covariates and tissue mixture matter
- Assays: bulk RNA-seq
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| TPM | RNA abundance in transcripts per million | measured | TPM | transcript |
| QTL statistics | Genotype-expression association, not a direct synthetic-sequence perturbation label | computed | unknown | transcript |

## Access and reuse

- Access: mixed
- Formats: GCT; TSV; VCF
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.gtexportal.org/home/faq

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Raw sequencing and protected donor fields require authorized access.
- Bulk tissue expression is a mixture of cell populations; it is not matched synthetic mRNA specificity.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.gtexportal.org/home/faq

- url: https://www.gtexportal.org/home/faq; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: not established.
