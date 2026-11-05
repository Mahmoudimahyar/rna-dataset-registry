# m6AVar (original release)

Registry ID: `m6avar` · database · **curated** · verification: **paper**

Variant annotations for potential effects on m6A, stratified by experimental or predicted source evidence.

## What the data contains

- Observation unit: A genetic variant associated computationally with a possible change to an m6A site or local modification context.
- RNA scope: mRNA
- Biological context: Human germline/somatic variation with integrated transcript annotations and disease associations.
- Assays: miCLIP; PA-m6A-seq; MeRIP-seq; sequence-based prediction
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| m6A-associated variant evidence class | High/medium/low source strata based on base-resolution assays, MeRIP or sequence prediction. | annotation | category | position |
| potential modification effect | Inferred possible effect of a variant, not an experimentally measured effect for every allele. | prediction | category | position |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- http://m6avar.renlab.org

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Legacy website delivery was not verified; paper-level resource metadata only.

- Even the high-confidence class describes evidence supporting a source m6A location; it is not universal causal validation of a variant.
- Prediction labels must not be used as measured chemical modification or expression.
- Do not relabel RMVar 2.0 as a verified release named m6AVar2.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC5753261/

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5753261/; supports: Original paper defines assay-based confidence strata and transcriptome-wide random-forest predictions.

Related models: not established. Related resources: rmvar-v2.
