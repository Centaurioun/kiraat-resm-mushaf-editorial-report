# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `625e5d7ee602bc3861c271558052126a2f18be0e` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-085`
- Next Fourth Report item: `F4-086`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-085.docx`
- Current working DOCX SHA-256: `d48b31281dc7e8ddde3b30856e2ce1d6edcfc4b079de2c87c63d0b54fdac0af1`
- Last known good commit basis: `625e5d7ee602bc3861c271558052126a2f18be0e`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-085.docx`
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
- F4-073–084 remain intact and validated from prior durable checkpoints.
- F4-085: explicit normative-status transition now separates common Uthmanic mushaf authority from the historical evidentiary role of personal Companion codices; 4.2 bookmark heading preserved.
- F4-086 category differentiation in 4.2 is next; F4-087 open editor note remains intentionally unresolved.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-085-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-085-VISUAL-QA.md`).

## Exact next action
Apply F4-086 to the current F4-085 binary. Reframe the 4.2 Companion-codex discussion so attributed differences are not collapsed into a single mensuh/tefsiri category. Preserve source-specific evidence, Arabic runs, and footnote identities; distinguish reading reports, explanatory/tafsiri expressions, word-order/writing differences, and disputed records, while keeping the Uthmanic written framework plus sound transmission as the normative criterion. Do not resolve unrelated F4-088/089 claims prematurely. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-085`.
