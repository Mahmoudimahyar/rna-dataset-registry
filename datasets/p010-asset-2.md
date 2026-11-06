# RiboNN original human endogenous mRNA TE atlas

Registry ID: `p010-asset-2` · derived_resource · **curated** · verification: **file_sample**

Original publisher Human supplement with transcript identities/sequences, cross-validation folds and78 context-specific TE estimates.

## What the data contains

- Observation unit: One gene/transcript row with repeated context-specific TE estimates
- RNA scope: RNA; exact type varies by source
- Biological context: Original Human transcript table with78context columns spanning source cell lines, primary populations and tissues; stock/species/condition metadata must be reconciled, including the TE_Vero_6 label.
- Assays: Matched Ribo-seq and RNA-seq; study-derived TE residuals
- Accessions: not established
- Scale: value: 10348; unit: gene/transcript rows in original Human sheet; basis: All rows parsed; 716913 numeric TE values across78 columns. Not that many independent sequences.; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| TE_* | Endogenous TE defined by the original paper as residuals from compositional linear regression of centered-log-ratio CDS RPF/RNA counts, then averaged within cell context. Not raw Ribo/RNA ratios, completed protein output, or synthetic reporter labels. | computed | source compositional-regression residual | transcript |
| fold | Original gene-level cross-validation fold | annotation | fold | transcript |

## Access and reuse

- Access: open
- Formats: XLSX
- Source license: Original paper states processed supplements available without restriction; preserve publisher/source terms
- Redistribution: Source remains with publisher; metadata only here

- https://static-content.springer.com/esm/art%3A10.1038%2Fs41587-025-02712-x/MediaObjects/41587_2025_2712_MOESM3_ESM.xlsx

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://static-content.springer.com/esm/art%3A10.1038%2Fs41587-025-02712-x/MediaObjects/41587_2025_2712_MOESM3_ESM.xlsx.

- GitHub example training table is explicitly fake TE in README; not used as biological labels.
- ContiTE reuses the RiboNN atlas; it is not an independent experimental dataset.
- ContiTE article states different counts from this inspected original Human supplement; reconcile exact input versions before reproducing or comparing.
- Publisher Supplementary Tables3/4 contain predicted TEs and must not be treated as measured labels.
- Same gene across contexts is a repeated observation, not a new independent sequence.
- No uniformly matched external HPA/DepMap assay condition established.

- May group multiple datasets or overlap other model assets; do not count as an independent experimental dataset.
- GitHub example training table is explicitly fake TE in README; not used as biological labels.
- ContiTE reuses the RiboNN atlas; it is not an independent experimental dataset.
- ContiTE article states different counts from this inspected original Human supplement; reconcile exact input versions before reproducing or comparing.
- Publisher Supplementary Tables3/4 contain predicted TEs and must not be treated as measured labels.
- Same gene across contexts is a repeated observation, not a new independent sequence.
- No uniformly matched external HPA/DepMap assay condition established.
- Endogenous TE defined by the original paper as residuals from compositional linear regression of centered-log-ratio CDS RPF/RNA counts, then averaged within cell context. Not raw Ribo/RNA ratios, completed protein output, or synthetic reporter labels.
- The Human sheet is a human-transcript benchmark, not independent verification of every context species or stock. In particular, TE_Vero_6 requires source-metadata reconciliation before assigning a human cell identity.

## Cell specificity

evidence: direct_multi_context; notes: Repeated endogenous transcripts across contexts; not synthetic-RNA cell-selective protein output.

## Sources

- https://www.nature.com/articles/s41587-025-02712-x
- https://github.com/Sanofi-Public/RiboNN
- https://static-content.springer.com/esm/art%3A10.1038%2Fs41587-025-02712-x/MediaObjects/41587_2025_2712_MOESM3_ESM.xlsx

- url: https://static-content.springer.com/esm/art%3A10.1038%2Fs41587-025-02712-x/MediaObjects/41587_2025_2712_MOESM3_ESM.xlsx; supports: Entire original Human table parsed; exact counts/hash in benchmark audit
- url: https://www.nature.com/articles/s41587-025-02712-x; supports: Methods define TE as compositional-regression residuals averaged within context

Related models: P010. Related resources: not established.
