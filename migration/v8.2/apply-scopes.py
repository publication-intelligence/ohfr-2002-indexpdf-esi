"""Preserve the provisional checkpoint and reopen only the scope/hash cascade."""
import datetime
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[2]
E = ROOT / 'evaluation'
ARCHIVE = E / 'archive/v8.2-adeb691-before-scope-patch'
RECEIPT = Path('/home/john/.codex/skills/evaluate-subject-index/installation-receipt.json')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_text())

def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

assert sha(RECEIPT) == 'f7d0b2bd830dfbca7b1e8c4f79c6320e2c7a945d075342807d24d6f9f7cd1204'
for name, digest in read(RECEIPT)['sha256_by_file'].items():
    assert sha(RECEIPT.parent / name) == digest, name
checkpoint = E / 'exports/indexpdf-v8.2-frozen.private-complete.zip'
assert sha(checkpoint) == 'a3b5fa30f66c5829ed076483b21bd83a695eed695fff1ce559e59c17ac5741a5'
assert not ARCHIVE.exists(), 'One-shot migration already started; inspect before resuming.'
with zipfile.ZipFile(checkpoint) as archive:
    for name in archive.namelist():
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
    archive.extractall(ARCHIVE)
state = read(E / 'evaluation-state.json')
assert sha(E / 'evaluation-state.json') == sha(ARCHIVE / 'evaluation-state.json')
for artifact in state['artifacts']:
    assert sha(E / artifact['path']) == sha(ARCHIVE / artifact['path']) == artifact['sha256']
proposal = read(ROOT / 'migration/v8.2/uncertainty-gate-scopes.proposed.json')
structure_path = ROOT / proposal['frozen_structure_artifact']
assert sha(structure_path) == proposal['frozen_structure_sha256']
structure = read(structure_path)
assert 'uncertainty_gate_scopes' not in structure
structure['uncertainty_gate_scopes'] = proposal['uncertainty_gate_scopes']
write(structure_path, structure)
kept = []
for artifact in state['artifacts']:
    if artifact['stage'] in ['scoring', 'web_report']:
        (E / artifact['path']).unlink()
    elif artifact['stage'] != 'structure_audit':
        kept.append(artifact)
state['artifacts'] = kept
for stage in ['structure_audit', 'scoring', 'web_report']:
    state['stages'][stage]['status'] = 'not_started'
for path in [E / 'scoring/v8-canonical-projection/data', E / 'scoring/v8-canonical-projection']:
    path.rmdir()
state['stages']['structure_audit']['notes'].append(
    'Authorized c11c6ccb V8.2 patch: added four evidence-backed uncertainty gate scopes only; '
    'all original uncertainty records, judgments, and denominators preserved. No audit rerun. '
    'Provisional adeb691 state and every artifact preserved in archive/v8.2-adeb691-before-scope-patch.'
)
state['updated_at'] = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
write(E / 'evaluation-state.json', state)
print('Preserved all 158 provisional artifacts; prepared additive scopes for registered rebuild.')
