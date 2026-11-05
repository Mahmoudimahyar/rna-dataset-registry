# m6A2Target

Registry ID: `m6a2target` · database · **curated** · verification: **paper**

Targets of m6A writers, erasers and readers, separated into low-throughput validated targets and high-throughput potential targets.

## What the data contains

- Observation unit: A regulator-to-target-gene association supported by a stated experiment.
- RNA scope: mRNA
- Biological context: Multiple source studies; context must be retained per source record.
- Assays: low-throughput validation curation; high-throughput regulator-target studies
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| validated target | Writer, eraser or reader target curated from low-throughput evidence. | annotation | association | transcript |
| potential target | Regulator-associated target inferred from high-throughput studies; not equivalent to a proven direct target. | computed | association | transcript |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- http://m6a2target.canceromics.org/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Current resource endpoint timed out; public availability is described by the paper, but current download access and formats are unknown.
- Organism coverage and exact source-table schema were not established in this inspection.

- Regulator perturbation or binding evidence is not a measured modification site or proof of a causal modification effect.
- Keep validated and potential target labels separate.
- RM2Target is an expanded related resource, not an independent source of all associations.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://pubmed.ncbi.nlm.nih.gov/32392583/
- https://doi.org/10.1093/bib/bbaa055

- url: https://pubmed.ncbi.nlm.nih.gov/32392583/; supports: Original paper explicitly defines validated versus potential target modules and gives the resource endpoint.
- url: https://doi.org/10.1093/bib/bbaa055; supports: Original publication identity and target-association scope.

Related models: not established. Related resources: rm2target.
