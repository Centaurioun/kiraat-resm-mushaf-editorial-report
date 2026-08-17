# BASELINE AMENDMENT 001 — CONNECTOR-ONLY WORKER MODE

Status: **binding amendment** for the parallel application workflow.

This amendment was added after F4-W01 correctly failed closed under the original worker contract because its ChatGPT execution environment could read GitHub text/replay artifacts but could not materialize the canonical DOCX binary into its local runtime.

## 1. Facts that remain authoritative

- Canonical application branch: `editorial/apply-fourth-fifth-reports`.
- Frozen application checkpoint for the Fourth wave: commit `c473b24d3f6f24508c761805218bbaa29686b47c`.
- Application state at that checkpoint: F4-001–047 completed; F4-048 next.
- Canonical source SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`.
- GitHub durable state records the F4-047 package/output SHA as `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.

A coordinator runtime also recovered the prior local `f4_047.docx` plus its byte-identical rerun and obtained whole-file SHA-256 `6621390ddf0a274b2f3827d636492ef990f765bb0743bf881926ac19ded40b57`. That recovered package has 696 body paragraphs, contains the documented F4-043–047 edits, and its protected `footnotes.xml`, styles, numbering, settings and document relationships match the canonical-source protected parts. The cause of the whole-package SHA discrepancy has **not yet been adjudicated**.

Therefore the whole-DOCX package SHA is no longer a worker-stage eligibility gate. The discrepancy must be resolved or explicitly dispositioned by the High integrator before canonical acceptance.

## 2. Two permitted worker execution modes

### Mode A — FULL_BINARY
Use this when the worker can materialize the DOCX, reconstruct the required logical baseline, and run actual local DOCX replay/validation/rendering.

A Mode-A worker may report full local binary validation and bounded visual QA.

### Mode B — CONNECTOR_ONLY_PREPARATION
Use this when GitHub/project text evidence is accessible but the DOCX binary cannot be materialized locally.

A Mode-B worker **must not stop merely because the DOCX binary is unavailable**. Instead it must:

1. verify the frozen GitHub checkpoint, task scope and report versions;
2. use the canonical current manuscript/extracted manuscript, accepted report text, prior replay specifications and other repository evidence to locate and understand only its assigned items;
3. inspect citation/footnote evidence available in repository text and explicitly identify any proposition-to-citation question that still requires actual OOXML confirmation;
4. prepare exact semantic anchors, replacement text, structural instructions, deterministic replay code/specification where possible, and a citation map;
5. fail closed on ambiguous textual anchors: 0 or multiple plausible targets are not guessed;
6. mark every binary-only check as deferred rather than pretending it passed;
7. leave actual DOCX mutation, OOXML validation, replay execution and visual QA to the integrator.

Mode-B worker disposition for a safely prepared item is:

`READY_FOR_INTEGRATION_DEFERRED_BINARY_QA`

This means the editorial/replay package is ready for High integration, **not** that the DOCX edit has already been canonically applied or verified.

## 3. When DEPENDENCY_BLOCKED is still correct

Use `DEPENDENCY_BLOCKED` only when the worker cannot obtain enough repository evidence to prepare its assigned item safely, or when a real semantic/structural prerequisite is missing.

Binary unavailability by itself is no longer sufficient for `DEPENDENCY_BLOCKED`.

## 4. Deferred checks are mandatory at integration

For every Mode-B item, the High integrator must perform before canonical status is advanced:

- actual target resolution in the integrated DOCX;
- genuine footnote/reference inspection and proposition mapping;
- field/Zotero/bookmark/hyperlink/section/RTL checks as applicable;
- deterministic replay execution and idempotency;
- technical package/XML validation;
- bounded visual QA after the edit;
- conflict adjudication against earlier integrated worker bundles.

No Mode-B result may become canonical `VERIFIED` merely from worker evidence.

## 5. Scope and Git safety are unchanged

This amendment changes only the worker baseline/runtime gate. It does **not** loosen any scope, citation, no-web, no-main, no-canonical-branch-mutation, no-fuzzy-targeting, Fourth-before-Fifth, or protected-DOCX rule.

Workers already started from orchestration commit `5e7bdf4cd24d45e06e733da87b2e695c75751226` should re-read the latest `parallel/WORKER-CONTRACT.md` and this amendment from `orchestration/f4f5-parallel-v1`, then continue only their original task scope on their existing worker branch.