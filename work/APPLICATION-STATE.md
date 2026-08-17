# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint commit: `SELF`
- Source commit: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`
- Canonical source: `source/manuscript/current/redaktorden_gelen.docx`
- Canonical SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: 116 items, blob `e880124fb0bdb72afb29cf10927e2dd15bae0676`
- Fifth Report: 94 items, blob `b2e184bf45c13fb548cd13ee2e4f829a52b4bb69`

## State machine
- Phase: `FOURTH_APPLY`
- Last fully completed Fourth item: `F4-022`
- Next Fourth item: `F4-023`
- Fifth Report: blocked until Fourth completion; next `F5-001`.
- DO-NOT-REPEAT: bootstrap and `F4-001–022`.

## Deterministic recovery pipeline
1. Canonical source → `work/apply_docx_edits.py` through F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. Output → `work/apply_f4_012_017.py` through F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. Output → `work/apply_f4_018_022.py` through F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
- Current reproducible logical DOCX SHA-256: `209b3a6e7719f44b7e9ed2b1a25b2992d00cdc7b6afa7e580fccd6f5d81c36f1`.
- Current body paragraphs: **700** (baseline 711).
- Current stage replay idempotency: **PASS, byte-identical**.
- Ledger through F4-022: commit `10bcd454d33399979e83c7d6ee90dfad34fe191f`, content SHA `fea2a58c97569bd2bd34bdc6dcdd0cb571eab4e7`.
- Edited binary is not falsely claimed persisted; connector lacks local binary DOCX upload. Durable recovery remains canonical source + replay stages + exact hashes + ledger + validation.

## Integrity
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged.
- Orphans/dangling/duplicates: **0/0/0**.
- `word/footnotes.xml`: exact baseline hash.
- Word fields: **520/520** — TOC 1, PAGEREF 52, REF 0, PAGE 1, ADDIN 466.
- Zotero: **465 item + 1 bibliography**, unchanged.
- Protected core OOXML unchanged except expected `word/document.xml`; ZIP/XML **PASS/PASS**.

## F4-018–022 result
- F4-018: APPLIED — cem distinction rewritten; notes 31 and 32 preserved at their supported propositions.
- F4-019: APPLIED — Hârice corrected from daughter to son, `Hârice b. Zeyd (ö. 100/718-19)`; note 35 preserved.
- F4-020: APPLIED — Ebû Bekir-era material standardized as `suhuf`; paragraph notes 43/44/45 unchanged.
- F4-021: APPLIED — malformed Zeyd b. Sâbit sentence replaced with report-approved wording; note inventory 34–37 unchanged.
- F4-022: APPLIED — Mervân b. Hakem death date corrected to `65/685`, terminology corrected to `sahifeler`, note 44 retained.
- Open HOLDs: none.

## Visual QA
- QA-only first 90 body paragraphs rendered as **21 pages**.
- Pages 13–21 inspected; key affected pages 13–15 additionally inspected at full resolution.
- No clipping, overlap, footnote overflow, unintended style/color propagation, or edit-caused pagination defect.
- Existing red editorial notes/markings outside these report items remain source content for later items.
- Final full-document all-page QA remains mandatory.

- Last validation: **PASS — F4-018–022 technical + citation preservation + byte-idempotency + 21-page bounded visual QA**.
- Exact next action: apply `F4-023` from CURRENT F4-022 state, then proceed sequentially.