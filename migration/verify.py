"""Verify the bounded migration against its byte-preserved local archive."""
import hashlib, json, pathlib, sys
sys.path.insert(0, '/home/john/.codex/skills/evaluate-subject-index/scripts')
import dimension_score_v8_cli as cli
import scoring_core as core
import web_projection
from state_cli import validate_state
ROOT=pathlib.Path(__file__).resolve().parents[1]/'evaluation'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=read(ROOT/'evaluation-state.json'); old=read(ROOT/'archive/v8-original/evaluation-state.json')
errors,warnings=validate_state(s,state_path=ROOT/'evaluation-state.json');assert not errors and not warnings,(errors,warnings)
for a in old['artifacts']:assert sha(ROOT/'archive/v8-original'/a['path'])==a['sha256'],a['path']
for a in s['artifacts']:assert sha(ROOT/a['path'])==a['sha256'],a['path']
for version in [ROOT,ROOT/'archive/v8-original']:
    conf=read(version/'scoring/dimension-calculation-input.v2.json')
    for v in conf['inputs'].values():
        for ref in v if isinstance(v,list) else [v]:assert sha(version/'scoring'/ref['path'])==ref['sha256']
reused_stages={'initialize','page_mapping','chunk_definition','source_chunk_preparation','source_subject_discovery','benchmark_synthesis','benchmark_review','benchmark_freeze','candidate_normalization','locator_chunk_preparation','locator_audit','missing_access_audit'}
for a in old['artifacts']:
    if a['stage'] in reused_stages:assert sha(ROOT/a['path'])==a['sha256'],a['path']
loaded,inventory,irecord,locs,missing,srecord=cli._calculation_loaded_from_state(s,ROOT/'evaluation-state.json',ROOT/'scoring/dimension-calculation-input.v2.json')
calc=core.json_output_value(cli.calculate_loaded(loaded)); saved=read(ROOT/'scoring/dimension-calculations.v6.json');assert calc==saved,'deterministic calculation'
items=cli._current_item_assessments(inventory,irecord,calc,loaded['structure'],locs,missing)
assert core.json_output_value(items)==read(ROOT/'scoring/item-assessments.v7.json'),'item provenance'
for file,schema in [('evaluation-result.v12.json','evaluation-result-v12.schema.json'),('web-report.v10.json','web-report-v10.schema.json'),('item-assessments.v7.json','item-assessments-v7.schema.json'),('projection-metadata.v2.json','v8-projection-metadata-v2.schema.json'),('dimension-calculations.v6.json','dimension-calculations-v6.schema.json')]:core.validate_schema_document(read(ROOT/'scoring'/file),schema,file)
bundle=ROOT/'scoring/v8-canonical-projection';projection=read(bundle/'projection.v1.json')
collections={k:read(bundle/'data'/f'{v}.v1.json') for k,v in [('index_records','index-records'),('source_subjects','source-subjects'),('density','density')]}
web_projection.validate_bundle(projection,collections)
original=read(ROOT/'archive/v8-original/scoring/dimension-calculations.v6.json')
for before,after in zip(original['dimensions'],calc['dimensions']):
    if before['dimension_id']!='findability_navigation':assert before['post_cap_percentage']==after['post_cap_percentage']
result=read(ROOT/'scoring/evaluation-result.v12.json')
assert result['evaluation_validity']['status']=='valid'
assert all(not x['triggered'] for x in result['critical_gates'])
assert all(not x['triggered'] for d in calc['dimensions'] for x in d['cap_evaluations'])
assert calc['overall_percentage']==97.19
print(json.dumps({'ok':True,'original_registered_artifacts_verified':len(old['artifacts']),'current_registered_artifacts_verified':len(s['artifacts']),'state_errors':errors,'state_warnings':warnings,'checks':['Original and current exact calculation input hashes','Source, page map, chunks, benchmark release and all locator/missing audits byte-identical','Current audit schema and causal semantics','Deterministic full calculation reconstruction','Deterministic item assessment/provenance reconstruction','Current result, report, items, metadata and calculation schemas','Full projection/collection schemas, content/file hashes, counts, delivered order, locator/task joins and privacy checks','Five unaffected dimension percentages unchanged','Zero triggered ceilings and gates; valid evaluation']},indent=2))
