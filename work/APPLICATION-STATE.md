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
- Last fully completed Fourth item: `F4-047`
- Next Fourth item: `F4-048`
- Fifth Report remains blocked until Fourth completion; next `F5-001`.
- DO-NOT-REPEAT: bootstrap and `F4-001–047`.

## Deterministic recovery pipeline
1. `work/apply_docx_edits.py` → F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. `work/apply_f4_012_017.py` → F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. `work/apply_f4_018_022.py` → F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
4. `work/apply_f4_023_027.py` → F4-027 (`a7e987b2ae84ada927b082974f5d90f4896d43d4`).
5. `work/apply_f4_028_032.py` → F4-032 (`30bf55f09fa02d4b805d6695c149061f2b24031d`).
6. `work/apply_f4_033_037.py` → F4-037 (`58d891d493331863b9f8fdfb0436267a97d33f4e`).
7. `work/apply_f4_038_042.py` → F4-042 (`89f8263a3fb90454727660654d103e6e2c132c16`).
8. `work/apply_f4_043_047.py` → F4-047; durable specification `work/F4-043-047-REPLAY-SPEC.md`.
- Current reproducible logical DOCX SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.
- Current body paragraphs: **696**.
- Latest-stage replay: **PASS, byte-identical**.
- Ledger through F4-047: commit `86ebf507741218a7b2f38c3008f2eac97c825c53`, content SHA `2b2e1cd1f9c025a395c25590206c917c61ba9c45`; exactly 210 records.
- Edited DOCX binary is not falsely claimed persisted because the connector has no local binary upload parameter. Durable recovery remains canonical source + replay pipeline + exact hashes + ledger + validation evidence.

## Integrity
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged.
- Orphans/dangling/duplicates: **0/0/0**.
- Word fields: **520/520** — TOC 1, PAGEREF 52, REF 0, PAGE 1, ADDIN 466.
- Zotero: **465 item + 1 bibliography**.
- RTL inventory: **365/365**; bookmarks 53/53; hyperlinks 52; comments/revisions 0/0; sections 10.
- `word/footnotes.xml`, styles, numbering, settings and document relationships: baseline-identical.
- ZIP/XML parse integrity: **PASS/PASS**.

## F4-043–047 result
- F4-043 APPLIED: direct conscious-design inference removed; compatibility with transmitted readings separated from historical causation. Footnote 142 preserved.
- F4-044 APPLIED: hazf definition corrected and repeated conclusion shortened; notes 145 and 151 preserved, with note 151 left on its source-specific examples rather than moved to the synthesis.
- F4-045 APPLIED: Ca‘berî corrected to `(ö. 732/1332)`; notes 158–163 preserved.
- F4-046 APPLIED: hemze causal overclaim replaced by early-writing/edâ formulation; notes 166–168 preserved.
- F4-047 APPLIED: Bakara reference corrected to `2/269`; existing Arabic/RTL runs reused; unsupported `fonetik zorunluluk` reasoning removed. Note 172 is retained only on the limited statement that some sources offer meaning-centred interpretations.
- Open HOLDs: none.

## Visual QA
- QA-only first 190 current body paragraphs rendered as **38 pages**; all 38 contact-scanned.
- Pages 32–38 inspected at full resolution.
- No clipping, overlap, footnote overflow, abnormal whitespace, unintended style propagation or edit-caused pagination defect. Arabic/RTL examples render correctly.
- Final all-page full-document acceptance remains mandatory.

- Last validation: **PASS — F4-043–047 technical + citation semantics + byte-idempotency + 38-page bounded visual QA**.
- Exact next action: apply `F4-048` from CURRENT F4-047 state and continue sequentially.