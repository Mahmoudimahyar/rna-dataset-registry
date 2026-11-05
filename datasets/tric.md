# tRic: tRNA in Cancer

Registry ID: `tric` · derived_resource · **curated** · verification: **paper**

Relative tRNA-expression estimates computed from TCGA miRNA sequencing across cancer types.

## What the data contains

- Observation unit: tRNA estimate by TCGA sample
- RNA scope: tRNA
- Biological context: Human TCGA tumors and comparison tissues across 31 cancer types.
- Assays: reanalysis of TCGA miRNA-seq
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: 31 cancer types reported; portal matrix dimensions not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| relative tRNA expression | Mapped-read estimate aggregated at gene, codon and amino-acid levels; not dedicated mature-tRNA quantification | computed | source normalized relative expression | transcript |
| clinical association | Source statistical associations with clinical annotations | computed | unknown | sample |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://hanlaboratory.com/tRic/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Portal landing page rendered limited content; downloadable matrices, normalization columns and current availability were not inspected.

- Conventional miRNA libraries can mix fragments and incomplete mature-tRNA coverage; retain estimation provenance.
- TCGA measurements overlap other TCGA-derived resources including DBtRend.

## Cell specificity

evidence: direct_multi_context; notes: Multi-cancer context associations from indirect estimates; not validated cell-resolved mature tRNA abundance.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC7567503/
- https://hanlaboratory.com/tRic/

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7567503/; supports: Relative tRNA estimates from TCGA miRNA-seq across 31 cancer types, with gene/codon/amino-acid aggregation

Related models: not established. Related resources: dbtrend; gtrnadb.
