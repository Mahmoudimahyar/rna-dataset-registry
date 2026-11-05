# Pseudo-seq: regulated pseudouridylation (Carlile et al., 2014)

Registry ID: `pseudo-seq-gse58200` · study · **curated** · verification: **metadata**

Early endogenous pseudouridine mapping in yeast and human cells using treatment-dependent reverse-transcription stops.

## What the data contains

- Observation unit: A treatment-dependent RT-stop signature at an RNA position in a source sample/condition.
- RNA scope: mRNA; other RNA
- Biological context: Yeast and HeLa cells; treatments, enzyme perturbations and technical subsets must be read per sample.
- Assays: Pseudo-seq; RNA-seq
- Accessions: GSE58200
- Scale: value: 109; unit: GEO samples (all subsets); basis: Counted Series_sample_id fields in live GEO series metadata; not a site count.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| pseudouridine site call | Modification inferred from treatment-dependent RT-stop enrichment. | computed | unknown | position |
| RPKM | Transcript-normalized RNA abundance in supplied companion tables; separate from modification evidence. | computed | RPKM | transcript |

## Access and reuse

- Access: open
- Formats: TXT.GZ (RPKM tables); TAR (supplementary archive); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE58200

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Main GEO HTML triggered a browser challenge; the public SOFT metadata endpoint succeeded.
- Archive members and quantitative site-call schema were not inspected.

- RT-stop enrichment is a modification-detection signature, not a direct absolute pseudouridine fraction.
- No RT-stop call is not a confirmed unmodified uridine.
- The site annotations are endogenous; do not merge as synthetic Ψ-mRNA reporter performance.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE58200&targ=self&form=text&view=full
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE58200

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE58200&targ=self&form=text&view=full; supports: Live SOFT metadata establishes title, Pseudo-seq scope, organisms, design, sample count and listed supplementary files.
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE58200; supports: Primary accession identifies endogenous yeast/HeLa pseudouridine mapping and treatment-dependent RT-stop logic.

Related models: not established. Related resources: praise-gse212210; rbs-seq-gse90963.
