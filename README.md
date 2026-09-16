# OHFR 2002 — IndexPDF subject-index evaluation

This repository evaluates IndexPDF’s delivered subject-index Markdown export for *The Oxford History of the French Revolution* (2002) using the current Evaluate Subject Index V8 workflow.

The single canonical workflow state and artifact inventory is [`evaluation/evaluation-state.json`](evaluation/evaluation-state.json). The evaluation ID is `ohfr-2002-indexpdf-v8`. The source has 425 pages; front matter and endnotes absent from that supplied file are outside the available source.

## Current milestone

The exact source, page map, 17 previously approved chapter chunks, and frozen V8 policy have been verified and registered. All 425 source pages have exactly one chunk owner. An independent candidate-blind compatibility review selected the existing native V8 benchmark (638 subjects, 281 relationships, 638 reader tasks); discovery and full editorial review are not being repeated.

Registration awaits a focused extension of the existing reviewed-legacy importer for native V8 release evidence. The older benchmark repository release has different policy semantics and denominators and is not substituted. The historical source-only release and prior candidate-preparation state remain recoverable in private checkpoints.

The delivered Markdown remains byte-preserved. [Evaluator PR #33](https://github.com/publication-intelligence/evaluate-subject-index/pull/33) corrects a parser error that treated five heading qualifiers as locators. Corrected candidate artifacts will be normalized, privately validated, and registered after benchmark compatibility import. Locator audits, missing-access audits, structure, scoring, and reporting are not yet complete; no score is claimed.

## Runtime and privacy

Use the installed skill and this project’s virtual environment:

```bash
.venv/bin/python /home/john/.codex/skills/evaluate-subject-index/scripts/state_cli.py validate --state evaluation/evaluation-state.json
.venv/bin/python /home/john/.codex/skills/evaluate-subject-index/scripts/state_cli.py next --state evaluation/evaluation-state.json
```

Restricted source, candidate, evidence, layout, and checkpoints are ignored by Git. Public reports will be emitted only through the evaluator’s standard reporting command and validated for privacy and generic website compatibility. Do not add a second manifest or benchmark lock.
