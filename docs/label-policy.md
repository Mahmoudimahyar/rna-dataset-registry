# Label policy

The registry describes source labels; it does not certify that all source processing is correct. Future observation tables should have one row per entity, condition, assay and observation. Keep the original value alongside any transformed target.

| Distinction | Required interpretation |
|---|---|
| Modification identity vs position | A chemical catalog defines a modification, not its presence on a transcript in a cell. |
| Modification site vs peak | Single-position calls and broad enrichment intervals have different resolutions. |
| Not detected vs absent | Low coverage and assay sensitivity can produce missing calls; do not generate negatives from every uncalled position. |
| Native vs synthetic chemistry | Native maps and experiments substituting modified nucleotides in synthetic mRNA answer different questions. |
| tRNA gene vs molecule | Genomic copy number/Pol III occupancy are not mature tRNA abundance. |
| Abundance vs charging | Total mature tRNA and aminoacylated fraction are distinct endpoints. |
| Full-length tRNA vs fragment | Fragment abundance from ordinary small-RNA libraries must not be relabeled as total mature tRNA. |
| TE vs MRL | Endogenous matched Ribo-seq/RNA-seq TE and reporter polysome-derived mean ribosome load are different labels. |
| TRAP vs Ribo-seq | Ribosome-associated mRNA enrichment is not positional ribosome footprint occupancy. |
| Ribo-STAMP vs RPF | Editing-based association is a proxy with its own detection biases. |
| Half-life vs consensus | Fitted half-life has source units; Saluki PC1 is a unitless aggregate target. |
| ON/OFF vs cell specificity | Trigger state in one assay is not automatically target/off-target cell behavior. |
| Subcellular vs cell type | Localization within a cell differs from expression specificity between cell types. |
| Prediction vs observation | Model outputs, imputed tracks and pseudo-labels cannot be treated as new experimental ground truth. |

Preserve taxon, assembly, annotation release, transcript/isoform ID, cell/tissue/state, treatment, time, donor, reporter, cargo, chemistry, assay protocol identifier, biological/technical replicate, source accession, processing version, uncertainty and missingness. Use a source-supported unit or `unknown`.

For ML evaluation, split by relevant source study, donor, gene/isoform, homologous family or shared construct, according to the hypothesis. A random row split can leak the same entity across train and test. Different datasets measured in different cells cannot be joined into matched specificity labels without checking entity overlap, assay and normalization compatibility.

Ontology references may include NCBI Taxonomy, Cell Ontology, UBERON, EFO, GENCODE/RefSeq and MODOMICS. Mapping to an ontology is annotation work, not new biological evidence.
