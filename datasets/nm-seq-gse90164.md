# Nm-seq (including published correction)

Registry ID: `nm-seq-gse90164` · study · **curated** · verification: **metadata**

Human mRNA 2′-O-methylation mapping resource with revised analysis/data described in a subsequent correction.

## What the data contains

- Observation unit: A candidate 2′-O-methylated position in a source cell-line profile.
- RNA scope: mRNA
- Biological context: HeLa and HEK mRNA profiles; original and corrected evidence must be identified before selecting labels.
- Assays: Nm-seq
- Accessions: GSE90164
- Scale: value: 10; unit: GEO samples; basis: Counted live GEO Series_sample_id fields; not distinct candidate sites.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Nm position | Chemical-enrichment-derived candidate 2′-O-methylation call. | computed | unknown | position |

## Access and reuse

- Access: open
- Formats: BED-like TXT.GZ; SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90164

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Corrected versus original file versions were not resolved by file inspection; candidate labels need this check before reuse.

- Adaptor-related artifacts affected the original consensus claim; treat original labels cautiously and retain correction provenance.
- A missing enrichment call is not a verified Nm-free base.
- Do not treat this resource as interchangeable with Nm-Mut-seq, which has different chemistry coverage.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90164&targ=self&form=text&view=full
- https://www.nature.com/articles/nmeth.4294
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6994179/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90164&targ=self&form=text&view=full; supports: Live GEO metadata identifies Nm-seq and listed HeLa/HEK coordinate-file names.
- url: https://www.nature.com/articles/nmeth.4294; supports: Primary article includes change history addressing adaptor/mispriming concerns.
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6994179/; supports: Published correction documents revised Nm-seq data deposited in the same accession.

Related models: not established. Related resources: nm-mut-seq-gse174518; rmbase-v3.
