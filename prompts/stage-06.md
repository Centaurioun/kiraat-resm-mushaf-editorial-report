# AŞAMA 6 — Nihai İçerik Adayının Bağımsız Son Denetimi ve Düzeltilmiş Son Sürümün Hazırlanması

Bu aşama **nihai raporu henüz oluşturmaz**. Aşama 5'te hazırlanan içerik adayını bağımsız ve kuşkucu bir son denetimden geçirir; eksik, tekrarlı, çelişkili veya yazar açısından kullanışsız kalan maddeleri düzeltir ve Aşama 7'nin doğrudan kullanacağı son içerik paketini üretir.

## Çalışma sözleşmesi

1. `AGENTS.md` dosyasını önce oku ve bağlayıcı kabul et.
2. Yalnız `editorial/fourth-report` dalında çalış. `main`, `source/`, `prompts/` ve önceki aşama çıktılarını değiştirme.
3. `work/stage-05-final-content.md` tamamlanmış değilse dur.
4. Aşama 1-5 çıktılarını denetim için okuyabilirsin; kaynak konusunda son hakem güncel kitap nüshasıdır.
5. Dış kaynak veya internet kullanma.
6. Bu aşamanın tek yazılabilir çıktısı `work/stage-06-final-audited-content.md` dosyasıdır. Placeholder içeriğini tamamen değiştir.
7. Aşama tamamlanınca yalnız bu aşama çıktısını commit et. Önerilen commit mesajı: `Stage 6: audit and finalize author-facing content set`.
8. `final/fourth-report.md` dosyasını henüz değiştirme. Aşama 7'ye geçme.

## Amaç

Aşama 5 çıktısını yalnız yeniden okumakla yetinme. Şu iki soruya bağımsız olarak cevap ver:

1. **Önceki bütün doğrulanmış ve yazarın müdahale edebileceği sorunlar eksiksiz temsil ediliyor mu?**
2. **Her madde yazarın başka bir belgeye veya teknik bilgiye ihtiyaç duymadan uygulayabileceği kadar açık ve güvenli mi?**

Eksik veya kusurlu bir madde bulursan yalnız rapor etme; proje kaynakları izin verdiği ölçüde **bu aşama çıktısında düzelt**.

## 1. Kapsam denetimi

Aşağıdakileri çapraz karşılaştır:

- `work/stage-02-verified-inventory.md`
- `work/stage-03-direct-revisions.md`
- `work/stage-04-crosscutting-revisions.md`
- `work/stage-05-final-content.md`

Aşama 2'de `VERIFIED` veya `NEW-SOURCE` olarak kalan ve yazarın müdahale edebileceği her sorunun Aşama 5'te:

- ayrı bir düzeltme maddesi,
- başka bir maddeyle açıkça birleştirilmiş çözüm,
- veya kaynak sınırı açıklaması

olarak karşılığı bulunmalı.

Sessizce kaybolmuş bir madde bulursan geri ekle.

## 2. Kaynakla yeniden örneklemeli doğrulama

Bütün kitabı sıfırdan dördüncü kez yeniden analiz etme; fakat Aşama 5'teki her ana bölümden ve yüksek riskli sorun türlerinden yeterli örnek seçerek güncel nüshayla yeniden karşılaştır.

Aşağıdaki yüksek riskli maddeleri **tam kapsamla** yeniden doğrula:

- metinde kalmış yazar/redaktör/yayınevi notları,
- B1-04 tipi birleştirme işlemleri,
- bölümler arası çelişkiler,
- kişi/tarih/kimlik sorunları,
- resm-i Osmânî'nin işlevini etkileyen bilimsel revizyonlar,
- yedi harf, arza-i âhire, sahâbe mushafları ve şâz kırâatle ilgili düzeltmeler,
- üçüncü bölümde mana/hikmet/i‘câz değerlendirmeleri,
- Aşama 4'te `CHANGE` verilen `değil/değildir` ve `Sonuç olarak` maddeleri,
- büyük paragraf birleştirme/bölme/taşıma ve ana bölüm geçişleri.

Bir önerilen metin güncel pasajı yanlış temsil ediyorsa düzelt.

## 3. Yazar kullanılabilirliği testi

Her maddede şu beş sorunun cevaplandığını doğrula:

1. **Nerede?** — bölüm/başlık, mümkünse sayfa ve paragraf başlangıcı.
2. **Ne yazıyor?** — gerekli mevcut metin.
3. **Sorun ne?** — sade ve kısa açıklama.
4. **Ne yapılmalı?** — işlemin açık sonucu.
5. **Yerine ne yazılmalı?** — kaynaklar izin veriyorsa doğrudan kullanılabilir nihai metin.

Yazarın hâlâ “nasıl birleştireceğim?”, “nereye taşıyacağım?”, “neyle değiştireceğim?” diye düşünmesi gerekiyorsa madde tamamlanmamıştır.

## 4. Teknik dil temizliği

Yazar-facing içerikte şu tür dili bırakma:

- Heading, TOC, PAGEREF,
- RTL, bidi, run, OOXML,
- Zotero field,
- `CAND-*`, `VERIFIED`, `CHANGE`, `KEEP`,
- kapatma matrisi, sınıf C/D/E,
- paragraf kimliği,
- render veya Word iç yapı talimatları.

Bu bilgiler iç denetim bölümünde bile yalnız gerçekten gerekli ise bulunabilir; Aşama 7'nin alacağı ana içerikte yer almamalıdır.

## 5. Tekrar ve çift çözüm denetimi

Aynı pasajın iki farklı maddede tekrarlandığı yerleri bul. Aynı değişiklik iki kez yapılacakmış izlenimi doğuyorsa tek maddeye indir.

