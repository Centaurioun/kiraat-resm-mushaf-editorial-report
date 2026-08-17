# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint basis: `f7597ed4f0aa33fe338666b17e7e7841e7a601ed` (metadata checkpoint commit follows this basis)

## Source / reports
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: `final/fourth-report-v2.md` — 116 items
- Fifth Report: `final/fifth-report-locked.md` — 94 items

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-078`
- Next Fourth Report item: `F4-079`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (do not start until Fourth Report validation passes)

## Current working state
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-078.docx`
- Current working DOCX SHA-256: `131913a4e602ec88fa0582ebe1cd40cfe8f9c1e9461c5692d12d4c4b36465e6f`
- Last known good commit basis: `f7597ed4f0aa33fe338666b17e7e7841e7a601ed`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-f4-078.docx`
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
- F4-073–077 remain intact and validated from the prior durable checkpoint.
- F4-078: old 3.7–3.12 architecture consolidated beneath one main heading, `Resm-i Osmânî’ye Bağlılığın Gerekçeleri ve Sınırları`; former 3.8–3.12 headings are bookmark-preserving normal-body transition sentences.
- F4-078: unique source-backed paragraphs and all citation identities are retained; only citation-free repetitive/defensive conclusions were removed.
- F4-078: F4-079 unverified Israel/Africa narrative, F4-080 counterfactual mushafaha claim, and F4-081 qirāʾa-loss claim remain intentionally unresolved for sequential application.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Holds / validation
- Open HOLD items: none.
- Last validation result: **PASS**.
- Deterministic replay/idempotency: PASS.
- Technical validation: PASS (`work/runtime/F4-078-TECHNICAL-VALIDATION.txt`).
- Bounded visual QA: PASS, 17/17 pages inspected (`work/F4-078-VISUAL-QA.md`).

## Exact next action
Apply F4-079 to the current F4-078 binary. Replace the unverified Israel/Africa tampered-mushaf narrative with the report-approved limited attribution and explicit verification caveat, remove the unsupported motive attribution, preserve all 469 footnote references by semantically reanchoring FNs341–347 rather than deleting them, then run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-078`.
