# Response to the scientific review

The review's central correction is accepted: the project should initially concern **cell-selective protein expression from mRNA or circRNA**. Reserve **translation selectivity** for evidence that separates intracellular RNA exposure, abundance/persistence and protein production. An endpoint protein/RNA ratio does not by itself identify a translation rate.

I am revising the recommendation from an asserted strongest new circRNA model to two testable, bounded options: an endogenous-mRNA TE benchmark with established comparators, or an assay-specific synthetic-circRNA relative-output benchmark. The [actual-file feasibility assessment](cell-specific-model-feasibility.md) explains which data support each. Neither is a broad novelty or reliability claim.

## Changes to model interpretation

| Topic | Revised interpretation |
|---|---|
| PARADE | UTR sequence, explicit cell-line identity and sequence annotations predict post-transcriptional activity and deviation from the across-cell mean. Six training cell lines do not imply arbitrary-cell inference. Stability/abundance effects remain part of reporter activity; cited version is a preprint. |
| RiboDecode | CDS, target mRNA abundance and a cellular RNA-expression profile predict **ln(5 × Ribo-seq RPKM + 1)**. This is not RNA-normalized TE or protein production per RNA. Preferential linear-mRNA expression and separate modified/circular-RNA validations do not jointly establish circRNA cell selectivity. |
| RiboNN | Sequence and coding-frame annotations feed fixed context-specific multitask outputs. Standard inference does not require a measured cellular-state vector. Separate supervised transfer learning is available. Its actual TE estimator is a compositional-regression residual, not a generic protein-output rate. |
| ContiTE | Sequence regions and learned context embeddings support few-shot target-context adaptation using labeled support examples. A zero-shot comparator is also evaluated. It reuses RiboNN data; the direct source-file dimensions require reconciliation with its reported benchmark counts. |
| Albatross | The language model infers structure; the functional atlas measures polysome-derived loading in synthetic circRNA reporters. Loading is a separate endpoint from completed protein output. The cited atlas is a preprint. |
| IRES-LM, IRES-EA and IRES-DM | Separate sequence classification from predictor-guided evolutionary optimization and diffusion generation. The inspected MPRA files concern an auxiliary reporter task, and sequence-to-barcode mapping was not verified. Reused circRNA positives with predicted probabilities are not new quantitative cross-cell labels. |
| CITActivator | The protein-feature classifier uses labels from an RBP reporter screen with forced recruitment. Tethered activity does not establish natural binding or cell specificity. Selected natural recruitment/context validations remain distinct experiments. |
| ADAR-GPT | A 201-nt candidate-site window supports threshold-defined edited-site classification. Its principal 15% task threshold does not turn positive-class probability into molecular editing fraction, sensor activation or leak. |
| TransRM | Modification-centered features support estimated site contributions and circRNA translation probability. These are not absolute yield, context-specific output or proven causal effects of installing/removing a modification. Exact implementation schema was not fully audited here. |
| tAI and SDA | Classic tAI uses codons, gene-copy-derived decoding weights and wobble assumptions; abundance-adapted variants can use measured tRNA. Supply-demand scores additionally incorporate transcriptome-weighted demand. Condition-specific scores already exist. Their existence and successful coding-sequence prediction do not establish cell-selective protein production. |
| SANDSTORM/GARDN and toehold models | Distinguish prediction from generation and bacterial toehold/RBS assays from the framework's other RNA tasks. Preserve the implementation's sequence-derived possible-base-pair compatibility arrays; do not describe them as experimentally measured structures or thermodynamic pairing probabilities. Accessibility alone is not a new modeling contribution. |
| Delivery models | Delivery-associated protein expression is a separate task from intracellular RNA-sequence regulation. A cell-resolved lipid model cannot supply intrinsic RNA translation labels. |

The original catalog cards for PARADE, RiboNN and RiboDecode were corrected. The [endpoint source check](../evidence/file-audit-20261105/cell-context/model_endpoint_review.json) records independent primary-page/code checks for eight named methods. This does not claim a fresh replication of every experiment in the supplied review.

## Prior art and experimental distinctions retained

- [Mammalian eToeholds](https://www.nature.com/articles/s41587-021-01068-2) provide directly relevant IRES-based sensing prior art; bacterial switch validation cannot be transferred as mammalian circRNA validation.
- [CellREADR](https://pmc.ncbi.nlm.nih.gov/articles/PMC10348343/) and [RADARS](https://www.nature.com/articles/s41587-022-01534-5) are experimental platforms. Keep original delivery format, endogenous versus supplied ADAR, and individual in-vivo demonstrations separate.
- [PROMITAR](https://www.nature.com/articles/s41467-023-43065-w) and [synthetic circRNA switches/circuits](https://pubmed.ncbi.nlm.nih.gov/36642090/) establish prior combinations of regulation modules. A molecular classifier is not necessarily trained ML. TargetScan's context++ target-repression setting is not a quantitative predictor of all synthetic gates.
- [CICADA](https://academic.oup.com/nar/article/53/1/gkae1179/7931345) and [cirCodAn](https://pubmed.ncbi.nlm.nih.gov/38448139/) preclude a blanket claim that sequence-based circRNA coding prediction is missing. Coding potential, coding-region identification and quantitative cell-specific output remain different targets.
- Scanning/uORF stress simulations, ligand switches and DNA-encoded protein circuits retain their original assay scope. Their components do not automatically establish every synthetic-RNA/cell-specific implementation.

These additional citations and distinctions were supplied in the review and retained as relevant prior art; the current file-audit scope does not constitute a complete independent re-review of all their data.

## What the file audit changes

1. **The immediate tRNA-aware circRNA claim is weaker than I previously suggested.** LAMAR varies IRES inserts in a shared Fluc CDS. There is no independent CDS/codon variation from which to learn a codon-by-tRNA-context interaction. The inspected tModBase condition is perturbed, and dedicated charging files have unresolved condition/schema issues.
2. **External cell profiles are useful covariates, not matched biological measurements.** Nine LAMAR cell labels have candidate numeric HPA/DepMap profiles; two aliases need particular caution. All culture/treatment/time matches remain unestablished.
3. **A larger endogenous-mRNA benchmark is presently better supported by actual labels.** The original human RiboNN file has 10,348 gene rows and 78 context columns. It supplies a defined target and established baselines. This is a strategic assessment of current data readiness, not proof that a new model will improve on them.
4. **The circRNA task remains credible within a narrower endpoint.** Predict LAMAR's relative reporter advantage, test sequence-by-cell effects against simple baselines and evaluate loading as a separate task. Time-resolved protein output and intracellular RNA persistence would support a stronger future claim, but those paired measurements are not supplied by the 20 databases audited here.
5. **A paper count does not establish novelty.** Any new contribution must specify the measured endpoint, cellular context, RNA format, comparator and demonstrated held-out generalization. No universal cell-type exclusivity is established.

No model was trained in this audit. The published additions are source links, provenance, file schemas/counts, checksums, join candidates and explicit limitations.
