# DARNED (original human reference release)

Registry ID: `darned-editing` · database · **curated** · verification: **paper**

Historical literature-integrated editing-location database with genomic, transcript-region and tissue-source annotations.

## What the data contains

- Observation unit: An editing-location annotation mapped to a reference genome with source information.
- RNA scope: mRNA; other RNA
- Biological context: Multiple source studies; context must be retained per source record.
- Assays: literature and transcript-sequence evidence integration
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| editing-location annotation | Published RNA-editing instance, mainly A-to-I in the original release. | annotation | unknown | position |
| source tissue | Tissue/cell source of supporting sequences rather than a quantitative specificity measurement. | annotation | category | sample |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- http://darned.ucc.ie

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- This record is scoped to the inspected 2010 paper, not an assertion about current site content or later organism additions.
- Current legacy delivery and export format not verified.

- Retain genome build and supporting-source provenance.
- Tissue source does not establish exclusive editing in that tissue.
- Unlisted positions are unobserved, not validated unedited negatives.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://academic.oup.com/bioinformatics/article/26/14/1772/178844

- url: https://academic.oup.com/bioinformatics/article/26/14/1772/178844; supports: Original paper defines the human resource, genomic mapping and tissue/region query fields.

Related models: not established. Related resources: rediportal; radar-editing.
