from audit_fetch import *
jobs={
 'ENCFF356YQN.tsv':'https://www.encodeproject.org/files/ENCFF356YQN/@@download/ENCFF356YQN.tsv',
 'ENCFF957CWU.tsv':'https://www.encodeproject.org/files/ENCFF957CWU/@@download/ENCFF957CWU.tsv',
 'encode_rbns_experiment.json':'https://www.encodeproject.org/experiments/ENCSR919USP/?format=json',
 'encode_eclip_experiment.json':'https://www.encodeproject.org/experiments/ENCSR846QXC/?format=json',
 'postar3_redirect_home.html':'http://111.198.139.65/',
 'postar3_redirect_download.html':'http://111.198.139.65/download.php',
 'mirtarbase_v11_http.csv':'http://awi.cuhk.edu.cn/miRTarBase/downloads/files/11.0/miRTarBase_MTI.csv',
 'mirtarbase_v10_http.xlsx':'http://mirtarbase.cuhk.edu.cn/~miRTarBase/miRTarBase_2025/cache/download/10.0/hsa_MTI.xlsx',
 'census_release_correct.json':'https://census.cellxgene.cziscience.com/cellxgene-census/v1/release.json',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for r in ex.map(lambda kv:fetch(*kv,cap=50_000_000),jobs.items()): print(json.dumps(r),flush=True)
