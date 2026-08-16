# V2 Aşama 2 — Faktik ve Kaynak Temelli Doğrulama

## Amaç

Bu dosya yazara gönderilecek nihai rapor değildir. `work/v2-master-inventory.md` içinde `FACT`, `SOURCE` ve `GOOGLE-LEAD` etiketi verilen yüksek riskli kayıtların, final rapora girmeden önce bilimsel ve bibliyografik olarak doğrulanması için hazırlanmıştır.

Bu aşamada üç ayrı soru birbirinden ayrılmıştır:

1. **Veri doğru mu?** Kişi, ölüm tarihi, eser, ayet, kronoloji veya olay doğrulanabiliyor mu?
2. **Kaynak gerçekten bu iddiayı taşıyor mu?** Kaynakta bulunan veri ile yazarın çıkardığı sonuç aynı şey mi?
3. **Doğru veri metinde hangi kesinlik düzeyiyle kullanılmalı?** Klasik yorum, tarihsel rivayet, çağdaş araştırma ve yazar çıkarımı birbirinden ayrılıyor mu?

Google AI dosyaları kanıt olarak kullanılmamıştır. Yalnız araştırma ipucu olarak değerlendirilmiş, önemli iddialar bağımsız kaynaklarla kontrol edilmiştir.

## Statü anahtarı

- **VERIFIED-CORRECT**: Mevcut bilgi güvenilir kaynaklarla doğrulandı.
- **VERIFIED-CORRECTION**: Manuscriptteki bilgi yanlış/bozuk; güvenilir düzeltme bulundu.
- **QUALIFY**: Bilginin çekirdeği kullanılabilir fakat mevcut kesinlik düzeyi fazla güçlü.
- **SOURCE-MISMATCH**: Verilen kaynak, manuscriptte kurulan daha geniş sonucu tek başına taşımıyor.
- **REMOVE-UNLESS-SOURCED**: İddia güçlü biçimde doğrulanamadı; birincil/sağlam kaynak bulunmadıkça çıkarılmalı veya açıkça iddia/rivayet olarak sınırlandırılmalı.
- **UNRESOLVED**: Bu turda güvenilir biçimde kesinleştirilemedi; tahmin edilmeyecek.

# I. Kişi kimlikleri ve ölüm tarihleri

## 1. Ca‘berî — CAND-044

**Güncel manuscriptte:**

> `Ca'berî (ö. 832/1428 ölüm tarihleri tekrar gözden geçirilmeli.)`

**Statü:** `VERIFIED-CORRECTION`

**Doğru bilgi:** Ebû İshâk Burhânüddîn İbrâhim b. Ömer el-Ca‘berî **732/1332** tarihinde vefat etmiştir. TDV İslâm Ansiklopedisi 15 Ramazan 732 / 10 Haziran 1332 tarihini vermektedir.

**V2 kararı:** Bu bilgi ilk anlamlı kullanım ise `Ca‘berî (ö. 732/1332)` biçimi kullanılmalıdır. Daha önce ölüm tarihi verilmişse yalnız `Ca‘berî` yeterlidir. Eski Stage 3/6 çözümündeki `832/1428` **yanlıştır** ve final rapora taşınmayacaktır.

**Google AI değerlendirmesi:** Google AI burada yararlı bir düzeltme yakalamıştır; ancak doğruluk Google çıktısından değil bağımsız biyografik kaynaktan teyit edilmiştir.

## 2. Hârice b. Zeyd — CAND-022

**Statü:** `VERIFIED-CORRECTION`

**Doğru bilgi:** Hârice b. Zeyd b. Sâbit, Zeyd b. Sâbit’in **oğludur**, kızı değildir; ölüm tarihi **100/718-19** olarak verilmektedir.

**V2 kararı:** Manuscriptte `Zeyd b. Sâbit’in kızı Hârice...` biçimindeki kullanım varsa `Zeyd b. Sâbit’in oğlu Hârice b. Zeyd...` olarak düzeltilmelidir. Bu, yalnız üslup değil kişi kimliği hatasıdır.

## 3. Ebû Şâme el-Makdisî — CAND-053

**Statü:** `VERIFIED-CORRECTION`

**Doğru bilgi:** Ebû Şâme el-Makdisî **665/1267** tarihinde vefat etmiştir. Manuscriptte görülen `665/1276` biçimi yanlıştır.

