from pathlib import Path
import hashlib,json,concurrent.futures,argparse
p=argparse.ArgumentParser();p.add_argument('--library',required=True);p.add_argument('--previous-inventory',required=True);a=p.parse_args()
B=Path(__file__).resolve().parents[1];root=Path(a.library)
excluded={'output','outputs','tmp','versions','__MACOSX','rna-dataset-registry'}
files=[f for f in root.rglob('*.pdf') if not any(q in excluded for q in f.relative_to(root).parts)]
def digest(f):
    h=hashlib.sha256()
    with f.open('rb') as z:
        for chunk in iter(lambda:z.read(1024*1024),b''):h.update(chunk)
    return dict(relative=str(f.relative_to(root)),sha256=h.hexdigest())
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(digest,files))
old=json.loads(Path(a.previous_inventory).read_text(encoding='utf-8'));known={r.get('sha256') for r in old}
new=[r for r in rows if r['sha256'] not in known]
summary=dict(checked_on='2026-11-05',source='User-provided RNA literature collection',source_pdf_files=len(rows),unique_pdf_byte_streams=len({r['sha256'] for r in rows}),duplicate_copies=len(rows)-len({r['sha256'] for r in rows}),new_unique_pdf_byte_streams_since_prior_review=len({r['sha256'] for r in new}),exclusions=sorted(excluded),limits='Hash inventory establishes corpus coverage, not scientific review or dataset completeness.')
(B/'evidence/library_snapshot.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
private=B/'evidence/private';private.mkdir(exist_ok=True)
(private/'library_hash_inventory.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
(private/'new_library_files.json').write_text(json.dumps(new,indent=2),encoding='utf-8')
print(json.dumps(summary));print('New PDFs:',json.dumps(new))
