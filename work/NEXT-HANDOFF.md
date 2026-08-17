# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Current phase: `FOURTH_APPLY`
- Applied but not yet VERIFIED: `F4-001`–`F4-003`
- Ledger remains at PENDING for these three until render QA is closed; do not falsely mark them VERIFIED.
- Next report item after closing that gate: `F4-004`
- Current working DOCX: reconstruct from `artifacts/checkpoints/manuscript-working-bootstrap.docx` with `work/apply_docx_edits.py`
- Expected reconstructed SHA-256: `40504b9d5b41ecae0ae9db64add341f37105e7bae1e8c0c164439ef3078fb5da`
- Last known good commit with persisted binary: `026fe5d382d51a6c31b489a89498946d545587f4`
- Last known good DOCX: `artifacts/checkpoints/manuscript-working-bootstrap.docx`
- Footnote baseline/current after reconstruction: **469 / 469**; references **469 / 469**; orphans 0; dangling 0; duplicate refs 0
- F4-003 footnote ID 2 preserved at the rewritten historical paragraph
- Word/Zotero state: 520 field instructions; ADDIN 466; Zotero 465 item + 1 bibliography; exact field instruction hashes unchanged
- Completed structural changes: none
- Open editorial HOLDs: none
- Operational QA pending: render/visual review. Untouched canonical source exhibits the same LibreOffice conversion hang.
- DO-NOT-REPEAT range: branch/source verification, canonical byte-identity, bootstrap inventory, ledger initialization, bootstrap persistence, F4-001–003 technical application
- Exact next action: run `python work/apply_docx_edits.py <bootstrap-docx> <working-docx>`; confirm expected SHA; complete visual QA; update ledger F4-001–003; commit/push that validation checkpoint; only then apply F4-004.