**V2 kararı:** Kitap genelinde tek biçim `665/1267` olmalıdır; tekrar eden kullanımlarda ilk kullanım ilkesi ayrıca uygulanacaktır.

## 4. Cevherî — Google AI biyografik düzeltmesi + CAND-056 bağlamı

**Statü:** `QUALIFY + SOURCE-MISMATCH`

**Biyografik veri:** TDV İslâm Ansiklopedisi Cevherî’yi **“ö. 400/1009’dan önce”** biçiminde verir. Google AI dosyalarındaki `393/1003` kesinliği bu aşamada güvenli kabul edilmemiştir.

**Daha önemli sorun:** Manuscript, Cevherî’nin sözlükteki `resm` açıklamasından hareketle kelimenin “zamanla Kur’an yazımına özgü teknik bir terime dönüştüğünü” Cevherî’ye nispet etmektedir. Sözlük kaynağı esasen lügavî anlamı destekler; tarihsel terimleşme sürecini Cevherî’nin bizzat kurduğu sonucunu aynı kaynak tek başına taşımaz.

**V2 kararı:** Cevherî lügavî anlam için kullanılabilir. “Kur’an yazımına özgü teknik terime dönüşme” ise ayrı tarihsel kaynakla desteklenmeli veya yazarın sonraki literatüre dayanarak kurduğu sentez olarak yeniden yazılmalıdır.

## 5. Varaka b. Nevfel — CAND-016

**Statü:** `VERIFIED-CORRECT-WITH-UNCERTAINTY`

**Doğru kullanım:** TDV İslâm Ansiklopedisi `Varaka b. Nevfel (ö. 610 [?])` biçimini kullanır ve alternatif ölüm tarihleri bulunduğunu açıkça belirtir.

**V2 kararı:** İlk kullanımda ölüm tarihi korunacaksa belirsizlik işaretiyle verilmelidir. `610` kesin tarih gibi yazılmamalıdır. Eski pipeline’ın tarihi bütünüyle silme yaklaşımı zorunlu değildir.

## 6. Muhammed Hamîdullah — CAND-038

**Statü:** `VERIFIED-CORRECTION`

**Doğru bilgi:** Muhammed Hamîdullah 17 Aralık **2002** tarihinde vefat etmiştir.

**V2 kararı:** `20029` açık yazım hatasıdır; gerekiyorsa `2002` olarak düzeltilmelidir. Doğru bilgi bulunabildiği için yalnız ölüm tarihini silmek tercih edilmeyecektir.

## 7. Bâkıllânî — CAND-043

**Statü:** `VERIFIED-CORRECTION`

**Doğru bilgi:** Ebû Bekir el-Bâkıllânî **403/1013**.

**V2 kararı:** `403/10113` yazım hatası `403/1013` olarak düzeltilmelidir; ilk kullanım değilse ölüm tarihi kaldırılabilir.

## 8. Süyûtî — CAND-033

**Statü:** `VERIFIED-CORRECT`

**Doğru bilgi:** Celâleddîn es-Süyûtî **911/1505**.

**V2 kararı:** Sorun tarih değil, tekrar/çalışma notudur. Tarih ilk kullanımda doğru biçimde korunup sonraki tekrarlar sadeleştirilebilir.

## 9. Mehdevî — CAND-122 çevresi

**Statü:** `VERIFIED-CORRECT-WITH-UNCERTAINTY`

**Doğru bilgi:** Ebü’l-Abbâs Ahmed b. Ammâr el-Mehdevî için TDV **440/1048-49 [?]** verir; kaynaklar arasında farklı tarihler bulunduğunu belirtir.

**V2 kararı:** İlk kullanımda tarih verilecekse ihtiyat korunmalıdır; `440/1048` mutlaklaştırılmamalıdır.

## 10. İbn Mu‘âz el-Cühenî — CAND-125

**Statü:** `VERIFIED-CORRECTION`

**Doğru bilgi:** Güncel hakemli çalışma İbn Mu‘âz el-Cühenî için **442/1050** tarihini verir.

**V2 kararı:** `442/10509` açık yazım hatasıdır; ilk kullanımsa `442/1050` olarak düzeltilmeli, yalnız silinmemelidir.

