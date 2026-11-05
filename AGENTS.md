# Registry maintenance

This repository catalogs public RNA data; it does not contain a unified biological training table.

- Use primary repositories, database documentation, accession metadata and original papers.
- Keep database, study, processed dataset, benchmark split, reference, prediction and example distinct.
- Never infer measured expression from sequence availability, tRNA abundance from gene copy number, or cell specificity from a single context.
- Preserve assay, units, label definition, resolution, negatives, biological context, source version and access terms.
- A URL visit is not a file inspection. Record verification levels and exact remaining gaps.
- Do not upload source PDFs, personal paths, credentials, controlled data, model weights or bulk biological data.
- Do not infer permission to redistribute from public accessibility. Unknown licenses remain unknown.
- Preserve original measurements; any derived label needs its own definition and provenance.
- Include missing values and uncertainty explicitly. Do not claim global completeness or world-largest status without a reproducible comparison.
- Agents write only their assigned `catalog/fragments/*.json` and supporting `evidence/` metadata files. The main coordinator integrates and validates.

See `docs/curation-guide.md` for the record format.
