# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `dec9b20712554b3adaa87936d0406c51328ca64b` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-086`
- Next Fourth Report item: `F4-087`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-086.docx`
- Current working DOCX SHA-256: `2d7e6dc15e60c4b85db6de9459cc5bdd24f41da98f77577d17871e68d477826c`
- Last known good commit basis: `dec9b20712554b3adaa87936d0406c51328ca64b`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-086.docx`
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
- F4-073–085 remain intact and validated from prior durable checkpoints.
- F4-086: 4.2 now carries an explicit category-differentiation synthesis without displacing source-specific examples or citations.
- F4-087 open editor note remains next; F4-088 active-agent wording remains pending.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-086-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 5/5 pages inspected (`work/F4-086-VISUAL-QA.md`).

## Exact next action
Apply F4-087 to the current F4-086 binary by removing only the explicit parenthetical editor note embedded in the FN377–378 paragraph and restoring normal spacing before `Bunun en meşhur örneklerinden biri...`. Preserve Arabic runs, FN377–378 and all surrounding text. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-086`.
