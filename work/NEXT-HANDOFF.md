# NEXT HANDOFF

- Repository: `Centaurioun/kiraat-resm-mushaf-editorial-report`
- Branch: `editorial/apply-fourth-fifth-reports`
- Branch/checkpoint HEAD: `SELF`
- Phase: `FOURTH_APPLY`
- Last completed: `F4-017`
- Next: `F4-018`
- DO-NOT-REPEAT: bootstrap and `F4-001–017`.

## Recovery pipeline
1. Canonical `source/manuscript/current/redaktorden_gelen.docx` → `work/apply_docx_edits.py` through F4-011 (`86f99b2186711a7d94159d9c1b7413b0248a0c5c`).
2. Result → `work/apply_f4_012_017.py` through F4-017 (`d533b450b20729130e850d7cbf37256a8e192306`).
- Current reproducible SHA-256: `9b983dcebda782bf1b5bbb69134dde43b0b45b5119ae63d5aa4f2379ec57885a`.
- Current body paragraphs: **700**.
- Ledger through F4-017: `154d696611e3b97fc92595982fa240097f89e7fe`.
- State commit: `f0eac152eed4d3762fb3023e42c5e0ded9a58f84`.
- Validation commit: `f3c9116afed8929607b8c18b7fb58a167dab301a`.

## Integrity
- Footnotes/references **469/469**; orphan/dangling/duplicate **0/0/0**; footnotes.xml unchanged.
- Fields **520/520**; Zotero **465 item + 1 bibliography**.
- Protected core OOXML unchanged except document.xml; ZIP/XML PASS.
- Replay idempotency PASS.
- First 80 current body paragraphs → 19 QA pages; 19/19 visually inspected; durable-pipeline render pixel-identical to independent validation render.
- Open HOLDs: none.

## Citation decisions already locked
- F4-008: footnotes 15 and 16 preserved on their specific source-backed propositions.
- F4-012: notes 19–21 preserved on the consolidated 1.2 opening.
- F4-015: notes 28–30 preserved on the cautious synthesis of both source families.
- Do not undo these semantic citation placements.

## Fifth overlap locks
- F5-014 may not restore the negative research-question paragraph removed by F4-007.
- F5-015 may only improve wording of the F4-011 synthesis without changing its scientific frame.

## Exact next action
Apply F4-018 from the CURRENT F4-017 state:
> Hz. Peygamber döneminde `cem` ifadesi bazı rivâyetlerde Kur’an'ın ezberlenmesi anlamında kullanılmakla birlikte vahyin çeşitli yazı malzemelerine kaydedildiği de bilinmektedir. Hz. Ebû Bekir dönemindeki cem faaliyetinin ayırt edici yönü, dağınık yazılı malzemenin ve hafızadaki aktarımın resmî bir derleme süreci içinde bir araya getirilmesidir.

Then continue F4-019 onward sequentially. F4-019 corrects Hârice b. Zeyd from daughter to son; F4-020 standardizes Ebû Bekir material to `suhuf`; F4-021 repairs the broken Zeyd b. Sâbit sentence; F4-022 corrects Mervân b. Hakem's death date and terminology. Re-locate all targets from CURRENT DOCX and preserve surrounding genuine notes.