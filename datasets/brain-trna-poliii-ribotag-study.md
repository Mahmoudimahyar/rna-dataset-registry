# Brain cell-type Pol III atlas and RiboTag translatome study

Registry ID: `brain-trna-poliii-ribotag-study` · study · **curated** · verification: **metadata**

Cell-type tRNA transcription-occupancy atlas paired with RiboTag-associated mRNA sequencing; mature tRNA levels are inferred from Pol III occupancy rather than directly sequenced.

## What the data contains

- Observation unit: Pol III genomic occupancy or RiboTag-associated mRNA by population
- RNA scope: tRNA; mRNA
- Biological context: Mouse: 11 nervous-system cell types for Pol III ChIP; six RiboTag cell populations: cerebellar and dentate granule cells, layer V cortical neurons, inhibitory interneurons, astrocytes and microglia.
- Assays: conditional epitope-tagged Pol III ChIP-seq; RiboTag-associated mRNA-seq
- Accessions: GSE250090; GSE239759
- Scale: value: unknown; unit: unknown; basis: GSE250090 has 41 GEO records including inputs; GSE239759 has 22 sequencing records for 18 biological samples plus four repeat-sequenced samples; as_of: 2026-11-04

## Labels

| Label | Meaning | Evidence type | Unit | Resolution |
|---|---|---|---|---|
| Pol III occupancy | Gene-locus transcription proxy; not measured mature total tRNA abundance | computed | source enrichment/normalized signal | interval |
| RiboTag translatome counts | Ribosome-associated mRNA expression; not tRNA abundance | computed | source expression counts | transcript |
| cell type | Source Cre-defined cell population | annotation | unknown | sample |

## Access and reuse

- Access: open
- Formats: GEO SOFT metadata; TAR of processed files listed; not inspected
- Source license: unknown
- Redistribution: not established

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE250090&targ=self&form=text&view=quick
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE239759&targ=self&form=text&view=quick

## Verification and remaining gaps

Checked: 2026-11-04. Actual files/headers inspected: not established.

- No processed count/enrichment table inspected.

- GSE239759 alone is RiboTag mRNA, not a dedicated tRNA assay.
- Selected samples declare mm10 for ChIP and Gencode M24 transcripts for RiboTag. Occupancy cannot measure mature abundance or charging.

## Cell specificity

evidence: direct_multi_context; notes: Direct cell-population comparison of occupancy and translatome, with indirect tRNA abundance inference.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11065635/
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE250090&targ=self&form=text&view=quick
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE239759&targ=self&form=text&view=quick

- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE250090&targ=self&form=text&view=quick; supports: 41 ChIP/input records, 11 CNS cell types and whole-tissue controls; design labels
- url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE239759&targ=self&form=text&view=quick; supports: Six cell populations, three biological replicates each, four repeat sequencings; 22 listed records
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11065635/; supports: Paired assay interpretation and cell-specific tRNA-transcription atlas

Related models: not established. Related resources: gtrnadb.
