# F5-016 ADJUDICATION

## Locked Fifth item
- **Item:** F5-016 — 1.1'de `Nitekim` ile örnek açma alışkanlığı
- **Location:** 1.1. İslâm'dan Önce Arap Yazısının Durumu
- **Locked expression:** `Tarihe dair eserlerde İslâm öncesi Mekke'de yazının kullanıldığına dair başka örneklere de rastlanmaktadır. Nitekim Hz. Peygamber'in dedelerinden Kusay b. Kilâb'ın (ö. 480) Mekke'nin yönetimiyle ilgili Huzâa ile Beni Bekr arasındaki mücadelede kendisine destek çıkması amacıyla anne bir kardeşi Razâh b. Rebîa'ya bir mektup yazıp gönderdiği rivâyet edilmektedir.`
- **Locked proposed form:** `Tarih kaynaklarında İslâm öncesi Mekke'de yazının kullanımına ilişkin başka örnekler de aktarılır. Kusay b. Kilâb'ın Razâh b. Rebîa'ya bir mektup gönderdiğine dair rivâyet bunlardan biridir.`

## Current durable context
Durable input is `artifacts/checkpoints/manuscript-working-f5-015.docx`, SHA-256 `c99826db06c605f5950e682c82af6d5c6f481d0c43a3364d029daadabe51fc19`, body paragraphs 674.

The current target is uniquely present at body paragraph P45 in house-style typography:

`Tarihe dair eserlerde İslâm öncesi Mekke’de yazının kullanıldığına dair başka örneklere de rastlanmaktadır. Nitekim Hz. Peygamber’in dedelerinden Kusay b. Kilâb’ın (ö. 480) Mekke’nin yönetimiyle ilgili Huzâa ile Beni Bekr arasındaki mücadelede kendisine destek çıkması amacıyla anne bir kardeşi Razâh b. Rebîa’ya bir mektup yazıp gönderdiği rivâyet edilmektedir.`

P45 also contains the following sentence, which is not part of F5-016 and must remain unchanged:

`Bu rivâyet doğru kabul edildiğinde yazının miladi altıncı yüzyılın başlarında bilindiği söylenebilir.`

The paragraph carries genuine footnote reference 14; its identity/order must remain unchanged.

## Fourth-over-Fifth adjudication
No accepted Fourth item rewrote this Kusay/Razâh example opening. F4-011 resolved the later 1.1 closing at P49, not P45. Therefore F5-016 remains an active language-edit target.

The Fifth proposal is scientifically safe because it does not strengthen the historicity of the report: it retains the event explicitly as a `rivâyet` and merely removes repetitive `Nitekim` rhythm and unnecessary genealogical/conflict detail from the example-opening sentence. The immediately following caution (`Bu rivâyet doğru kabul edildiğinde...`) remains intact.

## Decision
**APPLY** the smallest bounded edit:
1. Replace only the first two sentences of P45 with the locked Fifth wording, normalized to the manuscript's typographic apostrophe style.
2. Preserve the following caution sentence byte-for-text.
3. Preserve footnote reference 14 and all paragraph/run structure except text-node content required for the replacement.
4. Do not touch P44, P46, F5-017 or any later Fifth item.

Because manuscript bytes will change, bounded SHA-locked visual QA is required after technical replay/postflight PASS.