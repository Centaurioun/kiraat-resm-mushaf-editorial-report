# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `524d765f930ee80cf63898767672149c7206aa4d` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-111`
- Next Fourth Report item: `F4-112`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-111.docx`
- Current working DOCX SHA-256: `4c9eba6d4ca9e65dc7148921c8331a21f4768ecc3aed65c9c0deda0ff98166c9`
- Last known good commit basis: `524d765f930ee80cf63898767672149c7206aa4d`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-111.docx`
- Current body paragraph count: 676

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical

## Structural-edit state
- F4-073–110 remain intact and validated from prior durable checkpoints.
- F4-111: main-text house style now uses `Kur’an` and curated specific-name `İmam Mushaf` without altering bibliography, direct quotations, italic work titles or footnotes.
- Current body paragraph count remains 676; all 469 footnote identities, 520 fields, bookmarks and protected OOXML remain preserved.
- F4-112+ has not been pre-applied. Derived TOC field remains stale pending final Word refresh.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-111-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 19/19 pages inspected (`work/F4-111-VISUAL-QA.md`).

## Exact next action
Apply only F4-112 to current F4-111. Remove the surviving editorial/work notes from genuine footnotes 32, 41 and 105 while preserving the bibliographic citation content and the footnote IDs/references. Because `word/footnotes.xml` must change for this accepted item, use a footnote-specific validation that proves only the targeted footnote text changed and all 469 IDs/reference identities, fields, body XML structure and all other protected parts remain intact. Do not pre-apply F4-113+. Run deterministic replay and footnote-aware visual/technical QA. Do not repeat `F4-001`–`F4-111`.
