# ac4C mapping and mRNA stability/translation (Arango et al., 2018)

Registry ID: `ac4c-arango-gse102113` · study · **curated** · verification: **metadata**

Study combining endogenous ac4C-enrichment maps with RNA abundance, ribosome profiling and stability endpoints plus targeted reporter validation.

## What the data contains

- Observation unit: An enriched ac4C interval or transcript-specific expression/translation/stability measurement under a condition.
- RNA scope: mRNA
- Biological context: HeLa NAT10-competent/depleted contexts; endogenous transcript assays and targeted synthetic ac4C reporter experiments are distinct components.
- Assays: acRIP-seq; RNA-seq; Ribo-seq; BRIC-seq; targeted reporter measurements
- Accessions: GSE102113
- Scale: value: 41; unit: GEO samples (multiple assay types); basis: Counted live GEO Series_sample_id fields; cannot be used as a per-assay count.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ac4C-enriched region | Antibody-enriched interval, not a resolved acetylated nucleotide. | computed | enrichment | interval |
| translation efficiency | Ribosome-density relative to mRNA abundance, as defined in the source. | computed | ratio | transcript |
| mRNA half-life | Assay-fitted transcript stability endpoint; units/schema require table inspection. | computed | unknown | transcript |

## Access and reuse

- Access: open
- Formats: TAR.GZ (processed archive); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102113

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.

- Antibody peaks are intervals and do not imply per-base acetylation ground truth.
- NAT10 perturbation can affect multiple RNA processes; association alone is not a pure cis ac4C effect.
- Targeted synthetic reporters are not a large chemistry-specific reporter-library dataset.
- Keep mRNA abundance, half-life and translation efficiency as different labels.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102113&targ=self&form=text&view=full
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6295233/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE102113&targ=self&form=text&view=full; supports: Live GEO metadata confirms RIP, RNA-seq, Ribo-seq and BRIC-seq components.
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6295233/; supports: Original article distinguishes ac4C enrichment, transcript half-life, ribosome-density efficiency and targeted reporters.

Related models: not established. Related resources: sample2019-chemistry-reporters; rmbase-v3.
