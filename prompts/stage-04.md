# AŞAMA 4 — Kitap Genelindeki Tekrarlanan, Kalıplaşmış ve Geçişe İlişkin Sorunların Sistematik Çözümü

Bu aşama, tek bir bölüme bağlı olmayan ve kitap boyunca tekrar eden anlatım/akış sorunlarını sistematik olarak tarar. Aşama 3'te zaten çözülen pasajları gereksiz biçimde çoğaltma.

## Çalışma sözleşmesi

1. `AGENTS.md` dosyasını önce oku ve bağlayıcı kabul et.
2. Yalnız `editorial/fourth-report` dalında çalış. `main`, `source/`, `prompts/` ve önceki aşama çıktılarını değiştirme.
3. `work/stage-02-verified-inventory.md` ve `work/stage-03-direct-revisions.md` tamamlanmış değilse dur.
4. Dış kaynak veya internet kullanma.
5. Bu aşamanın tek yazılabilir çıktısı `work/stage-04-crosscutting-revisions.md` dosyasıdır. Placeholder içeriğini tamamen değiştir.
6. Aşama tamamlanınca yalnız bu aşama çıktısını commit et. Önerilen commit mesajı: `Stage 4: resolve cross-cutting repetition and transition issues`.
7. Aşama 5'e geçme.

## Kaynaklar

- bağlayıcı güncel nüsha: `source/manuscript/current/redaktorden_gelen.docx`
- arama yardımcısı: `source/manuscript/current/redaktorden_gelen_extracted.md`
- zorunlu redaktör/yazar notları: `source/notes/duzeltilecekler.docx`
- önceki bulgu ve işaret envanterleri: `source/reports/`
- Aşama 2 ve 3 çıktıları

Kırmızı biçimlendirme veya Word'e özgü işaret Markdown çıkarımında görünmüyorsa, üçüncü rapordaki işaret envanterini **yer bulma yardımcısı** olarak kullan ve mevcut metni güncel nüshada doğrula. Biçim bilgisini tahmin etme.

## Amaç

Aşağıdaki kitap-geneli örüntüleri tam kapsamayla gözden geçir ve yalnız gerçekten müdahale gerektiren örnekler için doğrudan uygulanabilir çözüm üret:

1. redaktörün işaretlediği `değil/değildir` kullanımları ve tekrarlanan negatif tanımlar,
2. Sonuç bölümü dışındaki `Sonuç olarak` kullanımları,
3. gereksiz ara sonuç ve özet paragrafları,
4. kalıplaşmış paragraf açılış ve kapanışları,
5. yakın mesafede tekrarlanan bağlaç/yüklem kalıpları,
6. zayıf paragraf, alt başlık ve ana bölüm geçişleri,
7. Aşama 3'te çözülmemiş açık çalışma notları.

Bu aşama bir “AI detector” çalışması değildir. Metnin kökeni hakkında hüküm verme; yalnız doğal akademik Türkçeyi zayıflatan örüntüleri değerlendir.

## 1. `değil/değildir` tam kapsama taraması

Redaktörün özellikle gözden geçirilmesini istediği bütün ilgili kullanımları tek tek değerlendir. Her birini iç kontrolde üç sonuçtan birine bağla:

- `CHANGE` — değiştirilmesi gerekir;
- `ALREADY_RESOLVED_STAGE3` — Aşama 3'te aynı pasaj zaten yeterli biçimde düzeltilmiştir;
- `KEEP` — karşıtlık anlam için gerekli ve mevcut kullanım doğaldır.

`KEEP` örneklerini yazarın nihai raporuna taşıma, fakat kapsam sayımında değerlendirildiğini göster.

`CHANGE` için mutlaka:

**Bölüm/Başlık → Sayfa → Bulmak için → Mevcut metin → Sorun → Önerilen düzeltme**

zincirini tamamla.

Amaç `değil` sözcüğünü eş anlamlıyla değiştirmek değil; gerekiyorsa cümleyi olumlu ve daha doğal yapıyla yeniden kurmaktır.

## 2. `Sonuç olarak` tam kapsama taraması

**Sonuç bölümü dışındaki** bütün `Sonuç olarak` kullanımlarını güncel metinde yeniden say ve tek tek incele. Önceki raporlardaki sayıyı otomatik kabul etme.

Her kullanım için iç kontrolde şu kararlardan birini ver:

- `KEEP-SYNTHESIS` — gerçek ve gerekli sentez;
- `CHANGE-TRANSITION` — doğal geçişe dönüştürülmeli;
- `MERGE` — önceki paragrafa yedirilmeli;
- `DELETE` — yeni değer taşımayan gereksiz ara sonuç;
- `ALREADY_RESOLVED_STAGE3`.

Yazar raporuna yalnız değişiklik gerektirenleri taşı. “Geçişe dönüştür”, “yedir”, “kısalt” gibi soyut talimat bırakma; sonucu tam metin olarak ver.

## 3. Gereksiz ara sonuç ve özetler

Bir paragrafı yalnız alt başlığın sonunda bulunduğu için gereksiz sayma. Şu testi uygula:

- Önceki iki/üç paragrafta söylenenleri yeni bilgi veya yeni analitik sonuç olmadan tekrar ediyor mu?
- Çıkarılırsa anlam kaybı oluyor mu?
- Sonraki başlığa geçiş için gerçekten gerekli mi?
- Aynı işlev bir önceki paragrafın tek cümlesiyle sağlanabilir mi?

Sorun varsa en ekonomik çözümü **uygulanmış metin** olarak ver.

## 4. Kalıplaşmış anlatım taraması

“Formülaik anlatım” terimini kullanma. Aşağıdaki kalıpları özellikle tara:

