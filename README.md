# OHFR 2002 — IndexPDF subject-index evaluation

This repository evaluates IndexPDF’s delivered subject-index Markdown export for *The Oxford History of the French Revolution* (2002) using the current Evaluate Subject Index V8 workflow.

The single canonical workflow state and artifact inventory is [`evaluation/evaluation-state.json`](evaluation/evaluation-state.json). The evaluation ID is `ohfr-2002-indexpdf-v8`. The source has 425 pages; front matter and endnotes absent from that supplied file are outside the available source.

## Current milestone

The exact source, page map, 17 previously approved chapter chunks, and frozen V8 policy have been verified and registered. All 425 source pages have exactly one chunk owner. An independent candidate-blind compatibility review selected the existing native V8 benchmark (638 subjects, 281 relationships, 638 reader tasks); discovery and full editorial review are not being repeated.

The independently approved native V8 benchmark is now registered through the reviewed-legacy compatibility workflow. Only approved evaluation-wrapper identities changed; source judgments, stable IDs, and policy are unchanged. The older benchmark repository release has different policy semantics and denominators and was not substituted.

The delivered Markdown remains byte-preserved. Evaluator PRs [33](https://github.com/publication-intelligence/evaluate-subject-index/pull/33) and [34](https://github.com/publication-intelligence/evaluate-subject-index/pull/34) are merged. Reviewed fixes cover structure path identities ([35](https://github.com/publication-intelligence/evaluate-subject-index/pull/35)), faithful cross-reference resolution ([36](https://github.com/publication-intelligence/evaluate-subject-index/pull/36)), density projection ([37](https://github.com/publication-intelligence/evaluate-subject-index/pull/37)), gate predicates ([38](https://github.com/publication-intelligence/evaluate-subject-index/pull/38)), generic consumer fields ([39](https://github.com/publication-intelligence/evaluate-subject-index/pull/39)), typed complete-bundle replacement ([40](https://github.com/publication-intelligence/evaluate-subject-index/pull/40)), and public metadata ([41](https://github.com/publication-intelligence/evaluate-subject-index/pull/41)). They were independently inspected and tested together before use. The user merged all evaluator PRs, including privacy support in [42](https://github.com/publication-intelligence/evaluate-subject-index/pull/42). PRs 39 and 42 merged into their feature-branch bases; [PR 43](https://github.com/publication-intelligence/evaluate-subject-index/pull/43) carries those changes to `main` and preserves nested source-uncertainty IDs. The installed skill exactly matches its reviewed head `c991281187f3075f1105a5c11e639da2c52f3d03`; all 124 coordinator evaluator tests pass. No PR was merged by the coordinator.

The candidate passed complete private validation: 2,548 records/paths, 2,812 displayed locators, 4,273 atomic assignments, and 257 cross-references. All 17 frozen locator packets collectively cover every assignment exactly once. All locator audits are complete and registered: 4,253 supported, 13 partially supported, 7 unsupported, and zero uninspectable assignments. Missing-access worksets cover 638 subjects, 638 reader tasks, and 1,569 coalesced expected treatments exactly once. All missing-access audits are complete and registered after independent semantic calibration: 1,514 treatments found and 55 missed; 592 reader tasks succeed, 33 partly succeed, and 13 fail.

Structure is registered with 2,292 heading nodes, 1,781 locator-bearing paths, 14 node exceptions, and 16 grouped defects. Ten locator lists triggered architectural review; three have confirmed subdivision defects. All 257 delivered cross-references are supported. The deterministic score is **95.60/100**, with three critical gates triggered. The regenerated report and public bundle pass canonical validation, all four existing website collection parsers, scoring-byte preservation, and source-overlap checks. Independent closure review and the generic website adapter fix are in progress; this is not a final release yet.

## Runtime and privacy

Use the installed skill and this project’s virtual environment:

```bash
.venv/bin/python /home/john/.codex/skills/evaluate-subject-index/scripts/state_cli.py validate --state evaluation/evaluation-state.json
.venv/bin/python /home/john/.codex/skills/evaluate-subject-index/scripts/state_cli.py next --state evaluation/evaluation-state.json
```

Restricted source, candidate, evidence, layout, and checkpoints are ignored by Git. Public reports will be emitted only through the evaluator’s standard reporting command and validated for privacy and generic website compatibility. Do not add a second manifest or benchmark lock.

## Review limitations

The frozen density denominator is **195,346 words**, summed from historical discovery measurements with differing extraction and counting methods. Independent review reconciled all 17 chunk joins and reproduced the canonical calculation byte for byte. It identified three measurement limitations: CHUNK-012's count exceeds current raw extraction without a recorded method; CHUNK-001's count omitted an eligible map caption; CHUNK-015 included estimated map labels that locator review excludes. The frozen counts remain unchanged for comparability. A future correction would require a uniform recount of all 17 chunks, not isolated patches.

The benchmark's 1,577 evidence records become 1,569 expected treatments through documented coalescing by subject, page, and treatment class; no evidence identities are lost. Chapter-level locator-bearing path presences sum to 1,864 because 66 paths occur in multiple chunks; the global distinct denominator is 1,781.

The Directory economic-crisis first-lookup judgment remains explicitly uncertain at medium confidence. All its expected treatments are found; the judgment concerns navigation across five routes.

Website scope is the complete public bundle and a generic adapter compatibility fix. No new IndexPDF study route, merge, or deployment is authorized in this run.
