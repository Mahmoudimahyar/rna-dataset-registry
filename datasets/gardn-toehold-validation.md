# GARDN-generated toehold reporter validation

Registry ID: `gardn-toehold-validation` · study · **curated** · verification: **file_sample**

New measured reporter table with construct identifiers and replicate ON/OFF outputs.

## What the data contains

- Observation unit: Construct by condition
- RNA scope: synthetic RNA
- Biological context: Toehold reporter validation; header alone provides no cell metadata.
- Assays: reporter fluorescence assay
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ON; OFF | Trigger-present/absent reporter readings | measured | source fluorescence units | construct |
| Avg. ON; Avg. OFF; ON/OFF Ratio | Source means and response ratio | computed | fluorescence / fold ratio | construct |

## Access and reuse

- Access: open
- Formats: CSV
- Source license: unknown
- Redistribution: not established

- https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/data/GARDN_toehold_processed_data.csv

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/data/GARDN_toehold_processed_data.csv (header only).

- Sequence/context joins require separate source tables.
- Blank replicate header cells mean this is not automatically a tidy schema.

- Keep constructs and related design groups together in splits.
- Predicted scores cannot replace measured readings.

## Cell specificity

evidence: mechanistic_sensor; notes: Molecular ON/OFF, not cell selectivity.

## Sources

- https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/GARDN_toehold_processed_data.csv
- https://www.nature.com/articles/s41467-025-59389-8

- url: https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/data/GARDN_toehold_processed_data.csv; supports: Live header with Name, ON/OFF, means and ratio.
- url: https://www.nature.com/articles/s41467-025-59389-8; supports: Experimental validation distinct from predicted scores.

Related models: P012. Related resources: gardn-sandstorm-release; toehold-flowseq-gse149225.
