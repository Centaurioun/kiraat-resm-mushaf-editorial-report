# HANDOFF — F4-W02

## Worker scope

Assigned only `F4-057`–`F4-062` on branch `worker/f4/w02-057-062`.

## Overall disposition

`DEPENDENCY_BLOCKED`

The worker contract requires an independently reconstructed F4-047 logical DOCX with exact SHA-256 `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7` before edits may be applied. This execution environment could not materialize and run the binary replay pipeline: repository cloning failed because outbound network resolution is disabled, while the GitHub connector provides text access and bounded base64 inspection but not a complete executable local DOCX. Therefore no assigned item is claimed applied, integrated, technically validated, visually validated, or canonically verified.

## Per-item handoff

- `F4-057` — `DEPENDENCY_BLOCKED`. Exact report replacement and manuscript anchor identified. Preceding note `[^216]` must remain on its original Âsım/Hafs/Şu'be proposition, not the transition.
- `F4-058` — `DEPENDENCY_BLOCKED`. Multi-view cautious replacement specified. Note `[^221]` requires proposition-level source verification before retention or relocation.
- `F4-059` — `DEPENDENCY_BLOCKED`, **AMBER citation/structure risk**. The required shortening must preserve unique cited material across 2.3; do not implement as blind paragraph deletion. Full footnote mapping on verified F4-047 is mandatory.
- `F4-060` — `DEPENDENCY_BLOCKED`. Active-causal wording replacement specified. Nearby note `[^225]` requires proposition-level re-evaluation.
- `F4-061` — `DEPENDENCY_BLOCKED`. Counterfactual replacement specified. No speculative movement of nearby `[^236]`.
- `F4-062` — `DEPENDENCY_BLOCKED`, **AMBER structural risk**. Transition text is specified, but the existing Third Section heading, style, numbering and bookmarks must be preserved and proven on the DOCX.

## Deliverables

- `TASK-RECEIPT.md`
- `ITEM-RESULTS.jsonl`
- `REPLAY-SPEC.md`
- `CITATION-MAP.md`
- `VALIDATION.md`
- `VISUAL-QA.md`
- `HANDOFF.md`

No canonical ledger/state file was modified.

## Integrator action

Do **not** integrate any F4-W02 item from this package as GREEN. First run the existing recovery pipeline in an environment with full repository/DOCX access, verify the required F4-047 SHA-256, then execute the fail-closed `REPLAY-SPEC.md`, perform citation mapping, full technical validation and bounded visual QA. F4-059 and F4-062 should remain AMBER until their citation/structural conditions are explicitly cleared.

## Commit provenance

Orchestration source commit: `5e7bdf4cd24d45e06e733da87b2e695c75751226`.

Evidence package immediately before this handoff-finalization commit: `bb1f9b3a265518442d62cda6f7f4e11e5154fd54`.

The exact final worker-branch HEAD containing this handoff is reported by the coordinator-facing completion message after the commit is created.
