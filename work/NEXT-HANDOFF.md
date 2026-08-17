# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Branch/checkpoint HEAD: `SELF`
- Phase: `FOURTH_APPLY`
- Last completed: `F4-047`
- Next: `F4-048`
- DO-NOT-REPEAT: bootstrap and `F4-001–047`.

## Current recovery pipeline
1. `work/apply_docx_edits.py` → F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. `work/apply_f4_012_017.py` → F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. `work/apply_f4_018_022.py` → F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
4. `work/apply_f4_023_027.py` → F4-027 (`a7e987b2ae84ada927b082974f5d90f4896d43d4`).
5. `work/apply_f4_028_032.py` → F4-032 (`30bf55f09fa02d4b805d6695c149061f2b24031d`).
6. `work/apply_f4_033_037.py` → F4-037 (`58d891d493331863b9f8fdfb0436267a97d33f4e`).
7. `work/apply_f4_038_042.py` → F4-042 (`89f8263a3fb90454727660654d103e6e2c132c16`).
8. `work/apply_f4_043_047.py` → F4-047; durable spec `work/F4-043-047-REPLAY-SPEC.md`.
- Current logical DOCX SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.
- Body paragraphs: **696**.
- Ledger through F4-047: `86ebf507741218a7b2f38c3008f2eac97c825c53`.
- State through F4-047: `d1bb29620e02f36a3568b4f9e07ad182015404b4`.
- Validation through F4-047: `ac1bce766dd2ab36c1f69889c3a7c76f302b6c9d`.

## Integrity
- Footnotes/references 469/469; orphan/dangling/duplicate 0/0/0.
- Fields 520/520; Zotero 465+1; RTL 365/365; bookmarks 53/53; hyperlinks 52; sections 10.
- Protected OOXML baseline-identical except expected document.xml changes; ZIP/XML PASS.
- Latest replay byte-idempotent; 38-page bounded visual QA PASS.
- Open HOLDs: none.

## Locked decisions
- F4-044: note 151 remains on preceding source-specific hazf examples, not on the new concise synthesis.
- F4-047: note 172 remains only on the limited statement that some sources offer meaning-centred explanations; it does not support a phonetic-necessity claim or the corrected examples themselves.
- Existing Arabic/RTL example runs were reused and must remain protected.
- All earlier citation and Fourth-vs-Fifth precedence locks remain active.

## Exact next action
Read the authoritative Fourth Report item `F4-048`, re-locate it from the CURRENT F4-047 logical DOCX, inspect affected citations/Arabic/OOXML, apply it safely, and continue sequentially in groups of at most five low-risk items or immediate checkpoint after any high-risk structural/citation change.