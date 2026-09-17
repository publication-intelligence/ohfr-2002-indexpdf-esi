# IndexPDF combined V8.2 migration

**Comparability hold:** PR 6 is draft while the coordinator investigates different frozen benchmark sizes across the four indexes. This IndexPDF migration retains the imported Published benchmark (638 subjects, 1,569 coalesced treatments). Do not merge, activate bundles, or claim direct cross-index score comparability until that investigation is resolved. No benchmark evidence has been rewritten.

**Reviewed patch applied:** methodology PR 50 (`c11c6ccb`) is installed and verified. The original `adeb691` checkpoint is preserved separately. Four explicit uncertainty scopes supplement the unchanged frozen uncertainty records; no audit was rerun.

**Score: 97.19 → 97.19.** Every numeric dimension, component, denominator, deduction, uncertainty bound, cap evaluation and weighted contribution is unchanged from the verified V8.1 checkpoint. There are still **zero triggered or binding ceilings**. No frozen judgments were edited.

**Readiness: publication ready → not publication ready.** V8.2 adds one triggered publication gate, `GATE-WRONG-LOCATOR`, supported by six distinct frozen delivered locator assignments. Gate assessment is **sufficient**, with no blockers; evaluation validity is **valid**, with no blockers. This is a gate-policy change, separate from numerical quality and audit validity.

| Dimension | V8.1 and V8.2 percentage |
|---|---:|
| Meaningful coverage | 95.85185185185185185185185185 |
| Editorial selectivity | 92.85558370331663418495020807 |
| Conceptual/stance fidelity | 100 |
| Page-reference reliability | 97.9897322222424284250851774 |
| Findability/navigation | 97.97826850242138773233665836 |
| Mechanics/consistency | 100 |

## Gate evidence

Each row below is already finalized as `unsupported` and `no_fit`, indexable, high confidence, source-linked and accompanied by an authored fit rationale in the frozen audit. None has unresolved uncertainty affecting that locator/path. Original **minor** severity is retained. V8.2 needs one confirmed wrong delivered destination; rate, spread and an additional defect record are not prerequisites.

| Locator ID | Page | Frozen source-linked evidence |
|---|---:|---|
| LOC-05BE1111509F | 105 | EVID-6049F7F3D636001F |
| LOC-0627DDDC45EE | 105 | EVID-78C77B00D4304DA7 |
| LOC-C853B3459625 | 105 | EVID-DE763C4E20B7EB1B |
| LOC-8909AEDE85AA | 329 | EVID-CHUNK014-8909AEDE85AA |
| LOC-B9B6F4DBC156 | 365 | EVID-015-B9B6F4DBC156 |
| LOC-5CEE64F02874 | 423 | EVID-CHUNK017-5CEE64F02874 |

These are **one gate and six unique assignments**, not six gates. Exact complete heading paths, audit axes and evidence IDs appear in the canonical public gate record and [change ledger](change-ledger.json), without private source summaries. Five rows have absent treatment; the final row has passing-mention treatment but zero complete-path fit. That distinction is preserved.

The seventh unsupported locator, `LOC-0D7950EB3BA7`, has `exact_fit` and weak treatment; it does not qualify. All 13 material partial fits, their ordinary deductions, and the 32 missing-route yellow signals remain unchanged. Nonzero fits and missing supplemental routes were not reclassified to force gates.

`GATE-BROKEN-REFERENCE` does not trigger. The frozen V6 structure ledger has no reference exceptions and attests all 257 delivered references as supported. That supported pass attestation is explicitly reusable under V8.2. No `target_resolution` rows were invented, no null normalized target was treated as a broken destination, and every original structure field remains unchanged. Only the additive scope supplement changes the structure bytes.

## Provenance and exact scope

The preserved original V8 policy is the actual candidate-blind policy at `evaluation/archive/v8-original/source/evaluation-policy.v4.json`. The latest V8.1 baseline was restored from the verified durable private checkpoint into `evaluation/archive/v8.1-before-v8.2`; its state and all 158 registered artifacts exactly matched this worktree before migration. The saved project's older 95.60 V8 state was not substituted or mixed with V8.1 files.

