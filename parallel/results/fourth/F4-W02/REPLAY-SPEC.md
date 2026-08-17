# REPLAY SPEC — F4-W02 / F4-057–062

## Status

This is a fail-closed editorial replay specification only. It was **not executed** because the mandatory F4-047 logical DOCX could not be reconstructed and independently SHA-256 verified in this worker environment. The integrator must not treat any item below as applied or technically validated.

## Global precondition

1. Reconstruct the logical F4-047 DOCX from the canonical source and the existing replay pipeline.
2. Verify exact SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.
3. For each operation below, locate the target by exact/semantic text anchor plus local section context; require exactly one plausible match.
4. If match count is 0 or >1, stop that item.
5. Preserve all genuine footnotes, fields, Zotero fields, bookmarks, hyperlinks, sections, styles, numbering, Arabic/RTL structures and relationships unless the item explicitly requires a targeted change.

## F4-057 — 2.2.3 end -> 2.3 transition

Expected current anchor begins:

`Sonuç olarak kırâatlerde otorite ekseni Kur'an'ın doğru okuyuşunu koruyan çok yönlü bir ilmî geleneği ifade eder.`

Replace the concluding summary paragraph with:

`Kırâatlerde otoritenin bu çok katmanlı yapısı, sözlü aktarımın müşterek mushaf yazısıyla nasıl ilişkilendiği sorusunu gündeme getirir. Bu ilişki, yedi harf ile Osmânî mushaf meselesinde daha belirgin hâle gelmektedir.`

Do not move the preceding genuine footnote attached to the Âsım/Hafs/Şu'be proposition onto this transition.

## F4-058 — 2.3 yedi harf / Osmânî mushaf relation

Expected current anchor includes:

`Doğruya yakın olan, mushafın ... sahih ve taşınabilir çeşitliliği koruyan bir çerçeve sunduğunu söylemektir.`

Replace the overconfident synthesis with the Fourth Report text:

`Osmânî mushaflarla yedi harf arasındaki ilişkinin nasıl anlaşılacağı konusunda klasik kaynaklarda farklı görüşler bulunmaktadır. Bir kısım âlimler Hz. Osman'ın ümmeti belirli bir harf üzerinde topladığını, bir kısmı ise mushaf resminin taşıdığı ölçüde birden fazla vechin korunduğunu ifade etmiştir. Bu görüşlerin her biri kendi kaynak ve yorum bağlamı içinde değerlendirilmelidir. Bununla birlikte bu tartışma, sahih kırâatlerin mushaf yazısından üretildiği anlamına gelmez. Kırâatlerin aktarımında telakki ve rivâyet belirleyici olmaya devam etmiş; resm ise nakledilen okuyuşların ortak mushaf yazısıyla bağdaşma sınırını göstermiştir.`

Footnote placement must be re-evaluated against the exact propositions in the verified DOCX. Do not automatically carry a note from the removed `Doğruya yakın olan` claim onto the entire replacement paragraph.

## F4-059 — 2.3 repeated history + closing transition

This item is **not safely reducible to a blind paragraph replacement**. On the verified baseline:

1. Delimit 2.3 from its heading through the paragraph immediately before 2.4.
2. Inventory each paragraph's genuine footnote references and the proposition supported by each note.
3. Identify material that merely repeats the Birinci Bölüm cem/istinsah narrative versus unique cited material specific to the yedi harf/Osmânî mushaf discussion.
4. Shorten only duplicated historical narration; preserve unique cited propositions and their genuine notes.
5. Replace the long closing summary beginning `Sonuç olarak Osmânî mushaf ile yedi harf meselesi...` with the report transition:

`Yedi harf ile Osmânî mushaf arasındaki ilişkiye dair bu farklı açıklamalar, resm-i Osmânî'nin sonraki kırâat değerlendirmelerinde nasıl ortak bir yazılı başvuru zemini hâline geldiği sorusunu gündeme getirmektedir. Bir sonraki başlık bu tarihsel sonucun kırâat ve tefsîr alanındaki yansımalarını ele almaktadır.`

If any unique cited proposition would be lost or any genuine note lacks a materially equivalent destination, stop F4-059 with a citation-placement conflict rather than deleting it.

## F4-060 — 2.4 active-causal framing

Expected current anchor includes:

`Bu gelişme doğrudan doğruya kırâat ve tefsîr alanını şekillendiren ölçülerden biri olmuştur.`

Replace the active-causal synthesis with:

`Osmânî mushafların ortak başvuru metni hâline gelmesi, kırâatlerin sonraki değerlendirilmesinde resme uygunluk ölçüsünün daha belirgin hâle gelmesine zemin hazırlamıştır. Bununla birlikte kırâat imamlarının otoritesi ve öğretim geleneklerinin yerleşmesi yalnız mushaf yazısıyla açıklanamaz; rivâyet zincirleri, bölgesel öğretim çevreleri ve ilmî kabul de bu sürecin temel unsurlarıdır. Tefsîr geleneğinde ise müşterek mushaf metni ortak bir yazılı zemin sağlamış, farklı kırâatlerin yorumdaki kullanımı rivâyet ve dil verileriyle birlikte sürmüştür.`

Re-evaluate any attached footnote at the proposition level before retaining it.

## F4-061 — 2.4 counterfactual history

Expected current anchor begins:

`Şayet mushaf yazısı ortak olmasaydı farklı bölgelerde farklı yazım gelenekleri ve metin varyantları üzerinden gelişen yorum anlayışları oluşabilirdi.`

Replace the counterfactual explanation with:

`Osmânî mushafların ortak başvuru metni hâline gelmesi, farklı merkezlerdeki kırâat rivâyetlerinin müşterek bir yazılı çerçeveyle ilişkilendirilmesine imkân vermiştir. Bunun sonraki kırâat ve tefsîr literatüründeki sonuçları, mevcut tarihsel uygulamalar ve kaynakların aktardığı değerlendirmeler üzerinden açıklanmalıdır.`

Do not preserve a footnote merely by moving it from a removed hypothetical proposition to the new methodological sentence unless the note genuinely supports it.

## F4-062 — 2.4 end -> Third Section transition

Expected boundary contains the closing 2.4 synthesis followed by the existing Third Section heading `RESM, KIRÂAT, LAFIZ VE MANA İLİŞKİSİ`.

Insert/replace only the transition prose immediately before the existing Third Section heading with:

`Resm-i Osmânî'nin kırâat rivâyetiyle ilişkisi genel ilkeler düzeyinde bu şekilde belirlendikten sonra, bu ilişkinin somut yazım örneklerinde nasıl göründüğünü incelemek gerekir. Üçüncü bölüm hazf, ziyâde, ibdâl, vasl-fasl ve benzeri resm özelliklerinin kırâat, lafız ve mana ile ilişkisini bu açıdan ele almaktadır.`

Preserve the existing Third Section heading paragraph, style, numbering, bookmarks and field relationships exactly. Do not recreate the heading text in a new paragraph if the existing heading can be retained.

## Required post-replay validation

After each accepted item compare pre/post inventories for genuine footnotes/reference IDs, orphan/dangling/duplicate notes, Word fields, Zotero item/bibliography fields, bookmarks, hyperlinks, relevant RTL/Arabic runs, comments/revisions, sections, ZIP/XML parse integrity and protected OOXML parts. Then render and inspect the affected page range and surrounding pages.
