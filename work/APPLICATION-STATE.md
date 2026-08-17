# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `b3223a23562193c5772d8a19305e12bb4bb393df` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-106`
- Next Fourth Report item: `F4-107`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-106.docx`
- Current working DOCX SHA-256: `cace4c42e6f82b75c31b6533fb732892aa2d916baf8ec7abf6168730d6e15f38`
- Last known good commit basis: `b3223a23562193c5772d8a19305e12bb4bb393df`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-106.docx`
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
- F4-073–105 remain intact and validated from prior durable checkpoints.
- F4-106: the Meclis is now the grammatical subject and the institutional-control claim is limited to supported scope.
- Current body paragraph count remains 677; FN467 and all protected OOXML remain preserved.
- F4-107+ has not been pre-applied. Derived TOC field remains stale pending final Word refresh.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-106-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 3/3 pages inspected (`work/F4-106-VISUAL-QA.md`).

## Exact next action
Apply only F4-107 to current F4-106. Keep 4.7 in the order early print chronology → regional/qiraat-rivayah printings → Ottoman/Türkiye control and publication experience → one final conclusion. Remove the premature pre-Türkiye conclusion and replace the repeated Türkiye ending with the report-approved single multicausal final paragraph. Preserve the 1873 decision/permission versus 1874 actual-printing distinction and all genuine citations; do not pre-apply F4-108+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-106`.
