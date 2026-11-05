# SAPIENs RBS dataset

Registry ID: `p012-asset-4` · model_release · **candidate** · verification: **unverified**

One bacterial ribosome binding site 17-nt RBS sequence arrays

## What the data contains

- Observation unit: One bacterial ribosome binding site
- RNA scope: RNA; exact type varies by source
- Biological context: Bacterial RBS; not human cap-dependent translation.
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently recounted; see prior evidence note; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| targets_train_validation.npy; targets_test.npy | RBS functional output from the upstream bacterial expression assay; exact normalization requires the source dataset documentation. | unknown | unknown | unknown |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://github.com/BorgwardtLab/SAPIENs

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- File names and training-array use inspected; binary arrays not downloaded. Notebook pools upstream arrays before repeated 80/20 splitting.
- Imported candidate. Prior evidence level: schema_inspected. Import is not a new file inspection or certification of labels.

- May group multiple datasets or overlap other model assets; do not count as an independent experimental dataset.

## Cell specificity

evidence: unknown; notes: Not direct mammalian cell-specificity evidence.

## Sources

- https://github.com/BorgwardtLab/SAPIENs
- https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/RBS_data/expected_data.txt
- https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/SANDSTORM/RBS_Predictor.ipynb

- url: https://github.com/BorgwardtLab/SAPIENs; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/RBS_data/expected_data.txt; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/SANDSTORM/RBS_Predictor.ipynb; supports: Previously recorded audit source; fresh dataset reconciliation pending

Related models: P012. Related resources: not established.
