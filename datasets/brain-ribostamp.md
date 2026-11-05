# Mouse-brain single-cell and isoform Ribo-STAMP study

Registry ID: `brain-ribostamp` · study · **curated** · verification: **metadata**

Single cell and isoform-specific translational profiling of the mouse brain

## What the data contains

- Observation unit: Cell/transcript or bulk sample, assay-specific
- RNA scope: mRNA
- Biological context: Mouse brain, source-defined cell types and isoforms
- Assays: Ribo-STAMP; short-read RNA-seq; long-read RNA-seq
- Accessions: GSE314176; GSE275091; GSE275133; GSE276504; GSE314058; GSE314059
- Scale: value: 25; unit: GEO sample records; basis: Counted in live series metadata; not independent biological replicates; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| editing / ribosome association | Ribosome-associated editing proxy, not direct ribosome footprints | measured | unknown | transcript |
| cell / isoform annotation | Cell identity and long-read isoform context | annotation | unknown | cell |

## Access and reuse

- Access: open
- Formats: GEO metadata; source processed files; SRA reads
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314176
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE314nnn/GSE314176/suppl/GSE314176_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- SuperSeries has multiple assay-specific subseries; do not pool all samples as one measurement type.
- Editing efficiency, expression and detection biases affect interpretation.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314176

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314176; supports: Resource identity, available label types and access route described in primary source documentation
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE314176&targ=self&form=text&view=brief; supports: Live SOFT series title, design, subseries relationships, sample IDs and supplementary filenames

Related models: not established. Related resources: geo; sra.
