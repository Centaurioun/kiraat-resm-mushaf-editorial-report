# APPLICATION STATE

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Source commit verified to contain all authoritative inputs: `b7633f23aa67d26e77da50f56ba4f24e2b1b1518`

## Authoritative sources
- Source manuscript path: `source/manuscript/current/redaktorden_gelen.docx`
- Source manuscript SHA-256: `d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54`
- Source manuscript Git blob SHA-1: `afb77260a59c4eabf5664dd1919c03fc68cc5196`
- Canonical-source decision: only one DOCX candidate exists under `source/manuscript/current/`; the Library long-filename copy was independently confirmed byte-identical by Git blob SHA and size. Canonical source remains unmodified.
- Fourth Report path: `final/fourth-report-v2.md`
- Fourth Report parsed item count: **116**
- Fifth Report path: `final/fifth-report-locked.md`
- Fifth Report parsed item count: **94**

## State machine
- Current phase: `FOURTH_APPLY`
- Last fully completed Fourth Report item: none (F4-001–003 are applied in the reproducible working state but not yet marked VERIFIED because render QA is pending)
- Next Fourth Report item: `F4-004` only after F4-001–003 render QA and ledger checkpoint are closed
- Last fully completed Fifth Report item: none
- Next Fifth Report item: `F5-001` (blocked until Fourth Report validation passes)

## Working document / recovery
- Current working DOCX: **not persisted as a Git binary at this interim recovery checkpoint**; reconstruct from `artifacts/checkpoints/manuscript-working-bootstrap.docx` by running `work/apply_docx_edits.py`.
- Reconstructed working DOCX expected SHA-256: `40504b9d5b41ecae0ae9db64add341f37105e7bae1e8c0c164439ef3078fb5da`
- Last known good commit with persisted DOCX: `026fe5d382d51a6c31b489a89498946d545587f4`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-bootstrap.docx`
- Binary checkpoint limitation: the current GitHub connector exposes text/tree/blob APIs but no local-file upload path; the edited DOCX binary is therefore not falsely claimed as pushed. Reproducible replay code, hashes, and state are persisted instead.

## Footnote state after reconstructed F4-001–003
- Baseline/current genuine footnotes: **469 / 469**
- Baseline/current body references: **469 / 469**
- Genuine footnote ID set: unchanged 1–469
- Footnote text hashes: **exactly unchanged**
- Orphan footnotes: **0**
- Dangling references: **0**
- Duplicate body references: **0**
- F4-003 affected footnote: ID **2**, reference preserved at end of the rewritten historical paragraph.

## Word / Zotero / OOXML state after reconstructed F4-001–003
- Word field instructions: **520 / 520**, exact instruction hashes unchanged
- TOC: 1; PAGEREF: 52; PAGE: 1; ADDIN: 466
- Zotero: 465 item fields + 1 bibliography field, unchanged
- Bookmarks/hyperlinks/comments/tracked revisions/sections: unchanged
- Arabic/RTL inventory: unchanged
- `word/document.xml`: expected changed part
- `word/footnotes.xml`, `word/styles.xml`, `word/numbering.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`: unchanged
- ZIP/package integrity: **PASS**
- XML parse integrity: **PASS**

## Editing state
- F4-001: authoritative Önsöz paragraph replacement applied.
- F4-002: authoritative Önsöz closing paragraph replacement applied.
- F4-003: authoritative Giriş historical paragraph replacement applied; footnote ID 2 preserved.
- Current structural-edit state: no heading/section movement or numbering change yet.
- Open editorial HOLD items: none
- Operational QA pending: DOCX render. The same headless LibreOffice conversion also hangs on the untouched canonical source, indicating an environment/baseline rendering issue rather than an edit-specific regression. Items are not marked VERIFIED until this gate is resolved or a documented equivalent visual QA path is completed.
- Last validation result: **TECHNICAL PASS; RENDER QA PENDING**
- Exact next action: reconstruct F4-001–003 with `work/apply_docx_edits.py`, complete render/visual QA, then update `application-ledger.jsonl` for F4-001–003 and checkpoint before applying F4-004.
