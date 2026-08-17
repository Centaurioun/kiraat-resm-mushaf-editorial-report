# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `aaf1558be1b3340de4f00bb1e2db726dcbe10981` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-110`
- Next item: `F4-111`
- DO-NOT-REPEAT: `F4-001`–`F4-110`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-110.docx`
- Current working SHA-256: `fcdca872a3efc36b96e9f9d600fd23ba73b45a4fec4857ea5434df2b6dd1c807`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–109 remain intact and validated from prior durable checkpoints.
- F4-110: Sonuç now ends with retained ilmî contribution, separate final judgment, separate future-research paragraph, followed by Kaynakça on a new page.
- Current body paragraph count is 676; all 469 footnote identities, 520 fields, bookmarks and protected OOXML remain preserved.
- F4-111+ has not been pre-applied. Derived TOC field remains stale pending final Word refresh.

## Evidence
- Replay: `work/apply_f4_110.py` revision 4
- Candidate: `artifacts/checkpoints/manuscript-working-f4-110.docx`
- SHA: `work/runtime/F4-110-SHA256.txt`
- Postflight: `work/runtime/F4-110-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-110-TECHNICAL-VALIDATION.txt`
- Human visual review: `work/F4-110-VISUAL-QA.md` — 5/5 PASS

## Open HOLDs
none

## Exact next action
Apply only F4-111 to current F4-110. Perform the report-required global main-text normalization of `Kur’an` and the specific-name form `İmam Mushaf`, while preserving bibliographic titles and direct quotations where original spelling must remain. Use a preflight inventory first so broad replacement does not touch fields, bibliography, quotations, Arabic/RTL runs or protected citation structures. Do not pre-apply F4-112+. Run deterministic replay, technical validation and bounded/global QA appropriate to the scope. Do not repeat `F4-001`–`F4-110`.
