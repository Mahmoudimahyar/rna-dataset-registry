# RBS-Seq simultaneous modification profiling

Registry ID: `rbs-seq-gse90963` · study · **curated** · verification: **metadata**

Bisulfite-based transcriptome profiling of m5C, pseudouridine and m1A with modification-specific mismatch/deletion signatures.

## What the data contains

- Observation unit: A candidate modified position with a chemistry-specific sequencing signature and source RNA fraction.
- RNA scope: mRNA; ncRNA; tRNA; rRNA
- Biological context: HeLa total/ribodepleted, small and poly(A) RNA; DKC1 knockdown and control subsets; validation includes HEK293.
- Assays: RBS-Seq
- Accessions: GSE90963
- Scale: value: 14; unit: GEO samples; basis: Counted live GEO Series_sample_id fields.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| m5C candidate site | Assay-specific candidate m5C call from bisulfite signatures. | computed | unknown | position |
| m1A candidate site | Assay-specific candidate m1A call; not a confirmed widespread mRNA label. | computed | unknown | position |
| pseudouridine candidate site | Candidate Ψ call supported by characteristic deletions. | computed | unknown | position |

## Access and reuse

- Access: open
- Formats: XLSX (candidate and validation tables); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90963

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.

- This accession is not an Nm-seq dataset.
- Candidate tables contain assay calls, not universally verified positive sites.
- Absence or failure to reproduce a call is not proof of an unmodified nucleotide in every context.
- Preserve separate chemistries, RNA fractions and orthogonal validation status.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90963&targ=self&form=text&view=full
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90963

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90963&targ=self&form=text&view=full; supports: Live GEO metadata identifies simultaneous m5C/Ψ/m1A RBS-Seq, HeLa design, sample count and named candidate XLSX files.
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90963; supports: Primary series reports substantial disagreement with earlier m5C/m1A maps, including little substantial m1A in mRNA.

Related models: not established. Related resources: m5c-atlas; pseudo-seq-gse58200; m1a-safra-gse97419.
