# Sample 2019 designed 5′UTR library (reused by SANDSTORM and GARDN)

Registry ID: `p012-asset-1` · model_release · **candidate** · verification: **unverified**

One 5′UTR reporter sequence 50-nt 5′UTR; one-hot sequence plus a sequence-derived possible-base-pair compatibility array (prototype_ppms_fast/contact_map).

## What the data contains

- Observation unit: One 5′UTR reporter sequence
- RNA scope: RNA; exact type varies by source
- Biological context: Human reporter translation; original Sample experiment context, not a multi-cell panel.
- Assays: not established
- Accessions: GSM3130443
- Scale: value: unknown; unit: unknown; basis: Not independently recounted; see prior evidence note; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| rl | Polysome-derived mean ribosome load; standardized in the SANDSTORM notebook before fitting. | unknown | unknown | unknown |

## Access and reuse

- Access: unknown
- Formats: not established
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3130443

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Upstream data must be supplied separately. The structural array encodes possible base-pair interactions from sequence; it is not experimentally measured structure or necessarily a thermodynamic pairing-probability matrix. Same Sample data, not an independent new functional dataset.
- Imported candidate. Prior evidence level: schema_inspected. Import is not a new file inspection or certification of labels.

- May group multiple datasets or overlap other model assets; do not count as an independent experimental dataset.
- Both imported entries reference GSM3130443; they share an upstream source, not independent experimental replication.

## Cell specificity

evidence: unknown; notes: Suitable for testing sequence/structure predictors; lacks matched multi-cell labels needed for cell selectivity.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3130443
- https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/UTR_data/expected_data.txt
- https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/SANDSTORM/UTR_Predictor.ipynb

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM3130443; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/data/UTR_data/expected_data.txt; supports: Previously recorded audit source; fresh dataset reconciliation pending
- url: https://github.com/AlexGreenLab/GARDN-SANDSTORM/blob/main/SANDSTORM/UTR_Predictor.ipynb; supports: Previously recorded audit source; fresh dataset reconciliation pending

Related models: P012. Related resources: sample2019-chemistry-reporters; p002-asset-2.
