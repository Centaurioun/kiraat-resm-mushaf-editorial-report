# AŞAMA 2 — Aday Sorunların Güncel Kitapta Doğrulanması ve Kesin Konumlandırılması

Bu aşama, Aşama 1'deki aday sorunların güncel kitapta gerçekten devam edip etmediğini doğrular. Henüz sistematik olarak yeni düzeltme metinleri yazma ve nihai raporu hazırlama.

## Çalışma sözleşmesi

1. `AGENTS.md` dosyasını önce oku ve bağlayıcı kabul et.
2. Yalnız `editorial/fourth-report` dalında çalış. `main`, `source/`, `prompts/` ve önceki aşama çıktılarını değiştirme.
3. Önkoşul olarak `work/stage-01-final-inventory.md` dosyasının placeholder olmadığını ve tamamlanmış Aşama 1 çıktısını içerdiğini doğrula. Değilse dur.
4. Dış kaynak veya internet kullanma.
5. Bu aşamanın tek yazılabilir çıktısı `work/stage-02-verified-inventory.md` dosyasıdır. Placeholder içeriğini tamamen değiştir.
6. Aşama tamamlanınca yalnız bu aşama çıktısını commit et. Önerilen commit mesajı: `Stage 2: verify candidate issues against current manuscript`.
7. Sonraki aşamaya geçme.

## Kaynak hiyerarşisi

Doğrulamada şu sırayı uygula:

1. `source/manuscript/current/redaktorden_gelen.docx` — bağlayıcı güncel nüsha.
2. `source/manuscript/current/redaktorden_gelen_extracted.md` — arama ve metin bulma yardımcısı.
3. `source/notes/duzeltilecekler.docx` — redaktör/yazar talimatlarının bağlamı.
4. `source/reports/` — adayın nereden geldiğini anlamak ve çapraz kontrol etmek için.
5. `source/manuscript/archive/` — yalnız tarihsel karşılaştırma gerektiğinde; güncel nüshanın yerine geçmez.

DOCX ile çıkarılmış Markdown arasında maddi fark görürsen **DOCX'i esas al ve farkı kaydet**. Biçim, kırmızı işaret, dipnot, Arapça yerleşim veya sayfa gibi Markdown'ın güvenilir taşımadığı unsurlarda DOCX'e dayan.

## Amaç

Aşama 1'de kalan her `CAND-*` adayını tek tek inceleyerek şu sorulara cevap ver:

- Sorun güncel kitapta hâlâ var mı?
- Sorun tam olarak nerede?
- Mevcut metin tam olarak ne söylüyor?
- Sorun tek cümle mi, paragraf mı, ardışık birkaç paragraf mı, yoksa iki ayrı bölüm arasındaki ilişki mi?
- Düzeltme yapılırken hangi çevre metin birlikte ele alınmalı?
- Adayın önceki rapordaki tanımı güncel metni doğru temsil ediyor mu?

## Her aday için zorunlu karar

Her `CAND-*` kaydı aşağıdaki durumlardan **tam olarak biriyle** sonuçlansın:

- `VERIFIED` — sorun güncel kitapta sürüyor ve yazar raporuna aday.
- `MERGED` — başka doğrulanmış adayla aynı editoryal işlem gerektiriyor; hedef kimliği belirt.
- `RESOLVED` — güncel nüshada artık sorun yok.
- `NOT_FOUND` — rapordaki ifadeyi güncel metinde güvenilir biçimde bulamadın.
- `TECHNICAL_EXCLUDED` — yazarın düzeltme raporuna ait olmayan teknik mesele.
- `UNRESOLVED_SOURCE_LIMIT` — sorun gerçek görünüyor ancak proje dosyaları güvenli bir çözüm için gerekli bilgiyi vermiyor.

Kararı kanıta dayandır. Eski raporda “düzeltilmemiş” yazdığı için otomatik `VERIFIED` verme.

## Kesin konumlandırma

`VERIFIED` her sorun için mümkün olduğunca şu üç konum bilgisini çıkar:

- **Bölüm/Başlık**
- **Güncel sayfa**
- **Bulmak için:** paragrafın ayırt edici ilk kelimeleri

`P52`, `P106`, `run 43` gibi iç teknik kimlikleri nihai konum olarak kullanma.

Sayfa numarasını güvenilir biçimde doğrulayamıyorsan tahmin etme. İç kayıtta `Sayfa: doğrulanamadı` yaz ve başlık + paragraf başlangıcını eksiksiz ver. Yanlış sayfa numarası, eksik sayfa numarasından daha kötüdür.

## Mevcut metni eksiksiz yakala

Sorunu açıklamak için gerekli kadar mevcut metni birebir kaydet:

- tek cümle yeterliyse cümle,
- paragraf yeniden yazılacaksa paragraf,
- iki paragraf birleştirilecekse ikisi,
- numaralı maddeler birleşecekse gerekli bütün maddeler,
- iki bölüm çelişiyorsa iki yerdeki ilgili pasajlar.

