# ADAPT Cas13a guide-target diagnostic activity

Registry ID: `adapt-cas13-activity` · study · **curated** · verification: **file_sample**

Measured diagnostic activity with curated, resampled-replicate and median data versions; upstream SANDSTORM benchmark.

## What the data contains

- Observation unit: Guide-target pair with replicate readings
- RNA scope: target RNA; guide RNA
- Biological context: Cell-free cleavage assay; not intracellular translation or delivery.
- Assays: Cas13a collateral-cleavage kinetics
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| out_logk_measurements | Source-transformed replicate kinetic activity measurements | measured | source log(k) scale | construct |
| out_logk_median; out_logk_stdev | Source replicate summary statistics | computed | source log(k) scale | construct |
| type | Experimental/control category | annotation | categorical | construct |

## Access and reuse

- Access: open
- Formats: TSV; TSV.gz
- Source license: MIT repository license; reused external data retain their terms
- Redistribution: MIT observed at repository level; external-source conditions still apply

- https://github.com/broadinstitute/adapt-seq-design/tree/main/data/CCF-curated

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://raw.githubusercontent.com/broadinstitute/adapt-seq-design/main/data/CCF-curated/CCF_merged_pairs_annotated.curated.tsv (header only); https://github.com/broadinstitute/adapt-seq-design/blob/main/data/README.md.

- Exact log base/normalization not established.
- No sequence strings or individual values retained.

- All resampled replicates and related targets belong in one split.
- Separate controls/predictions from measured experimental rows.
- Predicted assay designs are not independent wet-lab observations.

## Cell specificity

evidence: none; notes: Diagnostic activity is not cell-selective expression.

## Sources

- https://github.com/broadinstitute/adapt-seq-design
- https://www.nature.com/articles/s41587-022-01213-5

- url: https://raw.githubusercontent.com/broadinstitute/adapt-seq-design/main/data/CCF-curated/CCF_merged_pairs_annotated.curated.tsv; supports: Kinetic fields, replicate counts and pair/context header.
- url: https://github.com/broadinstitute/adapt-seq-design/blob/main/data/README.md; supports: Full/resampled variants; Cas9 playground not used in paper.

Related models: P012. Related resources: gardn-sandstorm-release.
