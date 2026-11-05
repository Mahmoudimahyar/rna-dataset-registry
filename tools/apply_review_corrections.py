"""Apply recorded scientific-review precision corrections to curator fragments."""
from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
for name in ['trna.json','modifications.json']:
    f=B/'catalog/fragments'/name;rows=json.loads(f.read_text(encoding='utf-8'))
    for r in rows:
        if r['id']=='brain-trna-poliii-ribotag-study':
            for l in r['labels']:
                if l['name']=='Pol III occupancy':l['resolution']='interval'
        if r['id']=='gtrnadb':
            r['labels']=[l for l in r['labels'] if l['name']!='isotype / anticodon / score']+[
                dict(name='isotype / anticodon',meaning='Predicted tRNA gene identity annotation',label_type='annotation',unit='category',resolution='interval'),
                dict(name='tRNAscan-SE confidence score',meaning='Computed confidence score for the predicted gene',label_type='computed',unit='source score',resolution='interval')]
        if r['id']=='charge-trnaseq-zenodo10778311':r['verification']['limitations']=[x.replace('Concept URL 8200906','Cited identifier 8200906') for x in r['verification']['limitations']]
        if r['id']=='m5c-atlas':
            for l in r['labels']:
                if l['name']=='m5C site':l['meaning']='Candidate site annotation from base-resolution assay sources; enrichment-only intervals are separate.'
            if not any(l['name']=='m5C enrichment interval' for l in r['labels']):r['labels'].append(dict(name='m5C enrichment interval',meaning='MeRIP/enrichment-based interval; cannot be treated as a resolved single-base call without supporting evidence',label_type='computed',unit='source enrichment/support',resolution='interval'))
            note='The integrated assay collection includes enrichment measurements; preserve interval versus base resolution and do not assign every source a single-position label.'
            if note not in r['integration_caveats']:r['integration_caveats'].append(note)
        if r['id']=='sample2019-chemistry-reporters':r['related_model_ids']=list(dict.fromkeys(r['related_model_ids']+['P002','P006','P007','P012','P018','P019']))
    f.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('Applied precision corrections; no evidence level promoted.')
