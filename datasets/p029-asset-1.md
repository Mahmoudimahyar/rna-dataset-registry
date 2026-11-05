# PARADE natural UTR MPRA / Library 1

Registry ID: `p029-asset-1` · model_release · **candidate** · verification: **unverified**

One UTR × cell line × replicate/fold seq; cell_type; 50-nt 5′UTR or 240-nt 3′UTR

## What the data contains

- Observation unit: One UTR × cell line × replicate/fold
- RNA scope: RNA; exact type varies by source
- Biological context: Matched UTRs across MDA-MB-231 c1, HepG2 c2, Jurkat c4, SW480 c6, PA-1 c13 and NALM6 c17.
- Assays: not established
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently recounted; see prior evidence note; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Sorting-bin counts; mass_center; diff | Relative reporter activity estimated from four expression bins; diff is a cell-specific deviation from the across-cell mean. These are not absolute protein concentrations. | unknown | unknown | unknown |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://github.com/autosome-ru/parade

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Schemas and preprocessing inspected, not the complete measurement table. Training notebooks reference CSVs absent from current tree. README mentions an associated Zenodo archive without its link; issue 2 asks for it and had no comments at inspection.
- Imported candidate. Prior evidence level: schema_inspected. Import is not a new file inspection or certification of labels.

- May group multiple datasets or overlap other model assets; do not count as an independent experimental dataset.

## Cell specificity

evidence: unknown; notes: Excellent biological design for expression specificity, but release/access must be resolved before supervised training.

## Sources

- https://github.com/autosome-ru/parade
- https://github.com/autosome-ru/parade/blob/master/predictor/regression_multiple/preprocess_utr3.ipynb
- https://github.com/autosome-ru/parade/blob/master/predictor/model/utrdata_cl.py
- https://github.com/autosome-ru/parade/blob/master/tutorials/predict_utr3.ipynb
- https://github.com/autosome-ru/parade/issues/2

- url: https://github.com/autosome-ru/parade; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/autosome-ru/parade/blob/master/predictor/regression_multiple/preprocess_utr3.ipynb; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/autosome-ru/parade/blob/master/predictor/model/utrdata_cl.py; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/autosome-ru/parade/blob/master/tutorials/predict_utr3.ipynb; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/autosome-ru/parade/issues/2; supports: Previously recorded audit source; fresh dataset reconciliation pending

Related models: P029. Related resources: not established.