## 11. Alemüddin es-Sehâvî — CAND-127 / Google AI karşılaştırması

**Statü:** `VERIFIED-CORRECTION`

**Doğru bilgi:** Alemüddin es-Sehâvî **643/1245** tarihinde vefat etmiştir.

**V2 kararı:** Google AI dosyasındaki `642/1244` **yanlıştır**. Bu örnek, Google AI’ın “fact-check” başlığı altında verdiği biyografik bilgilerin bile bağımsız doğrulama olmadan kullanılamayacağını göstermektedir.

## 12. Ebü’l-Fazl el-Huzâî — CAND-129

**Statü:** `VERIFIED-CORRECT`

**Doğru bilgi:** Ebü’l-Fazl Muhammed b. Ca‘fer el-Huzâî için **408/1017** tarihi biyografik kaynaklarda teyit edilmektedir.

**V2 kararı:** İlk kullanımda korunabilir; çalışma notu temizlenmelidir.

## 13. Amr b. Kays — CAND-037

**Statü:** `UNRESOLVED`

**Mevcut sorun:** Manuscript `Amr b. Kays (ö. ?)` biçimini kullanmaktadır. Mevcut dipnotlar onun Basra’ya gönderildiğine dair modern kaynaklara işaret etmekte, fakat bu turda güvenilir ve tartışmasız bir biyografik ölüm tarihi kesinleştirilememiştir.

**V2 kararı:** Ölüm tarihi tahmin edilmeyecektir. Kimlik ayrıca kesinleştirilmezse final öneride `Amr b. Kays` biçimi yeterlidir. `ö. ?` ana metinde bırakılmayacaktır.

# II. Birinci Bölümde yüksek riskli tarihsel iddialar

## 14. Mervân b. Hakem’in sahifeleri imha ettirmesi — CAND-025

**Statü:** `QUALIFY + SOURCE-MISMATCH`

**Doğrulanan çekirdek:** Mervân b. Hakem’in ölüm tarihi **65/685**’tir. İbn Ebû Dâvud kanalıyla nakledilen rivayette Mervân’ın, Hafsa’nın elindeki sahifelerde bulunanların mushaflarda yazılıp korunduğunu; ileride insanların “bunlardan bir şey yazılmadı” diye şüpheye düşmesinden endişe ettiği için sahifeleri imha ettirdiğini söylediği aktarılmaktadır. Bu gerekçe sırf modern bir psikolojik tahmin değildir; rivayette kendisine nispet edilen bir açıklaması vardır.

**Fakat manuscriptteki daha geniş sonuç:**

> `... temel endişe, Hz. Ebû Bekir döneminde cemedilen mushafın "yedi harf" ruhsatını yansıtıyor olması ve Hz. Osman döneminde gerçekleştirilen istinsah faaliyetlerinde ise "arza-i âhire" esas alınarak bu ruhsatın sınırlandırılmasıdır.`

Bu spesifik açıklama, Mervân rivayetinin söylediğinden daha ileri gitmektedir. Rivayet “ileride şüphe doğması” endişesini destekler; sahifelerin imhasını doğrudan `yedi harf → arza-i âhire ile sınırlandırma` mekanizmasına bağlamaz.

**V2 kararı:** Final raporda Mervân’ın rivayette açıkça söylediği gerekçe ile yazarın yedi harf/arza-i âhire açıklaması ayrılacaktır. İkinci kısım güçlü kaynakla desteklenmezse yazar hükmü olmaktan çıkarılmalıdır.

## 15. Mushaf sayısı ve gönderildikleri şehirler — CAND-034, 035, 036

**Statü:** `QUALIFY`

**Doğrulanan durum:** Klasik kaynaklarda sayı konusunda tek bir rakam yoktur. Dânî’nin el-Mukni‘’inde çoğunluğa nispet edilen **dört nüsha** görüşü (Kûfe, Basra, Şam ve yanında kalan nüsha) ile **yedi nüsha** görüşü birlikte aktarılır; Dânî dört görüşünü daha sahih sayar. Başka klasik aktarımlarda beş, altı, yedi ve daha farklı sayılar görülebilir.

