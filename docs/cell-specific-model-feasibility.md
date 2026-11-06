# What can support a cell-specific RNA model?

Checked 5 November 2026. **A scoped predictive benchmark is feasible. A reliable predictor of intrinsic translation selectivity has not been established.** The strongest immediate supervised dataset is the original endogenous-mRNA RiboNN atlas. A smaller synthetic-circRNA project can predict LAMAR's relative reporter output. These are different tasks.

The [20-resource file audit](../evidence/file-audit-20261105/summary.json) covers selected files, queries or API records from 16 resources, including chemical/identity references and an index with linked experiments. Four resources have numerical-data access gaps: RPFdb, TransCirc, CELLxGENE Census and miRTarBase. This is not a full-file audit of every holding in 20 databases. [Payload provenance and checksum scopes](../evidence/file-audit-20261105/verified_payloads.json) distinguish full downloads, query responses and partial inspection.

## Recommended combinations

| Task | Labels and features | What the current files support | Remaining limitation |
|---|---|---|---|
| Endogenous human mRNA TE | Original RiboNN Human table; sequence/region annotations; HPA **or** DepMap cell-expression profiles where identities match | A reproducible test of whether external cellular features improve gene/context generalization | External expression is not matched to the TE experiments. Results describe the source TE estimator, not synthetic-RNA protein output. |
| Synthetic circRNA reporter output | LAMAR insert sequences and relative-output labels; optional external HPA/DepMap profiles | A small, assay-specific sequence-by-cell benchmark with cell-identity and additive baselines | Few independent cell contexts, uncertain stock aliases, shared reporter CDS, no released replicate-level uncertainty or paired RNA-persistence measurements. |
| Synthetic circRNA ribosome loading | Albatross curated insert identities and polysome-loading labels | A separate loading task; possible shared sequence representation with a separate target head | Loading is not completed protein production. Cross-study loading agreement cannot validate protein-output accuracy. Sequence-field conflicts need reconciliation. |
| Mechanistic annotation | ENCODE/POSTAR, RASP, Sci-ModoM/m6A-Atlas, CircTarget, RNALocate | Optional assay-specific features or mechanistic priors after matching identifiers, assembly, sequence and context | Endogenous annotations and interactions are not additional synthetic-reporter activity labels. Some source schemas/assemblies remain unresolved. |
| Functional tRNA context | Dedicated tRNA studies discovered through T-psi-C/tModBase | A separate stress/charging analysis after resolving schema and condition conflicts | No matched CDS-varying, cell-context protein-output panel was found in these files. LAMAR's fixed Fluc CDS cannot identify a codon-by-tRNA interaction. |

HPA and DepMap can share upstream CCLE profiles. Choose one principal context source and use the other as a sensitivity analysis after checking provenance. Do not concatenate their rows as independent biological replicates.

## Actual supervised labels

**RiboNN original Human supplement:** all 10,348 gene/transcript rows were parsed. There are 78 `TE_*` columns, 716,913 numeric values and 1,577 genes with numeric values in all 78 contexts. Missing context values remain missing. These repeated contexts are not 716,913 independent sequences. `mean_te` is derived from context labels and must not be supplied as an input predictor for those labels.

