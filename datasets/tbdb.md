# T-box Riboswitch Annotation Database (TBDB)

Registry ID: `tbdb` · database · **curated** · verification: **paper**

Structurally annotated T-box riboswitch:tRNA pairs with predicted binding partners and downstream targets.

## What the data contains

- Observation unit: T-box entry with assigned tRNA partner
- RNA scope: T-box riboswitch; tRNA
- Biological context: Bacterial species, predominantly gram-positive organisms.
- Assays: comparative annotation; secondary-structure prediction
- Accessions: not established
- Scale: value: 23535; unit: entries reported in paper; basis: Published 2020 snapshot, not recounted live; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| specifier; cognate tRNA; target gene | Predicted binding specificity and target | prediction | categorical | unknown |

## Access and reuse

- Access: open
- Formats: CSV
- Source license: unknown
- Redistribution: not established

- https://tbdb.io/download/tbdb.csv

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- CSV URL declared by paper but not fetched.
- Predicted pairing is not a measured affinity or response label; data license unestablished.

- Split homologous families and organisms.
- Assigned partners are not uniformly experimental positives.

## Cell specificity

evidence: none; notes: Natural prokaryotic annotation.

## Sources

- https://doi.org/10.1093/nar/gkaa721
- https://tbdb.io
- https://github.com/mpiersonsmela/tbox/

- url: https://doi.org/10.1093/nar/gkaa721; supports: Primary source supports resource or study identity and the described context.
- url: https://tbdb.io; supports: Primary source supports resource or study identity and the described context.
- url: https://github.com/mpiersonsmela/tbox/; supports: Primary source supports resource or study identity and the described context.

Related models: not established. Related resources: ribocentre-switch; rfam-riboswitch-families.
