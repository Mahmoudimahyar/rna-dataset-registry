# Human Cell Atlas Data Portal

Registry ID: `human-cell-atlas` · database · **curated** · verification: **metadata**

Single-cell and other human atlas projects with project, donor, sample and matrix metadata.

## What the data contains

- Observation unit: Cell-by-gene measurement with project/sample context
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: scRNA-seq; multi-omics
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| gene expression counts | Assay-specific observed gene counts | measured | source read/UMI counts | cell |
| cell identity | Curated or inferred cell annotation with source-specific uncertainty | annotation | category | cell |

## Access and reuse

- Access: open
- Formats: matrix; H5AD; MTX; metadata manifest
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://data.humancellatlas.org/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Cell labels have source-specific uncertainty and ontology mappings.
- Expression identifies potential sensing inputs but does not validate a sensor response.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://data.humancellatlas.org/

- url: https://data.humancellatlas.org/; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: not established.
