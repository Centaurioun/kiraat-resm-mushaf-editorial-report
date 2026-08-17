# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint commit: `SELF`
- Canonical source: `source/manuscript/current/redaktorden_gelen.docx`
- Canonical SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: 116 items, blob `e880124fb0bdb72afb29cf10927e2dd15bae0676`
- Fifth Report: 94 items, blob `b2e184bf45c13fb548cd13ee2e4f829a52b4bb69`

## State machine
- Phase: `FOURTH_APPLY`
- Last fully completed Fourth item: `F4-042`
- Next Fourth item: `F4-043`
- Fifth Report remains blocked until Fourth completion; next `F5-001`.
- DO-NOT-REPEAT: bootstrap and `F4-001–042`.

## Deterministic recovery pipeline
1. `work/apply_docx_edits.py` → F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. `work/apply_f4_012_017.py` → F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. `work/apply_f4_018_022.py` → F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
4. `work/apply_f4_023_027.py` → F4-027 (`a7e987b2ae84ada927b082974f5d90f4896d43d4`).
5. `work/apply_f4_028_032.py` → F4-032 (`30bf55f09fa02d4b805d6695c149061f2b24031d`).
6. `work/apply_f4_033_037.py` → F4-037 (`58d891d493331863b9f8fdfb0436267a97d33f4e`).
7. `work/apply_f4_038_042.py` → F4-042 (`89f8263a3fb90454727660654d103e6e2c132c16`).
- Current reproducible logical DOCX SHA-256: `e23e7c57a52b5ef6f95c3f36ea2ab614274464bff6e65803198c5c868cb1181c`.
- Current body paragraphs: **696**.
- Latest-stage replay: **PASS, byte-identical**.
- Ledger through F4-042: commit `5969a0c676c80dadb1963c4245127d617c101f99`, content SHA `4c028ef704fb44b389fc7324e9448dc9cb43ab47`; exactly 210 records.
- Edited DOCX binary is not falsely claimed persisted because the connector has no local binary upload parameter. Durable recovery remains canonical source + replay pipeline + exact hashes + ledger + validation evidence.

## Integrity
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged.
- Orphans/dangling/duplicates: **0/0/0**.
- Word fields: **520/520** — TOC 1, PAGEREF 52, REF 0, PAGE 1, ADDIN 466.
- Zotero: **465 item + 1 bibliography**.
- RTL inventory: **365/365**; bookmarks 53/53; hyperlinks 52; comments/revisions 0/0; sections 10.
- `word/footnotes.xml`, styles, numbering, settings and document relationships: baseline-identical.
- ZIP/XML parse integrity: **PASS/PASS**.

## F4-038–042 result
- F4-038 APPLIED: Ebû Ubeyde paragraph restrained to an early-stage significance claim; footnote 108 retained.
- F4-039 APPLIED: Dânî and Ebû Dâvud repetitions replaced by the two report-approved concise formulations; footnotes 110/111/112 retained. The unique intervening Dânî/kırâat paragraph was preserved.
- F4-040 APPLIED: Zerkeşî paragraph now distinguishes kıyasî imlâ from transmitted mushaf writing and avoids assigning a special conscious purpose to every writing difference; notes 113–115 preserved in order.
- F4-041 APPLIED: Motzki/Sinai evidence is limited to the historical coexistence of oral and written transmission and is no longer presented as direct proof of the book's whole thesis; note 119 retained. The separate Déroche paragraph remains because the report's explicit replacement target did not authorize deleting it.
- F4-042 APPLIED: report-approved distinction inserted immediately after the protected 1.8 heading between historical origin/tevkîfîlik and later normative binding force; heading bookmarks remain intact.
- Open HOLDs: none.

## Visual QA
- QA-only first 175 current body paragraphs rendered as **35 pages**; all 35 reviewed in contact-sheet form.
- Pages 26–29, covering F4-038–042 and the transition into 1.8, inspected at full resolution.
- No clipping, overlap, footnote overflow, abnormal whitespace, unintended style/color propagation or edit-caused pagination defect.
- Final all-page full-document acceptance remains mandatory.

- Last validation: **PASS — F4-038–042 technical + citation semantics + byte-idempotency + 35-page bounded visual QA**.
- Exact next action: apply `F4-043` from CURRENT F4-042 state and continue sequentially.