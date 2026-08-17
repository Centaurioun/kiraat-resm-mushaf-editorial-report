# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Checkpoint basis HEAD: `625e5d7ee602bc3861c271558052126a2f18be0e` plus this metadata checkpoint commit
- Current phase: `FOURTH_APPLY`

## Resume boundary
- Last completed item: `F4-085`
- Next item: `F4-086`
- DO-NOT-REPEAT: `F4-001`–`F4-085`

## Working manuscript
- Current working DOCX: `artifacts/checkpoints/manuscript-working-f4-085.docx`
- Current working SHA-256: `d48b31281dc7e8ddde3b30856e2ce1d6edcfc4b079de2c87c63d0b54fdac0af1`
- Last known good DOCX: same path above

## Integrity snapshot
- Footnotes/references: 469/469; orphans/dangling/duplicates: 0/0/0
- Word fields: 520; ADDIN: 466; Zotero: 465 item + 1 bibliography
- Bookmarks: 53/53; hyperlinks: 52; RTL inventory canonical-equal
- Protected OOXML: baseline-identical

## Latest structural state
- F4-073–084 remain intact and validated from prior durable checkpoints.
- F4-085: explicit normative-status transition now separates common Uthmanic mushaf authority from the historical evidentiary role of personal Companion codices; 4.2 bookmark heading preserved.
- F4-086 category differentiation in 4.2 is next; F4-087 open editor note remains intentionally unresolved.
- Derived TOC field has not been recalculated; final Word field/TOC refresh is required after editorial application.

## Evidence
- Replay: `work/apply_f4_085.py`
- Candidate: `artifacts/checkpoints/manuscript-working-f4-085.docx`
- Candidate commit: `aa3b05436d460bb9d412fcecd488c4609fef407b`
- SHA: `work/runtime/F4-085-SHA256.txt`
- Postflight: `work/runtime/F4-085-POSTFLIGHT.txt`
- Technical validation: `work/runtime/F4-085-TECHNICAL-VALIDATION.txt`
- QA PDF: `work/runtime/F4-085-QA.pdf`
- Human visual review: `work/F4-085-VISUAL-QA.md` — 4/4 PASS

## Open HOLDs
none

## Exact next action
Apply F4-086 to the current F4-085 binary. Reframe the 4.2 Companion-codex discussion so attributed differences are not collapsed into a single mensuh/tefsiri category. Preserve source-specific evidence, Arabic runs, and footnote identities; distinguish reading reports, explanatory/tafsiri expressions, word-order/writing differences, and disputed records, while keeping the Uthmanic written framework plus sound transmission as the normative criterion. Do not resolve unrelated F4-088/089 claims prematurely. Run deterministic replay, technical validation and bounded visual QA. Do not repeat `F4-001`–`F4-085`.
