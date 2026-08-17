# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Branch/checkpoint HEAD: `SELF` — resolve as the current branch HEAD containing this handoff
- Validated F4-006 checkpoint commit: `a0679975bcaf2121eafd397255e6e649daccdbb7`
- F4-007/F4-008 preflight evidence commit: `4f4d6e664ad49590c6ca72b23e8fe1396751946a`
- Phase: `FOURTH_APPLY`

- Last completed: `F4-006`
- Next: `F4-007`

- Current logical DOCX: deterministic replay output of `work/apply_docx_edits.py` from canonical source
- Current working SHA-256: `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`
- Current body paragraph count: **705**
- Last known good reproducible commit: `dd41275b91dfaa7dffce0cb43e7b5e823db73756`
- Last known good logical DOCX SHA-256: `33743240d3bd6e1f5eda2efabf8ef5dfa66cbec9a5f655923206563ab605bb93`
- Last persisted DOCX binary: `artifacts/checkpoints/manuscript-working-bootstrap.docx` at commit `026fe5d382d51a6c31b489a89498946d545587f4`
- Binary note: edited DOCX binary is not claimed as GitHub-persisted because the current connector does not accept a local binary file parameter. Recovery is deterministic from canonical source + `work/apply_docx_edits.py` and verified by exact SHA.

- Source SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Fourth Report: 116 items, blob `e880124fb0bdb72afb29cf10927e2dd15bae0676` unchanged
- Fifth Report: 94 items, blob `b2e184bf45c13fb548cd13ee2e4f829a52b4bb69` unchanged

- Footnotes baseline/current: **469/469**
- Body references baseline/current: **469/469**
- Orphans: **0**
- Dangling references: **0**
- Duplicate references: **0**
- Footnote 7: retained with preserved F4-006 source-backed paragraph

- Word fields baseline/current: **520/520**
- TOC 1; PAGEREF 52; REF 0; PAGE 1; ADDIN 466
- Zotero: **465 item + 1 bibliography**, unchanged
- Protected OOXML unchanged except expected `word/document.xml`
- ZIP/XML: **PASS/PASS**

- Completed structural changes: F4-006 Giriş scope/method/contribution/chapter-plan consolidation; six repetitive/superseded paragraphs removed; three unique source-backed intervening paragraphs preserved exactly; downstream paragraph indices must not be reused from the pre-F4-006 structure.
- Open HOLDs: none at the durable completed boundary.

- Validation: F4-006 replay idempotency **PASS, byte-identical**; bounded current paragraphs 0–59 render = **14 pages**, visually inspected **14/14**, PASS.
- Full final all-page visual QA remains mandatory at `FINAL_VALIDATE`.

## Preflight immediately ahead
- Read `work/PREFLIGHT-F4-007-008.md` before applying F4-007/F4-008.
- F4-007 target is uniquely resolved, contains no footnote/field/bookmark/RTL protected structures, and overlaps F5-014. Fourth Report replacement must be applied first; Fifth must not later restore the removed negative research-question sentence.
- F4-008 target contains genuine footnote references **15 and 16**. Footnote 16 is specifically attached to the unique `bismikellâhümme` proposition, while F4-008's proposed replacement omits that proposition. Do not append footnote 16 to a generic replacement sentence. If no scientifically valid surviving destination is established, record `FOOTNOTE_PLACEMENT_CONFLICT` rather than guessing or deleting the note.

- DO-NOT-REPEAT: bootstrap and `F4-001–006`.
- Exact next action: apply F4-007 from the CURRENT F4-006 state only after updating the deterministic replay path and ledger in a checkpoint-safe way; then confront F4-008's documented footnote-placement issue explicitly before changing its paragraph.
