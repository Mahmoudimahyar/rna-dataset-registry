# ENCORI / starBase

Registry ID: `encori` · database · **curated** · verification: **metadata**

RNA-RNA, miRNA-target and RBP-RNA interaction resources with query/download APIs.

## What the data contains

- Observation unit: Interaction pair with support/assembly metadata
- RNA scope: mRNA; ncRNA; miRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: CLIP; RNA interaction assays
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| CLIP support / interaction evidence | Evidence-supported interaction annotation; keep prediction and experimental support distinct | annotation | unknown | interval |

## Access and reuse

- Access: open
- Formats: API tables; TSV
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://www.rnasysu.com/encori/tutorialAPI.php

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Metadata/schema review is not inspection of every underlying dataset file.

- Filter by assembly and evidence type; correlation or predicted targeting is not causal repression.
- ENCORI and starBase are aliases rather than independent datasets.

## Cell specificity

evidence: none; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://www.rnasysu.com/encori/tutorialAPI.php

- url: https://www.rnasysu.com/encori/tutorialAPI.php; supports: Resource identity, available label types and access route described in primary source documentation

Related models: not established. Related resources: not established.