**V2 kararı:** Final metin `5 bölgesel + 1 şahsî = 6 resmî akış` gibi modern bir sentezi tarihsel gerçeklik olarak kurmayacaktır. Her sayı açıkça görüş sahibine nispet edilecek; ardından yalnız “kaynaklarda sayı ve merkezler konusunda ihtilaf vardır” düzeyinde yazar sentezi yapılacaktır.

**Google AI değerlendirmesi:** Google AI’nın bu bölümde kurduğu “beş bölgesel + bir şahsî nüsha = altı ana/resmî akış” formülü kaynaklardaki ihtilafı çözmüyor, farklı rivayetleri yeni bir idari modele dönüştürüyor. Doğrudan kullanılmayacaktır.

## 16. `التابوت` örneği — CAND-029

**Statü:** `QUALIFY`

**Doğrulanan çekirdek:** Rivayet, Zeyd b. Sâbit ile Kureyşli komisyon üyeleri arasında kelimenin yazımı konusunda ihtilaf bulunduğunu ve Hz. Osman’ın Kureyş yazım/lügat biçimini tercih ettirdiğini aktarır.

**V2 kararı:** Bu örnek `lehçe = telaffuz = imlâ` biçiminde sunulmamalıdır. Kaynak öncelikle bir **yazım/lügat tercihi** hakkında bilgi verir; buradan doğrudan fonetik telaffuz farkı çıkarılmamalıdır.

## 17. Ebû Bekir suhufu, yedi harf ve arza-i âhire — CAND-024, 050

**Statü:** `QUALIFY`

Klasik kıraat literatüründe son arza ile Osmânî mushaflar arasında ilişki kuran güçlü bir yorum çizgisi vardır. Bununla birlikte ayrıntıda tek formül yoktur. İbnü’l-Cezerî’ye nispet edilen açıklamalarda, sahâbenin son arzada sabit olduğuna ve neshedilmediğine kanaat getirdiği okuyuşları yazdığı; şehir mushafları arasındaki sınırlı farklılıkların da dikkate alınması gerektiği belirtilir. Dolayısıyla “Osmânî mushaflar yalnız ve eksiksiz biçimde arza-i âhireyi mekanik olarak kopyaladı” şeklindeki düz bir tarihsel mekanizma fazla kesindir.

**V2 kararı:** Manuscriptte `Hz. Osman’ın istinsah faaliyetleri de bu son arzayı esas almıştır` gibi cümleler, “klasik literatürde bu süreç arza-i âhire ile ilişkilendirilmiştir” veya kaynak sahibine açık nispet veren bir yapıya çekilmelidir. Tarihsel rivayet ile klasik açıklama modeli ayrılmalıdır.

# III. Resm, sözlü rivayet ve erken yazı hakkında modern kanıt

## 18. Yazılı Uthmânî arketip ve sözlü aktarım birlikte düşünülmeli — CAND-067, 073, 083, 115

**Statü:** `VERIFIED-BALANCE`

Modern yazma araştırmaları kitabın ana ayrımını destekleyecek biçimde iki farklı veri kümesi sunmaktadır:

- Marijn van Putten’in 14 erken Kur’an yazmasını karşılaştırdığı çalışma, ortak ve sıra dışı imlâ özelliklerinin tek bir **yazılı arketipe** işaret ettiğini ve erken mushafların yazılı örneklerden kopyalandığını savunmaktadır.
- Hythem Sidky’nin kanonik kıraatler arasındaki i‘câm/dotting örüntülerine ilişkin çalışması ise Medine, Mekke-Basra ve Kûfe çevrelerinde **miras alınmış sözlü kıraat geleneklerinin** Osmânî istinsah dönemine veya ilk nesillere kadar uzanmasının muhtemel olduğunu göstermektedir.
- Van Putten’in kanonik kıraatlerin rasmle uyuşmazlıklarını incelediği çalışma, kanonik okuyuşların genel olarak standart konsonantal iskelete uyduğunu, fakat nadir istisnaların da bulunduğunu göstermektedir.

**V2 kararı:** Bu literatür “ya yazı ya söz” ikiliğini desteklememektedir. Final raporda sözlü rivayetin aslîliği korunurken erken yazılı aktarım güçlü biçimde kabul edilebilir; resm ise tek başına okuyuş üreten mekanizma gibi sunulmamalıdır.

## 19. Nokta ve harekelerin bulunmaması “farklı kırâatleri korumak için tasarlandı” diye kesinleştirilemez — CAND-150 ve bağlantılı CAND-083/091

