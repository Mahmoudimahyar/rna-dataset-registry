# Research priorities

These priorities are curation judgments based on label relevance, context and access; they are not a measured ranking of model performance.

| Question | Useful resources | Evidence boundary |
|---|---|---|
| How does synthetic mRNA chemistry affect translation? | Sample2019 chemistry-specific reporter libraries; direct-RNA chemical benchmarks as a separate modality | MRL labels support reporter translation analysis; natural modification maps alone do not measure therapeutic performance. |
| How do tRNA pools change with cell state? | Dedicated tRNA-seq differentiation/activation studies, including GSE227927; charging studies separately | Isodecoder mapping and assay biases matter. Transcript abundance/codon demand cannot substitute for measured tRNA supply. |
| Is charging different from abundance? | Charge-tRNAseq and other dedicated aminoacylation resources | Keep charged fraction, total counts and modification signatures separate. |
| Can RNA triggers regulate expression? | QC-defined GSE149225 toeholds, eToehold and ADAR sensor studies | Bacterial reporter results do not establish mammalian cell selectivity. Sensor papers may release sequencing while FCS/reporter measurements remain request-only. |
| Can UTRs support cell-selective expression? | Multi-context UTR reporters, MapUTR, PARADE concept/library records | Matched measurements are essential; PARADE release gaps currently limit reproducible retraining. |
| Can endogenous translation context help? | RPFdb, RiboSeq.Org, scRibo-seq, Ribo-STAMP and TRAP/RiboTag studies | These measure different endpoints; ordinary scRNA-seq is context, not direct translation ground truth. |
| What controls decay and processing? | Saluki source matrices, SLAM/ORFome studies, UTR-Seq, full-length UTR reporters, PolyASite/APARENT2 | Preserve decay method and units; PC1 consensus and cleavage profiles are not half-life in hours. |

The most useful early ML comparisons will use one well-defined endpoint and one compatible assay family, retain biological context and uncertainty, and evaluate on held-out studies/constructs. Larger heterogeneous collections are valuable for discovery and representation learning but do not automatically provide interchangeable supervised labels.

This registry supplies source identities and evidence limits. It does not supply sensor sequences, molecular designs, experimental procedures or a claim of validated cell-specific delivery.
