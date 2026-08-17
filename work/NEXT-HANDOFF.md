# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Branch/checkpoint HEAD: `SELF`
- Phase: `FOURTH_APPLY`
- Last completed: `F4-037`
- Next: `F4-038`
- DO-NOT-REPEAT: bootstrap and `F4-001–037`.

## Current recovery pipeline
1. `work/apply_docx_edits.py` → F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. `work/apply_f4_012_017.py` → F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
3. `work/apply_f4_018_022.py` → F4-022 (`7d32131a8681b3334cb405a68f79c2494b8db5e7`).
4. `work/apply_f4_023_027.py` → F4-027 (`a7e987b2ae84ada927b082974f5d90f4896d43d4`).
5. `work/apply_f4_028_032.py` → F4-032 (`30bf55f09fa02d4b805d6695c149061f2b24031d`).
6. `work/apply_f4_033_037.py` → F4-037 (`58d891d493331863b9f8fdfb0436267a97d33f4e`).
- Current logical DOCX SHA-256: `94bbdeec878f57d4d97f54ad393bddc79074230ec69886e1f0a455bbe483ed3a`.
- Body paragraphs: **695**.
- Ledger: `b0faacdd905a2da8b03a758ace888c3534a85102`.
- State: `c23bad01bb25fac0994dcee6dc221695397959b9`.
- Validation: `795f6f37e25b64b4baf887dc9a42906368a8e844`.

## Integrity
- Footnotes/references 469/469; orphan/dangling/duplicate 0/0/0.
- Fields 520/520; Zotero 465+1; RTL 365/365.
- Protected OOXML baseline-identical except expected document.xml changes; ZIP/XML PASS.
- Latest replay byte-idempotent; 32-page bounded visual QA PASS after correcting inherited italics in F4-035.
- Open HOLDs: none.

## Locked decisions
- F4-035: FN101 stays on the limited writing-order proposition, FN102 on Cevherî lexical evidence, FN103 on Dânî/later technical development.
- F4-036: FN100 stays on the technical-use definition.
- F4-037: main-text work notes are fixed; the editor note embedded inside footnote 105 is intentionally left for F4-112.
- All earlier citation/precedence locks remain active.

## Exact next group
- F4-038: replace the repetitive/over-strong Ebû Ubeyde paragraph with the report's restrained early-resm formulation.
- F4-039: consolidate Dânî and Ebû Dâvud repetition to the two report-approved paragraphs; preserve their genuine citations.
- F4-040: replace Zerkeşî repetition/negative framing with the report's kıyasî-imlâ vs transmitted-mushaf-writing distinction.
- F4-041: rewrite the modern-research cluster so Motzki/Sinai/Déroche-type evidence is not presented as directly proving the book's entire thesis.
- F4-042: add the report-approved distinction at the start of 1.8 between historical origin/tevkîfîlik and later binding force.

Re-locate all targets from CURRENT F4-037, preserve source-backed citations and Word structures, replay twice, run technical validation and affected-range visual QA, then checkpoint before F4-043.