**Statü:** `QUALIFY / HIGH-PRIORITY`

Erken Arap yazısında ayırt edici noktaların Hz. Osman’dan önce de bilindiğini gösteren epigrafik kanıt vardır. 24/644-45 tarihli Zuhayr yazıtı, işlevsel bir diakritik/noktalama sisteminin erken tarihte kullanıldığını göstermektedir. Ghabban ve Hoyland, klasik kaynaklarda mushafların farklı okuyuşları taşıyabilmesi için noktaların özellikle kaldırıldığı yönünde açıklamalar bulunduğunu kaydeder; ancak Hoyland bu açıklamanın tarihsel olarak **kesinleştirilemediğini** ve pious-fiction ihtimalinin dışlanamayacağını açıkça belirtir. Daha yeni Kur’an yazması çalışmaları da erken Hicazî mushafların bir kısmında ayırt edici noktaların bulunduğunu göstermektedir.

**V2 kararı:** Şu tür cümleler finalde kullanılmamalıdır:

> `Nokta ve hareke konulmamasının temel sebebi farklı kırâat vecihlerini tek resimde korumaktır.`

Bunun yerine iki düzey ayrılmalıdır:

1. erken Arap yazısının tarihsel grafik özellikleri;
2. sonraki resm/kıraat literatürünün bu özelliklere yüklediği işlevsel açıklama.

“Bilerek noktasız bırakıldı” görüşü kullanılacaksa açıkça klasik literatürdeki bir görüş olarak nispet edilmelidir.

## 20. Hazf, ziyâde ve ibdâlde “bilinçli/hikmetli tasarım” dili — CAND-064, 083, 084, 103, 146, 148

**Statü:** `QUALIFY`

Modern paleografik/ortografik veri, erken mushaflardaki birçok yazım özelliğinin erken Arap yazı geleneğinin tarihsel özellikleriyle açıklanabileceğini göstermektedir. Bu durum, bazı resm biçimlerinin rivayet edilmiş birden fazla okuyuşla bağdaşmasını reddetmez; fakat **uyumluluk ile tasarım niyeti aynı şey değildir**.

**V2 kararı:** `bilinçli olarak düşürüldü`, `hikmetli tercih`, `çoklu okuyuşları hedefleyen sistem`, `kırâatleri korumak için tasarlandı` gibi ifadeler, doğrudan kaynakta tarihsel niyet kanıtlanmadıkça yazarın nesnel hükmü olmayacaktır. Gerekirse “bazı âlimler bu yazım biçimini ... ile ilişkilendirmiştir” şeklinde nispet edilecektir.

# IV. Tevkîfîlik ve rivayetlerin kanıt değeri

## 21. Muâviye’ye yazı/kalem talimatı rivayeti — CAND-060

**Statü:** `QUALIFY / SOURCE-WEAK`

Muâviye’ye nispet edilen ayrıntılı kalem, harf ve estetik yazım talimatları klasik hadis değerlendirmelerinde sağlam bir kurucu delil değildir. Kaynaklarda rivayetin zayıf görüldüğü, bazı tariklerinin daha ağır eleştirildiği aktarılmaktadır.

**V2 kararı:** Rivayet tevkîfî resmin doğrudan tarihsel kanıtı olarak sunulmayacaktır. Kullanılacaksa “tevkîfîliği savunan bazı müelliflerin delil olarak zikrettiği, ancak sıhhati tartışmalı rivayetlerden biri” şeklinde çerçevelenecektir.

# V. Üçüncü ve Dördüncü Bölümde tarihsel/statüsel aşırı genellemeler

## 22. İbn Şenbûz olayı — CAND-120

**Statü:** `QUALIFY`

İbn Şenbûz’un kamusal kıraat uygulaması nedeniyle sorgulanıp bazı okuyuşlarından dönmeye zorlanması tarihsel kanonlaşma bağlamında önemlidir. Bununla birlikte olayı yalnız `resme aykırılık → şâzlık → ceza` formülüne indirgemek fazla basittir. Modern kıraat tarihi çalışmaları, bu hadiseyi rivayet, kamuya açık tilavet normu, icmâ/otorite ve Osmânî metin sınırı arasındaki daha geniş kanonlaşma sürecinde değerlendirmektedir.

