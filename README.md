# OHFR 2002 — IndexPDF subject-index evaluation

This repository evaluates IndexPDF’s delivered subject-index Markdown export for *The Oxford History of the French Revolution* (2002) using the current Evaluate Subject Index V8 workflow.

The single canonical workflow state and artifact inventory is [`evaluation/evaluation-state.json`](evaluation/evaluation-state.json). The evaluation ID is `ohfr-2002-indexpdf-v8`. The source has 425 pages; front matter and endnotes absent from that supplied file are outside the available source.

## Current milestone

The exact source, page map, 17 previously approved chapter chunks, and frozen V8 policy have been verified and registered. All 425 source pages have exactly one chunk owner. An independent candidate-blind compatibility review selected the existing native V8 benchmark (638 subjects, 281 relationships, 638 reader tasks); discovery and full editorial review are not being repeated.

The independently approved native V8 benchmark is now registered through the reviewed-legacy compatibility workflow. Only approved evaluation-wrapper identities changed; source judgments, stable IDs, and policy are unchanged. The older benchmark repository release has different policy semantics and denominators and was not substituted.

The delivered Markdown remains byte-preserved. Evaluator PRs [33](https://github.com/publication-intelligence/evaluate-subject-index/pull/33) and [34](https://github.com/publication-intelligence/evaluate-subject-index/pull/34) are merged. Reviewed fixes cover structure path identities ([35](https://github.com/publication-intelligence/evaluate-subject-index/pull/35)), faithful cross-reference resolution ([36](https://github.com/publication-intelligence/evaluate-subject-index/pull/36)), density projection ([37](https://github.com/publication-intelligence/evaluate-subject-index/pull/37)), gate predicates ([38](https://github.com/publication-intelligence/evaluate-subject-index/pull/38)), generic consumer fields ([39](https://github.com/publication-intelligence/evaluate-subject-index/pull/39)), typed complete-bundle replacement ([40](https://github.com/publication-intelligence/evaluate-subject-index/pull/40)), and public metadata ([41](https://github.com/publication-intelligence/evaluate-subject-index/pull/41)). They were independently inspected and tested together before use. The user merged all evaluator PRs, including privacy support in [42](https://github.com/publication-intelligence/evaluate-subject-index/pull/42). PRs 39 and 42 initially merged into their feature-branch bases; merged [PR 43](https://github.com/publication-intelligence/evaluate-subject-index/pull/43) carries those changes to `main` and preserves nested source-uncertainty IDs. Authoritative main `f7e96898a79a73e933432b01d8b2cd8134503723` contains those fixes. The installed skill now matches reviewed [PR 44](https://github.com/publication-intelligence/evaluate-subject-index/pull/44) commit `48de38b26eef479f076e10c3b79241341af9cba9`, which adds an optional public presentation summary through the standard reporting command; all 126 coordinator evaluator tests pass. The new section has passed independent privacy and numeric-binding review. No PR was merged by the coordinator.

The candidate passed complete private validation: 2,548 records/paths, 2,812 displayed locators, 4,273 atomic assignments, and 257 cross-references. All 17 frozen locator packets collectively cover every assignment exactly once. All locator audits are complete and registered: 4,253 supported, 13 partially supported, 7 unsupported, and zero uninspectable assignments. Missing-access worksets cover 638 subjects, 638 reader tasks, and 1,569 coalesced expected treatments exactly once. All missing-access audits are complete and registered after independent semantic calibration: 1,514 treatments found and 55 missed; 592 reader tasks succeed, 33 partly succeed, and 13 fail.

Structure is registered with 2,292 heading nodes, 1,781 locator-bearing paths, 14 node exceptions, and 16 grouped defects. Ten locator lists triggered architectural review; three have confirmed subdivision defects. All 257 delivered cross-references are supported. The deterministic score is **95.60/100**, with three critical gates triggered. The complete public report and companion bundle passed independent closure review, canonical validation, all four existing website collection parsers, scoring-byte preservation, and source-overlap checks. The generic website adapter compatibility fix remains in progress in a separate task.

## Results

The canonical score is **95.60/100 — Excellent**. Readiness is **Not publication ready**: central-omission, compound-path, and major-grounding gates are triggered. Gates restrict the readiness claim and do not change the arithmetic.

| Dimension | Percentage | Weight |
| --- | ---: | ---: |
| Meaningful coverage | 95.85185185 | 20 |
| Editorial selectivity | 92.85558370 | 15 |
| Conceptual and stance fidelity | 100 | 15 |
| Page-reference reliability | 97.98973222 | 25 |
| Findability and navigation | 90 | 20 |
| Mechanics and consistency | 100 | 5 |

Percentages above are shortened for reading. Canonical full-precision values and contributions are preserved in the structured result. Navigation is capped from 97.96256170 to 90.

The index has a coherent two-level hierarchy and 257 supported delivered cross-references. Important weaknesses include incomplete access to several high-priority subjects, 20 locator assignments requiring changes, and three lists needing subdivision. Subject coverage is 581 complete, 48 partial, and 9 missing.

## Runtime and privacy

Use the installed skill and this project’s virtual environment:

```bash
ESI_SKILL_DIR="${CODEX_HOME:-$HOME/.codex}/skills/evaluate-subject-index"
.venv/bin/python "$ESI_SKILL_DIR/scripts/state_cli.py" validate --state evaluation/evaluation-state.json
.venv/bin/python "$ESI_SKILL_DIR/scripts/state_cli.py" next --state evaluation/evaluation-state.json
```

Restricted source, candidate, evidence, layout, and checkpoints are ignored by Git. Public reports will be emitted only through the evaluator’s standard reporting command and validated for privacy and generic website compatibility. Do not add a second manifest or benchmark lock.

## Review limitations

The frozen density denominator is **195,346 words**, summed from historical discovery measurements with differing extraction and counting methods. Independent review reconciled all 17 chunk joins and reproduced the canonical calculation byte for byte. It identified three measurement limitations: CHUNK-012's count exceeds current raw extraction without a recorded method; CHUNK-001's count omitted an eligible map caption; CHUNK-015 included estimated map labels that locator review excludes. The frozen counts remain unchanged for comparability. A future correction would require a uniform recount of all 17 chunks, not isolated patches.

The benchmark's 1,577 evidence records become 1,569 expected treatments through documented coalescing by subject, page, and treatment class; no evidence identities are lost. Chapter-level locator-bearing path presences sum to 1,864 because 66 paths occur in multiple chunks; the global distinct denominator is 1,781.

The Directory economic-crisis first-lookup judgment remains explicitly uncertain at medium confidence. All its expected treatments are found; the judgment concerns navigation across five routes.

Website scope is the complete public bundle and a generic adapter compatibility fix. No new IndexPDF study route, merge, or deployment is authorized in this run.

Public source-specific stance narratives are explicitly withheld. Locator and access explanations are generated from structured judgments and evidence identities; the complete authored narratives remain private. This changes presentation only, preserving all canonical scoring files and uncertainty identities.
