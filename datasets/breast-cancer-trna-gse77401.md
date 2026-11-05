# Breast-cancer tRNA profiling and metastatic-state study

Registry ID: `breast-cancer-trna-gse77401` · study · **curated** · verification: **metadata**

Paper measures mature-tRNA families by a dedicated hybridization/probe-ligation readout and links them with translation context.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: MCF10A, MDA-MB-231 and CN34 parental cancer cells, and metastatic derivative lines.
- Assays: tRNA-specific hybridization / probe-ligation profiling; paired ribosome occupancy and transcript profiling
- Accessions: GSE77401
- Scale: value: 66; unit: GEO sample records; basis: Counted Series_sample_id entries in GEO text metadata; not independent donor counts or all tRNA-only libraries; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| tRNA-family abundance | Relative probe-based abundance across cell contexts | computed | source relative abundance | transcript |
| ribosome occupancy / mRNA stability | Separate paired-study endpoints, not direct tRNA abundance | computed | source-specific | transcript |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; source processed files; see exact extensions in data_urls
- Source license: unknown
- Redistribution: not established

- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE77nnn/GSE77401/suppl/GSE77401_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Selected metadata and listed headers only; raw reads and processed measurement rows were not inspected.
- Dedicated tRNA abundance matrix location/schema was not established in GEO subseries; paper supports the assay. Raw umbrella archive was not inspected.

- Probe families do not generally resolve individual isodecoder loci.
- GSE77401 is an umbrella series containing mRNA/microarray and ribosome subseries; 66 records are not 66 mature-tRNA libraries.

## Cell specificity

evidence: direct_multi_context; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE77401&targ=self&form=text&view=quick
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4915377/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE77401&targ=self&form=text&view=quick; supports: Series identity, organism, public status, sample-record count, linked processed files and study relationships
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4915377/; supports: Assay and biological measurement interpretation

Related models: not established. Related resources: gtrnadb.