The native policy builder consumed [policy-build-input.json](policy-build-input.json), the original policy through `--original-policy`, and the V8.1 policy through `--base-policy`. Its schema-defined `retrospective_migration` records the actual V8.2 time, `candidate_seen: true`, [existing authorization](AUTHORIZATION.md), original policy/freeze and exact reused-stage evidence hashes. The old `policy_profile.targeted_migration` workaround is removed. Source scope, audience, audit design, density settings and deviations are unchanged; existing V8.1 gates are retained and the two V8.2 direct gates added.

Identities are `subject-index-standard-policy-v8.2`, `subject-index-rubric-v8.2`, and `subject-index-dimension-calculation-v7`. Installed methodology revision `c11c6ccb16000fe79646af16b7be01f6cbeeac78` was verified across all 111 installed files against receipt SHA-256 `f7d0b2bd830dfbca7b1e8c4f79c6320e2c7a945d075342807d24d6f9f7cd1204`.

No source discovery, mapping, benchmark synthesis/review, normalization or audit was rerun. Original benchmark release, review and compatibility approval bytes remain separate unchanged historical provenance. The current policy is selected through canonical state and exact calculation-input hashes; historical worker and benchmark policy bindings are retained. The structure registration and scoring/reporting hash cascade were reopened and completed with registered `register-structure`, `score` and `build-report` commands. The scope patch does not rerun the audit: it adds three `measurement_provenance` rows for the frozen source extent, candidate representation and density limitations, and one `benchmark_access` row for the existing first-lookup uncertainty. All original targets remain; all original rows lack evidence IDs, so the supplements use empty arrays with grounded rationales. See the preserved [scope proposal](uncertainty-gate-scopes.proposed.json) and applied supplement in the change ledger.

Nine registered files change, plus canonical state:

- `source/evaluation-policy.v4.json`
- `staging/structure/structure-audit.v6.json`
- `scoring/dimension-calculation-input.v2.json`
- `scoring/dimension-calculations.v6.json`
- `scoring/item-assessments.v7.json`
- `scoring/projection-metadata.v2.json`
- `scoring/evaluation-result.v12.json`
- `scoring/web-report.v10.json`
- `scoring/v8-canonical-projection/projection.v1.json`
- `evaluation-state.json`

All paths above are relative to `evaluation/`. The other **149 registered artifacts**, including all locator and missing-access audits and **all three public data collections**, remain byte-identical. Item-assessment arrays also remain identical; their outer policy/calculation provenance changes. README and the files in this migration folder supply documentation, authorization, exact build input, validation and change records; the canonical state remains the sole workflow inventory.

## Validation and handoff

All **180 methodology tests passed**. Canonical state has no errors/warnings and no next action. Verification reconstructed the native policy, deterministic calculation and item assessment outputs; checked original/V8.1/V8.2 exact artifact hashes; and validated current schemas and complete projection/collection hashes, counts, order, joins and privacy checks. Entire dimension records compare identically after excluding only the formula-version label and exact policy/structure hash bindings. Against the provisional V8.2 calculation, only the structure hash binding changes. Diagnostic grades, structural arithmetic projection, review signals and all three public data collections are identical to both baselines. See [validation.json](validation.json) and the repeatable `verify.py` check.

Original V8 and V8.1 archives remain preserved, and separate provisional and final V8.2 private-complete checkpoints preserve both runtime releases. The [private-handoff receipt](private-handoff.json) records archive basenames and exact hashes. They are stored privately in the saved project's ignored `evaluation/exports/` directory. Restore the V8.2 checkpoint as the active evaluation, the original archive under `evaluation/archive/v8-original`, and the V8.1 checkpoint under `evaluation/archive/v8.1-before-v8.2` to retain the build-input evidence paths alongside this repository revision. Restore the provisional V8.2 checkpoint under `evaluation/archive/v8.2-adeb691-before-scope-patch` for repeatable before/after verification.

The saved project's active V8 checkout and private files are deliberately left coherent while this evaluation PR awaits user review. After approval/merge, activate the public checkout and matching private V8.2 files together; Git alone cannot transport ignored inputs. This is a staged handoff, not a claim that the saved active evaluation is already V8.2. No website deployment or evaluation-PR merge was performed.

The delivered-Markdown limitation, supplied-source exclusions, frozen density measurements and existing Directory navigation uncertainty remain as disclosed in the prior evaluation. There are no unresolved V8.2 destination-assessment blockers.
