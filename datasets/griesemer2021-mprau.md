# Griesemer MPRAu human 3-prime UTR variant panel

Registry ID: `griesemer2021-mprau` · study · **curated** · verification: **metadata**

Matched six-cell UTR-variant reporter study with released ENCODE functional-characterization experiments.

## What the data contains

- Observation unit: UTR allele/background by cell line and replicate
- RNA scope: mRNA
- Biological context: HEK293, HepG2, GM12878, SK-N-SH, K562 and primary mammary epithelial cells.
- Assays: MPRAu RNA/DNA reporter assay
- Accessions: ENCSR481QRH; ENCSR812PWW; ENCSR147BIK; ENCSR885ULM; ENCSR181PJG; ENCSR616NNF
- Scale: value: unknown; unit: unknown; basis: not independently counted; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| RNA/DNA relative expression | Normalized reporter RNA abundance relative to DNA | computed | ratio | construct |
| allelic skew | Reference-versus-alternate expression difference | computed | source log2 fold-change | construct |
| significance | Source statistical and multiple-testing results | computed | p-value / adjusted p-value | construct |

## Access and reuse

- Access: open
- Formats: ENCODE linked raw and processed files
- Source license: unknown
- Redistribution: not established

- https://www.encodeproject.org/ENCSR481QRH/
- https://www.encodeproject.org/ENCSR812PWW/
- https://www.encodeproject.org/ENCSR147BIK/
- https://www.encodeproject.org/ENCSR885ULM/
- https://www.encodeproject.org/ENCSR181PJG/
- https://www.encodeproject.org/ENCSR616NNF/

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- Archive metadata inspected; linked quantitative tables not inspected.
- Source reference-coding/indexing issues require QC/background flags.

- Group alleles, alternate backgrounds and tiling mutants in the same split.
- Cryptic reporter splicing can affect abundance; this is not automatically decay rate.
- Preserve cell identity and normalization.

## Cell specificity

evidence: direct_multi_context; notes: Direct matched reporter RNA-abundance effects; not absolute protein output.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC8487971/
- https://www.encodeproject.org/documents/3f7d5100-ebff-4829-8f6a-c36973d436ee/@@download/attachment/MPRAu_Methods.pdf
- https://www.encodeproject.org/ENCSR481QRH/
- https://www.encodeproject.org/ENCSR812PWW/
- https://www.encodeproject.org/ENCSR147BIK/
- https://www.encodeproject.org/ENCSR885ULM/
- https://www.encodeproject.org/ENCSR181PJG/
- https://www.encodeproject.org/ENCSR616NNF/

- url: https://www.encodeproject.org/ENCSR481QRH/?format=json; supports: Released MPRA experiment with matching biosample.
- url: https://www.encodeproject.org/ENCSR812PWW/?format=json; supports: Released MPRA experiment with matching biosample.
- url: https://www.encodeproject.org/ENCSR147BIK/?format=json; supports: Released MPRA experiment with matching biosample.
- url: https://www.encodeproject.org/ENCSR885ULM/?format=json; supports: Released MPRA experiment with matching biosample.
- url: https://www.encodeproject.org/ENCSR181PJG/?format=json; supports: Released MPRA experiment with matching biosample.
- url: https://www.encodeproject.org/ENCSR616NNF/?format=json; supports: Released MPRA experiment with matching biosample.
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8487971/; supports: Six-cell assay and allele interpretation.

Related models: not established. Related resources: maputr-2024.
