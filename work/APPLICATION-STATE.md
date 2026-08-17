# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `347545c6f74a5b9c55e39fc8d19d2914b7c00035` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-087`
- Next Fourth Report item: `F4-088`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-087.docx`
- Current working DOCX SHA-256: `cedcc233e5e3ce9150f3ebbd66b199075517dcac4a7d771a455a03db5e16a3ce`
- Last known good commit basis: `347545c6f74a5b9c55e39fc8d19d2914b7c00035`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-087.docx`
- Current body paragraph count: 678

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical

## Structural-edit state
- F4-073–086 remain intact and validated from prior durable checkpoints.
- F4-087: the open inline editor note in the FN377–378 paragraph has been removed without moving citations or Arabic runs.
- F4-088 active-agent/curatorial-authority wording in 4.2 is next; F4-089 Ibn Masud intent language remains pending.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-087-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-087-VISUAL-QA.md`).

## Exact next action
Apply F4-088 to the current F4-087 binary. Replace the 4.2 sentence that makes `Osmânî resm` an active selecting/curatorial authority with the report-approved distinction: the Uthmanic recension and subsequent common mushaf acceptance form the determining historical framework, while rasm is one written criterion for evaluating whether transmitted material accords with the common mushaf. Preserve surrounding source-backed paragraphs and footnotes; do not resolve F4-089 prematurely. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-087`.
