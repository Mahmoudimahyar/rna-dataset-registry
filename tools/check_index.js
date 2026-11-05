// Exercise the actual offline index script with a small DOM simulation.
// This checks behavior and escaping, not browser layout or visual rendering.
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const payload=html.match(/<script id="registry" type="application\/json">([\s\S]*?)<\/script>/)[1];
const script=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].at(-1)[1];
const data=JSON.parse(payload),summary=JSON.parse(fs.readFileSync(path.join(root,'catalog/summary.json'),'utf8'));
class Element{constructor(){this.value='';this.innerHTML='';this.textContent='';this.disabled=false;this.children=[];this.classList={add(){},remove(){}};}appendChild(e){this.children.push(e);}}
const elements={};for(const id of ['registry','search','status','topic','level','results','stats','count','resourcesBtn','modelsBtn'])elements[id]=new Element();
elements.registry.textContent=payload;elements.status.value='curated';
const context=vm.createContext({document:{getElementById:id=>{assert.ok(elements[id],id);return elements[id]},createElement:()=>new Element()},console});
vm.runInContext(script,context);
assert.equal(elements.count.textContent,summary.curated_records+' resource records shown');
assert.equal((elements.results.innerHTML.match(/class="card"/g)||[]).length,summary.curated_records);
elements.search.value='GSE227927';elements.search.oninput();
assert.equal(elements.count.textContent,'1 resource records shown');assert.match(elements.results.innerHTML,/human-differentiation-gse227927/);
elements.search.value='';elements.status.value='candidate';elements.status.onchange();assert.equal(elements.count.textContent,summary.candidate_records+' resource records shown');
elements.modelsBtn.onclick();assert.equal(elements.count.textContent,summary.model_family_records+' model/family records shown');assert.equal(elements.status.disabled,true);
elements.search.value='PARADE';elements.search.oninput();assert.equal(elements.count.textContent,'1 model/family records shown');
assert.equal(vm.runInContext(`esc('<script>"&')`,context),'&lt;script&gt;&quot;&amp;');
for(const r of data.resources)assert.equal((r.source_urls||[]).some(u=>/^https?:\/\//.test(u)),true,r.id);
console.log('PASS: resource/model counts, accession search, candidate filter, model view, escaping and source URLs. Browser visual layout was not tested.');
