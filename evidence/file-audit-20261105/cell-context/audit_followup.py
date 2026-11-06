"""Actual biological downloads; inherits output and metadata CLI arguments."""
from audit_fetch import *
jobs={
 'hpa_rna_celline_v25.tsv.zip':'https://www.proteinatlas.org/download/tsv/rna_celline.tsv.zip',
 'depmap_Model_24Q4.csv':'https://ndownloader.figshare.com/files/51065297',
 'depmap_OmicsProfiles_24Q4.csv':'https://ndownloader.figshare.com/files/51065723',
 'depmap_Expression_24Q4.csv':'https://ndownloader.figshare.com/files/51065489',
 'encode_rbns_files.json':'https://www.encodeproject.org/search/?type=File&output_type=enrichment&format=json&limit=10',
 'encode_rbns_set.json':'https://www.encodeproject.org/publication-data/ENCSR876DCD/?format=json',
 'postar3_home.html':'https://postar.ncrnalab.org/',
 'postar3_home2.html':'http://postar.ncrnalab.org/POSTAR3/',
 'mirtarbase_human_v10.xlsx':'https://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/cache/download/10.0/hsa_MTI.xlsx',
 'mirtarbase_v11.csv':'https://awi.cuhk.edu.cn/miRTarBase/downloads/files/11.0/miRTarBase_MTI.csv',
 'mirtarbase_license.txt':'http://awi.cuhk.edu.cn/miRTarBase/downloads/files/LICENSE',
 'hpa_cell_metadata.html':'https://www.proteinatlas.org/humanproteome/cell+line/data',
 'hpa_license.html':'https://www.proteinatlas.org/about/licence',
 'census_release_directory.json':'https://census.cellxgene.cziscience.com/cell-census/v1/release.json',
}
for typ in ['eclip','knockdown']:
    data=json.loads((D/('encode_'+typ+'.json')).read_text())
    for f in data.get('@graph',[])[:2]: jobs[f['accession']+'.'+f['file_format']+('.gz' if f['href'].endswith('.gz') else '')]='https://www.encodeproject.org'+f['href']
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
    for r in ex.map(lambda kv:fetch(*kv,cap=600_000_000),jobs.items()): print(json.dumps(r),flush=True)
