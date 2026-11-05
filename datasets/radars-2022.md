# RADARS reprogrammable ADAR sensors

Registry ID: `radars-2022` · study · **curated** · verification: **paper**

ADAR-dependent RNA sensing study. Reporter output, editing measurements and sequencing specificity data are separate endpoints.

## What the data contains

- Observation unit: Sensor/target/context condition; sequencing has a separate sample unit
- RNA scope: mRNA; synthetic RNA
- Biological context: Mammalian endogenous transcript sensing; multi-input and specificity contexts vary by experiment.
- Assays: reporter fluorescence; RNA editing quantification; RNA sequencing
- Accessions: PRJNA883765
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

- https://www.nature.com/articles/s41587-022-01534-5
- https://www.ncbi.nlm.nih.gov/bioproject/PRJNA883765

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Paper prospectively declares PRJNA883765; live ENA query returned zero runs. Public read release remains unconfirmed.
- Paper/supplement results available; original measurements are request-based. Table/FCS schema not inspected.
- Distinct from Kaseniit RADAR and the unrelated RADAR RNA-editing database.

- Preserve trigger, ADAR context, normalization and negative control.
- Group related sensors and target regions across splits.
- Intracellular expression does not establish delivery efficiency.
- Sequencing archive is not automatically a sensor-response training table.

## Cell specificity

evidence: mechanistic_sensor; notes: RNA-dependent intracellular expression in selected contexts; delivery and broad selectivity need separate evidence.

## Sources

- https://www.nature.com/articles/s41587-022-01534-5
- https://www.ncbi.nlm.nih.gov/bioproject/PRJNA883765
- https://github.com/abugoot-lab/RADARS

- url: https://www.nature.com/articles/s41587-022-01534-5; supports: Sensing context and available source material; original-data statement.
- url: https://www.ebi.ac.uk/ena/portal/api/filereport?accession=PRJNA883765&result=read_run&fields=study_accession,run_accession,scientific_name,sample_title,library_strategy&format=tsv; supports: Live archive metadata checked; run presence/absence and strategies recorded in public evidence.

Related models: not established. Related resources: eukaryotic-toeholds-zhao2021.
