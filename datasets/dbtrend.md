# DBtRend

Registry ID: `dbtrend` · derived_resource · **curated** · verification: **paper**

tRNA estimates from human small-RNA and miRNA sequencing projects, with source sample annotations and differential analyses.

## What the data contains

- Observation unit: Pipeline-defined tRNA entity by source sample
- RNA scope: tRNA
- Biological context: GEO biological conditions and TCGA cancers; source tissue, cell, disease and subtype labels retained.
- Assays: reanalysis of small RNA-seq / miRNA-seq
- Accessions: not established
- Scale: value: 14986; unit: samples in 2021 paper; basis: Historical paper reports 183 projects and 14,986 samples; current matrices not counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| individual / isodecoder / isoacceptor expression | Processed normalized mapped-read estimates | computed | log2 CPM; individual-tRNA RPKM/TPM | transcript |
| DEtRNA statistics | Source contrast outputs: logFC, logCPM, F, PValue, FDR, Sig | computed | unknown | transcript |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://trend.pmrc.re.kr/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Live portal files not inspected; scale is the publication snapshot.

- Authors explicitly report difficulty separating mature tRNAs from tRNA fragments.
- hg38 predicted reference and pipeline-defined groupings; batch correction and units must be preserved.
- TCGA entries overlap tRic; projects are not independent new experiments.

## Cell specificity

evidence: direct_multi_context; notes: Multi-context estimates; assay bias and fragment ambiguity constrain biological specificity.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC8535304/
- https://trend.pmrc.re.kr/

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8535304/; supports: 2021 snapshot size; small-RNA/miRNA sources, hg38 pipeline, CPM/RPKM/TPM and DE statistic definitions; explicit fragment ambiguity

Related models: not established. Related resources: tric; gtrnadb.
