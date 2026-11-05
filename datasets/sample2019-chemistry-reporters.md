# Sample et al. 2019 chemistry-specific 5′ UTR reporter libraries

Registry ID: `sample2019-chemistry-reporters` · study · **curated** · verification: **metadata**

Synthetic reporter-library measurements with separately labeled U, pseudouridine and N1-methylpseudouridine RNA chemistries.

## What the data contains

- Observation unit: A reporter-library member × RNA chemistry × experiment, with fraction counts and derived mean ribosome load.
- RNA scope: mRNA
- Biological context: Pooled reporter mRNAs assayed in HEK293T cells; chemistry-specific eGFP replicate pairs, mCherry and other library subsets must remain distinct.
- Assays: polysome profiling; fraction RNA sequencing
- Accessions: GSE114002; GSM3130435; GSM3130436; GSM3130437; GSM3130438; GSM3130439; GSM3130440
- Scale: value: 10; unit: GEO samples (all library subsets); basis: Counted live series/sample metadata; six samples are paired chemistry-specific eGFP libraries, not six independent variant sets.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RNA chemistry | Experimental U/Ψ/m1Ψ chemistry class, not an endogenous site annotation. | annotation | category | construct |
| mean ribosome load (MRL) | Fraction-weighted estimate of reporter ribosome occupancy. | computed | ribosomes per reporter (assay estimate) | construct |
| polysome distribution | Relative reporter counts across polysome fractions. | computed | relative count | construct |

## Access and reuse

- Access: open
- Formats: CSV.GZ (sample-level processed tables); TAR (series aggregate); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114002

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- No processed table header or biological data row was downloaded.
- GEO describes a 300,000-member randomized library whereas the paper analyzes 280,000; no unified construct count is asserted.
- GEO and paper also differ on some variant-result totals; these are not used as registry scale.

- This is a synthetic chemically modified mRNA performance study, not an endogenous pseudouridine-site map.
- MRL is an assay-derived translation proxy, not direct protein concentration, half-life or degradation rate.
- Treat chemistry and reporter context as explicit variables; shared library members/replicates require leakage-aware grouping.
- A canonical-U control is experimentally defined for this library, unlike unobserved sites in endogenous maps.

## Cell specificity

evidence: context_only; notes: The pooled assay context is HEK293T; it is not a multi-cell-type selectivity screen.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114002&targ=self&form=text&view=full
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114002&targ=gsm&form=text&view=full
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7100133/
- https://github.com/pjsample/human_5utr_modeling

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114002&targ=self&form=text&view=full; supports: Live series metadata names three RNA chemistries and distinct library subsets.
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114002&targ=gsm&form=text&view=full; supports: Live sample metadata confirms paired eGFP unmodified/pseudo/m1pseudo CSV files.
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7100133/; supports: Original paper defines MRL, HEK293T context and chemistry-specific reporter measurements.
- url: https://github.com/pjsample/human_5utr_modeling; supports: Author README links processed CSVs to GEO; repository code license is separate from data reuse rights.

Related models: P002; P006; P007; P012; P018; P019. Related resources: ac4c-arango-gse102113.
