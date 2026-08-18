# FINALIZATION ITEM 4 — PUBLISHING / DELIVERY FREEZE

## Status
**COMPLETED / PASS**

## Frozen delivery artifact
- `artifacts/delivery/kiraatlerin-rivayetinde-resm-i-mushafin-etkisi-final.docx`
- SHA-256: `67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4`
- Size: 348,264 bytes
- Byte-identical to the accepted item-3 candidate; no manuscript mutation occurred during freeze.

## Integrity gates
- ZIP/package integrity: PASS
- Body paragraphs: 674
- Body-text hash: `60c3f29968f6693de7cba0a389d41092528c0bb385a0be9f753bf6742c3463d9`
- Footnote-text hash: `a07e51f7ad77714aa9cdc6254dd0b62daa05bfa6f5a023795ec58f2906fcb0de`
- Genuine footnote references: 469/469
- Orphan/dangling/duplicate: 0/0/0
- Zotero/ADDIN: 466
- TOC/PAGEREF/PAGE: 1/46/1
- Bookmarks: 53/53
- Hyperlinks: 46
- Direct red `FF0000`: 0
- Tracked changes/comments: 0/0
- `w:updateFields=true`
- Deterministic two-pass freeze replay: BYTE_IDENTICAL=PASS
- Visual QA: inherited from the byte-identical item-3 candidate, 112/112 pages PASS.

## Evidence
- Freeze scope: `work/FINALIZATION-ITEM4-SCOPE.md`
- Freeze runner: `work/finalize_freeze_publishing_delivery.py`
- Validator: `work/validate_finalization_item4_delivery.py`
- Accepted application run: `32196971757`
- Replay: `work/runtime/FINALIZATION-ITEM4-REPLAY.txt`
- Checksum: `artifacts/delivery/kiraatlerin-rivayetinde-resm-i-mushafin-etkisi-final.sha256`
- Final receipt: `artifacts/delivery/FINAL-DELIVERY-RECEIPT.txt`
- Exact delivery export run: `32197076508`
- Exact delivery export artifact: `9346210282`

## Harness note
The first item-4 workflow attempt (`32196899464`) failed only in the new validator because its footnote hash was calculated with a different serialization convention than the already accepted item-3 validator. The freeze copy itself had already passed byte-identity checks. The validator was corrected to use the established sorted `footnote-id + text` convention and the accepted rerun passed every gate. This was a test-harness defect, not a manuscript defect; no failed-attempt delivery artifact was committed.

## Finalization result
Items 1–4 are complete. The repository finalization phase is closed. The frozen DOCX above is the final publishing/delivery artifact unless a new, separately adjudicated defect is discovered.
