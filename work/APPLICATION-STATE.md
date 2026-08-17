# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current branch HEAD / checkpoint commit: `SELF` — resolve as the branch HEAD containing this state file
- Replay/application commit through current boundary: `86f99b2186711a7d94159d9c1b7413b0248a0c5c`
- Ledger checkpoint commit through current boundary: `ed22ec36a0e94c04f58cc956f08a5d113f25443c`
- Source commit: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`
- Source manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Source manuscript Git blob: `afb77260a59c4eabf5664dd1919c03fc68cc5196`
- Fourth Report: `final/fourth-report-v2.md` — **116 items**, blob `e880124fb0bdb72afb29cf10927e2dd15bae0676`
- Fifth Report: `final/fifth-report-locked.md` — **94 items**, blob `b2e184bf45c13fb548cd13ee2e4f829a52b4bb69`

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: `F4-011`
- Next Fourth Report item: `F4-012`
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (blocked until Fourth Report completion)

## Working / recovery
- Current logical working DOCX: deterministic output of `work/apply_docx_edits.py` applied to the canonical source.
- Current working SHA-256 through F4-011: `577badf47a383f0fed2324efc5e984c1dec7ca258998b328a858360f8805a2fd`
- Current working body paragraph count: **704** (baseline 711; F4-006 state 705).
- Last known good reproducible edited-state commit: `86f99b2186711a7d94159d9c1b7413b0248a0c5c`
- Replay idempotency through F4-011: **PASS, byte-identical**; rerun SHA remains `577badf47a383f0fed2324efc5e984c1dec7ca258998b328a858360f8805a2fd`.
- Last persisted DOCX binary in GitHub remains `artifacts/checkpoints/manuscript-working-bootstrap.docx` at commit `026fe5d382d51a6c31b489a89498946d545587f4`.
- Binary persistence note: current connector does not accept a local binary DOCX file parameter. No false edited-binary persistence claim is made; recovery is deterministic from canonical source + replay script + exact hashes + ledger + validation evidence.

## Footnotes / citations
- Baseline/current genuine footnotes: **469 / 469**
- Baseline/current body references: **469 / 469**
- Genuine footnote ID set and body reference ID set unchanged.
- Orphans/dangling/duplicate references: **0 / 0 / 0**
- `word/footnotes.xml`: byte-hash unchanged from canonical baseline.
- F4-003: footnote 2 retained.
- F4-004: footnote 3 retained.
- F4-006: footnote 7 retained with its source-backed paragraph.
- F4-008: prior placement risk resolved without guessing. Footnote 15 remains attached to the Abdülmuttalib/Me’mûn proposition; footnote 16 remains attached to the `bismikellâhümme` proposition.
- F4-010: footnote references 12 and 13 remain on their original supported clauses.

## Word / Zotero / OOXML
- Word field instructions baseline/current: **520 / 520**
- TOC 1; PAGEREF 52; REF 0; PAGE 1; ADDIN 466
- Zotero item fields 465; Zotero bibliography field 1
- Aggregate field inventory unchanged.
- Bookmarks: 53 starts / 53 ends; hyperlinks: 52; comments: 0; tracked revisions: 0; sections: 10.
- Arabic/RTL inventory unchanged.
- ZIP/package integrity: **PASS**; XML parse integrity: **PASS**.
- Protected core OOXML unchanged except expected `word/document.xml`.

## Completed edits
- F4-001: VERIFIED
- F4-002: VERIFIED
- F4-003: VERIFIED
- F4-004: VERIFIED
- F4-005: VERIFIED
- F4-006: STRUCTURALLY_APPLIED + validated checkpoint
- F4-007: APPLIED — Giriş closing transition; overlaps F5-014, which must not restore the removed negative research-question paragraph.
- F4-008: APPLIED — evidence-level rewrite with semantic preservation of footnotes 15 and 16; prior placement conflict resolved safely.
- F4-009: APPLIED — `otaya` typo repaired; redundant mini-conclusion wording target superseded by F4-011 consolidation.
- F4-010: APPLIED — malformed Varaka b. Nevfel sentence repaired; footnotes 12/13 preserved.
- F4-011: STRUCTURALLY_APPLIED — two redundant 1.1 conclusions consolidated to one; overlaps F5-015, whose later stylistic contribution may not alter the Fourth Report scientific frame.
- Open HOLD items: none at this checkpoint.

## Visual QA
- Full-document PDF export remains a baseline renderer issue shared by the untouched source; this does not waive final all-page acceptance.
- F4-007–011 bounded QA slice: current first 65 body paragraphs rendered as **15 pages**.
- **15/15 pages visually inspected.** The first render exposed inherited red run styling on the new F4-011 synthesis; replay code was corrected to select a normal run, the affected pages were re-rendered and re-inspected.
- Final affected-range result: no clipping, overlap, footnote overflow, abnormal whitespace, unexpected font/color propagation or pagination defect caused by F4-007–011.

- Last validation result: **PASS — F4-007–011 technical + citation semantics + idempotency + bounded visual QA**
- DO-NOT-REPEAT: bootstrap and `F4-001–011`
- Exact next action: preflight and apply `F4-012` from the CURRENT F4-011 logical DOCX, explicitly preserving or scientifically resolving footnotes 19, 20 and 21 before any structural consolidation of the 1.2 opening.