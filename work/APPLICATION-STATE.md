# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `f755fa1188cdb034947f006f9f247a2876f169cb` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-095`
- Next Fourth Report item: `F4-096`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-095.docx`
- Current working DOCX SHA-256: `00eae3a5b7299a0522979562d73e1d4bbe52ff7c205ee59c37f09ba3b4b817ea`
- Last known good commit basis: `f755fa1188cdb034947f006f9f247a2876f169cb`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-095.docx`
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
- F4-073–094 remain intact and validated from prior durable checkpoints.
- F4-095: the FN401 imam-preference paragraph now foregrounds received rivayat/teaching and multi-factor evaluation rather than independent selector agency.
- FN402–403 and later 4.4 material remain untouched; F4-096 is next.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-095-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-095-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-096 to the current F4-095 binary. Distinguish meaning/nahw/rivayat-based waqf from rasm-related written cues such as wasl-fasl and word boundaries; preserve source-backed examples and do not pre-apply F4-097+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-095`.
