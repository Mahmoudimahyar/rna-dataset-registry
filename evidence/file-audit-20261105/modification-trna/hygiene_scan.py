"""Read-only publication-hygiene scan of audit JSON and Python files."""
import ast,json,pathlib,re,sys
root=pathlib.Path(__file__).resolve().parents[1]
findings=[];summaries=[]
pathpat=re.compile(r'(?<![A-Za-z0-9])[A-Z]:[\\/]|'+'file'+r'://|/(?:'+'Users'+r'|home)/',re.I)
credpat=re.compile(r'(?:[?&](?:token|signature|credential|api_key|password)=)[^&\s]+|(?:ghp_|github_pat_)[A-Za-z0-9_]{15,}|Bearer\s+[A-Za-z0-9_.-]{20,}',re.I)
seqpat=re.compile(r'(?<![A-Za-z])[ACGTUNRYKMSWBDHV-]{40,}(?![A-Za-z])',re.I)
def walk(v,path):
 if isinstance(v,dict):
  http=v.get('http_status',v.get('status'))
  if isinstance(http,int) and http>=400 and (v.get('parsed') is True or any(isinstance(v.get(k),int) and v[k]>0 for k in ['rows','data_rows'])):findings.append(dict(path=path,type='failed_http_with_positive_parse_claim'))
  if any(k in v for k in ['status','http_status','parsed','parse_status','data_rows','rows']):
   s={k:v[k] for k in ['status','http_status','parsed','parse_status','data_rows','rows','error'] if k in v and not isinstance(v[k],(dict,list))}
   if s:summaries.append(dict(path=path,fields=s))
  for k,x in v.items():walk(x,path+'.'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,path+f'[{i}]')
 elif isinstance(v,str):
  for label,pat in [('local_path',pathpat),('credential',credpat),('possible_sequence',seqpat)]:
   if pat.search(v):findings.append(dict(path=path,type=label))
for p in root.rglob('*'):
 if p.suffix not in {'.json','.py'}:continue
 rel=str(p.relative_to(root));t=p.read_text(encoding='utf-8-sig')
 try:
  if p.suffix=='.json':walk(json.loads(t),rel)
  else:
   tree=ast.parse(t)
   for node in ast.walk(tree):
    if isinstance(node,ast.Constant) and isinstance(node.value,str):walk(node.value,rel+':'+str(node.lineno))
 except Exception as e:findings.append(dict(path=rel,type='parse_error',detail=str(e)))
print(json.dumps(dict(files_checked=sum(p.suffix in {'.json','.py'} for p in root.rglob('*')),findings=findings,status_summary_records=len(summaries)),indent=2))
