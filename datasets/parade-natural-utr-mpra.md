# PARADE natural UTR MPRA / Library 1

Registry ID: `parade-natural-utr-mpra` · study · **curated** · verification: **schema**

Matched multi-cell reporter data underlying PARADE. Public code defines labels; complete measurement release remains unresolved.

## What the data contains

- Observation unit: UTR fragment by cell line and replicate/fold
- RNA scope: mRNA
- Biological context: Human MDA-MB-231, HepG2, Jurkat, SW480, PA-1 and NALM6; matched UTR panels across six contexts.
- Assays: four-bin fluorescence MPRA
- Accessions: not established
- Scale: value: 60000; unit: natural UTR fragments assayed; basis: Preprint total, not independently counted quality-filtered rows; as_of: 2026-11-04

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

Checked: 2026-11-04. Actual files/headers inspected: https://github.com/autosome-ru/parade/blob/master/predictor/regression_multiple/preprocess_utr3.ipynb.

- Complete natural-library measurement CSV not found in current tree.
- GEO deposition declared without accession; Zenodo named without a link.
- Unavailability refers to the located complete table, not proof no release exists elsewhere.

- Cell-line specificity is distinct from delivery tropism.
- Group identical UTRs, parent fragments and replicates in splits.
- Reporter context and 5-prime/3-prime task identity must remain visible.

## Cell specificity

evidence: direct_multi_context; notes: Direct matched assay design, with unresolved training-table access.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11722239/
- https://github.com/autosome-ru/parade

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11722239/; supports: Natural library, matched cell panel, preprint status.
- url: https://github.com/autosome-ru/parade/blob/master/predictor/regression_multiple/preprocess_utr3.ipynb; supports: Bin-count, mass_center and diff definitions.
- url: https://github.com/autosome-ru/parade/blob/master/README.md; supports: Associated Zenodo data named without URL.
- url: https://github.com/autosome-ru/parade/issues/2; supports: Archive-link issue is open with zero comments at inspection.

Related models: P029. Related resources: parade-generated-utr-mpra; parade-stability-assay.
