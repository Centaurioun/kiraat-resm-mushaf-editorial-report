# REPLAY SPEC — F4-W05

## Status

`DEPENDENCY_BLOCKED` — no editorial replay artifact was generated or executed.

## Mandatory precondition

The shared worker contract requires reconstruction of logical state `F4-047` from the canonical source plus the existing replay pipeline, followed by exact SHA-256 verification:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

The F4-047 manifest points to application checkpoint commit:

`c473b24d3f6f24508c761805218bbaa29686b47c`

Inspection of that checkpoint confirms the existing replay chain includes the generic DOCX editor and the F4 scripts through `apply_f4_043_047.py`; the logical F4-047 DOCX is not committed as a binary artifact at that checkpoint.

## Attempted bootstrap

1. Created/used exact worker branch `worker/f4/w05-074-082` from the orchestration branch.
2. Inspected baseline manifest and checkpoint tree.
3. Attempted local clone of the worker branch to obtain the canonical binary DOCX and replay scripts.
4. Clone failed with container network/DNS error: `Could not resolve host: github.com`.
5. GitHub connector access was then used for repository inspection; it supports UTF-8 repository files but rejects the DOCX as binary for direct fetch/materialization.
6. ChatGPT Files library candidates were probed as a possible byte source, but raw-byte materialization was not authorized, so no candidate could be SHA-256 matched to the repository source.

## Required structural replay once dependency is resolved

This is a specification only; it was **not executed**. A later capable F4-W05 rerun must:

1. Reconstruct and verify exact F4-047 SHA before touching the structural span.
2. Locate the 3.6 start anchor, all current 3.7–3.12 headings, and the Fourth Section boundary by exact semantic anchors plus local structural expectations; fail closed on 0 or >1 plausible match.
3. Inventory every genuine footnote reference and footnote body in the complete 3.6–3.12 span before any deletion/move.
4. Treat F4-074–082 as one architecture transaction with immediate local checkpoints after F4-074 and F4-078.
5. Reorder 3.6 conceptually as: normative reasons for adherence → historical origin/tevqif debate → language/grammar → hikmet/i‘jāz interpretations → Ibn Khaldun critique/responses.
6. Consolidate former 3.7–3.12 under `3.7. Resm-i Osmânî'ye Bağlılığın Gerekçeleri ve Sınırları`, preserving unique sourced material and deleting repetition, defensive teleology, and unsupported motive attribution.
7. For F4-079, prefer complete removal of the unverified Israel/Africa narrative unless the report-authorized verification-limited sentence can be retained with a valid supporting citation destination.
8. Replace the F4-080 counterfactual and F4-081 overstatement while preserving telakki/müşâfehe/edâ/rivâyet primacy.
9. Build the F4-082 transition into the Fourth Section without substantively touching F4-083.
10. Run idempotence/replay twice and require the second pass to detect already-applied state rather than duplicate changes.
11. Compare protected DOCX invariants and render the bounded full structural span for visual QA.

## No executable mutation code

Because the baseline precondition failed, writing a mutation script without observing the actual F4-047 XML, genuine footnote references, fields, bookmarks, and exact post-F4-047 anchors would violate the deterministic-targeting and citation rules. The correct fail-closed behavior is therefore to stop rather than fabricate replay code.
