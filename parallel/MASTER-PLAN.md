# MASTER PLAN — Parallel Application of Fourth and Fifth Reports

## Objective

Finish all remaining applicable changes from `final/fourth-report-v2.md` and then `final/fifth-report-locked.md` while materially reducing wall-clock time without weakening scientific, citation, OOXML, or visual-QA safeguards.

## Architecture

Use ten isolated workers per wave, one High integrator, and one independent High auditor. Reasoning and local proof run in parallel; authoritative DOCX mutation remains serial.

## Frozen starting point

The Fourth wave is anchored to application checkpoint `c473b24d3f6f24508c761805218bbaa29686b47c`, where F4-001–047 are complete and the reproducible logical DOCX SHA-256 is `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.

## Fourth wave ownership

- F4-W01: F4-048–056
- F4-W02: F4-057–062
- F4-W03: F4-063–069
- F4-W04: F4-070–073
- F4-W05: F4-074–082 — structural/high-risk cluster
- F4-W06: F4-083–090
- F4-W07: F4-091–099
- F4-W08: F4-100–107
- F4-W09: F4-108–110
- F4-W10: F4-112, F4-114–116 — footnote/bibliography specialist
- Integrator-reserved: F4-111 and F4-113

This covers every Fourth item from 48 through 116 exactly once when worker and integrator ownership are combined.

## Fourth integration order

Reconstruct F4-047 from canonical source and existing replay chain; verify exact logical SHA. Then integrate worker results in report order. F4-111 and F4-113 are global changes and are deliberately reserved for the integrator so they do not invalidate worker anchors. The canonical application ledger/state/log/handoff are updated only after accepted integration.

## Fourth acceptance gate

A fresh auditor must verify coverage F4-001–116, scientific meaning, footnote proposition placement, replayability, protected OOXML structures, and full-document visual integrity. Only then is an `F4_VERIFIED_BASELINE` allowed to exist.

## Fifth activation

Fifth work is blocked until `F4_VERIFIED_BASELINE` exists. Fifth wording never restores text removed or scientifically corrected by Fourth.

## Fifth wave ownership

- F5-W01: F5-001–014
- F5-W02: F5-015–024
- F5-W03: F5-025–034
- F5-W04: F5-035–042
- F5-W05: F5-043–054
- F5-W06: F5-055–061
- F5-W07: F5-062–064 — structural language merge/high-risk
- F5-W08: F5-065–070
- F5-W09: F5-071–080
- F5-W10: F5-081–085
- Integrator-reserved global sweep: F5-086–094

This covers F5-001–094 exactly once when worker and integrator ownership are combined.

## Fifth precedence

Fourth controls scientific/structural meaning. For a Fifth item whose original literal anchor has disappeared after Fourth:

- never restore the pre-Fourth wording;
- use `ALREADY_SATISFIED_AFTER_PRIOR_EDIT` when Fourth already solves it;
- use `APPLIED_WITH_FOURTH_FIFTH_MERGE` when Fifth adds compatible stylistic value;
- escalate if Fifth would weaken or contradict Fourth.

## Integration safety

No worker branch is merged into the canonical branch. The integrator reads the worker result package and replays it on a single integration branch. Anchor matching is fail-closed: zero matches or multiple matches stop the item; fuzzy best-guess application is forbidden.

## QA economy

Workers perform bounded visual QA only around their affected region. Integrators repeat technical validation after accepted bundles. Full-document rendering and all-page visual QA are mandatory at the F4 acceptance gate and final F5 acceptance gate.

## Completion

The project is complete only when all F4 and F5 items have one durable canonical disposition, no unresolved unsafe citation placement remains, the full replay is reproducible from the canonical source, DOCX integrity passes, and the final integrated document passes all-page visual QA.
