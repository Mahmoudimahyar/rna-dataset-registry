# YAMAT-seq breast-cell method study

Registry ID: `yamat-seq-srp096584` · study · **curated** · verification: **paper**

Dedicated mature-tRNA sequencing targeting terminal CCA-containing molecules.

## What the data contains

- Observation unit: tRNA entity by source sample or condition
- RNA scope: tRNA
- Biological context: Human MCF-7, SK-BR-3 and BT-20 breast-cancer cell lines; technical triplicates.
- Assays: YAMAT-seq
- Accessions: SRP096584
- Scale: value: 9; unit: technical libraries described in paper; basis: Three cell lines with technical triplicates, not nine independent biological samples; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| mature tRNA read abundance | Source counts/relative abundance after mature-CCA and length filters | computed | reads or source relative abundance | transcript |

## Access and reuse

- Access: open
- Formats: SRA raw reads; not downloaded
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/sra/?term=SRP096584

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- SRA run manifest and processed count tables were not inspected.

- Reference uses GRCh37 GtRNAdb nuclear tRNAs plus tRNAdb mitochondrial tRNAs; nonunique mapping permitted.
- Mature-end selection and RT bias can exclude fragments or heavily modified tRNAs; no charging label.

## Cell specificity

evidence: direct_multi_context; notes: Direct comparison among three cell lines; tissue or patient generalization is untested.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC5605243/
- https://www.ncbi.nlm.nih.gov/sra/?term=SRP096584

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5605243/; supports: Resource description and source-defined measurement or annotation scope
- url: https://www.ncbi.nlm.nih.gov/sra/?term=SRP096584; supports: Resource description and source-defined measurement or annotation scope

Related models: not established. Related resources: gtrnadb; trnadb.
