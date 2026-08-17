# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `1562e396962bce48ab2c81c6a3c1b8aad70a599e` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-099`
- Next Fourth Report item: `F4-100`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-099.docx`
- Current working DOCX SHA-256: `3c3a18fdd19dff05f2bb7e3a03979bc5eb0769085a36b7b2e1c4a61a81d4f8c0`
- Last known good commit basis: `1562e396962bce48ab2c81c6a3c1b8aad70a599e`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-099.docx`
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
- F4-073–098 remain intact and validated from prior durable checkpoints.
- F4-099: a single report-approved historical transition paragraph now bridges classical rasm transmission and the modern print-mushaf section.
- The bookmark-backed 4.6 heading and FN438+ source material remain preserved; F4-100+ has not been pre-applied.
- Derived TOC field has not been recalculated; final Word field/TOC refresh remains required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-099-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 3/3 pages inspected (`work/F4-099-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-100 to the current F4-099 binary. At the 4.7 opening, replace the claim that the absence of dotting/vocalization in early mushafs was fundamentally a conscious mechanism for preserving multiple qiraat with the report-approved historically cautious formulation. Preserve all affected footnotes/RTL/source material and do not pre-apply F4-101+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-099`.
