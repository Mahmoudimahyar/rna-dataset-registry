# RMVar 2.0

Registry ID: `rmvar-v2` · database · **curated** · verification: **paper**

Multi-modification variant resource with four source-evidence levels, including allele-specific MeRIP analysis and sequence-derived predictions.

## What the data contains

- Observation unit: A variant-to-possible-modification-effect annotation with an explicit evidence level.
- RNA scope: mRNA; other RNA
- Biological context: Human and mouse variants mapped to modification-associated annotations; disease links are separate annotations.
- Assays: single-base modification-source integration; allele-specific MeRIP-seq analysis; motif analysis; sequence-based prediction
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RM gain/loss-associated variant | Potential change inferred by overlap, motif analysis, allele-specific enrichment or prediction. | prediction | category | position |
| evidence level | Four source strata from single-base support through transcriptome-wide sequence prediction. | annotation | category | position |

## Access and reuse

- Access: open
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://rmvar.renlab.cn/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Interactive database table schema and downloadable data were not inspected.

- Source confidence is not direct causal evidence for each variant.
- Disease annotation or GWAS linkage is not an experimentally measured modification effect.
- Retain evidence levels; predicted effects cannot be pooled as observed modification labels.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://doi.org/10.1093/nar/gkae924
- https://rmvar.renlab.cn/

- url: https://doi.org/10.1093/nar/gkae924; supports: Original 2.0 paper defines four evidence levels and derivation of potential modification gain/loss variants.
- url: https://rmvar.renlab.cn/; supports: Endpoint responds but returned no readable static content in this inspection.

Related models: not established. Related resources: m6avar.