- Bu bağlamda
- Bu çerçevede
- Bu noktada
- Bu açıdan
- Bu yönüyle
- Bununla birlikte
- Nitekim
- Dolayısıyla
- Böylece
- Bu durum
- Bu yaklaşım
- Bu süreç
- söz konusu
- göstermektedir
- ortaya koymaktadır
- açıkça ortaya koymaktadır
- anlaşılmaktadır
- değerlendirilmektedir
- yalnız ... değil, aynı zamanda ...
- ne ... ne de ...
- bir taraftan ... diğer taraftan ...
- art arda `-maktadır/-mektedir` yüklemleri

Toplam kullanım sayısı **tek başına hata değildir**. Müdahale için özellikle yakın tekrar, aynı işlevin mekanik biçimde yinelenmesi, gerçek mantıksal ilişki olmadan bağlaç kullanılması, soyut dolgu veya aynı paragrafta tekdüze yüklem zinciri bulunmalı.

Bütün `Nitekim`leri veya bütün `göstermektedir`leri değiştirme. Yalnız bağlamda gerçekten sorun yaratan kullanımları seç ve cümlenin tamamını doğal biçimde düzenle.

## 5. Paragraf açılış/kapanış kümeleri

Yakın paragraflarda art arda benzer açılış veya kapanışlar bulunuyorsa kümeyi birlikte değerlendir. Örneğin:

- “Bu bağlamda...” / “Bu çerçevede...” / “Bu noktada...”
- “Bu durum ... göstermektedir.” / “Böylece ... ortaya çıkmaktadır.” / “Sonuç olarak ... anlaşılmaktadır.”

Yalnız ilk kelimeyi değiştirerek sahte çeşitlilik üretme. Gerekirse paragrafın ilk veya son cümlesini içerik merkezli yeniden kur.

## 6. Geçişlerin sistematik kontrolü

Aşama 2 ve önceki raporlarda işaretlenen bütün önemli geçişleri tek tek kontrol et. Aşama 3'te çözülmüşse tekrar üretme; çözüm yetersizse bu aşamada daha iyi tek çözüm hazırla.

Özellikle şu ana geçişlerin kapsandığını doğrula:

- Giriş → Birinci Bölüm
- Birinci Bölüm → İkinci Bölüm
- İkinci Bölüm → Üçüncü Bölüm
- Üçüncü Bölüm → Dördüncü Bölüm
- Dördüncü Bölüm → Sonuç

Ayrıca raporlarda işaretlenen önemli alt başlık geçişlerini de kapsa.

Geçiş çözümünde önce şu sırayı uygula:

1. önceki paragrafın son cümlesini düzelt,
2. sonraki paragrafın ilk cümlesini düzelt,
3. gereksiz ara paragrafı çıkar/birleştir,
4. yalnız gerçekten gerekliyse yeni geçiş cümlesi veya kısa paragraf ekle.

## 7. Metinde kalmış notlar için son tarama

Aşama 3'te çözülmemiş bütün açık çalışma notlarını yeniden kontrol et. Notun istediği işlem anlaşılabiliyorsa işlemi gerçekleştir ve nihai metni ver. B1-04 modeli burada da geçerlidir.

## 8. Sıklık bilgisi nasıl kullanılacak

Güncel metinden kesin sayılabilen belirgin kalıpları kısa bir iç özet olarak verebilirsin. Ancak sayıyı doğrudan “sorun” diye yorumlama. Örneğin:

> `Nitekim` toplam X kez geçmektedir; asıl müdahale gerektirenler yakın aralıklı ve aynı işlevli tekrarlar olarak aşağıda gösterilmiştir.

Kesin sayım yapılamıyorsa tahmin üretme.

## 9. Aşama 3 ile çakışma kuralı

Aynı pasaj Aşama 3'te zaten düzeltilmişse:

- öneri bütün sorunları çözüyorsa `ALREADY_RESOLVED_STAGE3` olarak kaydet ve yeniden yazar maddesi üretme;
- yeni çapraz tarama, Aşama 3 önerisinde gerçek eksik gösteriyorsa tek bir **revize nihai öneri** oluştur ve bunu açıkça Aşama 5'in Aşama 3 çözümünün yerine kullanması gerektiğini belirt.

## Çıktı

`work/stage-04-crosscutting-revisions.md` dosyasını şu yapıyla oluştur:

1. `# Aşama 4 — Kitap Geneli Anlatım ve Geçiş Düzeltmeleri`
2. `## Değil/Değildir — Müdahale Gerektiren Kullanımlar`
3. `## Sonuç Olarak ve Gereksiz Ara Sonuçlar`
4. `## Kalıplaşmış ve Mekanikleşen Anlatım Örnekleri`
5. `## Paragraf Açılış ve Kapanış Tekrarları`
6. `## Eksik veya Zayıf Geçişler`
7. `## Metinde Kalmış Çalışma Notları`
8. `## Aşama 3 Çözümlerinin Yerine Geçen Revizyonlar`
9. `## Kapsam ve Sayım Özeti`

Kapsam özetinde en az şunları ver:

- incelenen redaktör işaretli `değil/değildir` sayısı ve `CHANGE/KEEP/ALREADY_RESOLVED` dağılımı,
- Sonuç bölümü dışındaki `Sonuç olarak` toplamı ve karar dağılımı,
- kontrol edilen önemli geçiş sayısı ve değişiklik gerektiren sayı,
- kesin sayılabildiği ölçüde diğer belirgin kalıp sayımları.

Bu sayımlar iç denetim içindir; nihai yazar raporuna otomatik olarak taşınmayacaktır.

Dosyayı tamamla, Aşama 3 ile çakışmaları çöz, commit et ve **dur**.