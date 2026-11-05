# RMaP nanopore RNA-modification challenge

Registry ID: `rmap-challenge` · benchmark · **curated** · verification: **metadata**

Community benchmark of m5C, m6A and pseudouridine detection/frequency estimation using synthetic modified and canonical RNA signal mixtures.

## What the data contains

- Observation unit: A read-position chemistry label or per-reference-position modification target frequency within a challenge.
- RNA scope: synthetic RNA
- Biological context: Synthetic in-vitro reference data; pseudouridine challenge has a documented training/test division.
- Assays: nanopore direct RNA sequencing; synthetic modification-control benchmarking
- Accessions: PRJEB84053
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| source modification class | Chemistry-defined modified or canonical input class. | synthetic | category | position |
| target modification frequency | Reference mixture-based modified fraction used for benchmark scoring. | synthetic | fraction | position |
| reported modification frequency | Participant/model estimate assessed against source target frequencies. | prediction | fraction | position |

## Access and reuse

- Access: open
- Formats: FAST5; bedRMod (reported-result format)
- Source license: unknown
- Redistribution: not established

- https://www.ebi.ac.uk/ena/browser/view/PRJEB84053

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Challenge files, labels and exact train/test molecule membership were not opened.
- Paper describes original private submission infrastructure; public project access does not imply participant submissions are all public.

- Ground truth is synthetic source/mixture labeling, not an endogenous RNA chemical map.
- Reference-frequency accuracy and per-read classification are different endpoints.
- Shared templates and chemistry distributions constrain external generalization; no mammalian functional labels are measured.

## Cell specificity

evidence: none; notes: Synthetic assay benchmark without cell-selectivity measurements.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11993749/
- https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB84053

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11993749/; supports: Original challenge paper documents three chemistries, target frequencies, pseudouridine split and source accession.
- url: https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB84053; supports: Live ENA project title independently confirms RMaP challenge provenance.

Related models: not established. Related resources: tandemmod-ivet-gse227087; dorado-rna004-modification-benchmark.