**V2 kararı:** Final öneri, resme uygunluğu önemli bir unsur olarak koruyacak; fakat isnad/kabul/otorite ve kamusal tilavet boyutlarını silmeyecektir.

## 23. İsrail/Afrika’da tahrif edilmiş mushaf anlatısı — CAND-093, CAND-114

**Statü:** `REMOVE-UNLESS-SOURCED / HIGH-RISK`

**Mevcut manuscript iddiası:** 1960-1964 yılları arasında İsrail’in yaklaşık altı bin mushafı kasıtlı olarak tahrif edip Afrika ülkelerinde dağıttığı kesin tarihsel olay gibi aktarılmaktadır. Başka bir paragrafta ise belirli bir silmenin “suçlulardan dikkati uzaklaştırma” amacı taşıdığı ileri sürülmektedir.

**Kaynak problemi:** Manuscriptin kendi çalışma notu, bu iddianın dayandığı gazete kayıtlarının yazar tarafından yeniden bulunamadığını ve bağlantıların çalışmadığını açıkça kabul etmektedir. Yeni taramada güncel ikincil bir haber kaynağı benzer 1960 Mısır basını iddialarını yeniden aktarmaktadır; fakat bu, olayın bağımsız ve birincil doğrulaması değildir. Bu aşamada listelenen gazete nüshalarının güvenilir taranmış kopyaları doğrudan doğrulanamamıştır.

**V2 kararı:**

- Birincil gazete nüshaları veya güvenilir akademik çalışma bulunamazsa olay kesin tarihsel kanıt olarak kullanılmamalıdır.
- Tutulacaksa yalnız “1960’ta bazı Mısır gazetelerinde bu yönde iddialar yayımlandığı aktarılmıştır” seviyesine çekilmelidir.
- `Bu son silmenin amacı ... suçlulardan dikkati uzaklaştırmaktır` cümlesi, kaynaklanmış açık bir niyet beyanı bulunmadıkça çıkarılmalıdır.

Bu kayıt final raporda güçlü bir düzeltme maddesi gerektirir.

# VI. Matbu mushaf kronolojisi — CAND-130, 131, 132, 133, 157

## 24. Hinckelmann ve Marracci

**Statü:** `VERIFIED-CORRECT-WITH-QUALIFICATION`

Hamburg’da Hinckelmann’ın 1694 baskısı ile Padova’da Marracci’nin 1698 baskısı erken Avrupa Kur’an baskıları arasında güvenli biçimde yer alır. Ancak “ilk basılı Kur’an” gibi mutlak ifadeler daha erken Avrupa teşebbüsleri/baskıları nedeniyle ayrıca tanımlanmalıdır.

**V2 kararı:** Manuscriptteki “Avrupa’da matbu mushaf tarihinin erken örnekleri” ifadesi güvenli; “ilk” gibi mutlaklaştırma yapılmamalıdır.

## 25. Saint Petersburg 1787 baskısı ve `Mevlây Osman (?)`

**Statü:** `VERIFIED-CORRECTION / IDENTITY-WORDING`

**Doğrulanan çekirdek:** II. Katerina’nın emriyle Saint Petersburg’daki Şnor matbaasında 1787’de Kur’an basılmıştır. Türkçe ve Rusça çalışmalarda baskının hazırlanmasında `Molla Osman` / `Osman İsmagıylev` adıyla anılan bir Müslüman görevlinin rolü zikredilir.

**Sorun:** Manuscriptteki `Mevlây Osman (?) hattı esas alınarak` ifadesi hem kişi adını belirsizleştirmekte hem de kaynağın desteklediğinden daha özel bir “hat esas alma” iddiası kurabilmektedir.

**V2 kararı:** Final öneride, kullanılan kaynağa göre `1787’de II. Katerina’nın emriyle Saint Petersburg’da gerçekleştirilen baskı` denmeli; Molla Osman’ın rolü ancak kaynakta nasıl tanımlanıyorsa o düzeyde belirtilmelidir. `Mevlây Osman (?)` kaldırılacaktır.

## 26. Osmanlı Devleti’nde yasal Kur’an basımı: 1873/1874

**Statü:** `VERIFIED-CORRECTION`

