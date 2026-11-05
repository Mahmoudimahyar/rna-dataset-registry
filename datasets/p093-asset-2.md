# 3UTRBERT runnable example tables

Registry ID: `p093-asset-2` · model_release · **candidate** · verification: **unverified**

One tokenized sequence with a binary label Overlapping 3-mer tokens

## What the data contains

- Observation unit: One tokenized sequence with a binary label
- RNA scope: RNA; exact type varies by source
- Biological context: Example task identity requires resolving the full bundle/documentation.
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently recounted; see prior evidence note; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| label 0/1 | Binary task label in the example; precise assay/RBP meaning is not documented in the header alone. | unknown | unknown | unknown |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://github.com/yangyn533/3UTRBERT/tree/main/example/data

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Actual TSV header and sample inspected via bounded raw fetch after connector returned empty content for a large text object. A binary label is not automatically a cell-specific label.
- Imported candidate. Prior evidence level: file_inspected. Import is not a new file inspection or certification of labels.

- May group multiple datasets or overlap other model assets; do not count as an independent experimental dataset.

## Cell specificity

evidence: unknown; notes: Useful interface example, not sufficient alone to establish cell-specificity supervision.

## Sources

- https://github.com/yangyn533/3UTRBERT/tree/main/example/data
- https://github.com/yangyn533/3UTRBERT/blob/main/example/data/test.tsv
- https://github.com/yangyn533/3UTRBERT/blob/main/example/process_data_example.fa
- https://github.com/yangyn533/3UTRBERT/blob/main/functions/data_loaders.py

- url: https://github.com/yangyn533/3UTRBERT/tree/main/example/data; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/yangyn533/3UTRBERT/blob/main/example/data/test.tsv; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/yangyn533/3UTRBERT/blob/main/example/process_data_example.fa; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/yangyn533/3UTRBERT/blob/main/functions/data_loaders.py; supports: Previously recorded audit source; fresh dataset reconciliation pending

Related models: P093. Related resources: not established.