Ancak iki ayrı konum gerçekten iki ayrı değişiklik gerektiriyorsa ikisini de koru.

Özellikle bölüm içindeki bir sorun ile “Kitap Genelinde Tekrarlanan ve Kalıplaşmış Anlatımlar” bölümünün aynı pasajı tekrar edip etmediğini kontrol et.

## 6. Bilimsel güvenlik denetimi

Her önerilen metni şu açılardan yeniden kontrol et:

- resm-i Osmânî bağımsız kırâat kaynağı gibi mi sunuluyor?
- telakki, müşâfehe, edâ, isnad ve rivâyetin aslî aktarım zemini oluşu korunuyor mu?
- resme uygunluk ile isnad sahihliği karışıyor mu?
- teorik yazım ihtimali sahihlik gibi mi sunuluyor?
- kırâat/rivâyet/tarîk/vecih terimleri birbirine mi karışıyor?
- tarihsel rivâyet kesin olay gibi mi anlatılıyor?
- klasik yorum kaynak görüşüymüş gibi mi genişletiliyor?
- sahâbe mushaflarının tarihsel değeri ile Osmânî mushafların müşterek normatif statüsü karışıyor mu?
- yazım özelliğine delilsiz mana/hikmet/i‘câz yükleniyor mu?

Sorun varsa öneriyi bu aşamada düzelt.

## 7. Kaynak ve bibliyografik güvenlik

- Yeni tarih, kişi kimliği, eser, rivâyet, kırâat vechi, DOI veya bibliyografik ayrıntı üretme.
- Doğru bilgi proje dosyalarından kesinleşmiyorsa şüpheli ayrıntıyı kaldıran veya ihtiyatlılaştıran çözümü tercih et.
- Doğrudan alıntıları serbestçe yeniden yazma.
- Mevcut dipnotun desteklediği iddianın anlamını revizyonla genişletme.

## 8. Geçiş ve paragraf mimarisi denetimi

Önemli geçiş önerilerinin gerçekten iki tarafı birbirine bağladığını kontrol et. Yeni geçiş cümlesi yalnız “Bu bağlamda/Bu çerçevede” gibi biçimsel bir köprü olmamalı; mantıksal ilişkiyi kurmalıdır.

Birleştirilen veya bölünen paragraflarda:

- anlam kaybı,
- dipnot ilişkisinin bozulması,
- yeni tekrar,
- gereksiz sonuç cümlesi

oluşmadığını kontrol et.

## 9. `değil/değildir` ve `Sonuç olarak` kapsam kanıtı

Aşama 4'ün kapsam özetini kontrol et. Redaktör işaretli `değil/değildir` örneklerinin tamamı değerlendirilmiş mi? Sonuç bölümü dışındaki bütün `Sonuç olarak` kullanımları karar almış mı?

Sayısal uzlaştırma tutmuyorsa Aşama 4'ü sessizce varsayma; güncel metin ve ilgili raporlarla eksik vakayı bul ve Aşama 6 çıktısında çöz.

## 10. Nihai yapı ve tablo politikası

Aşama 7'ye aktarılacak yazar-facing ana içerik şu sırayı izlesin:

1. Kısa Kullanım Açıklaması için hazır metin
2. Önsöz
3. Giriş
4. Birinci Bölüm
5. İkinci Bölüm
6. Üçüncü Bölüm
7. Dördüncü Bölüm
8. Sonuç
9. Kitap Genelinde Tekrarlanan ve Kalıplaşmış Anlatımlar
10. Kaynakça ve Açık Bibliyografik Düzeltmeler

Tablo yalnız gerçekten bir bakışta karşılaştırma yararı sağlıyorsa korunmalı. Uzun envanter, durum, kod veya teknik takip tabloları Aşama 7'ye aktarılmamalıdır.

## 11. Son kullanıcı simülasyonu

En azından her ana bölümden birkaç maddeyi şu şekilde zihinsel olarak uygula:

> Yazar ilgili sayfaya gidiyor, mevcut metni buluyor, rapordaki açıklamayı okuyor ve önerilen metni yerine koyuyor.

Bu senaryoda belirsiz kalan işlem varsa maddeyi yeniden yaz.

## Çıktı

`work/stage-06-final-audited-content.md` dosyasını iki ana bölümle oluştur:

### I. `# Aşama 6 — Nihai Denetimden Geçmiş Yazar-Odaklı İçerik`

Bu bölüm, Aşama 7'nin doğrudan kullanacağı **tam ve düzeltilmiş yazar-facing içerik** olsun. İç denetim kodlarını ve eski rapor tarihçesini içerme.

### II. `# İç Denetim Makbuzu — Aşama 7'ye Aktarılmayacak`

Kısa ama doğrulanabilir biçimde şunları kaydet:

- Aşama 2'deki doğrulanmış sorunların Aşama 6'ya uzlaştırma sonucu,
- geri eklenen eksik maddeler,
- birleştirilen mükerrer maddeler,
- bilimsel güvenlik nedeniyle değiştirilen öneriler,
- kaynak sınırı nedeniyle tam çözülemeyen maddeler,
- `değil/değildir` ve `Sonuç olarak` kapsam uzlaştırmasının sonucu,
- Aşama 7'ye geçmeye engel açık bir eksik bulunup bulunmadığı.

Açık ve ciddi bir eksik varsa “hazır” ilan etme; ana içerikte mümkünse düzelt. Kaynak yetersizliği nedeniyle çözülemiyorsa açıkça kaydet.

Dosyayı tamamla, iç denetim makbuzuyla ana içeriğin tutarlı olduğunu doğrula, commit et ve **dur**. `final/fourth-report.md` dosyasına dokunma.