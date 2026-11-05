# RADAR modular programmable RNA sensing

Registry ID: `radar-2022` · study · **curated** · verification: **metadata**

ADAR-dependent RNA sensing study. Reporter output, editing measurements and sequencing specificity data are separate endpoints.

## What the data contains

- Observation unit: Sensor/target/context condition; sequencing has a separate sample unit
- RNA scope: mRNA; synthetic RNA
- Biological context: Mammalian cell-line sensing of endogenous/altered transcript identity or abundance; plant experiments are separate contexts.
- Assays: reporter fluorescence; RNA editing quantification; amplicon sequencing
- Accessions: PRJNA874842
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

- https://www.nature.com/articles/s41587-022-01493-x
- https://www.ncbi.nlm.nih.gov/bioproject/PRJNA874842

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- ENA returned 42 human AMPLICON runs, not a full sensor reporter table.
- Paper states raw flow cytometry is available upon request.
- November 2022 author correction must be retained; code access does not imply FCS release.

- Preserve trigger, ADAR context, normalization and negative control.
- Group related sensors and target regions across splits.
- Intracellular expression does not establish delivery efficiency.
- Sequencing archive is not automatically a sensor-response training table.

## Cell specificity

evidence: mechanistic_sensor; notes: RNA-dependent intracellular expression in selected contexts; delivery and broad selectivity need separate evidence.

## Sources

- https://www.nature.com/articles/s41587-022-01493-x
- https://www.ncbi.nlm.nih.gov/bioproject/PRJNA874842
- https://github.com/kristjaneerik/radar-rna-sensing

- url: https://www.nature.com/articles/s41587-022-01493-x; supports: Sensing context and available source material; original-data statement.
- url: https://www.ebi.ac.uk/ena/portal/api/filereport?accession=PRJNA874842&result=read_run&fields=study_accession,run_accession,scientific_name,sample_title,library_strategy&format=tsv; supports: Live archive metadata checked; run presence/absence and strategies recorded in public evidence.

Related models: not established. Related resources: eukaryotic-toeholds-zhao2021.
