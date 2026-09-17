"""Prepare only the authorized V8.2 metadata transition from the verified checkpoint."""
import datetime, hashlib, json, os, pathlib, zipfile
ROOT=pathlib.Path(__file__).resolve().parents[2]
E=ROOT/'evaluation'; HERE=pathlib.Path(__file__).resolve().parent
SNAP=E/'archive/v8.1-before-v8.2'
ZIP=pathlib.Path('/home/john/Development/evaluate-subject-index-repos/ohfr-2002-indexpdf-esi/evaluation/exports/indexpdf-v8.1-frozen.private-complete.zip')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
assert sha(ZIP)=='5323b2877227600d51969c678d6e48b6e5a3931f0f59e23e443db44a5eeffe3b'
assert not SNAP.exists(),'Never overwrite the preserved baseline'
with zipfile.ZipFile(ZIP) as z:
 state_bytes=z.read('evaluation-state.json');s=json.loads(state_bytes)
 assert state_bytes==(E/'evaluation-state.json').read_bytes()
 for a in s['artifacts']:
  p=pathlib.Path(a['path']);assert not p.is_absolute() and '..' not in p.parts
  data=z.read(a['path']);assert hashlib.sha256(data).hexdigest()==a['sha256']==sha(E/p),str(p)
  q=SNAP/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data)
 (SNAP/'evaluation-state.json').write_bytes(state_bytes)
original=E/'archive/v8-original/source/evaluation-policy.v4.json';o=read(original)
p=read(SNAP/'source/evaluation-policy.v4.json')
def ref(path):return {'path':os.path.relpath(path,HERE),'sha256':sha(path)}
stages=['page_mapping','chunk_definition','source_subject_discovery','benchmark_synthesis','benchmark_review','benchmark_freeze','candidate_normalization','source_chunk_preparation','locator_chunk_preparation','locator_audit','missing_access_audit','structure_audit']
reused={stage:{'rerun':False,'evidence':[ref(SNAP/a['path']) for a in s['artifacts'] if a['stage']==stage]} for stage in stages}
assert all(v['evidence'] for v in reused.values())
build={'schema_version':'subject-index-policy-build-input-v1','policy_id':'ohfr-2002-indexpdf-v8.2-retrospective-policy','source_scope':p['source_scope'],'audience':p['audience'],'audit_design':p['audit_design'],'deviations':p['deviations'],'retrospective_migration':{'original_policy':{'policy_id':o['policy_id'],'policy_profile_id':o['policy_profile']['id'],'policy_sha256':o['policy_sha256'],'artifact':ref(original),'freeze':o['freeze']},'migrated_at':datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'),'candidate_seen':True,'authorization':{'authorized_by':'user, dispatched through the Published OHFR coordinating task','reference':'migration/v8.2/AUTHORIZATION.md'},'change_ledger_reference':'migration/v8.2/change-ledger.json','reused_stages':reused}}
write(HERE/'policy-build-input.json',build)
print('Verified durable V8.1 checkpoint restored as separate archive; live state exactly matches all 158 registered inputs. Build input ready.')