Bağlamı eksilterek sonraki aşamada yanlış revizyona yol açma.

## Bağlam gerektiren editoryal işlemler

Özellikle eski raporlarda şu tür talimatlar varsa çevre metni genişlet:

- “ikinci maddeye yedir”
- “önceki paragrafa birleştir”
- “sonraki başlığa taşı”
- “kısalt”
- “geçiş ekle”
- “iki paragrafı birleştir”

B1-04 benzeri bir maddede, numaralı listenin girişini, ilgili ikinci ve üçüncü maddeleri ve geçiş için gerekliyse öncesi/sonrası metni birlikte doğrula. Aşama 3'ün işlem yapabilmesi için eksik bağlam bırakma.

## Çelişkilerde iki tarafı da doğrula

Bir aday iki bölüm arasındaki tutarsızlığa dayanıyorsa her iki pasajı da birebir bul. Hangisinin tek başına değiştirilmesinin yeterli olup olmayacağını yalnız not et; çözümü Aşama 3'e bırak.

## Tekrar, ara sonuç ve geçişlerde bağlam testi

Bir paragrafı “gereksiz tekrar” veya “zayıf geçiş” diye doğrulamadan önce:

- önceki paragrafı,
- ilgili paragrafı,
- sonraki paragrafı

birlikte oku.

Alt başlık geçişinde önceki başlığın son paragrafı ile sonraki başlığın ilk paragrafını birlikte değerlendir. Gerçek işlevi olan kısa hatırlatmayı gereksiz tekrar diye işaretleme.

## `Sonuç olarak` ve `değil/değildir`

Aşama 1'den gelen ilgili adayları bu aşamada **konum ve bağlam bakımından doğrula**, fakat kitap genelindeki tüm kullanımları henüz sistematik olarak çözme; bu Aşama 4'ün görevidir.

Her `Sonuç olarak` adayı için gerçek işlevi not et: sentez / geçiş / tekrar / gereksiz mini-sonuç.

Her `değil/değildir` adayı için not et:

- tam mevcut cümle,
- yakın çevrede benzer negatif yapı olup olmadığı,
- karşıtlığın anlam için gerekli olup olmadığı,
- olumlu yeniden kurmanın makul görünüp görünmediği.

## Metin içinde kalmış çalışma notları

“silinsin”, “yedirecektiniz”, “daha önce geçti mi?”, “burası düzeltilmemiş”, `(?)` ve benzeri notları yalnız kelime olarak değil, **istenen editoryal işlemle birlikte** doğrula. Notun talebi açık değilse tahmin etme; `UNRESOLVED_SOURCE_LIMIT` veya açıklayıcı not kullan.

## Aşama 1 dışında yeni bir açık sorun görürsen

Bu aşama esasen doğrulamadır; ancak güncel metni incelerken açık ve önemli bir sorunla karşılaşırsan onu sessizce görmezden gelme. `NEW-SOURCE-001` gibi ayrı bir kimlikle kaydet ve neden Aşama 1'de bulunmadığını kısaca belirt.

Yeni sorun üretmek için kitabı sınırsız biçimde yeniden tarama; yalnız doğrulama sırasında doğrudan karşılaştığın açık bulguları ekle.

## Doğrulanamayan ayrıntılar

Doğru tarih, kişi kimliği, eser bilgisi veya bibliyografik ayrıntı proje dosyalarından kesinleşmiyorsa tahmin etme. Sorunun varlığını ve çözüm sınırını açıkça kaydet.

## Çıktı biçimi

`work/stage-02-verified-inventory.md` dosyasını şu bölümlerle oluştur:

1. `# Aşama 2 — Güncel Kitapla Doğrulanmış Sorun Envanteri`
2. `## Doğrulanmış ve Dördüncü Rapora Taşınacak Sorunlar`
3. `## Birleştirilen Sorunlar`
4. `## Güncel Nüshada Çözülmüş veya Bulunamayan Sorunlar`
5. `## Kaynak Sınırı Nedeniyle Açık Kalanlar`
6. `## Doğrulama Sırasında Yeni Bulunan Açık Sorunlar`
7. `## Kapsam ve Sayım Özeti`

Her `VERIFIED` veya `NEW-SOURCE` maddesinde en az:

- kimlik,
- bölüm/başlık,
- sayfa veya `doğrulanamadı`,
- paragraf başlangıcı,
- gerekli mevcut metin,
- kısa sorun açıklaması,
- düzeltmenin kapsaması gereken metin parçaları,
- varsa kaynak sınırı

bulunsun.

Bu aşamada **sistematik nihai revizyon metinleri yazma**. Dosyayı tamamla, Aşama 1 ile sayısal ve mantıksal tutarlılığını kontrol et, commit et ve **dur**.