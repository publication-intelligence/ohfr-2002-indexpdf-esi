"""Reopen only derived stages after building the new policy; typed commands finish them."""
import hashlib,json,pathlib,datetime
E=pathlib.Path(__file__).resolve().parents[2]/'evaluation'
s=json.loads((E/'evaluation-state.json').read_text());assert s['configuration']['policy_profile']=='subject-index-standard-policy-v8.1'
p=json.loads((E/'source/evaluation-policy.v4.json').read_text());assert p['policy_profile']['id']=='subject-index-standard-policy-v8.2'
assert p['freeze']['candidate_seen'] and 'retrospective_migration' in p
s['configuration'].update(policy_profile='subject-index-standard-policy-v8.2',rubric_version='subject-index-rubric-v8.2',scoring_identity={'rubric_version':'subject-index-rubric-v8.2','dimension_calculation_profile':'subject-index-dimension-calculation-v7'})
kept=[]
for a in s['artifacts']:
 if a['stage'] in ['scoring','web_report']:(E/a['path']).unlink()
 else:
  if a['stage']=='define_policy':a['sha256']=hashlib.sha256((E/a['path']).read_bytes()).hexdigest()
  kept.append(a)
s['artifacts']=kept
for stage in ['scoring','web_report']:s['stages'][stage]['status']='not_started'
for p in [E/'scoring/v8-canonical-projection/data',E/'scoring/v8-canonical-projection']:p.rmdir()
s['stages']['define_policy']['notes'].append('Authorized combined V8.2 migration: native retrospective_migration preserves original candidate-blind policy and truthful current visibility; latest V8.1 scoring settings retained. Six no-fit locator findings remain frozen. All 257 reference passes and the complete structure audit are reused without target-resolution edits. No discovery, review, normalization or audits rerun.')
s['updated_at']=datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
(E/'evaluation-state.json').write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n')
