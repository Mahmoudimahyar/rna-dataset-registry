# PARADE generated UTR validation / Library 2

Registry ID: `parade-generated-utr-mpra` · study · **curated** · verification: **schema**

Measured generated/control UTR validation across the same panel; distinct from predictions.

## What the data contains

- Observation unit: Generated/control fragment by cell line
- RNA scope: mRNA
- Biological context: Human MDA-MB-231, HepG2, Jurkat, SW480, PA-1 and NALM6; matched UTR panels across six contexts.
- Assays: four-bin fluorescence MPRA
- Accessions: not established
- Scale: value: 15849; unit: UTRs passing reported QC; basis: Derived sum of preprint counts 10174 (5-prime) and 5675 (3-prime); not recounted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| 1; 2; 3; 4 | Source four-bin reporter counts | measured | counts | construct |
| mass_center | Count-weighted reporter-bin center from code | computed | source bin scale | construct |
| diff | Cell-context mass_center minus sequence mean across contexts | computed | source bin-scale difference | construct |

## Access and reuse

- Access: unavailable
- Formats: CSV schema referenced in notebooks
- Source license: Code MIT; preprint CC BY-NC-ND 4.0; measurement-data license unknown
- Redistribution: not established

- Not established.

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: https://github.com/autosome-ru/parade/blob/master/predictor/library2/preprocess_deltas_utr3.ipynb.

- Complete validation measurement CSV not found.
- Code removes c15; use final panel/processing when interpreting contexts.
- Preprint rounds total to 15800; precise QC sum differs.

- Cell-line specificity is distinct from delivery tropism.
- Group identical UTRs, parent fragments and replicates in splits.
- Reporter context and 5-prime/3-prime task identity must remain visible.
- Retain generated families and reused controls to prevent parent/control leakage.

## Cell specificity

evidence: direct_multi_context; notes: Measured matched panel; complete-table access unresolved.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11722239/
- https://github.com/autosome-ru/parade/tree/master/predictor/library2

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11722239/; supports: Separate validation library and reported QC counts.
- url: https://github.com/autosome-ru/parade/blob/master/predictor/library2/preprocess_deltas_utr3.ipynb; supports: Library-specific counts and activity/contrast processing.
- url: https://github.com/autosome-ru/parade/issues/2; supports: Unresolved measurement-archive link.

Related models: P029. Related resources: parade-natural-utr-mpra; parade-stability-assay.
