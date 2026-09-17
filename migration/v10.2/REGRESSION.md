# PR64 policy-identity regression evidence

No evaluation was finalized from this diagnostic work.

## Direct-helper invocation that produced the V6 hash

Run from the repository root without an explicit semantic runtime profile:

```sh
python3 - <<'PY'
import json,sys
from copy import deepcopy
sys.path.insert(0,'/home/john/.codex/skills/evaluate-subject-index/scripts')
import v10_migration,study_comparison as s
from runtime_profile import identity
p=json.load(open('evaluation/evaluation/migration/v10-r2-final/release-policy.json'))
t=v10_migration.policy_content(p)
print('target',t['schema_version'],s.digest(t))
l=deepcopy(t)
l['schema_version']=identity('subject-index-evaluation-policy-v4',profile='v10')
print('legacy',l['schema_version'],s.digest(l))
print('lock',json.load(open('evaluation/evaluation/migration/v10-r2-final/study-benchmark-lock.v1.json'))['policy_semantic_sha256'])
PY
```

Inputs:

- installed evaluator receipt tested revision: `b55f27dc6a3a301224a3da67aa3afb3c15dcb109`
- installed runtime payload: `36508cd8d6f6f238803393b65edabb781daea7445b9f90cf178fa681f1bab8c3`
- source policy: `evaluation/evaluation/migration/v10-r2-final/release-policy.json`
- historical lock: `evaluation/evaluation/migration/v10-r2-final/study-benchmark-lock.v1.json`

Observed output:

```text
target subject-index-evaluation-policy-v6 6f0291ba3611cbdd94daed6d358ef27ee4605d824d8517216662fffab229fe5d
legacy subject-index-evaluation-policy-v6 6f0291ba3611cbdd94daed6d358ef27ee4605d824d8517216662fffab229fe5d
lock 7fea875a46370351481128234c15825225ac5cdabffb0f0bd22ea7adfb0d2beb
```

This was a direct helper import and did not activate the public semantic V10 CLI profile. It therefore demonstrates the bypass path, not the expected public-entry-point identity.

## Public CLI observations

The public command was:

```sh
python3 /home/john/.codex/skills/evaluate-subject-index/scripts/v10_cli.py score score \
  --state evaluation/evaluation-state.json \
  --output-dir scoring-v10.2
```

With the original decision-v1 lock and policy it stopped with `V10 target policy differs from the approved semantic amendment`. With the coordinated decision-v3 V7 policy/lock preparation it advanced past that check, then stopped on study-package binding and policy validation while the local preparation was still incomplete. No scoring artifacts were registered.
