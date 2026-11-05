# NanoConsensus rRNA modification benchmark/study

Registry ID: `nanoconsensus-rrna-benchmark` · benchmark · **curated** · verification: **metadata**

Comparative DRS benchmark with source-defined rRNA controls and a separate study of antibiotic-associated rRNA modification differences.

## What the data contains

- Observation unit: A source-defined rRNA read/position benchmark label or a differentially modified region from pairwise comparison.
- RNA scope: rRNA
- Biological context: Bacterial and yeast rRNA reference/control comparisons; antibiotic-exposure data are a distinct application subset.
- Assays: nanopore direct RNA sequencing; comparative modification calling
- Accessions: PRJEB42568; PRJEB48806; PRJEB37798
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| benchmark modified/unmodified assignment | Source assumes wild-type reads modified and corresponding enzyme-deficient reads unmodified at selected reference sites. | annotation | category | position |
| differentially modified region | Consensus computational signal difference; qualitative or semi-quantitative and not single-base resolved. | computed | score | interval |

## Access and reuse

- Access: open
- Formats: FAST5; source-data tables; BED (documented analysis outputs)
- Source license: unknown
- Redistribution: not established

- https://www.ebi.ac.uk/ena/browser/view/PRJEB42568
- https://www.ebi.ac.uk/ena/browser/view/PRJEB48806
- https://www.ebi.ac.uk/ena/browser/view/PRJEB37798

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- Only three relevant project titles were independently read; other accessions mentioned by the paper are not asserted as separately verified records.
- Correction content and full supplementary benchmark definitions require review before numerical reuse.

- Wild-type 100%/control 0% assignments are benchmark assumptions at selected sites, not general measured stoichiometry for every molecule.
- NanoConsensus output regions lack single-nucleotide resolution and do not inherently give change direction.
- This is primarily rRNA evidence; it is not a mammalian synthetic mRNA expression dataset.
- Repeated mixtures/subsampling of the same molecules are not independent biological examples.

## Cell specificity

evidence: none; notes: Species/strain and exposure contrasts do not establish mammalian cell specificity.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11607429/
- https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB42568
- https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB48806
- https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB37798
- https://www.nature.com/articles/s41467-024-54368-x

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11607429/; supports: Original paper documents benchmark assumptions, lower-resolution differential regions and limitations in direction/quantification.
- url: https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB42568; supports: Live ENA project title verifies single-control-strain study provenance.
- url: https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB48806; supports: Live ENA project title verifies antibiotic-exposure subset.
- url: https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB37798; supports: Live ENA project title verifies reused yeast total-RNA modification data.
- url: https://www.nature.com/articles/s41467-024-54368-x; supports: Primary article notes a 2025 author correction and separates generated versus reused accession families.

Related models: not established. Related resources: modomics; dorado-rna004-modification-benchmark.
