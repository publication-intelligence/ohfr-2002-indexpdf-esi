# OHFR 2002 — IndexPDF subject-index evaluation

This repository is prepared to evaluate the forthcoming IndexPDF subject index for *The Oxford History of the French Revolution* (2002) with the current `evaluate-subject-index` V8 workflow.

## Current state

The candidate-blind benchmark is frozen and the exact 425-page source has been reconnected. The canonical state is [`evaluation/evaluation-state.json`](evaluation/evaluation-state.json); its next stage is `candidate_normalization`.

The imported benchmark retains evaluation ID `ohfr-2002-original-published-index-v8`. That identity is intentionally unchanged because it is embedded in the frozen benchmark. The IndexPDF artifact receives its own candidate ID during normalization.

The checkpoint's scoring identity was advanced from calculation profile V4 to V5, as required by the current V8 runtime. The benchmark, policy, page map, chunk manifest, and candidate-blind judgments were not changed. A retired source-chunk inventory record was removed because the current `split-pdf` command no longer creates or consumes that artifact.

Private source, benchmark, evidence, candidate, and checkpoint artifacts are ignored by Git; only canonical control state and eventual public reports are eligible for version control. `evaluation-state.json` is the only control inventory; do not add another manifest or benchmark lock.

## Runtime

Use the installed skill as the runtime rather than copying its scripts into this repository:

```bash
source .venv/bin/activate
export ESI_SKILL="$HOME/.codex/skills/evaluate-subject-index"

python "$ESI_SKILL/scripts/state_cli.py" validate \
  --state evaluation/evaluation-state.json
python "$ESI_SKILL/scripts/state_cli.py" next \
  --state evaluation/evaluation-state.json
```

The local virtual environment contains the dependencies required by the current skill. To recreate it:

```bash
uv venv .venv
uv pip install --python .venv/bin/python \
  -r ../evaluate-subject-index/requirements.txt
```

## When the IndexPDF candidate arrives

Place the exact candidate at `evaluation/candidate/restricted/ohfr-2002-indexpdf.pdf` and convert it mechanically to the published `candidate-layout-extraction-v1` contract. The adjacent methodology checkout currently provides the converter:

```bash
mkdir -p evaluation/candidate/preparation
python ../evaluate-subject-index/utilities/subject_index_converter.py \
  --candidate-id ohfr-2002-indexpdf \
  --input evaluation/candidate/restricted/ohfr-2002-indexpdf.pdf \
  --source-sha256 5f89aa2592218983c594278bfd86cc1e4b74be1dd6dd8aac5c2610a48fa34047 \
  --output evaluation/candidate/preparation/candidate-layout-extraction.v1.json
```

Then run the current preparation sequence:

```bash
python "$ESI_SKILL/scripts/candidate_preparation_cli.py" normalize \
  --candidate-id ohfr-2002-indexpdf \
  --candidate-file evaluation/candidate/restricted/ohfr-2002-indexpdf.pdf \
  --state evaluation/evaluation-state.json \
  --page-map evaluation/source/page-map.json \
  --chunk-manifest evaluation/source/chunk-manifest.json \
  --policy evaluation/source/evaluation-policy.v4.json \
  --source-edition 2002 \
  --layout evaluation/candidate/preparation/candidate-layout-extraction.v1.json \
  --output-dir evaluation/candidate/preparation/normalized
```

If normalization writes an issues report, disposition every issue before continuing. Next run `validate-private`, then `register` with `evaluation/source/source-benchmark.v2.json`, and finally `page_chunk_cli.py prepare-locator-chunks`. Use `state_cli.py next` after each transition rather than maintaining workflow state by hand.
