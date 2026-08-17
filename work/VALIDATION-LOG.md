# VALIDATION LOG

## Bootstrap baseline — 2026-08-17
Source SHA-256 `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`; ZIP/XML PASS; genuine footnotes/references 469/469; orphans/dangling/duplicates 0/0/0; fields 520; TOC 1; PAGEREF 52; PAGE 1; ADDIN 466; Zotero item 465 + bibliography 1; bookmarks 53/53; hyperlinks 52; comments/revisions 0; sections 10; F4 count 116; F5 count 94. Result **PASS**.

## Bootstrap persistence — 2026-08-17
Commit `026fe5d382d51a6c31b489a89498946d545587f4`; recovery DOCX equals canonical source blob. Result **PASS**.

## F4-001–003 — 2026-08-17
Replay commit `46a5014e1c87bce2bceda20278481055975ccb39`; reconstructed SHA `40504b9d5b41ecae0ae9db64add341f37105e7bae1e8c0c164439ef3078fb5da`; footnotes/fields/Zotero/protected OOXML preserved; 12-page bounded QA slice inspected 12/12, including footnote 2. Verification commit `551ae04f8be22d979432011d99d1c81ccbabf8be`. Result **PASS**.

## F4-004–005 technical — 2026-08-17
- F4-004 current paragraph index 23: target sentence replaced only; genuine footnote 3 and all surrounding paragraph content preserved.
- F4-005 current paragraph index 24: target final sentence replaced only.
- Current SHA-256: `567f7847958364b27d68c45c073481c9d7e6030bba561d7d0dc011d8c0cf6355`
- ZIP/XML: **PASS/PASS**
- Footnotes/references: **469/469**; sets unchanged; orphans/dangling/duplicates 0/0/0
- `word/footnotes.xml`: unchanged from baseline
- Word fields and field types: exact baseline match; Zotero 465 + 1 unchanged
- Bookmarks/hyperlinks/comments/revisions/sections/Arabic/RTL: unchanged
- Protected core OOXML unchanged except expected `word/document.xml`
- Replay script commit: `8ba3fe378240d3d42e0c62b0cc7e9936c907bdf8`
- Replay on already-correct F4-001–005 DOCX returns all items `ALREADY_SATISFIED` and produces byte-identical SHA: **IDEMPOTENCY PASS**

## F4-004–005 visual — 2026-08-17
- QA-only slice: body paragraphs 0–59, 12 rendered pages.
- Pages 1–4 and 10–12: pixel-hash unchanged from prior validated slice.
- Pages 5–9: reflowed and individually visually inspected; no clipping, overlap, footnote overflow, abnormal whitespace or unexpected formatting caused by edits.
- Page 5: F4-004 replacement clean; footnote 3 marker/text preserved.
- Page 6: F4-005 replacement clean.
- Result: **PASS**.

## F4-006 high-risk structural checkpoint — 2026-08-17
- Application/recovery replay commit: `dd41275b91dfaa7dffce0cb43e7b5e823db73756`.
- Ledger recording commit: `90f473c52b404507eb0ccbb5928d65ccfa179f34`.
- Pre-F4-006 verified input SHA-256: `567f7847958364b27d68c45c073481c9d7e6030bba561d7d0dc011d8c0cf6355` — exact match to F4-001–005 state.
- F4-006 output SHA-256: `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`.
- Replay on F4-006 output: F4-001–006 all already satisfied; rerun output SHA identical. **IDEMPOTENCY PASS**.
- Body paragraphs: **711 baseline → 705 current**.
- Accepted three F4-006 replacement paragraphs each occur exactly once.
- Removed only six true repetition/superseded detailed-plan paragraphs from the former contiguous Giriş cluster.
- Preserved unique paragraphs beginning `Çalışmanın son halkasında...`, `Yöntem bakımından kitap...`, and `Araştırmanın kaynak zemini...`; normalized text hashes exactly unchanged versus F4-005.
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged; orphans/dangling/duplicates **0/0/0**.
- Footnote 7 remains in the preserved source-backed paragraph; `word/footnotes.xml` unchanged.
- Word fields: **520/520**; TOC 1; PAGEREF 52; REF 0; PAGE 1; ADDIN 466; Zotero 465 item + 1 bibliography.
- Protected core OOXML unchanged except expected `word/document.xml`; ZIP/XML **PASS/PASS**.
- Bounded QA-only slice rendered as **14 pages**; inspected **14/14**. Result **PASS — F4-006 STRUCTURAL CHECKPOINT VALIDATED**.

## F4-007–011 checkpoint — 2026-08-17
- Deterministic replay/application commit: `86f99b2186711a7d94159d9c1b7413b0248a0c5c`.
- Ledger recording commit: `ed22ec36a0e94c04f58cc956f08a5d113f25443c`.
- Verified input state through F4-006 SHA-256: `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`.
- Output SHA-256 through F4-011: `577badf47a383f0fed2324efc5e984c1dec7ca258998b328a858360f8805a2fd`.
- Replay on the F4-011 output is byte-identical; output SHA remains `577badf47a383f0fed2324efc5e984c1dec7ca258998b328a858360f8805a2fd`. **IDEMPOTENCY PASS**.
- Body paragraph count: **705 → 704** in this batch; baseline remains 711.
- F4-007: Giriş closing paragraph replaced with the accepted transition into Birinci Bölüm. No protected structure affected. F5-014 overlap recorded; Fifth must not restore the removed negative research-question paragraph.
- F4-008: prior footnote-placement preflight risk resolved semantically rather than by mechanical relocation. The revised evidence-level paragraph retains the source-backed Abdülmuttalib/Me’mûn proposition with footnote **15**, and the `bismikellâhümme` proposition with footnote **16**. Neither citation was attached to unsupported generic prose.
- F4-009: `otaya koymaktadır` corrected to `ortaya koymaktadır`; the awkward first mini-synthesis no longer survives because F4-011 correctly removes the redundant conclusion.
- F4-010: malformed Varaka b. Nevfel sentence repaired; existing footnote refs 12 and 13 remain on their original supported clauses.
- F4-011: two 1.1 concluding syntheses consolidated to one accepted synthesis; one true redundant paragraph removed. F5-015 overlap recorded.
- Genuine footnotes/references: **469/469**; exact ID/reference sets unchanged; orphans/dangling/duplicates **0/0/0**.
- `word/footnotes.xml`: byte-hash exact baseline match.
- Word field instructions: **520/520**; field inventory exact baseline match (TOC 1; PAGEREF 52; REF 0; PAGE 1; ADDIN 466).
- Zotero fields: **465 item + 1 bibliography**, unchanged.
- `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`: exact baseline hashes; expected content changes confined to `word/document.xml` among protected core parts.
- All XML parts parse; ZIP/package integrity **PASS**.
- Canonical source SHA-256 rechecked and remains `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`.
- Bounded QA-only slice: first 65 current body paragraphs rendered as **15 pages**. All **15/15** pages visually inspected.
- First visual pass detected an inherited red run style on the newly inserted F4-011 synthesis. Replay code was corrected to choose a normal, non-red source run; affected pages were re-rendered and re-inspected. Final render shows normal black text.
- Final visual result: no clipping, overlap, footnote overflow, abnormal whitespace, unintended color/font propagation or pagination defect caused by F4-007–011. Existing unrelated red editorial markings elsewhere remain source content for later report items.
- Result: **PASS — F4-007–011 CHECKPOINT VALIDATED**.