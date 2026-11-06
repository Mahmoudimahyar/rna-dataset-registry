# LAMAR multicell circRNA reporter-output panel

Registry ID: `lamar-circrna-multicell-output` · study · **curated** · verification: **file_sample**

305IRES inserts in a shared synthetic circRNA reporter;3915observed sequence-cell pairs across13cell lines.

## What the data contains

- Observation unit: IRES insert by cell line in shared reporter
- RNA scope: circRNA
- Biological context: Shared Fluc circRNA reporter; mixed human/mouse cell lines;24-hour output; source-selected IRES candidates.
- Assays: Reporter luminescence
- Accessions: not established
- Scale: value: 3915; unit: observed sequence-cell pairs;305unique insert sequences; basis: All activity and metadata rows inspected; complete280-by13or305-by11subsets.; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Raw Activity | Reporter luminescence relative to modified linear mRNA control after mock subtraction | computed | relative activity | construct |
| Predicted probability | LAMAR classification score; not experimental activity | prediction | probability | construct |

## Access and reuse

- Access: open
- Formats: XLSX
- Source license: unknown
- Redistribution: not established; metadata only redistributed

- https://static-content.springer.com/esm/art%3A10.1186%2Fs13059-025-03752-x/MediaObjects/13059_2025_3752_MOESM2_ESM.xlsx

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://static-content.springer.com/esm/art%3A10.1186%2Fs13059-025-03752-x/MediaObjects/13059_2025_3752_MOESM2_ESM.xlsx.

- These are IRES insert sequences in a shared circRNA reporter context, not complete independent circRNA designs.
- The same sequence is repeated across cells; do not treat 3915 pairs as 3915 independent sequence examples.
- Contains 305 viral-derived candidates and 13 cell contexts; model training must group sequence-related records and account for source and assay differences.
- No imputation was performed; exactly 25 IDs lack both Neruo-2a and U87 values.
- Three metadata records (IDs 92, 135, 275) have sequence length unequal to End-Start+1. This audit does not infer the reason. Use the supplied Sequence column and exact IRES ID join; do not silently reconstruct sequences from accession coordinates.
- Methods report two replicates, but workbook contains one scalar per pair and no replicate uncertainty.
- Cell-specific reference-mRNA normalization limits interpretation to relative reporter advantage.
- Shared FlucCDS cannot identify a varying-CDS codon by tRNA-context interaction.

- These are IRES insert sequences in a shared circRNA reporter context, not complete independent circRNA designs.
- The same sequence is repeated across cells; do not treat 3915 pairs as 3915 independent sequence examples.
- Contains 305 viral-derived candidates and 13 cell contexts; model training must group sequence-related records and account for source and assay differences.
- No imputation was performed; exactly 25 IDs lack both Neruo-2a and U87 values.
- Three metadata records (IDs 92, 135, 275) have sequence length unequal to End-Start+1. This audit does not infer the reason. Use the supplied Sequence column and exact IRES ID join; do not silently reconstruct sequences from accession coordinates.
- Methods report two replicates, but workbook contains one scalar per pair and no replicate uncertainty.
- Cell-specific reference-mRNA normalization limits interpretation to relative reporter advantage.
- Shared FlucCDS cannot identify a varying-CDS codon by tRNA-context interaction.

## Cell specificity

evidence: direct_multi_context; notes: Same inserts across named cells; relative output only, not intrinsic translation rate or arbitrary unseen-cell generalization.

## Sources

- https://link.springer.com/article/10.1186/s13059-025-03752-x
- https://static-content.springer.com/esm/art%3A10.1186%2Fs13059-025-03752-x/MediaObjects/13059_2025_3752_MOESM2_ESM.xlsx

- url: https://static-content.springer.com/esm/art%3A10.1186%2Fs13059-025-03752-x/MediaObjects/13059_2025_3752_MOESM2_ESM.xlsx; supports: Full metadata/activity workbook joined byIRESID and counted

Related models: not established. Related resources: not established.
