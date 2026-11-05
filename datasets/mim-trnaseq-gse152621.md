# mim-tRNAseq method study

Registry ID: `mim-trnaseq-gse152621` · study · **curated** · verification: **schema**

Dedicated mature-tRNA profiling with separate abundance, modification-signature and charging applications.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Human HEK293T/K562, budding and fission yeast, and Drosophila cells; method conditions and charging subsets.
- Assays: mim-tRNAseq
- Accessions: GSE152621
- Scale: value: 29; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| isodecoder / anticodon counts | Processed mature-tRNA abundance counts | computed | mapped reads | transcript |
| misincorporation signature | RT-derived modification-associated signal; chemistry not necessarily identified | computed | fraction | position |
| charging fraction | Only dedicated charging comparisons; do not assign to every library | computed | fraction | transcript |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Dmel_anticodon_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Dmel_isodecoder_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Hsap_anticodon_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Hsap_isodecoder_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Scer_anticodon_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Scer_isodecoder_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Spom_anticodon_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Spom_isodecoder_counts.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Dmel_isodecoder_counts.csv.gz (CSV header only).

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Only Drosophila isodecoder CSV header inspected; human and charging tables not inspected.

- Selected sample lists S288c, 972h, dm6 and hg19 builds.
- Source clustering and Single_isodecoder flag matter; ambiguous near-identical tRNAs may not resolve individual loci.
- RT signatures are assay-dependent and distinct from modification stoichiometry.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE152621&targ=self&form=text&view=quick
- https://doi.org/10.1016/j.molcel.2021.01.028

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE152621&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://doi.org/10.1016/j.molcel.2021.01.028; supports: Assay and biological measurement interpretation
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE152nnn/GSE152621/suppl/GSE152621_Dmel_isodecoder_counts.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected

Related models: not established. Related resources: gtrnadb; modomics.
