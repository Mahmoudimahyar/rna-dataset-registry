# QuantM-tRNA-seq tissue study

Registry ID: `quantm-trnaseq-gse141436` · study · **curated** · verification: **schema**

Dedicated mature-tRNA profiling with tissue-dependent isodecoder and anticodon measurements.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Mouse cortex, cerebellum, medulla oblongata, spinal cord, heart, liver and tibialis; human-cell method comparisons.
- Assays: QuantM-tRNA-seq
- Accessions: GSE141436
- Scale: value: 29; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| isodecoder / anticodon raw counts | Mapped read counts; source downstream analyses also use RPM | computed | reads | transcript |
| variant / truncation fraction | Modification-associated RT signal, not a definitive chemical identity | computed | fraction | position |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_293FlpIn_DM_isodecoder_raw_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_293FlpIn_isodecoder_raw_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_Mouse_tissue_anticodon_raw_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_Mouse_tissue_isodecoder_raw_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_Mouse_tissue_variant_counts.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_Mouse_tissue_variant_counts_DM.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_293FlpIn_DM_isodecoder_raw_counts.csv.gz (CSV header only); https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_Mouse_tissue_isodecoder_raw_counts.csv.gz (CSV header only).

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Tissue matrix header confirms seven tissue labels with three columns each; measurement rows were not examined.

- GtRNAdb Release 18; human hg38 and mouse mm10; identical reference sequences collapsed.
- Stable anticodon pools can coexist with tissue-dependent isodecoder composition. RT and short-read mapping affect recovery.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE141436&targ=self&form=text&view=quick
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7428014/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE141436&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7428014/; supports: Assay and biological measurement interpretation
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_293FlpIn_DM_isodecoder_raw_counts.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected
- url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE141nnn/GSE141436/suppl/GSE141436_Mouse_tissue_isodecoder_raw_counts.csv.gz; supports: Inspected CSV header confirms named sample columns; no measurement rows inspected

Related models: not established. Related resources: gtrnadb; modomics.
