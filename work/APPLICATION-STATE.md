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
- Last fully completed Fourth item: `F4-037`
- Next Fourth item: `F4-038`
- Fifth Report remains blocked until Fourth completion; next `F5-001`.
- DO-NOT-REPEAT: bootstrap and `F4-001–037`.

## Deterministic recovery pipeline
1. `work/apply_docx_edits.py` → F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. `work/apply_f4_012_017.py` → F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. `work/apply_f4_018_022.py` → F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
4. `work/apply_f4_023_027.py` → F4-027 (`a7e987b2ae84ada927b082974f5d90f4896d43d4`).
5. `work/apply_f4_028_032.py` → F4-032 (`30bf55f09fa02d4b805d6695c149061f2b24031d`).
6. `work/apply_f4_033_037.py` → F4-037 (`58d891d493331863b9f8fdfb0436267a97d33f4e`).
- Current reproducible logical DOCX SHA-256: `94bbdeec878f57d4d97f54ad393bddc79074230ec69886e1f0a455bbe483ed3a`.
- Current body paragraphs: **695** (baseline 711).
- Latest-stage replay: **PASS, byte-identical**.
- Ledger through F4-037: commit `b0faacdd905a2da8b03a758ace888c3534a85102`, content SHA `307b9254459b394e01d9c016b50d20437cdcf5e8`; exactly 210 records.
- Edited DOCX binary is not falsely claimed persisted because the connector has no local binary upload parameter. Durable recovery remains canonical source + replay pipeline + exact hashes + ledger + validation evidence.

## Integrity
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged.
- Orphans/dangling/duplicates: **0/0/0**.
- Word fields: **520/520** — TOC 1, PAGEREF 52, REF 0, PAGE 1, ADDIN 466.
- Zotero: **465 item + 1 bibliography**.
- RTL inventory: **365/365**.
- Bookmarks 53/53; hyperlinks 52; comments 0; tracked revisions 0; sections 10.
- `word/footnotes.xml`, styles, numbering, settings and document relationships: baseline-identical.
- ZIP/XML parse integrity: **PASS/PASS**.

## F4-033–037 result
- F4-033 APPLIED: 1.5 now closes with a direct transition from historical mushaf distribution to the conceptual discussion of `resm` and `resm-i Osmânî`; no Markdown backticks were inserted into the DOCX.
- F4-034 STRUCTURALLY_APPLIED: three meta-heavy 1.6 opening paragraphs consolidated to one direct conceptual frame; two redundant paragraphs removed.
- F4-035 APPLIED: Cevherî is now used only for the lexical meaning of `resm`; technical development is attributed to later resm literature. Footnote 101 remains on the limited writing-order proposition, 102 on Cevherî's lexical evidence, and 103 on Dânî/resm-literature technical development.
- F4-036 APPLIED: 1.6.2 opens directly with the technical definition; footnote 100 remains on the technical-use proposition.
- F4-037 APPLIED: Kastallânî main-text work note removed and correct first-use date `(ö. 923/1517)` retained; Bâkıllânî's repeated malformed date/work note removed because he had already appeared earlier. Footnote 105's internal editor note is intentionally deferred to F4-112 rather than silently edited under the wrong report item.
- Open HOLDs: none.

## Visual QA
- QA-only first 155 current body paragraphs rendered as **32 pages**; all 32 reviewed in contact-sheet form.
- Pages 23–25 and 30–32 inspected at full resolution.
- First visual pass exposed inherited italics across the new F4-035 paragraph because the source paragraph began with an italic `Resm` run. The replay helper was corrected to avoid italic/bold/red/protected template runs; the document was regenerated and re-rendered. Final F4-035 text is normal black regular body text.
- No clipping, overlap, footnote overflow, unintended style/color propagation or edit-caused pagination defect after correction.
- Final full-document all-page acceptance remains mandatory.

- Last validation: **PASS — F4-033–037 technical + citation semantics + byte-idempotency + 32-page bounded visual QA**.
- Exact next action: apply `F4-038` from CURRENT F4-037 state and continue sequentially.