# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `0694386d412e3ffc7eb3276ab5fc013eb1aa2eba` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-113`
- Next Fourth Report item: `F4-114`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-113.docx`
- Current working DOCX SHA-256: `e4287570d99f9d3c20f96752497787e6d97f6a07047555ecbe5c05e5c69bdac1`
- Last known good commit basis: `0694386d412e3ffc7eb3276ab5fc013eb1aa2eba`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-113.docx`
- Current body paragraph count: 676

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical except explicitly authorized footnote-text changes in `word/footnotes.xml`; target footnote structure unchanged

## Structural-edit state
- F4-073–112 remain intact and validated from prior durable checkpoints.
- F4-113: genuine footnote text house style now uses `Dânî`, `Zürkânî`, `Suyûtî` for the targeted author-name variants and an articleless sura-name convention in explicit verified Qur'anic verse references.
- Bibliographic work titles and unrelated article-bearing lexical contexts are preserved; no F4-114 transliteration work has been pre-applied.
- Current body paragraph count remains 676; all 469 footnote identities/references, 520 fields, Zotero/ADDIN fields, bookmarks, hyperlinks and RTL structural inventory remain preserved.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-113-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 19/19 pages inspected (`work/F4-113-VISUAL-QA.md`).

## Exact next action
Fetch the exact F4-114 item from `final/fourth-report-v2.md`, resolve it against the current durable F4-113 binary, run a read-only preflight, and apply only F4-114 if unambiguous. Do not pre-apply F4-115+ or repeat `F4-001`–`F4-113`.
