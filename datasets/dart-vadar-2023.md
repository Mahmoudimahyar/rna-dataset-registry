# DART VADAR autocatalytic RNA sensing

Registry ID: `dart-vadar-2023` · study · **curated** · verification: **metadata**

ADAR-dependent RNA sensing study. Reporter output, editing measurements and sequencing specificity data are separate endpoints.

## What the data contains

- Observation unit: Sensor/target/context condition; sequencing has a separate sample unit
- RNA scope: mRNA; synthetic RNA
- Biological context: Human reporter assays and mouse C2C12 differentiation-state sensing; keep contexts separate.
- Assays: reporter fluorescence; RNA editing quantification; amplicon sequencing; RNA-seq
- Accessions: PRJNA932010
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| reporter output | Protein reporter response to target RNA | measured | source relative fluorescence | construct |
| fold response | Source reporter signal relative to a matched control | computed | fold ratio | construct |
| editing fraction | A-to-I editing readout | measured | fraction or percent; retain source scale | position |

## Access and reuse

- Access: mixed
- Formats: source data; supplementary information; SRA reads
- Source license: unknown
- Redistribution: not established

- https://www.nature.com/articles/s41467-023-36851-z
- https://www.ncbi.nlm.nih.gov/bioproject/PRJNA932010

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- ENA returned 48 human runs with AMPLICON and RNA-Seq strategies.
- Paper supplies fold changes, editing rates and RT-qPCR calculations; raw FCS and some scripts are request-based.
- DART VADAR is one named study/system, not separate DART and VADAR datasets.

- Preserve trigger, ADAR context, normalization and negative control.
- Group related sensors and target regions across splits.
- Intracellular expression does not establish delivery efficiency.
- Sequencing archive is not automatically a sensor-response training table.

## Cell specificity

evidence: mechanistic_sensor; notes: RNA-dependent intracellular expression in selected contexts; delivery and broad selectivity need separate evidence.

## Sources

- https://www.nature.com/articles/s41467-023-36851-z
- https://www.ncbi.nlm.nih.gov/bioproject/PRJNA932010
- https://github.com/joncchen/dart_vadar

- url: https://www.nature.com/articles/s41467-023-36851-z; supports: Sensing context and available source material; original-data statement.
- url: https://www.ebi.ac.uk/ena/portal/api/filereport?accession=PRJNA932010&result=read_run&fields=study_accession,run_accession,scientific_name,sample_title,library_strategy&format=tsv; supports: Live archive metadata checked; run presence/absence and strategies recorded in public evidence.

Related models: not established. Related resources: eukaryotic-toeholds-zhao2021.
