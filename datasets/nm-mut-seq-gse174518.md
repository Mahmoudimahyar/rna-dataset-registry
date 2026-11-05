# Nm-Mut-seq

Registry ID: `nm-mut-seq-gse174518` · study · **curated** · verification: **metadata**

Mutation-signature mapping and quantitative calibration of Am, Cm and Gm, with explicit lack of Um detection.

## What the data contains

- Observation unit: A covered Am/Cm/Gm candidate position in an assay context, or a calibration observation.
- RNA scope: mRNA; rRNA
- Biological context: HeLa/HepG2 total and poly(A)+ RNA; includes calibration sets and HepG2 FBL/FTSJ3 perturbation subsets.
- Assays: Nm-Mut-seq
- Accessions: GSE174518
- Scale: value: 53; unit: GEO samples (profiling, calibration and perturbation subsets); basis: Counted live GEO Series_sample_id fields.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Am/Cm/Gm site | Modification inferred from source mutation signatures; Um is outside assay detection. | computed | unknown | position |
| Nm methylation fraction | Assay-derived estimate informed by source calibration curves. | computed | fraction | position |

## Access and reuse

- Access: open
- Formats: XLSX (site, rRNA, calibration tables); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174518

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.

- Um non-detection is an assay blind spot, not evidence that uridines lack 2′-O-methylation.
- Calibration and profiling rows have distinct observation units.
- Comparisons with Nm-seq require assay-specific bias and version control; endogenous noncalls are not definitive negatives.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174518&targ=self&form=text&view=full
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10474006/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174518&targ=self&form=text&view=full; supports: Live series metadata explicitly states Am/Cm/Gm detection, Um non-detection, calibration and perturbation subsets.
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10474006/; supports: Original study describes base-resolution quantitative Nm mapping and GEO linkage.

Related models: not established. Related resources: nm-seq-gse90164.
