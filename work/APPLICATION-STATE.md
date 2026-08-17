# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint commit: `SELF`
- Source commit: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`
- Canonical source: `source/manuscript/current/redaktorden_gelen.docx`
- Canonical SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: 116 items, blob `e880124fb0bdb72afb29cf10927e2dd15bae0676`
- Fifth Report: 94 items, blob `b2e184bf45c13fb548cd13ee2e4f829a52b4bb69`

## State machine
- Phase: `FOURTH_APPLY`
- Last fully completed Fourth item: `F4-017`
- Next Fourth item: `F4-018`
- Fifth Report: blocked until Fourth completion; next `F5-001`.
- DO-NOT-REPEAT: bootstrap and `F4-001–017`.

## Deterministic recovery pipeline
1. Canonical source → `work/apply_docx_edits.py` (F4-001–011), replay commit `86f99b2186711a7d94159d9c1b7413b0248a0c5c`.
2. Output → `work/apply_f4_012_017.py` (F4-012–017), replay commit `d533b450b20729130e850d7cbf37256a8e192306`.
- Current reproducible logical DOCX SHA-256: `9b983dcebda782bf1b5bbb69134dde43b0b45b5119ae63d5aa4f2379ec57885a`.
- Current body paragraphs: **700** (baseline 711).
- Batch replay idempotency: **PASS, byte-identical**.
- Ledger through F4-017: commit `154d696611e3b97fc92595982fa240097f89e7fe`.
- Edited binary is not falsely claimed persisted; connector lacks local binary DOCX upload. Durable recovery is canonical source + replay pipeline + exact hashes + ledger + validation.

## Integrity
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged.
- Orphans/dangling/duplicates: **0/0/0**.
- `word/footnotes.xml`: exact baseline hash.
- Word fields: **520/520** — TOC 1, PAGEREF 52, REF 0, PAGE 1, ADDIN 466.
- Zotero: **465 item + 1 bibliography**, unchanged.
- Protected core OOXML unchanged except expected `word/document.xml`; ZIP/XML **PASS/PASS**.

## F4-012–017 result
- F4-012: STRUCTURALLY_APPLIED — three repetitive 1.2 opening paragraphs consolidated; notes 19–21 retained in ascending order on supported surviving synthesis.
- F4-013: APPLIED — terminal period restored; notes 22–23 untouched.
- F4-014: APPLIED — second/third reasons merged and explicit editor note removed; notes 24–26 preserved.
- F4-015: STRUCTURALLY_APPLIED — two-model certainty replaced with cautious synthesis; notes 28–30 preserved on the sentence summarizing both source families.
- F4-016: APPLIED — evidentiary certainty weakened to report-approved wording.
- F4-017: APPLIED — 1.3 now opens directly with the Ebû Bekir cem transition.
- Open HOLDs: none.

## Visual QA
- First 80 current body paragraphs rendered as **19 pages**; **19/19 inspected**.
- The durable two-script pipeline render is pixel-identical page-for-page to the independently produced F4-017 validation render (19/19 SHA matches).
- No clipping, overlap, footnote overflow, unintended style propagation, or pagination defect caused by F4-012–017.
- Existing red editorial text outside this batch remains source content for later report items.
- Final full-document all-page QA remains mandatory.

- Last validation: **PASS — F4-012–017 technical + citation semantics + byte-idempotency + 19/19 bounded visual QA**.
- Exact next action: apply `F4-018` from CURRENT F4-017 state, then continue sequentially.