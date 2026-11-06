# RNALocate

Registry ID: `rnalocate` · database · **curated** · verification: **file_sample**

RNA subcellular localization records with separately downloadable experimental and prediction data.

## What the data contains

- Observation unit: RNA-localization-context association
- RNA scope: mRNA; ncRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| localization | Compartment annotation; experimental and predicted entries must remain separate | annotation | unknown | transcript |

## Access and reuse

- Access: open
- Formats: tables; API
- Source license: Non-commercial use/distribution with citation; commercial users must contact source
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.rnalocate.org/download
- https://www.rnalocate.org/show_search?dataset=Symbol&Keyword=ACTB&category=mRNA&species=Homo+sapiens&subcellular_loc=All&page=1&score1=0.0&score2=1.0&sources=experiment&sortBy=None&last_id=&download=yes

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://www.rnalocate.org/show_search?dataset=Symbol&Keyword=ACTB&category=mRNA&species=Homo+sapiens&subcellular_loc=All&page=1&score1=0.0&score2=1.0&sources=experiment&sortBy=None&last_id=&download=yes.

- Bulk mRNA and circRNA ZIP links returned404; selected query CSV works.
- Localization does not establish translation rate; RNALocate noncommercial terms apply.
- Bounded file audit: evidence/file-audit-20261105/auxiliary/audit.json; selected coverage only.

- Subcellular localization is not cell-type specificity.
- Experimental records and model predictions are separate downloads.

## Cell specificity

evidence: none; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.rnalocate.org/download

- url: https://www.rnalocate.org/download; supports: Resource identity, available label types and access route described in primary source documentation

## Selected-file audit

Localization annotation with computed confidence;55ACTB mRNA query-export rows.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/auxiliary/audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
