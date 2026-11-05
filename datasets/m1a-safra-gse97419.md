# Single-base cytosolic/mitochondrial m1A map (Safra et al., 2017)

Registry ID: `m1a-safra-gse97419` · study · **curated** · verification: **metadata**

Semi-quantitative m1A mapping with antibody, RT and chemical-control comparisons, distinguishing sparse cytosolic calls from mitochondrial m1A.

## What the data contains

- Observation unit: A candidate m1A position and assay-dependent misincorporation/stoichiometry estimate.
- RNA scope: mRNA
- Biological context: Accession profiling uses HEK293 RNA with RT, immunoprecipitation, chemical rearrangement and TRMT6/TRMT61A comparisons; broader tissue/development observations are reported in the paper.
- Assays: m1A mapping with RT-signature and antibody controls
- Accessions: GSE97419
- Scale: value: 20; unit: GEO samples; basis: Counted live GEO Series_sample_id fields.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| m1A site | Control-supported single-base candidate m1A annotation. | computed | unknown | position |
| semi-quantitative m1A level | Assay-derived relative/stoichiometric estimate; numerical schema was not inspected. | computed | unknown | position |

## Access and reuse

- Access: open
- Formats: TAR (supplementary archive); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE97419

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.

- Do not inherit broad m1A-positive labels from older enrichment maps without reconciling resolution and artifacts.
- A cell-line GEO subset does not itself establish every tissue/development result in the paper.
- Noncalls are coverage/control-dependent and do not certify globally unmethylated adenosines.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE97419&targ=self&form=text&view=full
- https://pubmed.ncbi.nlm.nih.gov/29072297/

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE97419&targ=self&form=text&view=full; supports: Live series metadata gives HEK293 profiling contrasts and semi-quantitative map scope.
- url: https://pubmed.ncbi.nlm.nih.gov/29072297/; supports: Original paper reports limited low-stoichiometry cytosolic m1A and a tissue/development-regulated mitochondrial ND5 site.

Related models: not established. Related resources: rbs-seq-gse90963.
