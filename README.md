# OHFR 2002 — IndexPDF subject-index evaluation

This repository evaluates IndexPDF’s delivered subject-index Markdown export for *The Oxford History of the French Revolution* (2002) using the current Evaluate Subject Index V8 workflow.

The single canonical workflow state and artifact inventory is [`evaluation/evaluation-state.json`](evaluation/evaluation-state.json). The evaluation ID is `ohfr-2002-indexpdf-v8`. The source has 425 pages; front matter and endnotes absent from that supplied file are outside the available source.

## Current milestone

The exact source, page map, 17 previously approved chapter chunks, and frozen V8 policy have been verified and registered. All 425 source pages have exactly one chunk owner. An independent candidate-blind compatibility review selected the existing native V8 benchmark (638 subjects, 281 relationships, 638 reader tasks); discovery and full editorial review are not being repeated.

The independently approved native V8 benchmark is now registered through the reviewed-legacy compatibility workflow. Only approved evaluation-wrapper identities changed; source judgments, stable IDs, and policy are unchanged. The older benchmark repository release has different policy semantics and denominators and was not substituted.

The delivered Markdown remains byte-preserved. Merged evaluator [PR #33](https://github.com/publication-intelligence/evaluate-subject-index/pull/33) corrects five heading qualifiers incorrectly parsed as locators; merged [PR #34](https://github.com/publication-intelligence/evaluate-subject-index/pull/34) supports exact native V8 benchmark reuse. Reviewed evaluator [PR #35](https://github.com/publication-intelligence/evaluate-subject-index/pull/35) corrects structure registration for separate records sharing one heading path. The installed runtime matches its tested commit `9246f075c40e735048f7f6d9445732332a64f734`; 105 evaluator and 20 converter tests passed.

The candidate passed complete private validation: 2,548 records/paths, 2,812 displayed locators, 4,273 atomic assignments, and 257 cross-references. All 17 frozen locator packets collectively cover every assignment exactly once. All locator audits are complete and registered: 4,253 supported, 13 partially supported, 7 unsupported, and zero uninspectable assignments. Missing-access worksets cover 638 subjects, 638 reader tasks, and 1,569 coalesced expected treatments exactly once. Missing-access audits are under coordinator and independent calibration review; structure, scoring, and reporting remain pending. No score is claimed yet.

## Runtime and privacy

Use the installed skill and this project’s virtual environment:

```bash
.venv/bin/python /home/john/.codex/skills/evaluate-subject-index/scripts/state_cli.py validate --state evaluation/evaluation-state.json
.venv/bin/python /home/john/.codex/skills/evaluate-subject-index/scripts/state_cli.py next --state evaluation/evaluation-state.json
```

Restricted source, candidate, evidence, layout, and checkpoints are ignored by Git. Public reports will be emitted only through the evaluator’s standard reporting command and validated for privacy and generic website compatibility. Do not add a second manifest or benchmark lock.
