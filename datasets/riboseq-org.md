# RiboSeq.Org portal family

Registry ID: `riboseq-org` · database · **curated** · verification: **file_sample**

Ribo-seq data portal plus genome/transcript browsers and processing tools.

## What the data contains

- Observation unit: Ribo-seq sample or processed track
- RNA scope: mRNA
- Biological context: Varies by contributing study; retain source sample metadata
- Assays: Ribo-seq
- Accessions: not established
- Scale: value: unknown; unit: unknown; basis: Not independently counted; freeze source release before acquisition; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| ribosome footprint coverage | Processed RPF evidence; ORF and translation summaries depend on pipeline | measured | unknown | transcript |

## Access and reuse

- Access: open
- Formats: browser tracks; processed files
- Source license: unknown
- Redistribution: See explicit source license; public accessibility alone is not redistribution permission

- https://riboseq.org/
- https://rdp.ucc.ie/sample_select_form/?download-metadata=Cell-Line%3DA549
- https://rdp.ucc.ie/static2/bigwig/SRR328/SRR3286544.forward.bw

## Verification and remaining gaps

Checked: 2026-11-05. Actual files/headers inspected: https://rdp.ucc.ie/sample_select_form/?download-metadata=Cell-Line%3DA549; https://rdp.ucc.ie/static2/bigwig/SRR328/SRR3286544.forward.bw.

- One cell-filtered metadata export and one 1-MiB BigWig prefix were inspected, not all studies
- 227 Ribo-Seq, 5 RNA-Seq, 1 tRNA-Seq, 1 SSU entries are not 234 independent comparable TE measurements
- Same cell name includes normal, drug, infection and genetic perturbation contexts
- Footprint occupancy can reflect elongation or stalling and is not direct protein synthesis rate
- Do not pool with reporter luminescence or polysome-loading labels
- Deduplicate upstream accessions against RPFdb and model training atlases
- Bounded file audit: evidence/file-audit-20261105/translation/translation_file_audit.json; selected coverage only.

- Portal, GWIPS-viz and Trips-viz views may show the same source experiments.
- Do not add sample counts from overlapping Ribo-seq resources.

## Cell specificity

evidence: context_only; notes: Context annotation can support stratified analysis; it does not establish selective expression or delivery of a synthetic construct.

## Sources

- https://riboseq.org/

- url: https://riboseq.org/; supports: Resource identity, available label types and access route described in primary source documentation

## Selected-file audit

Endogenous footprint signal and study/sample discovery; possible mRNA TE after matched RNA-seq processing

Selected payload inspected: True. Coverage: Selected files/API responses, not all source holdings.

[Inspection evidence](../evidence/file-audit-20261105/translation/translation_file_audit.json). [Combination assessment](../docs/cell-specific-model-feasibility.md).

Related models: not established. Related resources: rpfdb3; sra.
