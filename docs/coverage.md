# Coverage and remaining work

The release contains individually investigated resource/study records,52 mapped paper-level RNA model/family records, and86 explicitly unverified imported asset records from an earlier audit. Consult `catalog/summary.json` for actual current totals after curation.

The literature collection was re-inventoried by SHA-256:193 source PDF copies,181 unique byte streams, no newly added unique PDF since the earlier review. Historical output/tmp/version folders were excluded. This establishes which files were in scope; it does not establish complete interpretation of every model or supplement.

All52 known GitHub URLs in the model inventory were checked through public repository metadata.51 were reachable and the cited codonGPT release returned404. These are URL checks, not52 confirmed official repositories or52 unique models.49 READMEs were scanned for data pointers; two reachable repositories had no root README located. No count certifies that every nested file or dataset used by a paper has been inspected. Alternative hosts such as Bitbucket and Hugging Face remain explicit in model provenance/candidate records.

Remaining work includes:

- Reconcile every main-paper and supplementary dataset, source accession, release and train/validation/test membership for every model.
- Replace imported candidate assets with individually curated source records, avoiding duplicate studies and source mirrors.
- Inspect full tables and manifests where public; validate labels, replicate identity, missingness, schema drift and units.
- Resolve unavailable/request-only archives and document access grants without storing credentials or controlled data.
- Verify source-specific licensing and checksums before acquisition/redistribution.
- Add more studies through accession discovery and primary review. Database children are not automatically curated because the parent portal is listed.
- Compare scope with other public collections before making a world-largest claim. No such comparison has been completed.

Examples of corrected source interpretation: GSE270249 is the miRNA companion assay inside GSE270254, whereas GSE270252 contains the reporter amplicon sequencing. GSE239759 is RiboTag mRNA; GSE250090 provides paired Pol III occupancy evidence rather than direct mature-tRNA abundance. GSE149225's244,000-row source library and91,534 QC-passed ratio observations are distinct denominators.
