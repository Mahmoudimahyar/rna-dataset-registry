# UTR-Seq zebrafish reporter timecourses

Registry ID: `utr-seq-zebrafish` · study · **curated** · verification: **schema**

Reporter UTR timecourse analysis; public repository includes an example rather than proof of the entire experimental release.

## What the data contains

- Observation unit: Reporter UTR by timepoint
- RNA scope: mRNA
- Biological context: Zebrafish embryogenesis; source-specific A+/A- conditions
- Assays: UTR reporter timecourse
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| AR01..AR11 | Timecourse abundance columns; time mapping comes from source documentation | measured | counts | transcript |
| decay parameters | Fitted reporter degradation properties | computed | unknown | transcript |

## Access and reuse

- Access: open
- Formats: TXT; Matlab
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://github.com/rabanilab/UTR-Seq

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Example data is not the entire experiment.
- Timepoint labels must be mapped from README; abundance counts are not already half-life.

## Cell specificity

evidence: none; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://github.com/rabanilab/UTR-Seq

- url: https://github.com/rabanilab/UTR-Seq; supports: Resource identity, available label types and access route described in primary source documentation

Related models: P022. Related resources: not established.
