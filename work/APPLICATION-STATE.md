# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `c876c78ccd2913dccaf9aef896c5cf1a93e8018f` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-105`
- Next Fourth Report item: `F4-106`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-105.docx`
- Current working DOCX SHA-256: `640fdbf06ee48de553d7341b88592cff5ead107010ccef15e2278f684f36b118`
- Last known good commit basis: `c876c78ccd2913dccaf9aef896c5cf1a93e8018f`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-105.docx`
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
- F4-073–104 remain intact and validated from prior durable checkpoints.
- F4-105: qiraat spread/standardization is now framed as multicausal; print increases written visibility/use without being the sole explanatory cause.
- Current body paragraph count remains 677; P438+ Türkiye chronology and all protected OOXML remain preserved.
- F4-106+ has not been pre-applied. Derived TOC field has not been recalculated; final Word field/TOC refresh remains required.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-105-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 3/3 pages inspected (`work/F4-105-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-106 to the current F4-105 binary. Repair the 1889 Teftis-i Mesahif-i Serife Meclisi sentence so the Meclis is the grammatical subject and the claim is limited to supported institutional inspection/control of mushaf publication. Map genuine FN467 to the retained proposition before editing; do not pre-apply F4-107+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-105`.
