# GARDN-SANDSTORM release and source-data map

Registry ID: `gardn-sandstorm-release` · model_release · **curated** · verification: **metadata**

Code/model release reuses four upstream assay families and adds validation. Zenodo is a repository archive, not an independent biological dataset.

## What the data contains

- Observation unit: Source task dataset or validation record
- RNA scope: synthetic RNA; mRNA
- Biological context: Mixed bacterial translation, human UTR translation, cell-free diagnostic and aptamer-sensor contexts.
- Assays: upstream measured assays; computational benchmark
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| source-specific endpoints | ON/OFF, ribosome load, RBS activity and Cas13 diagnostic activity stay distinct | annotation | not comparable | unknown |

## Access and reuse

- Access: mixed
- Formats: CSV; XLSX; NPY; notebooks; Git LFS
- Source license: Custom Academic Open Source License for software; source data terms vary
- Redistribution: Software academic/noncommercial use subject to LICENSE.txt; data rights require source-specific review

- https://github.com/AlexGreenLab/GARDN-SANDSTORM/tree/main/data
- https://github.com/AlexGreenLab/GARDN-SANDSTORM/tree/main/aptamer/data

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/README.txt; https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/toehold_data/expected_data.txt; https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/LICENSE.txt.

- No model execution or weight download performed.
- Sequence-derived compatibility arrays are not measured structure.

- Do not count upstream reuse as new observations.
- Separate predictions/generated examples from wet-lab labels.
- Keep bacterial, mammalian, aptamer and diagnostic endpoints separate.

## Cell specificity

evidence: context_only; notes: Native tasks are not a matched mammalian selectivity panel.

## Sources

- https://github.com/AlexGreenLab/GARDN-SANDSTORM
- https://www.nature.com/articles/s41467-025-59389-8
- https://zenodo.org/records/15058435

- url: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/README.txt; supports: Release task map and Zenodo archive link.
- url: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/toehold_data/expected_data.txt; supports: Upstream toehold file points to Angenent-Mari and CL_RNA_SynthBio.
- url: https://www.nature.com/articles/s41467-025-59389-8; supports: New experimental versus upstream reused data.
- url: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/LICENSE.txt; supports: Academic/noncommercial software license.

Related models: P012. Related resources: toehold-flowseq-gse149225; sample2019-chemistry-reporters; sapiens-uaspire-rbs; adapt-cas13-activity; gardn-aptaswitch-screen; gardn-aptaswitch-validation; gardn-toehold-validation; gardn-predicted-utr-traces.
