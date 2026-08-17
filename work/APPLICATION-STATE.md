# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `7fb10d31754be6f3fc1e43806084a61476f707ba` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-104`
- Next Fourth Report item: `F4-105`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-104.docx`
- Current working DOCX SHA-256: `641e964820181acf70d8c7e5af7608e1347e7e4faecb2a1a19bfb7628710ee13`
- Last known good commit basis: `7fb10d31754be6f3fc1e43806084a61476f707ba`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-104.docx`
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
- F4-073–103 remain intact and validated from prior durable checkpoints.
- F4-104: modern mushaf standardization is framed as multicausal rather than as the direct natural result of one rasm theory.
- Current body paragraph count remains 677; protected OOXML and all footnote identities remain preserved.
- F4-105+ has not been pre-applied. Derived TOC field has not been recalculated; final Word field/TOC refresh remains required.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-104-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-104-VISUAL-QA.md`).

## Exact next action
Read and apply only F4-105 to the current F4-104 binary. Replace the current 4.7 closure that presents printed mushafs as actively causing qiraat spread/standardization with the report-approved multicausal formulation: printed mushafs increase written visibility/use, while regional spread also depends on teaching traditions, regional qiraat preferences, official publication policy and educational institutions. Preserve surrounding source-backed chronology and do not pre-apply F4-106+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-104`.
