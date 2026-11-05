# GARDN in-silico UTR score traces

Registry ID: `gardn-predicted-utr-traces` · derived_resource · **curated** · verification: **file_sample**

Before/after computational score table; the path's experiments name does not establish wet-lab measurement.

## What the data contains

- Observation unit: Before/after score pair
- RNA scope: mRNA
- Biological context: In-silico output; no measured cellular response.
- Assays: computational scoring
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Pre_Optimized_Value; Post_Optimized_Value; Target_Value; Delta | Predictor scores and differences | prediction | predictor scale | construct |

## Access and reuse

- Access: open
- Formats: CSV
- Source license: unknown
- Redistribution: not established

- https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/data/sequence_experiments/UTR_big_sequence_experiments.csv

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/data/sequence_experiments/UTR_big_sequence_experiments.csv (header only).

- No model execution or independent prediction validation performed.

- Exclude prediction-only rows from measured activity labels.
- Shared model/training data creates circular evaluation risk.

## Cell specificity

evidence: none; notes: No selectivity measurement.

## Sources

- https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/sequence_experiments/UTR_big_sequence_experiments.csv

- url: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/sequence_experiments/UTR_big_sequence_experiments.csv; supports: Primary source supports resource or study identity and the described context.

Related models: P012. Related resources: gardn-sandstorm-release; sample2019-chemistry-reporters.