Hakemli Belleten araştırması, Bâb-ı Âli’nin basım kararını **1873**’te aldığını; Osmanlı Devleti’nde yasal yollarla Kur’an basımının Maarif Nezareti denetiminde ilk defa **1874**’te gerçekleştirildiğini göstermektedir.

**V2 kararı:** `1873’te ilk resmî/yasal Osmanlı mushafı basıldı` şeklindeki kullanım düzeltilmelidir. Doğru ayrım: **karar 1873, basım 1874**.

# VII. Google AI dosyaları için faktik güvenilirlik kararı

Google AI dosyalarının bu aşamadaki durumu tek yönlü değildir:

### Yararlı doğrulama ipuçları

- Ca‘berî için `732/1332` düzeltmesi doğru çıktı.
- Bazı bozuk çalışma notlarını ve tarihlerdeki açık hataları fark etmiş olması yararlı.
- Bölüm bazlı yeni kaynak adayları üretmesi sonraki zenginleştirme aşamasında değerlendirilebilir.

### Doğrudan kullanılamayacağını gösteren örnekler

- Alemüddin es-Sehâvî için `642/1244` vermesi yanlıştır; güvenilir biyografik kaynak `643/1245` verir.
- Cevherî için `393/1003` kesinliği güvenli değildir; TDV `400/1009’dan önce` biçiminde ihtiyatlıdır.
- Mushaf sayısını farklı klasik rivayetlerden yeni bir “altı resmî akış” modeline dönüştürmesi kaynakların söylediğinden ileri gider.
- “Noktasız yazım özellikle kıraatleri taşımak için tasarlandı”, “grafik plastisite”, “tam konsensüs” gibi cümlelerde tarihsel veri, sonraki klasik yorum ve Google’ın kendi sentezi birbirine karışmaktadır.

**Bağlayıcı V2 ilkesi:** Google AI dosyası hiçbir durumda tek başına `VERIFIED` statüsü oluşturamaz. Her bilgi bağımsız kaynakla doğrulanacak; kabul edilen bilgi bile yazarın mevcut üslubunda yeniden yazılacaktır.

# VIII. Modern kaynaklardan kitaba gerçekten değer katabilecek seçili ek kaynaklar

Bu kaynaklar final rapora otomatik olarak eklenmeyecektir. Yalnız ilgili maddede mevcut dipnotun yetersiz kaldığı veya yazarın metni çağdaş araştırmayla zenginleştirmek istediği durumlarda APA 7 önerisi olarak kullanılabilir.

1. **Van Putten, M. (2019).** “The Grace of God” as evidence for a written Uthmanic archetype: The importance of shared orthographic idiosyncrasies. *Bulletin of the School of Oriental and African Studies, 82*(2), 271–288. https://doi.org/10.1017/S0041977X19000338
   - Kullanım alanı: erken yazılı arketip, ortak ortografik özellikler, yazılı örnekten kopyalama.

2. **Sidky, H. (2023).** Consonantal dotting and the oral Quran. *Journal of the American Oriental Society, 143*(4), 785–814. https://doi.org/10.7817/jaos.143.4.2023.ar029
   - Kullanım alanı: kanonik kıraatlerde miras alınmış bölgesel sözlü aktarımın erkenliği.

3. **van Putten, M. (2022).** When the readers break the rules: Disagreement with the consonantal text in the canonical Quranic reading traditions. *Dead Sea Discoveries, 29*(3), 438–462. https://doi.org/10.1163/15685179-02903008
   - Kullanım alanı: kanonik kıraatlerin rasmle genel uyumu ve nadir uyumsuzluk istisnaları.

4. **Ghabban, ‘A. I., & Hoyland, R. (2008).** The inscription of Zuhayr, the oldest Islamic inscription (24 AH/AD 644–645), the rise of the Arabic script and the nature of the early Islamic state. *Arabian Archaeology and Epigraphy, 19*(2), 210–237. https://doi.org/10.1111/j.1600-0471.2008.00297.x
   - Kullanım alanı: erken Arap yazısında ayırt edici noktaların varlığı; mushafların bilerek noktasızlaştırıldığına ilişkin klasik açıklamanın tarihsel olarak ayrı değerlendirilmesi.

