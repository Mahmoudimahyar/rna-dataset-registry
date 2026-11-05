# Single-cell ribosome profiling

Registry ID: `single-cell-ribo` · study · **curated** · verification: **metadata**

Ribosomal profiling in single cells reveals cell-cycle dependent translational pausing

## What the data contains

- Observation unit: Cell/condition by ribosome footprint or positional count
- RNA scope: mRNA
- Biological context: See source sample/condition metadata
- Assays: scRibo-seq
- Accessions: GSE162060
- Scale: value: 37; unit: GEO sample records; basis: Counted in live series metadata; not independent biological replicates; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ribosome footprint counts | Direct RPF signal; sparse at single-cell scale | measured | count | position |
| pausing summary | Derived analysis of footprints; not a directly counted pausing target | computed | source-defined score | position |

## Access and reuse

- Access: open
- Formats: GEO metadata; source processed files; SRA reads
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162060
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_EE_Dis_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_EE_Mid_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_EE_Pro_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_EE_RPFcounts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_EE_metadata.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_HEK293T_RPFcounts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_HEK293T_Starv_RPFcounts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_HEK293T_Starv_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_HEK293T_Starv_metadata.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_HEK293T_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_HEK293T_metadata.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_RPE-FUCCI_RPFcounts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_RPE-FUCCI_metadata.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_RPE_G0_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_RPE_KO_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_RPE_MGI_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_RPE_Mit_layout.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE162nnn/GSE162060/suppl/GSE162060_RPE_SR2_layout.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Single-cell footprint data is sparse; retain UMI/cell quality and cell-cycle labels.
- Not interchangeable with ordinary scRNA-seq or ribosome-associated editing.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162060

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162060; supports: Resource identity, available label types and access route described in primary source documentation
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162060&targ=self&form=text&view=brief; supports: Live SOFT series title, design, subseries relationships, sample IDs and supplementary filenames

Related models: not established. Related resources: geo; sra.
