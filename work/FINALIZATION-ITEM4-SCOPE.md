# FINALIZATION ITEM 4 — PUBLISHING / DELIVERY FREEZE

- Source candidate: `artifacts/finalization/manuscript-editorial-marks-cleaned.docx`
- Source SHA-256: `67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4`
- Operation: immutable byte-for-byte copy only; no Word/LibreOffice save, no OOXML rewrite, no text or formatting edit.
- Delivery path: `artifacts/delivery/kiraatlerin-rivayetinde-resm-i-mushafin-etkisi-final.docx`
- Required gates: source SHA match, ZIP/package integrity, byte identity, deterministic replay/idempotency, body/footnote text hashes, references, Zotero/ADDIN, fields, bookmarks, hyperlinks, red-format absence, tracked-change/comment absence, and inherited 112/112 visual QA from the byte-identical item-3 candidate.
- Item 4 closes FINALIZATION only if every gate passes.
