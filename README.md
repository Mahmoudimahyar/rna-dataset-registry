# RNA dataset registry

A source-backed catalog of RNA and mRNA resources for machine learning: chemical modifications, tRNA abundance and charging, cell state, RNA sensors, translation, stability, binding, structure, localization and polyadenylation.

**This is a resource registry, not a bundled or harmonized training corpus.** Source data remain with their original hosts. Counts mix resource/study/reference/benchmark levels and must not be interpreted as independent datasets or summed RNA observations. No world-largest or exhaustive-coverage claim is made.

## Explore

- Open [index.html](index.html) locally for offline search and filtering. GitHub displays its source; download/clone the repository to use the browser.
- Browse the [dataset index](docs/dataset-index.md) and individual [dataset cards](datasets/).
- Review the [52 model/family records from the literature collection](docs/model-index.md), including unresolved release and dataset gaps.
- Load [JSON](catalog/registry.json), [CSV](catalog/registry.csv), [model coverage](catalog/model_coverage.json) or the [access manifest](catalog/access_manifest.json).
- See [current counts and verification levels](catalog/summary.json) and [validation results](evidence/validation.json).
- Read the [20-resource actual-file audit and model feasibility assessment](docs/cell-specific-model-feasibility.md), [machine-readable audit](evidence/file-audit-20261105/summary.json), [candidate cell joins](catalog/cell_context_join_manifest.json) and [task-specific combination plan](catalog/combination_plan.json).
- Review the [response to scientific criticism](docs/review-response-2026-11-05.md), including corrected endpoints and the unresolved ContiTE source-dimension discrepancy.

Current file-audit release: **220 resource records**, including **132 source-backed records** and **88 candidates**. Selected data/reference payloads or linked study files were inspected for **16 of the 20 reviewed resources**. Four retain numerical-data access gaps. Reference entries, index records and repeated observations are not independent training datasets. The original human RiboNN supplement and two synthetic-circRNA reporter studies have separate label definitions and provenance; no trained predictor or harmonized biological corpus is claimed.

Research window: **4–5 November 2026**. The source library contains 193 PDF copies / 181 unique byte streams; no new source PDFs were found since the earlier review. This hash inventory does not certify scientific completeness. All 52 paper-level RNA model/family records are mapped; some records represent several algorithms/models. Known repository URLs were rechecked, with README pointer scans where retrievable. These checks do not establish that every paper dataset has been inspected.

Initial release: **122 source-backed records** (59 studies, 8 benchmarks, 31 databases, 11 references, 8 derived resources, 4 archives and 1 model release), plus **87 candidates** (86 imported model assets and 1 unverified project release). Evidence among the 122 source-backed records: 6 file samples, 14 schemas, 76 metadata reviews and 26 paper reviews. These counts describe records, not 122 independent biological datasets.

## Evidence levels

| Level | What it establishes |
|---|---|
| `file_sample` | A stated data file/header/sample or selected columns were inspected; extent is recorded. |
| `schema` | Loader/schema/example documentation was inspected; full source data may be absent. |
| `metadata` | Primary database/accession/release metadata was inspected. |
| `paper` | Original paper supports the description; direct data access may remain unresolved. |
| `unverified` | Candidate only, including imported model assets awaiting reconciliation. |

`curated` means source-backed metadata with an explicit verification level. It does **not** mean ready-to-train, full-file validation, license clearance or independent replication. Imported assets from the earlier nonexhaustive model audit remain candidates. Unavailable/controlled/request-only sources stay visible with their limits.

## Correct label use

- Separate natural modification maps from synthetic mRNA chemistry-performance experiments.
- Separate site calls, broad peaks, stoichiometry, chemical identity and predicted modifications.
- Separate mature tRNA abundance, charging, fragments, genomic copy number and Pol III occupancy.
- Separate endogenous translation efficiency, reporter mean ribosome load, TRAP/RiboTag enrichment and editing-based translation proxies.
- Separate bacterial switch ON/OFF activity from mammalian cell specificity, and intracellular regulation from physical delivery.
- Preserve assay, condition, units, resolution, negative-label definition, biological replicates and source provenance.

See [label policy](docs/label-policy.md), [research priorities](docs/research-priorities.md) and the [curation guide](docs/curation-guide.md).

## Rebuild and validate

Python3 standard library is sufficient for the catalog tools. They do not install or run RNA models.

```bash
python tools/build_registry.py
python tools/validate_registry.py
node tools/check_index.js
python tools/query_registry.py --topic chemical_modification --status curated
```

Curators edit `catalog/fragments/*.json`. Generated exports/cards/browser are rebuilt. Metadata-only archive helpers support further source discovery. The access manifest distinguishes file URLs from landing/API links; a listed URL is not proof of a downloaded or validated file. Source checksums, when not verified, remain null.

## Scope and reuse

This initial release extends the source literature collection and the supplied research leads. It is not an index of every RNA study in GEO/SRA/ENA or every experiment inside each database. [Coverage gaps](docs/coverage.md) are part of the release.

Original dataset licenses, consent and access rules apply. Public availability does not imply redistribution rights. No biological sequence corpus, raw reads, controlled human data, source PDFs or model weights are redistributed. Registry metadata are CC BY4.0; original software in `tools/` and `web/` is MIT. These licenses do not relicense the sources. See [LICENSE](LICENSE).
