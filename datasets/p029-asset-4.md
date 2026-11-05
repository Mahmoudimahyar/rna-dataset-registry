# PARADE prediction tutorials and benchmark summaries

Registry ID: `p029-asset-4` · model_release · **candidate** · verification: **unverified**

One arbitrary input sequence or aggregate benchmark result Random tutorial sequences; model/ablation conditions

## What the data contains

- Observation unit: One arbitrary input sequence or aggregate benchmark result
- RNA scope: RNA; exact type varies by source
- Biological context: Tutorial outputs include cell columns c1,c13,c17,c2,c4,c6.
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently recounted; see prior evidence note; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Predicted activity by cell or aggregate Pearson correlation | Predictions and performance summaries, not experimentally measured sequence-level labels. | unknown | unknown | unknown |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://github.com/autosome-ru/parade/tree/master/tutorials

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Do not train/evaluate a new method against synthetic tutorial predictions and call it biological validation.
- Imported candidate. Prior evidence level: file_inspected. Import is not a new file inspection or certification of labels.

- May group multiple datasets or overlap other model assets; do not count as an independent experimental dataset.

## Cell specificity

evidence: unknown; notes: Useful for checking inference interfaces only.

## Sources

- https://github.com/autosome-ru/parade/tree/master/tutorials
- https://github.com/autosome-ru/parade/blob/master/tutorials/predict_utr3.ipynb
- https://github.com/autosome-ru/parade/blob/master/predictor/regression_multiple/ablation/rna_act_test.tsv

- url: https://github.com/autosome-ru/parade/tree/master/tutorials; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/autosome-ru/parade/blob/master/tutorials/predict_utr3.ipynb; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/autosome-ru/parade/blob/master/predictor/regression_multiple/ablation/rna_act_test.tsv; supports: Previously recorded audit source; fresh dataset reconciliation pending

Related models: P029. Related resources: not established.
