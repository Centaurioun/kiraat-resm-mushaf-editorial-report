# F5-017 adjudication

## Locked item
- Item: `F5-017`
- Section: `1.2. Erken Dönemde Kur'an'ın Yazı ile İlişkisi`
- Locked target: `Bu döneme ilişkin rivâyetler, vahyin yazıya geçirilmesi hususunda çok daha sistemli ve titiz bir uygulamanın bulunduğunu göstermektedir.`
- Problem: the Medine evidence is first summarized, then introduced again with `Nitekim`, then concluded a second time.
- Locked Fifth resolution: consolidate the sequence into three direct sentences: the reported Medine writing practice, the Zeyd b. Sâbit example, and a source-limited concluding sentence.

## Durable input
- DOCX: `artifacts/checkpoints/manuscript-working-f5-016.docx`
- SHA-256: `cc3d906b77ae5325b6bcb9b5e458b1af30ef37191c5ee956455613161bd693da`
- Body paragraphs: 674
- Current target: unique at body paragraph P53.
- Current P53 footnote references: `24, 25, 26` in that order.

## Fourth Report constraints
- F4-012 already shortened the general 1.2 opening at P51 and established that writing complemented oral transmission; F5-017 must not recreate the removed general preamble.
- F4-016 deliberately weakened the Medine conclusion from an over-certain claim to a source-limited formulation: `Bu rivâyetler, Medine döneminde vahyin yazıyla kaydedilmesinin düzenli bir uygulama olarak aktarıldığına işaret etmektedir.`
- Therefore the F5-017 consolidation must preserve the epistemic level of `rivâyetlerde / aktarılır / yer alır`, not state the practice as independently verified fact.
- F4-014's later explanation of why the material was not compiled into a codex remains outside F5-017 and must be preserved.

## Exact bounded edit
Only P53 may change.
1. Replace the first two repetitive sentences with: `Medine dönemine ilişkin rivâyetlerde Hz. Peygamber’in vahiy geldiğinde kâtiplerden birini çağırdığı ve âyetleri yazdırdığı aktarılır.` FN24 remains immediately after this sentence.
2. Remove only the redundant `Nitekim ... çok sayıda rivâyet bulunmaktadır. Bu rivâyetlerden biri, ` lead-in. Preserve the existing `Zeyd b. Sâbit’in (ö. 45/665)` identification, quotation runs, and FN25 position.
3. Change the phrase after FN25 so the quotation becomes an example: `şeklindeki ifadesi bu uygulamanın örneklerinden biridir.`
4. Replace the second mini-conclusion with the Fifth source-limited form: `Rivâyetlerde Medine dönemindeki vahiy kaydı düzenli bir uygulama olarak yer alır.`
5. Preserve everything from `Ancak Hz. Peygamber hayatta iken...` onward byte-structurally except for unavoidable document.xml serialization; preserve FN26 and all later Fourth-approved wording.

## Fail-closed conditions
- Input SHA differs from the durable F5-016 SHA.
- Target is not uniquely P53.
- P53 footnote order differs from `['24','25','26']`.
- Any body paragraph other than P53 changes.
- FN24/FN25/FN26 identity/order changes.
- F5-018 target in P54 is altered or pre-applied.
- Fields, Zotero instructions, bookmarks, hyperlinks, footnote reference inventory, or RTL structural inventory changes.

## Expected result
`F5-017 = APPLIED`, P53 only; deterministic second replay `ALREADY_SATISFIED`; visual QA required because manuscript bytes change; next permitted item remains F5-018 only.
