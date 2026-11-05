# Curation guide

One registry record describes one resource or one distinct study/dataset family. It is not one experimental observation. A database resource and a study it indexes may both have records, with their relationship made explicit; never add their sizes together.

Each JSON record has these fields:

```json
{
  "id": "stable-lowercase-id",
  "name": "Source's name",
  "kind": "database|archive|reference|study|benchmark|model_release|software_example|derived_resource",
  "topics": ["chemical_modification"],
  "rna_scope": ["mRNA"],
  "description": "What this resource contains, in plain language",
  "source_urls": ["https://primary.source/"],
  "paper_doi": [],
  "accessions": [],
  "organisms": [],
  "biological_context": "Tissues, cells, states, conditions; unknown when not established",
  "assays": [],
  "observation_unit": "What one source observation represents",
  "labels": [{"name":"source field or endpoint", "meaning":"what it measures", "label_type":"measured|computed|annotation|prediction|synthetic|unknown", "unit":"unknown", "resolution":"sample|cell|transcript|position|interval|construct|unknown"}],
  "scale": {"value":null,"unit":"unknown","basis":"not independently counted","as_of":"2026-11-04"},
  "access": {"level":"open|mixed|controlled|request|unavailable|unknown", "data_urls":[],"formats":[],"license":"unknown","redistribution":"not established"},
  "verification": {"level":"file_sample|schema|metadata|paper|unverified", "checked_on":"2026-11-04", "evidence":[{"url":"https://primary.source/","supports":"specific supported fact"}],"files_inspected":[],"limitations":[]},
  "ml_tasks": [],
  "cell_specificity": {"evidence":"direct_multi_context|context_only|mechanistic_sensor|none|unknown","notes":"What can actually be inferred"},
  "integration_caveats": [],
  "related_model_ids": [],
  "related_resource_ids": [],
  "priority": "high|medium|context",
  "status": "curated|candidate|blocked"
}
```

Do not fill unavailable details from memory. Exact quantitative scale, labels, licenses and accessions require primary evidence. `metadata` means metadata was actually inspected, not that the dataset is usable or correctly processed. File samples establish only their observed schema/content. `file_sample` does not mean every file was validated.

`source_urls` and `verification.evidence` should support a record's claims. Where source and paper disagree, preserve both statements in `verification.limitations`. Use `unknown` or null when appropriate. Keep natural modification mapping distinct from experiments comparing chemically modified synthetic mRNA. Do not label mammalian specificity for a bacterial switch assay.

Use one `catalog/fragments/<topic>.json` array per assigned curator. Record a manageable, genuinely investigated collection rather than padding the count with unvisited candidates. A candidate is allowed but stays clearly unverified and outside curated-source counts.
