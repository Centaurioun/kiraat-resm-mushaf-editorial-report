# PREFLIGHT — F4-007 / F4-008

Date: 2026-08-17
Branch: `editorial/apply-fourth-fifth-reports`
Durable completed boundary before this preflight: `F4-006`

## F4-007

- Authoritative Fourth Report item: Giriş final-paragraph transition.
- CURRENT F4-006 DOCX target resolves uniquely at current body paragraph index 34 (zero-based).
- Target paragraph has no footnote references, Word field instructions, field chars, hyperlinks, RTL runs, or bookmarks.
- Fourth Report replacement is a whole-paragraph transition: `Bu ilişkinin nasıl kurulduğunu açıklayabilmek için önce resm-i Osmânî'nin ortaya çıktığı tarihsel ve kavramsal zemini belirlemek gerekir. Birinci bölüm bu zemini incelemektedir.`
- Fifth Report overlap: `F5-014`, which addresses the same old negative research-question sentence. Precedence rule applies: Fourth removes/replaces the old paragraph; Fifth must later transfer only its stylistic intention and must not restore the removed sentence.
- Local non-durable trial application was technically clean and idempotent, but **F4-007 is NOT marked durable/completed here**. GitHub state remains F4-006 completed / F4-007 next until a fully compliant ledger+state checkpoint is committed.

## F4-008 — citation/footnote preflight

- Authoritative Fourth Report target begins: `Cahiliye döneminde panayırlarda okunan ve büyük beğeni toplayan şiirlerin Kâbe duvarlarına asıldığına dair gelen rivâyetler...`
- CURRENT target paragraph resolves uniquely and contains genuine footnote references **15 and 16**.
- Footnote 15 cites: İbnü’n-Nedîm, *el-Fihrist*; M. Fuad Sezgin, *Buhârî’nin Kaynakları*; M. Emin Maşalı, *Kur’ân’ın Metin Yapısı*.
- Footnote 16 cites: Ebû Muhammed Abdullah b. Muhammed Batalyevsî, *el-İktidâb fî şerhi edebü’l-küttâb*, 1/199.
- In the CURRENT manuscript, footnote 16 is attached specifically to the claim that pre-Islamic Arabs began writing with the expression `bismikellâhümme`.
- F4-008's proposed replacement discusses different evidence levels, literary reports, and functional writing use, but it **does not preserve the specific `bismikellâhümme` proposition**.
- Search of the CURRENT manuscript found no other occurrence of `bismikellâhümme`; the proposition is unique in the book at this stage.

### Risk decision

Do **not** blindly replace the whole paragraph while simply appending footnotes 15/16 to the new generic paragraph. That would detach footnote 16 from the claim it actually supports and violate citation-safe application rules.

Unless a scientifically valid surviving destination for footnote 16 is established from the authoritative reports/current context, F4-008 must use status `FOOTNOTE_PLACEMENT_CONFLICT` rather than guessing, deleting the footnote, or attaching it to an unsupported generic proposition.

This file is preflight evidence only. It does not advance `Last fully completed Fourth Report item` beyond F4-006.
