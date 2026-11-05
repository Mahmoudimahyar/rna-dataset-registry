# Drosophila ecdysone-response small-RNA study

Registry ID: `ecdysone-smallrna-gse69934` · study · **curated** · verification: **metadata**

tRNA estimates from size-enriched small-RNA libraries in a paired transcript/protein study.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Drosophila Kc167 cells; ecdysone response and a separately labelled heat-shock component in the deposited series.
- Assays: ordinary small RNA-seq; paired transcriptomics / proteomics in paper
- Accessions: GSE69934
- Scale: value: 16; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| tRNA abundance estimate | Relative reads at annotated tRNA loci; may include precursor or fragment signal | computed | source normalized counts | transcript |
| tRNA fold change | Source condition contrast | computed | fold change | transcript |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE69nnn/GSE69934/suppl/GSE69934_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Series contains more conditions than the ecdysone paper comparison; no processed matrix was inspected.

- Dm6 release-6 annotations; paper states missing tRNA-type annotations limit coverage.
- Multimappers are randomly assigned and regions extend beyond tRNA bodies; not a dedicated mature-total-tRNA assay.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE69934&targ=self&form=text&view=quick
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4574756/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE69934&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4574756/; supports: Assay and biological measurement interpretation

Related models: not established. Related resources: gtrnadb.
