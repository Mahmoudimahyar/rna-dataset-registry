# T-cell activation tRNA study

Registry ID: `tcell-activation-gse165537` · study · **curated** · verification: **schema**

Dedicated mouse T-cell tRNA subseries with paired mRNA/ribosome measurements in a separate subseries.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Naive CD4 T cells and 20-, 48- and 72-hour activation; later CD62L-high/low states and assay demethylase subsets.
- Assays: DM-tRNA-seq adapted tRNA sequencing; LC/MS in paired paper experiments
- Accessions: GSE165537
- Scale: value: 30; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| cytosolic tRNA / anticodon RPM | Source relative read abundance | computed | RPM | transcript |
| activation and sorting state | Timepoint, naive status and later high/low group labels | annotation | unknown | sample |
| RT / modification signal | Assay-dependent modification evidence; not synonymous with abundance | computed | source-specific | position |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE165nnn/GSE165537/suppl/GSE165537_set1_cytosolictRNAReads_RPM.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE165nnn/GSE165537/suppl/GSE165537_set1_cytosolictRNA_byAntiCodon_RPM.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE165nnn/GSE165537/suppl/GSE165537_set2_cytosolictRNAReads_RPM.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE165nnn/GSE165537/suppl/GSE165537_set2_cytosolictRNA_byAntiCodon_RPM.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE165nnn/GSE165537/suppl/GSE165537_set1_cytosolictRNAReads_RPM.csv.gz (CSV header only).

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Processed header includes hi/lo columns; linkage to CD62L labels comes from the paper, not the abbreviated column strings alone.

- Selected sample declares mm10. Multi-mapping reads use source allocation; gene-level values are not unambiguous locus measurements.
- Modification changes can alter RT recovery; preserve demethylase and sorting labels. GSE165536 is RNA/Ribo-seq, not this tRNA matrix.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE165537&targ=self&form=text&view=quick
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8594584/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE165537&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8594584/; supports: Assay and biological measurement interpretation
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE165nnn/GSE165537/suppl/GSE165537_set1_cytosolictRNAReads_RPM.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected

Related models: not established. Related resources: gtrnadb; modomics.
