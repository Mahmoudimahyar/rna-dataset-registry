# mRNA m5C in pluripotent stem cells and derived cardiomyocytes

Registry ID: `hpsc-m5c-gse240569` · study · **curated** · verification: **metadata**

RNA bisulfite profiles of human pluripotent stem-cell sources and derived cardiomyocytes, with separate expression companion outputs.

## What the data contains

- Observation unit: A candidate m5C locus and methylation estimate within one sample/condition; companion expression rows have a different unit.
- RNA scope: mRNA
- Biological context: Three human pluripotent stem-cell sources and their cardiomyocyte derivatives; full sample/assay mapping requires local source-file inspection.
- Assays: mRNA bisulfite sequencing; RNA-seq
- Accessions: GSE240569
- Scale: value: 38; unit: GEO samples (all assay types); basis: Counted live GEO Series_sample_id fields; cannot be equated with 38 m5C profiles.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| m5C locus/methylation level | Bisulfite-derived candidate position and methylation estimate. | computed | unknown | position |
| gene read count | Companion expression count rather than a modification-site label. | computed | read count | transcript |
| differential expression | DESeq2 comparison statistic supplied separately. | computed | unknown | transcript |

## Access and reuse

- Access: open
- Formats: XLSX (m5C loci, DEGs); TXT.GZ (HTSeq counts); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE240569

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.

- Series includes expression companions; modification and expression labels must not be conflated.
- Cell-state comparison is not a synthetic-mRNA expression or degradation experiment.
- Coverage, conversion efficiency and replicate agreement constrain negative/site calls.

## Cell specificity

evidence: direct_multi_context; notes: The study compares pluripotent and differentiated states; donor/source and assay confounding require sample-aware analysis.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE240569&targ=self&form=text&view=full
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8541012

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE240569&targ=self&form=text&view=full; supports: Live series metadata establishes source/derivative comparison, title, sample list and m5C/expression supplementary filenames.
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8541012; supports: Sample metadata describes hg38 reference and source supplementary-file roles.

Related models: not established. Related resources: m5c-atlas; ubs-seq-gse225614.
