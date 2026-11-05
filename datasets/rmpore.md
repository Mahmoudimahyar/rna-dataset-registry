# RMPore

Registry ID: `rmpore` · database · **curated** · verification: **paper**

Recent multi-tool nanopore modification database with genomic/transcript annotations, confidence strata and supporting-tool/sample counts.

## What the data contains

- Observation unit: A tool-derived modification call and its evidence at genomic or transcript position; some analyses retain molecule-level information.
- RNA scope: mRNA; other RNA
- Biological context: Multiple source studies; context must be retained per source record.
- Assays: nanopore direct RNA sequencing; multi-tool computational integration
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| modification call | Tool-derived putative modification identity/position. | prediction | unknown | position |
| evidence level | Source confidence stratum based on independent annotation/controls and supporting data. | annotation | category | position |
| modification stoichiometry | Caller-derived abundance of modified reads, not a uniformly validated chemical fraction. | computed | unknown | position |

## Access and reuse

- Access: open
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://rmpore.renlab.cn/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Interactive table/export schema and data files were not inspected; no exact current site count asserted.

- Multi-tool agreement is not independent chemical validation.
- Calls are dependent on sequencing chemistry, basecaller and modification-caller versions.
- Molecule-level predictions and pooled per-site frequencies are separate units; missing calls are not unmodified negatives.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://academic.oup.com/nar/article/54/D1/D291/8315799
- https://rmpore.renlab.cn/

- url: https://academic.oup.com/nar/article/54/D1/D291/8315799; supports: Original paper documents multi-species DRS integration, tool-specific thresholds and confidence classes.
- url: https://rmpore.renlab.cn/; supports: Current endpoint responded without readable static table content.

Related models: not established. Related resources: directrmdb; modomics.
