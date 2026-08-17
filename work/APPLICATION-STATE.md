# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `8049212a4afb00d5c9c2b5ae6c36fc098519e6e2` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-083`
- Next Fourth Report item: `F4-084`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-083.docx`
- Current working DOCX SHA-256: `d4adb180cd58a6d74d1557a6c14fe2bc2b1fc42018c7b4bcffaf2029e2993127`
- Last known good commit basis: `8049212a4afb00d5c9c2b5ae6c36fc098519e6e2`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-083.docx`
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
- F4-073–082 remain intact and validated from prior durable checkpoints.
- F4-083: 4.1 now distinguishes transmitted qiraat from rasm as a written compatibility/evaluation criterion; repeated historical material is reduced without dropping FN365–367.
- F4-084 `Kırâat sünnettir` evidence-language correction remains intentionally unresolved for its own sequential application.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-083-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 4/4 pages inspected (`work/F4-083-VISUAL-QA.md`).

## Exact next action
Apply F4-084 to the current F4-083 binary. In P350, retain the source-backed `Kırâat sünnettir` and Ebû Amr evidence but replace the over-strong historical inference with the report-approved bounded statement that these reports indicate the centrality of rivâyet and telakki in qiraat transmission. Preserve FN361–364 and do not disturb the F4-083 P351/P352 reframe. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-083`.
