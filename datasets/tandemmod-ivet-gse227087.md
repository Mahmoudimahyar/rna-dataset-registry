# TandemMod IVET/DRS benchmark datasets

Registry ID: `tandemmod-ivet-gse227087` · benchmark · **curated** · verification: **metadata**

Modification-labeled in-vitro epitranscriptome data and direct-RNA experiments released with TandemMod; synthetic benchmark labels remain distinct from in-vivo predictions.

## What the data contains

- Observation unit: A nanopore read-position/signal observation with source chemistry label; pooled in-vivo calls form a separate endpoint.
- RNA scope: mRNA; synthetic RNA
- Biological context: Rice-cDNA-derived IVET calibration data, synthetic RNA controls and rice in-vivo DRS subsets; independent human validation uses reused public studies.
- Assays: nanopore direct RNA sequencing; source-defined modified/unmodified calibration
- Accessions: GSE227087
- Scale: value: 8; unit: GEO samples (mixed IVET, synthetic and rice contexts); basis: Counted live GEO Series_sample_id fields; not a count of labeled sites or transcripts.; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| IVET modification class | Experimental source chemistry class, including m6A/m1A/m5C calibration sets; not a native site-discovery label. | synthetic | category | position |
| nanopore modification prediction | Model-derived modification probability/call for native RNA, distinct from benchmark truth. | prediction | probability | position |

## Access and reuse

- Access: open
- Formats: TAR (series archive); FAST5 (paper-described raw signals); XLSX (paper source data)
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE227087
- https://github.com/yulab2021/TandemMod

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Raw signal archive and benchmark split membership were not inspected.
- The same paper reuses other DRS/orthogonal datasets; they are not counted as newly generated observations here.

- Synthetic chemistry labels and orthogonal-assay labels have different evidential strength.
- Training/test division must control shared transcripts and signal batches; no validated leakage-free split is claimed.
- Modification calibration data do not measure therapeutic-mRNA expression or degradation.

## Cell specificity

evidence: none; notes: Calibration chemistry and rice context do not establish mammalian cell selectivity.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11094168/
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE227087&targ=self&form=text&view=full
- https://github.com/yulab2021/TandemMod

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11094168/; supports: Original paper distinguishes IVET labels, in-vivo validation, predictions and new data under GSE227087.
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE227087&targ=self&form=text&view=full; supports: Live metadata confirms title, eight samples and listed archives.
- url: https://github.com/yulab2021/TandemMod; supports: Author repository documents separate training/prediction modes and data-related assets; no model was executed.

Related models: not established. Related resources: nanobaselib; rmap-challenge.
