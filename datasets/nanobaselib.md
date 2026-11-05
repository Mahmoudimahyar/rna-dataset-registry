# NanoBaseLib

Registry ID: `nanobaselib` · benchmark · **curated** · verification: **metadata**

Unified reprocessing and benchmark collection for nanopore tasks, including RNA-modification detection alongside DNA and non-modification tasks.

## What the data contains

- Observation unit: A raw/read-level signal, aligned event, or site label depending on benchmark task.
- RNA scope: mRNA; synthetic RNA; other RNA
- Biological context: Mixture of source studies and species, synthetic controls and native RNA; isolate the relevant RNA task/subset.
- Assays: nanopore sequencing; source orthogonal assays for benchmark labels
- Accessions: 10.5281/zenodo.10889896
- Scale: value: 16; unit: integrated source datasets (all DNA/RNA tasks); basis: Author homepage reports 16 input datasets; not independently file-counted or restricted to RNA-modification tasks.; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RNA modification benchmark label | Source-defined reference label from synthetic chemistry or orthogonal assays; provenance varies by subset. | annotation | category | position |
| per-site modification probability | Algorithm output; distinct from reference benchmark labels. | prediction | probability | position |

## Access and reuse

- Access: open
- Formats: TAR.GZ archives; FAST5 and processed intermediate files (documented)
- Source license: CC BY 4.0 for processed dataset (author-stated); source data terms remain source-specific
- Redistribution: Processed dataset reuse is author-licensed under CC BY 4.0; upstream raw-source rights require separate checking.

- https://zenodo.org/records/10889896
- https://nanobaselib.github.io/

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- No source or processed archive opened; task-specific file schema, completeness and split integrity are not established.
- Zenodo page did not expose a readable license value in browser extraction; CC BY 4.0 wording is supported by the current author site.

- Source datasets overlap separate study records; neither read counts nor dataset counts can be added across them.
- DNA, poly(A) and basecalling observations are not RNA modification labels.
- Absent source modification calls are not automatically true negatives; retain each subset's control definition.
- Benchmark performance from a fixed preprocessing/basecaller release does not transfer automatically to new chemistry.

## Cell specificity

evidence: none; notes: A heterogeneous sequencing benchmark is not a cell-specific functional assay.

## Sources

- https://nanobaselib.github.io/
- https://zenodo.org/records/10889896
- https://papers.nips.cc/paper_files/paper/2024/file/8bce223b376f52fb86a148097eebb10d-Supplemental-Datasets_and_Benchmarks_Track.pdf

- url: https://nanobaselib.github.io/; supports: Current author page describes tasks, mixed DNA/RNA scope and separate dataset/code licenses.
- url: https://zenodo.org/records/10889896; supports: Zenodo metadata establishes versioned dataset identity and available archive names without downloading them.
- url: https://papers.nips.cc/paper_files/paper/2024/file/8bce223b376f52fb86a148097eebb10d-Supplemental-Datasets_and_Benchmarks_Track.pdf; supports: Author checklist states processed dataset CC BY licensing and repository/benchmark documentation.

Related models: not established. Related resources: tandemmod-ivet-gse227087.
