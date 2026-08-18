# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `79024ef4f3c894e8c0eb79069a9ffa2303b4b9e7` plus this metadata checkpoint commit
- Current phase: `FIFTH_APPLY`

## Resume boundary
- Last completed Fourth item: `F4-116`
- Last completed Fifth item: `F5-007`
- Next Fifth item: `F5-008`
- DO-NOT-REPEAT Fourth: `F4-001`–`F4-116`
- DO-NOT-REPEAT Fifth: `F5-001`–`F5-007`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f5-007.docx`
- Current working SHA-256: `81ea83b68eb3ee24061c522aad07f96507e4b0ff00847a5f140a8dbe66d60c80`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: Accepted prior package preserved except authorized Fifth P25 text consolidation and one xml:space=preserve attribute on the existing Telakki text run required to preserve the visible sentence-boundary whitespace; all non-document package parts remained byte-identical
- Latest Fifth visual status: PASS

## Latest state
- Fourth Report and prior Fifth items remain accepted.
- F5-007 is APPLIED at P25 using the remediated R2 candidate; the first visually defective candidate is explicitly rejected.
- P25 now gives the kırâat/rivâyet/tarîk/vecih hierarchy positively and preserves the İbnü’l-Cezerî and Telakki/edâ context.
- Current SHA is `81ea83b68eb3ee24061c522aad07f96507e4b0ff00847a5f140a8dbe66d60c80`; body 674.
- F5-008 remains PENDING.

## Evidence
- Adjudication: `work/F5-007-ADJUDICATION.md`
- Rejected visual QA: `work/F5-007-VISUAL-QA-FAIL-R1.md`
- Remediated replay script: `work/apply_f5_007.py`
- R2 replay: `work/runtime/F5-007-REPLAY.txt`
- R2 SHA: `work/runtime/F5-007-SHA256.txt`
- R2 human visual QA: `work/F5-007-VISUAL-QA.md` — 3/3 PASS
- R2 QA export workflow: run 32087726229 / artifact 9307270173

## Open HOLDs
none

## Exact next action
Fetch the exact F5-008 item from `final/fifth-report-locked.md`, resolve it against the durable F5-007 binary, and apply only F5-008 if unambiguous. Preserve Fourth scientific meaning and do not pre-apply F5-009+.
