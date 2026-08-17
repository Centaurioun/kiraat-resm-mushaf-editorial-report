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
- Last fully completed Fourth item: `F4-027`
- Next Fourth item: `F4-028`
- Fifth Report remains blocked; next `F5-001` after Fourth completion.
- DO-NOT-REPEAT: bootstrap and `F4-001–027`.

## Deterministic recovery pipeline
1. `work/apply_docx_edits.py` → F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. `work/apply_f4_012_017.py` → F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. `work/apply_f4_018_022.py` → F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
4. `work/apply_f4_023_027.py` → F4-027 (`a7e987b2ae84ada927b082974f5d90f4896d43d4`).
- Current reproducible logical DOCX SHA-256: `fe24f174ad7826dba8045a2584bc62e1b8a6ced867c8fbf2041da272f8fc3448`.
- Body paragraphs: **700**.
- Latest stage replay: **PASS, byte-identical**.
- Ledger through F4-027: commit `d06c188c7130336b9a5f672b95f0f0ad63959caf`, content SHA `9abcca5c4dcf1cce93b13dd0b2a163cfd468bcb4`.

## Integrity
- Genuine footnotes/references **469/469**; orphan/dangling/duplicate **0/0/0**.
- `word/footnotes.xml`: baseline-identical.
- Word fields **520/520**; Zotero **465 item + 1 bibliography**.
- Protected core OOXML unchanged except expected `word/document.xml`; ZIP/XML **PASS/PASS**.

## F4-023–027 result
- F4-023 APPLIED: direct Mervân→yedi harf/arza causal mechanism replaced by source-level distinction.
- F4-024 APPLIED: arza-i âhire framed as an explanatory view rather than certain historical mechanism; genuine footnote 49 retained on the corresponding arza/son-mukabele proposition.
- F4-025 APPLIED: Ebû Bekir cem restored to written-memory complementarity.
- F4-026 APPLIED: dramatic conflict language reduced; first body occurrence of Taberî corrected to `(ö. 310/923)` and work note removed; footnote 66 retained on concrete reading-variation evidence.
- F4-027 APPLIED: `tam baş senede` removed without inventing a duration; note 63 unaffected.
- Open HOLDs: none.

## Visual QA
- QA-only first 100 current body paragraphs rendered as **23 pages**.
- Pages 15–23 inspected; key affected pages 15, 16 and 19 separately inspected full resolution.
- No clipping, overlap, footnote overflow, or unintended styling/pagination defect caused by F4-023–027.
- Final all-page full-document QA remains mandatory.

- Last validation: **PASS — F4-023–027 technical + source/citation placement + byte-idempotency + 23-page bounded visual QA**.
- Exact next action: apply `F4-028` from CURRENT F4-027 state and continue sequentially.