# F4-043–047 deterministic recovery specification

Input state: deterministic F4-042 output SHA-256 `e23e7c57a52b5ef6f95c3f36ea2ab614274464bff6e65803198c5c868cb1181c`.
Validated output SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.
Second application to the output is byte-identical and returns all five items already satisfied.

## F4-043
In the paragraph beginning `Bu kurallar şunlardır: harf düşmesi (hazf)`, replace only the sentence `Bu tespit Osman mushaflarının hazırlanışında yazı ile okuyuş arasında bilinçli bir uyum gözetildiğini ortaya koymaktadır.` with:

`Bu örnekler, bazı mushaf yazımlarının rivâyet yoluyla sabit birden fazla okuyuşla bağdaşabildiğini göstermektedir. Bununla birlikte her yazım özelliğinin doğrudan kırâat farklılıklarını korumak amacıyla ortaya çıktığı söylenemez; erken Arap yazı geleneği ile kırâatlerin resmle ilişkisi ayrı ayrı değerlendirilmelidir.`

Preserve genuine footnote 142 and all other paragraph structures.

## F4-044
Replace the opening paragraph of `1.9.1. Hazf` with:

`Hazf, lafızda bulunan bazı harflerin mushaf yazısında gösterilmemesidir. Bu özellik resm-i Osmânî'de düzenli biçimde görülen yazım uygulamalarından biridir. Bununla birlikte bütün hazf örneklerinin aynı sebeple ortaya çıktığı veya doğrudan kırâat farklılığını koruma amacı taşıdığı söylenemez. Bazı örnekler erken yazı geleneğiyle açıklanırken bazı yazımlar rivâyetle sabit birden fazla okuyuşla bağdaşabilmektedir.`

Preserve genuine footnote 145. In the later paragraph beginning `Med harflerinin hazfi:`, remove the two-sentence `Sonuç olarak hazf...` overclaim and append this concise synthesis *after* genuine footnote 151, leaving note 151 attached to the preceding source-specific examples:

`Bu örnekler, hazfın resm-i Osmânî'de yaygın bir yazım özelliği olduğunu ve bazı durumlarda farklı kırâatlerle bağdaşabildiğini göstermektedir.`

## F4-045
In the ibdâl paragraph, replace only the malformed Ca‘berî sentence with:

`Ca‘berî (ö. 732/1332), resm kurallarını sıralarken ibdâli müstakil bir başlık altında ele almış ve bunun erken yazı geleneğiyle ilişkili olduğunu belirtmiştir.`

Preserve all genuine notes 158–163 in their original positions; note 161 continues to follow the Ca‘berî sentence.

## F4-046
In the paragraph beginning `Hemze bazen hiç yazılmamış,`, retain the existing examples and genuine notes 166/167, but replace the overdetermined historical-cause tail with:

`Hemzenin erken mushaflarda bugünkü imlâdaki biçimiyle her zaman ayrı ve düzenli bir işaretle gösterilmemesi, erken Arap yazısının imlâ ve işaretleme uygulamaları çerçevesinde değerlendirilmelidir. Hemze kimi kelimelerde med harfleriyle temsil edilmiş, kimi yerlerde ise yazıda ayrıca gösterilmemiştir. Bu özellik tek başına belirli bir kırâati ortaya çıkarmaz; okuyuşun nasıl icra edildiği rivâyet ve edâ yoluyla bilinmektedir.`

Preserve genuine note 168 at the end.

## F4-047
In the `Ziyâde,` paragraph, preserve the entire opening through genuine footnote 171. Replace the later example/causal tail with the following content, reusing the existing Arabic/RTL runs for `أُوْلوُا`, `سَأُوْرِيكُمْ`, and `بِأَيْيْدٍ` rather than recreating their formatting:

`Ziyâdeye örnek olarak Bakara sûresinin 269. âyetindeki أُوْلوُا lafzında yer alan vav zikredilmiştir. سَأُوْرِيكُمْ (el-Enbiyâ 21/37) kelimesindeki bazı harfler ile بِأَيْيْدٍ (ez-Zâriyât 51/47) kelimesindeki yâ da resm kaynaklarında ziyâde başlığı altında ele alınan örnekler arasındadır. Bazı kaynaklarda bu tür ziyâdeler anlam merkezli yorumlarla da açıklanmış olmakla birlikte, bu yorumlar yazımın zorunlu tarihsel sebebi olarak sunulmamalıdır.`

Preserve genuine note 172 after the final caution sentence. This note is not reassigned to the corrected examples: its own source text supports the limited statement that some scholars give meaning-centred interpretations. Remove the unsupported `fonetik zorunluluktan dolayı` reasoning.

## Required invariants after replay
- genuine footnotes/references 469/469;
- exact ID/reference sets unchanged;
- orphan/dangling/duplicate 0/0/0;
- Word fields 520/520;
- Zotero 465 item + 1 bibliography;
- RTL inventory 365;
- bookmarks 53/53; hyperlinks 52; sections 10;
- protected `footnotes.xml`, styles, numbering, settings and document relationships baseline-identical;
- only expected `word/document.xml` content changes;
- output SHA exactly `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`.