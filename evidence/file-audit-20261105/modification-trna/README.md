# Modification and tRNA data-file audit

`audit.json` is the authoritative five-resource result. It distinguishes complete selected files, a bounded compressed prefix, numerical API responses, and index metadata. `tmod_api_audit.json` records the exact read-only GraphQL queries; `sci_selected_retrieval.json` records the selected numerical dataset and response checksum. The other scripts and manifests document discovery and inspection, including unsuccessful route probes. They do not establish that every database file is validated.

Bulk response bodies are deliberately excluded. Scripts accept an external `--download-dir`; do not choose a directory inside this repository. Use Python with `requests` and `beautifulsoup4`; read-only table analyses additionally use Python's standard library. No sequence values are written to public evidence.

Verified selected data:

- Sci-ModoM: 163 dataset metadata entries and the complete 543-site HEK293T BID-seq pseudouridine export. Current deployment uses legacy endpoints; the current documentation's newer dataset routes returned 404.
- m6A-Atlas: complete human high-resolution site and site-condition tables, a complete EIF4G2 API response, and a bounded quantification-file prefix. Site-support rows are not independent sites or calibrated modification fractions.
- tModBase: all 528 dataset metadata records and one complete numerical response for 650 tRNA entities in an ALKBH7-mutant-rescue HepG2 condition. Only 81 entities have nonzero counts/coverage. The `total` field is zero in every entity despite nonzero `counts`; interpretation remains unresolved.
- T-psi-C: a method/study discovery index. Its linked GSE239867 processed archive contains 12 count files. Separately inspected charging study GSE188855 contains 12 files with 67 tRNA IDs each. Three charging-ratio entries are missing; preserve them as missing.
- MODOMICS: one complete reference-position ZIP containing three legacy `.mods` tables, without cell-line or output measurements.

The GSE188855 `Ratio` values equal `100*CCA/(CCA+CC)` within rounding where reported. Its GSM5691036 title indicates starvation while the treatment metadata says untreated. Resolve this conflict before assigning a condition. GSE239867 has unlabeled colon-separated numerical fields; do not assign charged/uncharged column order without confirming the source.

None of the five resources supplies a matched synthetic-RNA sequence-by-cell protein-output table. Shared cell labels support exploratory annotation joins, not claims of matched culture, RNA exposure, persistence, modification state, or translation rate.
