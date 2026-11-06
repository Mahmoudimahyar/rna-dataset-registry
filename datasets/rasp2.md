# RASP v2

Registry ID: `rasp2` · database · **curated** · verification: **file_sample**

Transcriptome-wide/targeted RNA probing and RNA-RNA interaction datasets; some tracks have imputed missing values.

## What the data contains

- Observation unit: Nucleotide reactivity or interaction pair under assay condition
- RNA scope: RNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: SHAPE; DMS; proximity ligation
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| reactivity | Chemical-probing signal under source normalization | measured | unknown | position |
| imputed reactivity | Model-filled missing signal; not measured ground truth | prediction | unknown | position |

## Access and reuse

- Access: open
- Formats: tracks; tables
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://rasp2.zhanglab.net/download/
- https://rasp2.zhanglab.net/api/query_bwfiles/?species=hg38
- https://rasp2.zhanglab.net/api/downloadfile/?filetype=bed&filelist=hg38%2FicSHAPE_CR_2021_Sun%2FHepG2.bed.gz

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://rasp2.zhanglab.net/api/query_bwfiles/?species=hg38; https://rasp2.zhanglab.net/api/downloadfile/?filetype=bed&filelist=hg38%2FicSHAPE_CR_2021_Sun%2FHepG2.bed.gz.

- Human API lists124 raw and54 imputed tracks; only one raw track inspected.
- Native genomic structure need not transfer to synthetic reporters; match assembly, condition and sequence.
- Bounded file audit: evidence/file-audit-20261105/auxiliary/audit.json; selected coverage only.

- Keep raw versus imputed track identity and probe.
- Probing conditions/in-vivo status affect interpretation; reactivity is not a binary pairing truth.

## Cell specificity

evidence: none; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://doi.org/10.1093/nar/gkae1117

- url: https://doi.org/10.1093/nar/gkae1117; supports: Resource identity, available label types and access route described in primary source documentation

## Selected-file audit

Measured structure features:7732882 six-column raw HepG2 icSHAPE BED rows in selected track.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/auxiliary/audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
