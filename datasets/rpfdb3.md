# RPFdb v3

Registry ID: `rpfdb3` · database · **curated** · verification: **metadata**

Reprocessed Ribo-seq and matched RNA-seq resources, ORF annotations and pausing summaries.

## What the data contains

- Observation unit: Gene/ORF or position by biological sample
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: Ribo-seq; matched RNA-seq
- Accessions: not established
- Scale: value: 5018; unit: Ribo-seq samples advertised on v3 page; basis: Source-reported; not independent biological replicates or current global total; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ribosome occupancy | Ribosome-protected fragment signal | measured | unknown | transcript |
| translation efficiency | Source-defined comparison of ribosome occupancy and matched RNA abundance | computed | unknown | transcript |
| pause score | Processed tripeptide-motif pausing score; exact table schema remains unchecked | computed | unknown | unknown |

## Access and reuse

- Access: open
- Formats: tracks; tables
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://sysbio.gzzoc.com/rpfdb/index.html

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Matched RNA-seq exists for a subset, not every Ribo-seq sample.
- Preserve P-site/periodicity quality, source studies and TE definition; TE is not mean ribosome load.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://sysbio.gzzoc.com/rpfdb/index.html

- url: https://sysbio.gzzoc.com/rpfdb/index.html; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: not established.
