# UBS-seq m5C benchmark: RNA subset

Registry ID: `ubs-seq-gse225614` · study · **curated** · verification: **metadata**

Ultrafast-bisulfite assay study containing both DNA experiments and a distinct RNA m5C profiling subset.

## What the data contains

- Observation unit: A covered RNA cytosine with a source methylation estimate; DNA observations are outside the RNA subset.
- RNA scope: mRNA; other RNA
- Biological context: RNA subset includes HeLa/HEK293T poly(A)+ RNA and selected NSUN2/NSUN6 perturbations; mouse and cfDNA experiments are distinct DNA subsets.
- Assays: UBS-seq; conventional bisulfite-seq comparison
- Accessions: GSE225614
- Scale: value: 44; unit: GEO samples (mixed DNA and RNA); basis: Counted live GEO Series_sample_id fields; RNA-only sample count not asserted.; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RNA m5C site | RNA-bisulfite-derived m5C call in a source condition. | computed | unknown | position |
| RNA methylation stoichiometry | Coverage- and conversion-dependent estimate, distinct from DNA methylation output. | computed | unknown | position |

## Access and reuse

- Access: open
- Formats: TSV.GZ (RNA site tables); TAR (BW archive); SRA
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225614

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.

- Do not import DNA methylation rows into an RNA modification dataset.
- The total series scale is not an RNA sample/site count.
- Bisulfite nonconversion, structure and coverage affect m5C inference; a noncall is not a universally unmodified cytosine.

## Cell specificity

evidence: context_only; notes: Source context annotations do not by themselves establish cell-selective function.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225614&targ=self&form=text&view=full
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225614
- https://www.nature.com/articles/s41587-023-02034-w.pdf

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225614&targ=self&form=text&view=full; supports: Live series metadata confirms mixed DNA/RNA title and RNA-specific HeLa/HEK293T site tables.
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225614; supports: Primary accession lists RNA poly(A)+ contexts and NSUN2/NSUN6 perturbations separately from DNA samples.
- url: https://www.nature.com/articles/s41587-023-02034-w.pdf; supports: Original article establishes RNA/DNA m5C assay scope and accession linkage.

Related models: not established. Related resources: m5c-atlas; rbs-seq-gse90963; hpsc-m5c-gse240569.
