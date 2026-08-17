# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `aaf1558be1b3340de4f00bb1e2db726dcbe10981` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-110`
- Next Fourth Report item: `F4-111`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-110.docx`
- Current working DOCX SHA-256: `fcdca872a3efc36b96e9f9d600fd23ba73b45a4fec4857ea5434df2b6dd1c807`
- Last known good commit basis: `aaf1558be1b3340de4f00bb1e2db726dcbe10981`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-110.docx`
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
- F4-073–109 remain intact and validated from prior durable checkpoints.
- F4-110: Sonuç now ends with retained ilmî contribution, separate final judgment, separate future-research paragraph, followed by Kaynakça on a new page.
- Current body paragraph count is 676; all 469 footnote identities, 520 fields, bookmarks and protected OOXML remain preserved.
- F4-111+ has not been pre-applied. Derived TOC field remains stale pending final Word refresh.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-110-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 5/5 pages inspected (`work/F4-110-VISUAL-QA.md`).

## Exact next action
Apply only F4-111 to current F4-110. Perform the report-required global main-text normalization of `Kur’an` and the specific-name form `İmam Mushaf`, while preserving bibliographic titles and direct quotations where original spelling must remain. Use a preflight inventory first so broad replacement does not touch fields, bibliography, quotations, Arabic/RTL runs or protected citation structures. Do not pre-apply F4-112+. Run deterministic replay, technical validation and bounded/global QA appropriate to the scope. Do not repeat `F4-001`–`F4-110`.
