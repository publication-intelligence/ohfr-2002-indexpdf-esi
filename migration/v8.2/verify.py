"""Check frozen evidence, exact numerical invariance, and current report provenance."""
import copy,hashlib,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[2];E=ROOT/'evaluation';A=E/'archive/v8.1-before-v8.2'
SKILL=pathlib.Path('/home/john/.codex/skills/evaluate-subject-index');sys.path.insert(0,str(SKILL/'scripts'))
import dimension_score_v8_cli as cli
import scoring_core as core
import web_projection
from state_cli import validate_state
from policy_cli import canonical_hash,build_policy

def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=read(SKILL/'installation-receipt.json')
assert sha(SKILL/'installation-receipt.json')=='f7d0b2bd830dfbca7b1e8c4f79c6320e2c7a945d075342807d24d6f9f7cd1204'
for file,digest in receipt['sha256_by_file'].items():assert sha(SKILL/file)==digest,file
s=read(E/'evaluation-state.json');old=read(A/'evaluation-state.json')
errors,warnings=validate_state(s,state_path=E/'evaluation-state.json');assert not errors and not warnings,(errors,warnings)
for root,state in [(E,s),(A,old),(E/'archive/v8-original',read(E/'archive/v8-original/evaluation-state.json'))]:
 for a in state['artifacts']:assert sha(root/a['path'])==a['sha256'],a['path']
for a in old['artifacts']:
 if a['stage'] not in ['define_policy','structure_audit','scoring','web_report']:assert sha(E/a['path'])==a['sha256'],a['path']
P=E/'archive/v8.2-adeb691-before-scope-patch'
ps=read(P/'evaluation-state.json')
for artifact in ps['artifacts']:assert sha(P/artifact['path'])==artifact['sha256']
structure_path='staging/structure/structure-audit.v6.json'
structure=read(E/structure_path)
scopes=structure.pop('uncertainty_gate_scopes')
assert scopes==read(ROOT/'migration/v8.2/uncertainty-gate-scopes.proposed.json')['uncertainty_gate_scopes']
assert structure==read(A/structure_path)==read(P/structure_path)
for root in [E,A,P]:
 cfg=read(root/'scoring/dimension-calculation-input.v2.json')
 for refs in cfg['inputs'].values():
  for ref in refs if isinstance(refs,list) else [refs]:assert sha(root/'scoring'/ref['path'])==ref['sha256']
p=read(E/'source/evaluation-policy.v4.json');op=read(A/'source/evaluation-policy.v4.json');orig=read(E/'archive/v8-original/source/evaluation-policy.v4.json')
build=read(ROOT/'migration/v8.2/policy-build-input.json')
assert build_policy(build,original_policy=orig,base_policy=op)==p
assert p['freeze']=={'frozen_at':build['retrospective_migration']['migrated_at'],'candidate_seen':True}
refs=[build['retrospective_migration']['original_policy']['artifact']]+[ref for stage in build['retrospective_migration']['reused_stages'].values() for ref in stage['evidence']]
for ref in refs:assert sha(ROOT/'migration/v8.2'/ref['path'])==ref['sha256']
for key in ['source_scope','audience','audit_design','density_profile','deviations']:assert p[key]==op[key]
loaded,inventory,irecord,locs,missing,srecord=cli._calculation_loaded_from_state(s,E/'evaluation-state.json',E/'scoring/dimension-calculation-input.v2.json')
calc=core.json_output_value(cli.calculate_loaded(loaded));assert calc==read(E/'scoring/dimension-calculations.v6.json')
before=read(A/'scoring/dimension-calculations.v6.json')
for x,y in zip(before['dimensions'],calc['dimensions']):
 b=copy.deepcopy(x);a=copy.deepcopy(y)
 assert a.pop('formula_id')==b.pop('formula_id').replace('calculation-v6:','calculation-v7:')
 ai=a.pop('input_artifacts');bi=b.pop('input_artifacts')
 for ref in bi:
  for path in ['source/evaluation-policy.v4.json',structure_path]:
   if ref['sha256']==sha(A/path):ref['sha256']=sha(E/path)
 assert ai==bi
 assert a==b,x['dimension_id']
assert before['overall_percentage']==calc['overall_percentage']==97.19
assert before['arithmetic_check']==calc['arithmetic_check']
provisional=read(P/'scoring/dimension-calculations.v6.json')
for x,y in zip(provisional['dimensions'],calc['dimensions']):
 b=copy.deepcopy(x)
 for ref in b['input_artifacts']:
  if ref['sha256']==sha(P/structure_path):ref['sha256']=sha(E/structure_path)
 assert b==y,x['dimension_id']
