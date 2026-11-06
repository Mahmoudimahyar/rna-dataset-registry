# T-psi-C tRNA sequencing study index

Registry ID: `t-psi-c-sequencing-index` · reference · **curated** · verification: **metadata**

Method/source index; linked charging experiments audited separately.

## What the data contains

- Observation unit: Source-specific record
- RNA scope: tRNA
- Biological context: See selected-file audit; not matched to reporter assay conditions.
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Selected inspection scope is recorded separately; no database-wide recount; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Study/method/accession | Reference discovery metadata | annotation | category | sample |

## Access and reuse

- Access: open
- Formats: not established
- Source license: unknown
- Redistribution: not established; metadata only redistributed

- https://tpsic.igcz.poznan.pl/trna-sequencing/all/
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE239nnn/GSE239867/suppl/GSE239867_RAW.tar
- https://ftp.ncbi.nlm.nih.gov/geo/series/GSE188nnn/GSE188855/suppl/GSE188855_RAW.tar

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: not established.

- GSE239867 covers mouse MEFs and human NTERT keratinocytes under stress; unlabeled colon-separated count columns require mapping before calculation
- GSE188855 has12 samples and67 tRNA IDs per file, with Ratio equal to100*CCA/(CCA+CC) within rounding
- GSE188855 sample GSM5691036 title is Lung_starvation_rep1 but treatment metadata says untreated; preserve the conflict and resolve against study design before assigning labels
- The GSE188855 study is a separately investigated charging experiment; current T-psi-C index explicitly links GSE239867
- No circRNA/mRNA protein-output labels in these tRNA processed files
- Bounded file audit: evidence/file-audit-20261105/modification-trna/audit.json; selected coverage only.

- Not established.

## Cell specificity

evidence: none; notes: Not a matched synthetic RNA protein-output experiment

## Sources

- https://tpsic.igcz.poznan.pl/trna-sequencing/all/

- url: https://tpsic.igcz.poznan.pl/trna-sequencing/all/; supports: Primary resource documentation and file routes

## Selected-file audit

Useful study discovery. Downloaded charging studies support their own stress/cell-state analyses; neither is a matched cell-context covariate matrix for the circRNA reporter panels.

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/modification-trna/audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: not established.
