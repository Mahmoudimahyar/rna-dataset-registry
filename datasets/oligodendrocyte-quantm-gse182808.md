# Oligodendrocyte differentiation QuantM-seq study

Registry ID: `oligodendrocyte-quantm-gse182808` · study · **curated** · verification: **schema**

Dedicated tRNA subseries of a paired tRNA, mRNA-decay and ribosome-profiling study.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Mouse epiblast-derived oligodendrocyte progenitors (OPC), oligodendrocytes (OL) and astrocytes.
- Assays: QuantM-seq
- Accessions: GSE182808
- Scale: value: 7; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| isodecoder / anticodon RPM | Relative cytosolic tRNA abundance | computed | RPM | transcript |
| differential statistics | OPC-versus-OL DESeq2 contrast outputs | computed | log difference and p-value | transcript |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE182nnn/GSE182808/suppl/GSE182808_OPC_OL_astro_anticodon_RPM.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE182nnn/GSE182808/suppl/GSE182808_OPC_OL_astro_gene_cyto_RPM.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE182nnn/GSE182808/suppl/GSE182808_OPC_OL_tRNA_anticodon_diff_DESeq2.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE182nnn/GSE182808/suppl/GSE182808_OPC_OL_tRNA_gene_diff_DESeq2.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE182nnn/GSE182808/suppl/GSE182808_OPC_OL_astro_anticodon_RPM.csv.gz (CSV header only).

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Header confirms OPC_1-3, OL_1-2 and Astrocyte_1-2; no modification-table rows inspected.

- mm10 reference; seven tRNA libraries, distinct from GSE182811 SuperSeries total.
- GSE182809 decay, GSE182810 ribosome profiling and GSE198271 yeast controls are different assay/organism subsets; do not pool as mouse tRNA samples.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE182808&targ=self&form=text&view=quick
- https://www.nature.com/articles/s41467-022-32766-3

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE182808&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://www.nature.com/articles/s41467-022-32766-3; supports: Assay and biological measurement interpretation
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE182nnn/GSE182808/suppl/GSE182808_OPC_OL_astro_anticodon_RPM.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected

Related models: not established. Related resources: gtrnadb.
