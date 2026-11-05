# Angenent-Mari toehold Flow-seq library (GSE149225)

Registry ID: `toehold-flowseq-gse149225` · study · **curated** · verification: **file_sample**

Bacterial trigger-responsive reporter library. GEO, CL_RNA_SynthBio and SANDSTORM reuse belong to this source family.

## What the data contains

- Observation unit: Switch configuration with ON/OFF gate-count measurements
- RNA scope: synthetic RNA
- Biological context: Bacterial in vivo reporter assay. ON and OFF indicate trigger states; viral/human trigger provenance is not assay cell species.
- Assays: Flow-seq; fluorescence sorting and sequencing
- Accessions: GSE149225; PRJNA627694; SRP258130
- Scale: value: 91534; unit: switches with QC_ON_OFF >= 2; basis: Independently counted non-sequence QC columns of the 244000-row processed CSV; matches final QC2 set; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ON; OFF | Source-normalized reporter activity with and without trigger | measured | source-normalized fluorescence | construct |
| ON_OFF | Ratio of measured ON and OFF activity | computed | fold ratio | construct |
| QC_ON; QC_OFF; QC_ON_OFF | Endpoint-specific source quality strata | annotation | ordinal QC level | construct |

## Access and reuse

- Access: open
- Formats: CSV.gz; SRA reads
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE149nnn/GSE149225/suppl/GSE149225_toehold_processed_datafile.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE149nnn/GSE149225/suppl/GSE149225_toehold_processed_datafile.csv.gz (header and aggregate QC columns only).

- Nucleotide fields and individual activity values were not retained or validated.
- Separate ON/OFF endpoint QC and missingness must be preserved.
- Full processing and absolute fluorescence calibration not reproduced.

- Keep related triggers, tiled regions and matched ON/OFF configurations in the same split.
- Lower-QC gate-boundary artifacts and source-normalized scale remain relevant.
- Do not double-count CL_RNA_SynthBio or SANDSTORM reuse.

## Cell specificity

evidence: mechanistic_sensor; notes: Bacterial ON/OFF molecular states are not mammalian cell types.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE149225
- https://www.nature.com/articles/s41467-020-18677-1
- https://github.com/lrsoenksen/CL_RNA_SynthBio

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE149225&targ=self&form=text&view=full; supports: GEO identity, public status, processed file and related accessions.
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE149nnn/GSE149225/suppl/GSE149225_toehold_processed_datafile.csv.gz; supports: Header and aggregate QC columns: 244000 total rows; 91534 at ratio QC >= 2.
- url: https://www.collinslab.mit.edu/s/naturecommunications_nico-44zm.pdf; supports: Paper chooses QC2 threshold and discusses lower-QC sorting artifacts.

Related models: P012. Related resources: not established.
