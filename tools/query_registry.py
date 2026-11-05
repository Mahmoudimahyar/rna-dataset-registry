from pathlib import Path
import argparse,json
p=argparse.ArgumentParser();p.add_argument('--topic');p.add_argument('--status',choices=['curated','candidate','blocked']);p.add_argument('--search');p.add_argument('--json',action='store_true');a=p.parse_args()
rows=json.loads((Path(__file__).resolve().parents[1]/'catalog/registry.json').read_text(encoding='utf-8'))['resources']
rows=[r for r in rows if (not a.topic or a.topic in r['topics']) and (not a.status or r['status']==a.status) and (not a.search or a.search.lower() in json.dumps(r,ensure_ascii=False).lower())]
if a.json:print(json.dumps(rows,ensure_ascii=False,indent=2))
else:
    for r in rows:print(r['id']+'\t'+r['name']+'\t'+r['status']+'\t'+r['verification']['level'])
    print(str(len(rows))+' resource records')