5. **Zengin, Z. S. (2023).** Osmanlı Devleti’nde Kur’an Basımının İlk Safhası. *Belleten, 87*(309), 527–557. https://doi.org/10.37879/belleten.2023.527
   - Kullanım alanı: 1873 karar / 1874 yasal basım ayrımı ve Osmanlı basım politikası.

6. **Özdemir, F. (2025).** Hicrî Beşinci Asrın Resmü’l-Mushaf Literatürüne Katkısı Bağlamında İbn Muʿāz el-Cühenî ve “Kitâbü’l-Bedîʿ fî maʿrifeti mâ rusime fî Muṣḥafi ʿOs̱mān” Adlı Eseri. *Tefsir Araştırmaları Dergisi*. [Bibliyografik cilt/sayı/sayfa bilgisi final atıf önerisinden önce Zotero/dergi kaydından tamamlanacaktır.]
   - Kullanım alanı: İbn Mu‘âz kimliği/ölüm tarihi ve resm literatürü.

# IX. V2 final raporuna taşınacak bağlayıcı kararlar

1. **Doğru bilgi bulunabiliyorsa silmek yerine düzelt.** Ca‘berî, Hamîdullah, Bâkıllânî, İbn Mu‘âz gibi kayıtlar bunun açık örnekleridir.
2. **Tekrar eden ölüm tarihini bilgi hatasıyla karıştırma.** Tarih doğruysa fakat daha önce verilmişse yalnız tekrarında kaldır.
3. **Google AI fact-check değildir.** Doğru çıkan bilgiler de bağımsız kaynaktan doğrulanmış olarak kullanılacak.
4. **Kaynak rivayeti ile yazarın mekanizma açıklamasını ayır.** Mervân örneğinde bu ayrım zorunludur.
5. **Arza-i âhire ilişkisini “kanıtlanmış mekanizma” olarak değil, kaynak/klasik yorum düzeyine göre ifade et.**
6. **Rasm ile kıraati tek yönlü nedensellikle bağlama.** Modern yazma ve kıraat araştırmaları hem erken yazılı aktarımı hem erken sözlü gelenekleri destekleyen veriler sunmaktadır.
7. **Erken noktalama yokluğu için amaç yükleme.** Tarihsel yazı özelliği ile sonraki işlevsel yorum ayrılacaktır.
8. **İsrail/Afrika iddiası kaynak sağlığı çözülmeden tarihsel kanıt olarak kalamaz.**
9. **Matbu mushaf kronolojisinde 1873 karar / 1874 basım ayrımı korunacak.**
10. **Final raporda bilimsel doğrulama görünmez arka plan olacaktır.** Yazara teknik kaynak denetim günlüğü değil, anlaşılır `Yer → İfade → Sorun → Önerilen düzeltme` maddesi gösterilecektir.

# X. Açık kalan hedefli doğrulamalar

Aşağıdaki kayıtlar final öneri yazılmadan önce gerektiğinde bir tur daha hedefli kaynak kontrolüne alınacaktır:

- `Amr b. Kays` kimliği ve güvenilir biyografik tarih (CAND-037).
- `Hâlid b. Ebü’l-Heyyâc` kimliği ve ilgili mushaf/hatt rivayetinin tam bağlamı (CAND-128).
- 1960 Mısır gazetelerinde İsrail/Afrika mushaf iddiasının birincil taranmış nüshaları (CAND-093/114). Birincil kayıt bulunamazsa madde `REMOVE-UNLESS-SOURCED` kalacaktır.
- 1905/1950’lerde Hz. Osman’a nispet edilen mushafların tıpkıbasımlarıyla ilgili manuscript kronolojisinin tam bibliyografik temeli.
- CAND-130–133’teki matbu mushaf ayrıntılarının her bir baskı için kaynak bazında exact eşleştirilmesi.
- Bozuk DOI’ler ve kaynakça biçimi, V2 bibliyografik aşamasında ayrı ele alınacaktır.

## Aşama sonucu

**PASS WITH TARGETED OPEN ITEMS.**

Yüksek riskli faktik alanların önemli bir bölümü doğrulandı ve eski pipeline’da yanlış/eksik çözülen bazı kayıtlar için güvenli düzeltme yolu bulundu. Açık kalan maddelerde tahmin yapılmayacak; bunlar sonraki author-facing metin üretiminden önce hedefli biçimde yeniden kontrol edilecektir.