The original [paper's Methods](https://www.nature.com/articles/s41587-025-02712-x) define TE as residuals from compositional linear regression of centered-log-ratio RNA-seq and ribosome-footprint CDS counts, then average within cell context. Keep that estimator separate from a raw footprint/RNA ratio, RiboDecode's transformed footprint abundance and measured protein output. The [workbook audit](../evidence/file-audit-20261105/benchmarks/ribonn_human_original.json) records exact columns, missingness and digest. The author repository's example training file explicitly contains **fake TE values**; it is not ground truth. The Human sheet identifies the transcript benchmark, not independently verified species or stock for every context: the `TE_Vero_6` label particularly needs source-metadata reconciliation before a human-cell identity is assigned.

**LAMAR:** 305 unique supplied IRES insert sequences have 3,915 observed sequence-cell pairs. Complete subsets are 305 inserts across 11 cells or 280 inserts across 13 cells. The endpoint is reporter luminescence relative to a modified linear-mRNA reference after background subtraction. A cell-dependent denominator can affect this relative advantage. This is not absolute circRNA protein yield or protein synthesis per intracellular RNA. Its `Predicted probability` field is a model output and must not become an experimental label or a leakage-prone predictor. See the [original study](https://link.springer.com/article/10.1186/s13059-025-03752-x) and [file audit](../evidence/file-audit-20261105/benchmarks/lamar.json).

**Albatross:** the GEO workbook has 576 ID-cell loading estimates, with 96 IDs in six cells. IRES reference and endpoint sheets have different sequence cardinalities and five discordant ID-to-sequence assignments; alias reconciliation is also needed. The functional atlas is distinct from the structure model. The [audit](../evidence/file-audit-20261105/benchmarks/albatross.json) and [source workbook](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE347nnn/GSE347508/suppl/GSE347508_Supplement_S1.xlsx) preserve the original source version. Do not equate loading, reporter fluorescence and luminescent output by rescaling them to the same numerical range.

## Cell joins that the inspected files actually permit

The [join manifest](../catalog/cell_context_join_manifest.json) preserves source labels, proposed Cellosaurus identities, numeric coverage and uncertainty. All cross-study assay-condition matches remain **unestablished**.

- LAMAR: nine of its 13 cell labels have candidate numeric profiles in both inspected HPA and DepMap releases: A204, A549, AGS, HCT116, HepG2, JURKAT, SY5Y, THP-1 and U87. `SY5Y` and `U87` require source-identity clarification; seven less ambiguous candidates remain after withholding those two. Stock/subline confirmation remains required for a definitive identity claim.
- LAMAR's HFF1 and three mouse lines lack profiles in these selected human references. Do not impute mouse profiles from a human cell with a similar name.
- Albatross: Huh7, SHSY5Y and U2OS have candidate numeric profiles. HEK293T, HCT8 and mouse N2A do not. HCT-8 exists in DepMap's model metadata but has no row in the inspected expression matrix. HEK293 must not replace HEK293T.
- Human/mouse separation, source spelling, parental relationships, stock/subline and assay condition are separate mapping dimensions. A Cellosaurus synonym supports identity reconciliation; it does not establish identical culture, treatment, passage or time point.

A 7-cell context-feature benchmark still has about seven independent context profiles, even when each profile repeats across hundreds of sequences. It does not have thousands of independent cell states.

## Why the other databases cannot be pooled as labels

| Resource | Actual inspected extent | Appropriate role |
|---|---|---|
| RPFdb | No numerical payload retrieved: 403/DNS/timeout on attempted official routes | Further study discovery; not cleared as a new numerical source here |
| RiboSeq.Org | 234 A549 metadata records; 1,024 footprint intervals from a 1-MiB BigWig prefix | Endogenous footprint evidence. All five RNA-seq entries in this export were unprocessed; no ready paired TE matrix established |
| HPA | Complete 25.1 expression ZIP: 24,315,372 rows; 20,162 genes by 1,206 lines | External RNA-expression context; aggregate profiles lack replicate columns |
| DepMap | Complete 24Q4 expression CSV: 1,673 models by 19,193 genes, plus model/profile metadata | External RNA-expression context; this is a versioned inspected release, not a claim about the latest release |
| CELLxGENE Census | Release manifest; no numerical slice obtained with the available native runtime | Potential primary-cell relevance, not verified expression rows in this audit |
| ENCODE | Two K562 peak files, DDX24-knockdown gene/transcript quantifications and one cell-free RBNS enrichment file | Binding/motif priors. Knockdown expression alone is not an effect estimate; RBNS is not cell-specific binding |
| POSTAR3 | 5,361 ALKBH1/HeLa transcript-overlap rows; 1,971 unique sites | Binding annotation. Headerless extra scores and assembly remain unresolved; do not make coordinate joins yet |
| Sci-ModoM | 543 HEK293T pseudouridine sites with frequency and coverage | Endogenous modification evidence; not modification effects on synthetic RNA |
| m6A-Atlas | 427,760 human sites, 843,678 site-condition links and a bounded quantification prefix | Endogenous site/context annotation. Support rows are not independent sites or calibrated fractions |
| tModBase | 528 dataset metadata records; one 650-entity HepG2 numerical response | Exploratory tRNA evidence. Inspected condition is ALKBH7-mutant rescue; `total` is zero despite positive counts in 81 entities |
| T-psi-C | Study index and linked/independently investigated charging files | Study discovery. GSE188855 has a title-versus-treatment conflict; GSE239867 count-column ordering remains unresolved |
| MODOMICS | Three reference-position tables in one complete archive | Chemical identity/reference annotation; no cell-specific abundance or output |
| RASP | One raw HepG2 icSHAPE track: 7,732,882 valid numerical BED rows | Native RNA structural accessibility. Imputed tracks and synthetic reporter structures remain separate |
| RNALocate | 55 ACTB localization records in a complete selected CSV query; bulk ZIP links failed | Localization annotation with computed confidence; not output measurements |
| circAtlas | Complete human coordinate table: 768,986 entries | Identifier/coordinate reference. This particular file has no expression or translation labels |
| riboCIRC | Selected context and literature archives: 86 circRNAs/134 footprint-evidence rows and 80 literature rows | Coding/translation evidence; no uniform calibrated synthetic-output labels |
| TransCirc | Official data routes failed; no numerical rows retrieved | Candidate evidence source with unresolved access/version |
| CircTarget | 1,677 A549 RNA-RNA interaction rows, including 1,142 BSJ-supported rows | Endogenous interaction evidence. Same cell name does not match synthetic reporter sequences |
| miRTarBase | Current interaction file rejected requests; no interaction rows retrieved | Candidate miRNA evidence; not cleared for numerical integration |
| Cellosaurus | 18 selected JSON reference profiles | Cell identity/synonym/species reconciliation only |

## Evaluation needed before a reliability claim

1. Define one target, source estimator, RNA format and normalization per task. A protein/RNA ratio at one time point still reflects protein synthesis/degradation history and RNA persistence.
2. Compare sequence-only, cell-only, sequence-plus-cell-identity and additive sequence-effect-plus-cell-effect baselines. Test whether explicit context features predict **sequence-dependent differences between cells**, beyond broad output offsets.
3. Use held-out genes/sequence families, held-out cells and a combined held-out-sequence/held-out-cell test. Keep all measurements of a sequence family together for the corresponding sequence-generalization test. Fit feature selection, normalization and hyperparameters on training data only.
4. Deduplicate upstream studies and accessions. ContiTE reuses RiboNN; it is not independent validation. Different portals can expose the same Ribo-seq experiment. Quantify replicate and study variation where those data are available.
5. Report within-cell ranking, cell-contrast performance, uncertainty and failures on low-output examples. Bootstrap at biological sampling units such as gene families, cells and studies, rather than treating every repeated row as independent.
6. Treat external HPA/DepMap profiles as imperfect covariates. Demonstrating reliable synthetic cell-selective expression requires independent measurements of the same engineered RNAs across intended target/off-target contexts. Delivery, intracellular RNA amount/persistence and protein-output timing must be characterized for a translation-selectivity claim.

No predictor was trained or validated by this file audit. It establishes accessible evidence, plausible joins and limits. It does not certify predictive reliability or broad novelty.

## Provenance discrepancy requiring reconciliation

ContiTE's supplementary pages 3-4 report 11,798 human genes and 96 contexts, and the actual PDF hyperlink points to the original RiboNN MOESM3 workbook audited here. That current file contains 10,348 gene rows and 78 TE columns. The [provenance audit](../evidence/file-audit-20261105/translation/contite_source_audit.json) records the link, page locations and hashes. The exact preprocessing/version/count definition is unresolved. This finding does **not** show that predicted or fake labels were used. Use the recounted file dimensions and reproduce preprocessing before comparing against reported benchmark results.
