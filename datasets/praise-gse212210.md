# PRAISE: quantitative human pseudouridylation

Registry ID: `praise-gse212210` · study · **curated** · verification: **metadata**

Human RNA pseudouridine mapping and quantification using deletion signatures, with IVT and enzyme-perturbation controls.

## What the data contains

- Observation unit: A genomic/transcript position with treatment-dependent deletion evidence in a specific RNA fraction and condition.
- RNA scope: mRNA; ncRNA; tRNA; rRNA
- Biological context: HEK293T total/poly(A)+/small RNA; wild type, selected pseudouridine-synthase perturbations and IVT controls.
- Assays: PRAISE
- Accessions: GSE212210
- Scale: value: 38; unit: GEO samples (all subsets); basis: Counted live GEO Series_sample_id fields; not independent sites.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| pseudouridine site | Deletion-signature-based call after assay-specific filtering. | computed | unknown | position |
| quantitative pseudouridine level | Assay-derived pseudouridylation estimate; exact file column/scale requires data inspection. | computed | unknown | position |
| enzyme dependence | Modification difference associated with a particular synthase perturbation. | computed | unknown | position |

## Access and reuse

- Access: open
- Formats: TAR (supplementary archive); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212210

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- No archive members or numerical stoichiometry column was inspected.

- Untreated, IVT and perturbation controls serve different purposes; do not pool their labels.
- Endogenous noncalls may reflect coverage or filtering; IVT negatives are an experimentally defined control class.
- Nuclear and mitochondrial positions and RNA fractions must remain identifiable.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212210&targ=self&form=text&view=full
- https://www.nature.com/articles/s41589-023-01304-7

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE212210&targ=self&form=text&view=full; supports: Live series metadata describes HEK293T fractions, IVT negative control, enzyme perturbations and sample list.
- url: https://www.nature.com/articles/s41589-023-01304-7; supports: Original article defines quantitative pseudouridine profiling and confirms accession GSE212210.

Related models: not established. Related resources: pseudo-seq-gse58200; rbs-seq-gse90963.
