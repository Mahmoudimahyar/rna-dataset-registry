# GARDN-SANDSTORM 384-member aptaswitch screen

Registry ID: `gardn-aptaswitch-screen` · study · **curated** · verification: **file_sample**

New measured aptamer-sensor screen; fluorescence is distinct from protein translation.

## What the data contains

- Observation unit: Aptaswitch/target with dilution and control fields
- RNA scope: aptamer; synthetic RNA
- Biological context: Cell-free aptamer fluorescence, target present versus absent; no cell panel.
- Assays: fluorescent aptamer assay
- Accessions: not established
- Scale: value: 384; unit: aptaswitches; basis: Paper reports 384; high_throughput sheet has 385 declared rows including header; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ON_1/2/4; OFF_1/2/4 | Measured fluorescence at source dilution labels | measured | source fluorescence units | construct |
| ADJ_ON; ADJ_OFF; ADJ_ON_OFF | Adjusted outputs and ratio | computed | source-normalized output / fold ratio | construct |

## Access and reuse

- Access: open
- Formats: XLSX
- Source license: unknown
- Redistribution: not established

- https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/aptaswitch_data.xlsx

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/aptaswitch_data.xlsx (sheet names, dimensions, header only).

- Values/formulas not audited.
- Sheet name high_throughput does not override paper's manual low-throughput characterization description.
- Exact concentration units and adjustments not independently established.

- Hairpin templates overlap toehold source data; these fluorescence measurements are new.
- Keep target/template families together across splits and retain controls.

## Cell specificity

evidence: mechanistic_sensor; notes: Cell-free target-responsive signal.

## Sources

- https://www.nature.com/articles/s41467-025-59389-8
- https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/aptamer/data/aptaswitch_data.xlsx

- url: https://media.githubusercontent.com/media/AlexGreenLab/GARDN-SANDSTORM/main/aptamer/data/aptaswitch_data.xlsx; supports: high_throughput sheet dimensions and output schema.
- url: https://www.nature.com/articles/s41467-025-59389-8; supports: Screen identity; fluorescent aptamer rather than translation endpoint.

Related models: P012. Related resources: gardn-sandstorm-release; toehold-flowseq-gse149225; gardn-aptaswitch-validation.
