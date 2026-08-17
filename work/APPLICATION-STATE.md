# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `7ee1b0ab66f38e3499d28de3e271e108ac36983b` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-084`
- Next Fourth Report item: `F4-085`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-084.docx`
- Current working DOCX SHA-256: `459e8be1b0a4d294cb5ac5473d19073d68b879bd5069405eda2da02a8281f86d`
- Last known good commit basis: `7ee1b0ab66f38e3499d28de3e271e108ac36983b`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-084.docx`
- Current body paragraph count: 677

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical

## Structural-edit state
- F4-073–083 remain intact and validated from prior durable checkpoints.
- F4-084: P350 evidence language is now bounded to rivâyet/telakki centrality while FN361–364 and later Kastallânî/Dânî discussion are preserved.
- F4-085 4.1→4.2 status-transition correction is next.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-084-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 3/3 pages inspected (`work/F4-084-VISUAL-QA.md`).

## Exact next action
Apply F4-085 to the current F4-084 binary. At the 4.1→4.2 boundary, explicitly distinguish the normative role of the Uthmanic mushaf tradition from the historical evidentiary value of personal Companion codices using the Fourth Report wording. Preserve the 4.2 heading/bookmark and surrounding citations, then run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-084`.
