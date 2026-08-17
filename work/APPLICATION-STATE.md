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
- Last fully completed Fourth item: `F4-032`
- Next Fourth item: `F4-033`
- Fifth Report remains blocked until Fourth completion; next `F5-001`.
- DO-NOT-REPEAT: bootstrap and `F4-001–032`.

## Deterministic recovery pipeline
1. `work/apply_docx_edits.py` → F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. `work/apply_f4_012_017.py` → F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. `work/apply_f4_018_022.py` → F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
4. `work/apply_f4_023_027.py` → F4-027 (`a7e987b2ae84ada927b082974f5d90f4896d43d4`).
5. `work/apply_f4_028_032.py` → F4-032 (`30bf55f09fa02d4b805d6695c149061f2b24031d`).
- Current reproducible logical DOCX SHA-256: `7623dbd834b79effef62991932ec3d506cb7d6e4b77db0c976c495b50a24b127`.
- Current body paragraphs: **697** (baseline 711).
- Latest-stage replay: **PASS, byte-identical**.
- Ledger through F4-032: commit `75a27b5c7be2863ae25b1b37a50a768021fae6c0`, content SHA `0154d4b4fa14f0db27049005e61a64b4bac97488`; exactly 210 records.
- Edited DOCX binary is not falsely claimed persisted because the connector has no local binary upload parameter. Durable recovery remains canonical source + replay pipeline + hashes + ledger + validation.

## Integrity
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged.
- Orphans/dangling/duplicates: **0/0/0**.
- Word fields: **520/520** — TOC 1, PAGEREF 52, PAGE 1, ADDIN 466.
- Zotero: **465 item + 1 bibliography**.
- RTL inventory: **365/365**, unchanged from baseline.
- Bookmarks 53/53; hyperlinks 52; comments 0; tracked revisions 0; sections 10.
- `word/footnotes.xml`, styles, numbering, settings and document relationships: baseline-identical.
- ZIP/XML parse integrity: **PASS/PASS**.

## F4-028–032 result
- F4-028 APPLIED: second `Hülasa` closure replaced by direct transition into the mushaf-count section.
- F4-029 STRUCTURALLY_APPLIED: one cautious multi-rivâyet synthesis replaces the new six-copy certainty. Footnote 88 remains only on Kevserî's own view. Three uncited repetition/certainty paragraphs were removed because leaving them would directly undo the report correction.
- F4-030 APPLIED: Ebû Şâme corrected to `(ö. 665/1267)`; Ahvâzî death date omitted as requested.
- F4-031 APPLIED: `(ö. ?)` removed after Amr b. Kays.
- F4-032 APPLIED: contemporary-literature frame corrected, including Hamîdullah `(ö. 2002)`; the later sentence claiming a common six-copy consensus was replaced with an explicit non-convergence statement while notes 94/95 remained untouched.
- Open HOLDs: none.

## Visual QA
- First 115 current body paragraphs rendered as **25 pages**; contact-sheet scan completed and affected pages 20–25 inspected at full resolution.
- No clipping, overlap, footnote overflow, unintended red/style propagation or batch-caused pagination defect.
- Existing red editorial notes outside this batch remain source material for later report items.
- Final full-document all-page acceptance remains mandatory.

- Last validation: **PASS — F4-028–032 technical + citation semantics + byte-idempotency + 25-page bounded visual QA**.
- Exact next action: apply `F4-033` from CURRENT F4-032 state, then proceed sequentially.