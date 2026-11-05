# RNA004 modification-aware basecalling benchmark (Diensthuber et al., 2026)

Registry ID: `dorado-rna004-modification-benchmark` · benchmark · **curated** · verification: **metadata**

Recent RNA004 DRS benchmark of modification-caller specificity, stoichiometry and cross-reactivity with synthetic controls plus multi-species native RNA.

## What the data contains

- Observation unit: A read-position modification probability or per-site frequency linked to a known input chemistry/control context.
- RNA scope: synthetic RNA; rRNA
- Biological context: Synthetic chemistry controls and native/IVT RNA across species; SeqTagger demultiplexing training data are separate from modification-caller benchmarking.
- Assays: nanopore direct RNA sequencing (RNA004); known-chemistry calibration; native-versus-IVT/control comparisons
- Accessions: PRJEB91026; PRJEB90280
- Scale: value: unknown; unit: unknown; basis: No current biological-data count independently established.; as_of: 2026-11-05

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| input modification chemistry/proportion | Source-defined benchmark condition, including cognate and noncognate chemistries. | synthetic | category/proportion | position |
| per-read modification probability | Modification-aware basecaller output. | prediction | probability | position |
| per-site modification stoichiometry | Aggregated caller estimate; paper documents systematic biases. | computed | fraction | position |

## Access and reuse

- Access: open
- Formats: POD5; BAM; reference annotation files (paper-described; not opened)
- Source license: unknown
- Redistribution: not established

- https://www.ebi.ac.uk/ena/browser/view/PRJEB91026
- https://www.ebi.ac.uk/ena/browser/view/PRJEB90280

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: not established.

- No biological data file was inspected; this record establishes resource metadata and documented endpoints only.
- No signal, alignment or reference file was inspected.
- Benchmark conclusions apply to the paper's specified caller/model versions; no model execution or current-version performance check was performed.

- PRJEB90280 is demultiplexing training data; do not call it an independent modification benchmark split.
- Cross-reactivity means a high predicted modification probability is not uniquely established chemistry.
- Canonical IVT controls are experimentally defined negatives for their construction; native noncalls remain coverage/caller-dependent.
- Paper notes duplicate sequencing of one low-proportion subset; lower-coverage duplicates were excluded by authors.
- Source evaluation used Dorado v0.8.0 with v5.1.0 modification-aware models; preserve these versions and RNA004 chemistry when reproducing reported comparisons.

## Cell specificity

evidence: none; notes: Multi-species detection controls are not a screen for cell-selective mRNA function.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC13273306/
- https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB91026
- https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB90280

- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13273306/; supports: Original 2026 article documents RNA004, synthetic/native controls, cross-reactivity and caller-specific stoichiometry bias.
- url: https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB91026; supports: Live project metadata independently verifies modification-aware basecalling benchmark identity.
- url: https://www.ebi.ac.uk/ena/browser/api/xml/PRJEB90280; supports: Live project metadata independently identifies b96_RNA004 SeqTagger training data as a distinct subset.

Related models: not established. Related resources: rmap-challenge; nanoconsensus-rrna-benchmark.
