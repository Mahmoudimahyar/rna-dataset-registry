# EMBL-EBI Expression Atlas

Registry ID: `expression-atlas` · derived_resource · **curated** · verification: **metadata**

Baseline and differential expression studies with download indexes, processed counts and analysis results.

## What the data contains

- Observation unit: Gene by condition/sample or differential contrast
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| counts / baseline abundance | RNA-seq expression quantification | measured | unknown | transcript |
| log2 fold change / significance | Processed contrast-specific differential expression | computed | unknown | transcript |

## Access and reuse

- Access: open
- Formats: TSV; R object; ZIP
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.ebi.ac.uk/gxa/download.html

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Differential tables are not raw abundance matrices; preserve contrast definition.
- Absent rows in filtered downloads are not expression zeros.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.ebi.ac.uk/gxa/download.html

- url: https://www.ebi.ac.uk/gxa/download.html; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: geo.