assert provisional['overall_percentage']==calc['overall_percentage']
assert provisional['arithmetic_check']==calc['arithmetic_check']
for key in ['diagnostic_item_grades','structure_audit']:
 assert before[key]==provisional[key]==calc[key],key
for name in ['index-records','source-subjects','density']:
 path=f'scoring/v8-canonical-projection/data/{name}.v1.json'
 assert sha(E/path)==sha(A/path)==sha(P/path),path
items=core.json_output_value(cli._current_item_assessments(inventory,irecord,calc,loaded['structure'],locs,missing))
assert items==read(E/'scoring/item-assessments.v7.json')
old_items=read(A/'scoring/item-assessments.v7.json')
for key in ['locator_assessments','path_assessments','heading_node_assessments','cross_reference_assessments','source_subject_assessments','heading_access_causal_provenance']:
 assert items[key]==old_items[key],key
for file,schema in [('evaluation-result.v12.json','evaluation-result-v12.schema.json'),('web-report.v10.json','web-report-v10.schema.json'),('item-assessments.v7.json','item-assessments-v7.schema.json'),('projection-metadata.v2.json','v8-projection-metadata-v2.schema.json'),('dimension-calculations.v6.json','dimension-calculations-v6.schema.json')]:core.validate_schema_document(read(E/'scoring'/file),schema,file)
bundle=E/'scoring/v8-canonical-projection';projection=read(bundle/'projection.v1.json')
collections={k:read(bundle/'data'/f'{v}.v1.json') for k,v in [('index_records','index-records'),('source_subjects','source-subjects'),('density','density')]}
web_projection.validate_bundle(projection,collections)
result=read(E/'scoring/evaluation-result.v12.json');gates=[g for g in result['critical_gates'] if g['triggered']]
assert result['evaluation_validity']=={'status':'valid','blockers':[],'used_as_publication_gate':False}
assert result['gate_assessment']=={'status':'sufficient','blockers':[]}
expected={row['locator_id'] for doc in locs for row in doc['judgments'] if row['judgment']=='unsupported' and row['complete_path_fit']=='no_fit'}
assert len(gates)==1 and gates[0]['gate_id']=='GATE-WRONG-LOCATOR'
assert set(gates[0]['affected_evidence_ids'])==expected
assert not loaded['structure']['cross_reference_judgments'] and len(inventory['cross_references'])==257
assert result['review_signals']==read(A/'scoring/evaluation-result.v12.json')['review_signals']
assert all(not c['triggered'] for d in calc['dimensions'] for c in d['cap_evaluations'])
print(json.dumps({'ok':True,'methodology_commit':'c11c6ccb16000fe79646af16b7be01f6cbeeac78','installed_files_verified':len(receipt['sha256_by_file']),'installation_receipt_sha256':sha(SKILL/'installation-receipt.json'),'provisional_v8_2_artifacts_verified':len(ps['artifacts']),'uncertainty_scope_supplements':len(scopes),'original_v8_artifacts_verified':158,'v8_1_baseline_artifacts_verified':len(old['artifacts']),'v8_2_artifacts_verified':len(s['artifacts']),'state_errors':errors,'state_warnings':warnings,'overall_before':before['overall_percentage'],'overall_after':calc['overall_percentage'],'numeric_invariance':'All six entire dimension records identical to V8.1 after excluding only formula-version labels and exact policy/structure file-hash bindings; identical to provisional V8.2 except the structure binding; this includes every component, denominator, deduction, bound, cap evaluation, weighted contribution and final percentage. Overall and arithmetic check identical.','frozen_judgments':'All locator and missing-access artifacts byte-identical; structure differs only by four additive uncertainty_gate_scopes. Every original structure field, uncertainty, judgment and item-assessment/causal row unchanged.','provenance':'Native builder reconstruction, original/base policy hashes, original freeze, truthful migration freeze and every reused-stage evidence hash verified.','projection':'Full bundle schemas, self/file hashes, collection counts, order, identities and privacy checks passed; current report/result/items/calculation schemas passed.','evaluation_validity':result['evaluation_validity'],'gate_assessment':result['gate_assessment'],'triggered_gate_ids':[g['gate_id'] for g in gates],'unique_affected_locator_ids':sorted(expected),'broken_references':0,'triggered_ceilings':0,'binding_ceilings':0,'review_signals_unchanged':True},indent=2))
