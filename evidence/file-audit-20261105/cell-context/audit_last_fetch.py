from audit_fetch import *
jobs={
 'postar3_ALKBH1.binding.sites.zip':'http://111.198.139.65/download/human_RBP/ALKBH1.binding.sites.zip',
 'postar3_help.html':'http://111.198.139.65/help.php',
 'ENCFF335XEM.tsv':'https://www.encodeproject.org/files/ENCFF335XEM/@@download/ENCFF335XEM.tsv',
 'encode_eclip_real_experiment.json':'https://www.encodeproject.org/experiments/ENCSR720BJU/?format=json',
 'encode_knockdown_experiment.json':'https://www.encodeproject.org/experiments/ENCSR067LLB/?format=json',
 'encode_data_policy.html':'https://www.encodeproject.org/help/data-use-policy/'
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    for r in ex.map(lambda kv:fetch(*kv,cap=100_000_000),jobs.items()): print(json.dumps(r),flush=True)
