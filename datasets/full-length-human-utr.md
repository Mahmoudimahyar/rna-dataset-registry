# Full-length human 3-prime UTR regulation study

Registry ID: `full-length-human-utr` · study · **curated** · verification: **metadata**

The quantitative impact of 3′UTRs on gene expression

## What the data contains

- Observation unit: UTR construct or companion assay sample
- RNA scope: mRNA
- Biological context: Human full-length UTR reporter study with distinct promoter contexts
- Assays: amplicon-seq; RNA-seq; PRO-seq; miRNA-seq; plasmid-seq
- Accessions: GSE270254; GSE270247; GSE270248; GSE270249; GSE270252; GSE270253
- Scale: value: 118; unit: GEO sample records; basis: Counted in live series metadata; not independent biological replicates; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RNA stability | Reporter-specific stability outcome | measured | unknown | transcript |
| translation / protein output | Distinct reporter endpoints; not all present in every subseries | measured | unknown | transcript |
| companion miRNA counts | Small-RNA context measurement in GSE270249; not the reporter target itself | measured | unknown | transcript |

## Access and reuse

- Access: open
- Formats: GEO metadata; source processed files; SRA reads
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE270254

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- GSE270249 alone is4sample miRNA-seq; reporter amplicon subseries isGSE270252.
- Preserve promoter, reporter, library, normalization and biological replicate.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE270254

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE270254; supports: Resource identity, available label types and access route described in primary source documentation
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE270254&targ=self&form=text&view=brief; supports: Live SOFT series title, design, subseries relationships, sample IDs and supplementary filenames

Related models: not established. Related resources: geo; sra.
