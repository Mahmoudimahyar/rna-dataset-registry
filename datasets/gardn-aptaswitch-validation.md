# GARDN-generated aptaswitch validation

Registry ID: `gardn-aptaswitch-validation` · study · **curated** · verification: **file_sample**

Measured generated-sensor table, distinct from the 384-member screen and from predictor scores.

## What the data contains

- Observation unit: Named generated aptaswitch with target/control measurements
- RNA scope: aptamer; synthetic RNA
- Biological context: Cell-free fluorescence; no cell-type label.
- Assays: fluorescent aptamer assay
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ON_1/2/4; OFF_1/2/4 | Measured target-present/absent outputs | measured | source fluorescence units | construct |
| ADJ_ON; ADJ_OFF; ADJ_ON_OFF | Adjusted fluorescence and ratio | computed | source-normalized output / fold ratio | construct |

## Access and reuse

- Access: open
- Formats: CSV; XLSX
- Source license: unknown
- Redistribution: not established

- https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/processed_gardn_data_6_28.csv
- https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/aptaswitch_data.xlsx

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/processed_gardn_data_6_28.csv (header only); https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/aptaswitch_data.xlsx (forward_designed header and dimensions only).

- Full cardinality and adjustments not validated.
- Not assumed identical to all screen measurements.

- Separate validation from screen/train rows.
- Shared templates/controls create split leakage.

## Cell specificity

evidence: mechanistic_sensor; notes: No mammalian selectivity panel.

## Sources

- https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/aptamer/data/processed_gardn_data_6_28.csv
- https://www.nature.com/articles/s41467-025-59389-8

- url: https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/processed_gardn_data_6_28.csv; supports: Header has identity, concentration, raw and adjusted-output fields.
- url: https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/aptaswitch_data.xlsx; supports: Separate forward_designed sheet exists.

Related models: P012. Related resources: gardn-aptaswitch-screen; gardn-sandstorm-release.
