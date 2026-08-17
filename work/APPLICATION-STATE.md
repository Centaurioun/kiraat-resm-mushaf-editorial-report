# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `4b725caaefbd48ef6957438c249e8c32ffb3685f` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-108`
- Next Fourth Report item: `F4-109`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-108.docx`
- Current working DOCX SHA-256: `38926bbf6e31f5b1d74ca5a883d1867bae35fa06ef89187d0d35d2860edf6bfa`
- Last known good commit basis: `4b725caaefbd48ef6957438c249e8c32ffb3685f`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-108.docx`
- Current body paragraph count: 675

## Integrity
- Genuine footnotes/references: 469/469
- Orphan/dangling/duplicate references: 0/0/0
- Word field instructions: 520/520; ADDIN: 466/466
- Zotero: 465 item + 1 bibliography preserved
- Bookmarks: 53/53; hyperlinks: 52
- Arabic/RTL structural inventory: canonical-equal
- Protected OOXML parts: baseline-identical

## Structural-edit state
- F4-073–107 remain intact and validated from prior durable checkpoints.
- F4-108: Sonuç begins with a two-focus thesis statement rather than repeated restatements, while unique historical and application results remain.
- Current body paragraph count is 675; all 469 footnote identities and protected OOXML remain preserved.
- F4-109+ has not been pre-applied. Derived TOC field remains stale pending final Word refresh.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-108-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 5/5 pages inspected (`work/F4-108-VISUAL-QA.md`).

## Exact next action
Apply only F4-109 to current F4-108. Reframe the Sonuç paragraph on modern printed-mushaf standardization so print is not presented as a one-way sole driver of a qiraat's standardization/spread. Use the report-approved multicausal formulation and preserve the unique classical-source/resm-zabt relationship already present in that paragraph. Do not pre-apply F4-110+. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-108`.
