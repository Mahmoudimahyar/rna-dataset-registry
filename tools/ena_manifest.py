"""Retrieve a public ENA run/file manifest, never sequence files.

Example: python tools/ena_manifest.py PRJNA522258 --output downloads/ena.json
An empty report is recorded as empty, not interpreted as proof of non-release.
"""
import argparse,urllib.request,urllib.parse,json,csv,io
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('accession');p.add_argument('--output',required=True);a=p.parse_args()
if not __import__('re').fullmatch(r'(?:PRJNA|PRJEB|SRP|ERP)\d+',a.accession):p.error('Use a study/BioProject accession')
fields='study_accession,sample_accession,run_accession,scientific_name,library_strategy,library_source,library_selection,fastq_ftp,fastq_md5,fastq_bytes'
url='https://www.ebi.ac.uk/ena/portal/api/filereport?'+urllib.parse.urlencode(dict(accession=a.accession,result='read_run',fields=fields,format='tsv',download='false'))
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'rna-dataset-registry-metadata/0.1'}),timeout=60) as f:text=f.read(20_000_000).decode('utf-8')
rows=list(csv.DictReader(io.StringIO(text),delimiter='\t'))
out=dict(accession=a.accession,source_url=url,runs=rows,sequence_files_downloaded=False,limits='Source-reported file metadata/checksums only; access, license and downloaded file integrity not validated.')
dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(str(len(rows))+' run metadata records; no sequence files downloaded')
