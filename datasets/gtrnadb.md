# GtRNAdb

Registry ID: `gtrnadb` · reference · **curated** · verification: **metadata**

Genome-based tRNA gene predictions and assembly-specific annotations; a reference for tRNA mapping, not a tissue-expression atlas.

## What the data contains

- Observation unit: Predicted tRNA gene locus
- RNA scope: tRNA
- Biological context: Genome assemblies across taxa; no sample-specific tissue or cell-state expression.
- Assays: tRNAscan-SE genomic prediction
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Release 22 (September 2024) displayed on homepage; no expression observations counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| gene copy count | Number of predicted tRNA loci per assembly; not RNA abundance | computed | loci | unknown |
| isotype / anticodon | Predicted tRNA gene identity annotation | annotation | category | interval |
| tRNAscan-SE confidence score | Computed confidence score for the predicted gene | computed | source score | interval |

## Access and reuse

- Access: open
- Formats: not established
- Source license: unknown
- Redistribution: not established

- Not established.

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No release download or gene table was inspected.

- Bind locus IDs to genome assembly and GtRNAdb release. Identical mature transcripts can arise from multiple loci.
- Gene copy count and tRAP activity predictions cannot replace measured mature tRNA abundance.

## Cell specificity

evidence: none; notes: Evidence applies only to the recorded biological contexts.

## Sources

- https://gtrnadb.ucsc.edu/
- https://doi.org/10.1093/nar/gkv1309

- url: https://gtrnadb.ucsc.edu/; supports: Data Release 22 (September 2024), genome-based predictions and tRNAscan-SE resource scope
- url: https://doi.org/10.1093/nar/gkv1309; supports: Genome-specific tRNA gene lists, isotype/anticodon annotations and scores; no tissue abundance endpoint

Related models: not established. Related resources: not established.
