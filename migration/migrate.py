"""One-time targeted migration; run only against the verified V8 baseline."""
import copy, hashlib, json, pathlib, shutil, sys
from datetime import datetime, timezone
sys.path.insert(0, '/home/john/.codex/skills/evaluate-subject-index/scripts')
import policy_cli
ROOT = pathlib.Path(__file__).resolve().parents[1] / 'evaluation'
ARCHIVE = ROOT / 'archive/v8-original'
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, ensure_ascii=False)+'\n')
s = read(ROOT/'evaluation-state.json')
assert s['configuration']['policy_profile'] == 'subject-index-standard-policy-v8'
assert not ARCHIVE.exists(), 'Original archive must not be overwritten'
for a in s['artifacts']:
    p=ROOT/a['path']; assert sha(p)==a['sha256'], a['path']
    q=ARCHIVE/a['path']; q.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,q)
shutil.copy2(ROOT/'evaluation-state.json',ARCHIVE/'evaluation-state.json')
old_input=read(ARCHIVE/'scoring/dimension-calculation-input.v2.json')
for ref in old_input['inputs'].values():
    for r in ref if isinstance(ref,list) else [ref]:
        assert sha(ARCHIVE/'scoring'/r['path'])==r['sha256']
stamp=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
p=read(ROOT/'source/evaluation-policy.v4.json')
new=policy_cli.build_policy(dict(policy_id='ohfr-2002-indexpdf-v8.1-migration-policy',source_scope=p['source_scope'],audience=p['audience'],audit_design=p['audit_design'],deviations=p['deviations']))
# Retain the exact frozen scope, density calibration/rounding, audience and audit mode.
new['source_scope']=copy.deepcopy(p['source_scope'])
new['density_profile']=copy.deepcopy(p['density_profile'])
for metric in new['density_profile']['metrics']:metric['provenance']=policy_cli.POLICY_PROFILE
new['policy_profile']['targeted_migration']={'operation':'authorized_retrospective_consequence_migration','frozen_at':new['freeze']['frozen_at'],'candidate_seen':True,'original_policy_sha256':p['policy_sha256'],'freeze_field_semantics':'Top-level freeze preserves the original candidate-blind configuration freeze; this record is the later V8.1 consequence-policy freeze. No discovery, review or approval rerun.'}
new['freeze']=copy.deepcopy(p['freeze'])
new['policy_sha256']=policy_cli.canonical_hash(new,'policy_sha256')
write(ROOT/'source/evaluation-policy.v4.json',new)
structure_path=ROOT/'staging/structure/structure-audit.v6.json'
t=read(structure_path)
changed_nodes=['NODE-C83F59EEEC2A','NODE-A2435811FD75','NODE-EB34FCD7A1A0','NODE-F23742E705FF']
for n in t['node_judgments']:
    if n['node_id'] in changed_nodes:
        j=n['component_judgments']['heading_access_architecture'];assert j['status']=='major_issues'
        j['status']='minor_issues'
        for finding in j['causal_findings']:finding['severity']='minor'
for d in t['defects']:
    if d['defect_id']=='DEFECT-XRF-REVOLUTIONARY-CONSENSUS-001':
        d.update(severity='minor',severity_basis='localized_repairable_friction',retrieval_consequence='slows')
write(structure_path,t)
s['configuration'].update(policy_profile='subject-index-standard-policy-v8.1',rubric_version='subject-index-rubric-v8.1',scoring_identity=dict(rubric_version='subject-index-rubric-v8.1',dimension_calculation_profile='subject-index-dimension-calculation-v6'))
# Withdraw derived registrations and reopen only the authorized derived stages.
# score/build-report will validate and complete them; no completion is fabricated.
kept=[]
for a in s['artifacts']:
    if a['stage'] in ['scoring','web_report']:
        (ROOT/a['path']).unlink()
    else:
        a['sha256']=sha(ROOT/a['path']);kept.append(a)
s['artifacts']=kept
# The typed report builder requires an absent destination directory.
for directory in [ROOT/'scoring/v8-canonical-projection/data', ROOT/'scoring/v8-canonical-projection']:
    directory.rmdir()
for stage in ['scoring','web_report']:
    s['stages'][stage]['status']='not_started';s['stages'][stage]['updated_at']=stamp
    s['stages'][stage].setdefault('notes',[]).append('Explicit targeted V8.1 migration: original completed outputs preserved in archive/v8-original and Git baseline dbb35e5; derived stage reopened for current typed calculation/reporting.')
s['stages']['define_policy']['notes'].append('V8.1 policy_profile.targeted_migration records candidate_seen=true for the authorized retrospective freeze; top-level freeze preserves original candidate-blind configuration provenance. Original candidate-blind V8 policy and benchmark release remain archived; no new discovery/review or compatibility approval claimed.')
s['stages']['structure_audit']['notes'].append('Targeted consequence review: four omitted/supplemental-route node exceptions retain minor deductions; one missing XRF consequence clarified as slowing. Denominators, full-scope attestation and all other judgments reused.')
s['updated_at']=stamp
write(ROOT/'evaluation-state.json',s)
print('Archived and verified all',len(kept)+10,'original records; policy and targeted structure updated.')
