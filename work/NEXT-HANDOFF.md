# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Branch/checkpoint HEAD: `SELF`
- Phase: `FOURTH_APPLY`
- Last completed: `F4-032`
- Next: `F4-033`
- DO-NOT-REPEAT: bootstrap and `F4-001–032`.

## Current recovery pipeline
1. `work/apply_docx_edits.py` → F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. `work/apply_f4_012_017.py` → F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. `work/apply_f4_018_022.py` → F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
4. `work/apply_f4_023_027.py` → F4-027 (`a7e987b2ae84ada927b082974f5d90f4896d43d4`).
5. `work/apply_f4_028_032.py` → F4-032 (`30bf55f09fa02d4b805d6695c149061f2b24031d`).
- Current logical DOCX SHA-256: `7623dbd834b79effef62991932ec3d506cb7d6e4b77db0c976c495b50a24b127`.
- Body paragraphs: **697**.
- Ledger through F4-032: `75a27b5c7be2863ae25b1b37a50a768021fae6c0`.
- State: `e17a168d97e120ecc763f5a338a722210f416b32`.
- Validation: `df007ea599c1a98f0281f028a1fe21e9a666a340`.

## Integrity
- Footnotes/references 469/469; orphan/dangling/duplicate 0/0/0.
- Fields 520/520; Zotero 465+1; RTL 365/365.
- Protected OOXML baseline-identical except expected document.xml changes; ZIP/XML PASS.
- Latest replay byte-idempotent; 25-page bounded QA PASS.
- Open HOLDs: none.

## Locked semantic/citation decisions
- F4-029: do not restore a section-level six-copy certainty. Footnote 88 belongs only to Kevserî's specific view.
- F4-032: do not restore a claim that all contemporary researchers converge on six copies; detailed source-specific paragraphs and notes 89–95 remain.
- Earlier locks for F4-008, F4-012, F4-015, F4-018, F4-024 and F4-026 remain in force.

## Exact next group
- F4-033: end 1.5 with the report transition from historical mushaf distribution to `resm` / `resm-i Osmânî` concepts (no literal Markdown backticks in DOCX).
- F4-034: replace the meta-heavy 1.6 opening with the direct conceptual frame.
- F4-035: revise the Cevherî paragraph so dictionary evidence supports only the lexical meaning; technical terminology is attributed to later resm literature. If Cevherî date is retained, normalize it to `ö. 400/1009'dan önce`.
- F4-036: replace the 1.6.2 opening with the direct technical definition of resm.
- F4-037: remove embedded Kastallânî/Bâkıllânî work notes; retain death dates only if these are their first current body occurrences.

Re-locate all targets from CURRENT F4-032, preserve genuine citations, validate, and checkpoint after this five-item group.