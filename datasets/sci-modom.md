# Sci-ModoM

Registry ID: `sci-modom` · database · **curated** · verification: **file_sample**

Quantitative transcriptome-wide modification database retaining reported coverage and frequency in the standardized bedRMod representation.

## What the data contains

- Observation unit: A modification position within one assay/context dataset with coverage, score and frequency.
- RNA scope: mRNA; lncRNA
- Biological context: Multiple source studies; context must be retained per source record.
- Assays: whole-transcriptome base-resolution modification assays
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| coverage/score | Valid assay coverage reported for confidence assessment. | computed | read/call count | position |
| frequency | Reported modification frequency; preserve dataset technology and source definition. | computed | unknown | position |

## Access and reuse

- Access: open
- Formats: bedRMod; REST API metadata
- Source license: unknown
- Redistribution: not established

- https://scimodom.dieterichlab.org/
- https://dieterich-lab.github.io/scimodom/api.html
- https://scimodom.dieterichlab.org/api/v0/dataset/list_all
- https://scimodom.dieterichlab.org/api/v0/transfer/dataset/fhx8RaDLaBC3

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://scimodom.dieterichlab.org/api/v0/dataset/list_all; https://scimodom.dieterichlab.org/api/v0/transfer/dataset/fhx8RaDLaBC3.

- Source-code AGPL licensing was identified; it is not assumed to govern all contributed data.
- One HEK293T BID-seq pseudouridine dataset audited; no database-wide numerical validation
- Dataset title says three replicates, but exported file has one record per site without replicate columns
- Current docs describe newer /datasets routes that return404 on this deployed site; legacy routes discovered from its own public application work
- Cross-study cell identity does not establish matching culture, dose, time or intracellular RNA modification state
- Bounded file audit: evidence/file-audit-20261105/modification-trna/audit.json; selected coverage only.

- bedRMod coordinates are 0-based and half-open; conversions must be explicit.
- Retain technology, assembly/annotation and context metadata; reported frequency is assay-dependent.
- A missing row is unobserved under that dataset, not a proven unmodified base.
- MODOMICS imports a filtered subset, so the resources overlap.

## Cell specificity

evidence: direct_multi_context; notes: Dataset contexts are retained; cross-context measurements need comparable coverage and assay.

## Sources

- https://scimodom.dieterichlab.org/
- https://academic.oup.com/nar/article/53/D1/D310/7875981
- https://dieterich-lab.github.io/scimodom/bedrmod.html

- url: https://scimodom.dieterichlab.org/; supports: Primary page documents quantitative datasets and free browsing without login.
- url: https://academic.oup.com/nar/article/53/D1/D310/7875981; supports: Original paper describes source-linked data integration and scope.
- url: https://dieterich-lab.github.io/scimodom/bedrmod.html; supports: Schema documentation specifies headers, coverage/frequency and 0-based half-open coordinates.

## Selected-file audit

Can annotate endogenous sequence/site context or support modification-assay analyses. Not a direct label or measured modification state for delivered synthetic RNA.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/modification-trna/audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: modomics.
