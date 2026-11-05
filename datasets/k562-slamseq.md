# K562 SLAM-seq endogenous decay

Registry ID: `k562-slamseq` · study · **curated** · verification: **metadata**

SLAM-seq for K562 endogenous mRNA decay

## What the data contains

- Observation unit: Gene/transcript by timepoint
- RNA scope: mRNA
- Biological context: K562 endogenous mRNA decay
- Assays: SLAM-seq
- Accessions: GSE126522
- Scale: value: 16; unit: GEO sample records; basis: Counted in live series metadata; not independent biological replicates; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| conversion-aware abundance / decay | Metabolic-labeling-based decay observations and fitted estimates; preserve exact fit/unit | measured | unknown | transcript |

## Access and reuse

- Access: open
- Formats: GEO metadata; source processed files; SRA reads
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126522
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE126nnn/GSE126522/suppl/GSE126522_RNAlevels.csv.gz
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE126nnn/GSE126522/suppl/GSE126522_time_course_slam_CPM.csv.gz

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- GSE126523 is the parent SuperSeries; do not count parent and this child as independent data.
- Retain timepoint, replicate and conversion/QC metadata.

## Cell specificity

evidence: none; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126522

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126522; supports: Resource identity, available label types and access route described in primary source documentation
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126522&targ=self&form=text&view=brief; supports: Live SOFT series title, design, subseries relationships, sample IDs and supplementary filenames

Related models: not established. Related resources: geo; sra.
