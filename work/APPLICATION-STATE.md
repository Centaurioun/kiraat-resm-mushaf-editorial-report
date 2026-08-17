# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `7be56d5640002fca2594b06c891a8ec46cab1c18` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-112`
- Next Fourth Report item: `F4-113`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-112.docx`
- Current working DOCX SHA-256: `58e23edd3cdbffbacaf8a2e14fc2dff5ea5357dd76b15cda30c4d31820e12e9a`
- Last known good commit basis: `7be56d5640002fca2594b06c891a8ec46cab1c18`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-112.docx`
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
- F4-073–111 remain intact and validated from prior durable checkpoints.
- F4-112: genuine footnotes 32, 41 and 105 now contain only their bibliographic citation text; editor/work notes are removed.
- Current body paragraph count remains 676; all 469 footnote identities/references, 520 fields, bookmarks, hyperlinks and body XML structure remain preserved.
- F4-113+ has not been pre-applied. Derived TOC field remains stale pending final Word refresh.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-112-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 3/3 pages inspected (`work/F4-112-VISUAL-QA.md`).

## Exact next action
Apply only F4-113 to current F4-112. Inventory author-name article variants and sura-name article variants in genuine footnotes before editing. Normalize author-name house-style forms such as `ez-Zürkânî`, `es-Suyûtî`, `ed-Dânî` to `Zürkânî`, `Suyûtî`, `Dânî` only where they function as author names; do not mechanically strip articles from sura names, work titles or other lexical contexts. Establish and apply one internally consistent sura-name article convention without altering bibliographic titles. Use footnote-specific validation and identity-preserving visual QA. Do not pre-apply F4-114+ or repeat `F4-001`–`F4-112`.
