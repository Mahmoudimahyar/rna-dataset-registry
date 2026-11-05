# PARADE 3-prime UTR RNA/gDNA assay

Registry ID: `parade-stability-assay` · study · **curated** · verification: **schema**

Separate abundance/stability-proxy task referenced by PARADE; not a time-course half-life label.

## What the data contains

- Observation unit: 3-prime UTR construct
- RNA scope: mRNA
- Biological context: Cellular 3-prime UTR assay; complete sample/cell metadata not recovered.
- Assays: RNA/genomic-DNA-normalized reporter assay
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RNA/gDNA | Normalized RNA abundance relative to genomic DNA representation | computed | ratio | construct |

## Access and reuse

- Access: unavailable
- Formats: CSV schema referenced in code
- Source license: Code MIT; measurement-data license unknown
- Redistribution: not established

- Not established.

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://github.com/autosome-ru/parade/blob/master/predictor/model/stability_data.py.

- Full table and normalization not validated; cell identity not assumed.
- Abundance proxy is not measured half-life or six-cell specificity.

- Separate RNA/gDNA from protein output and decay constants.

## Cell specificity

evidence: context_only; notes: Matched specificity not established for this separate task.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11722239/
- https://github.com/autosome-ru/parade/tree/master/predictor/regression_stability

- url: https://github.com/autosome-ru/parade/blob/master/predictor/model/stability_data.py; supports: Default target field RNA/gDNA.
- url: https://github.com/autosome-ru/parade/blob/master/README.md; supports: Separate stability task and unlinked archive.

Related models: P029. Related resources: parade-natural-utr-mpra.
