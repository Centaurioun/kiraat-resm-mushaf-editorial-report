# AŞAMA 5 — Bütün Düzeltmelerin Tekilleştirilmesi ve Yazar-Odaklı Nihai İçerik Adayının Oluşturulması

Bu aşama, Aşama 3 ve 4'te üretilen çözümleri bir araya getirerek **tek, tutarlı ve yazarın anlayabileceği içerik adayı** oluşturur. Henüz nihai Dördüncü Rapor Markdown dosyasını oluşturma.

## Çalışma sözleşmesi

1. `AGENTS.md` dosyasını önce oku ve bağlayıcı kabul et.
2. Yalnız `editorial/fourth-report` dalında çalış. `main`, `source/`, `prompts/` ve önceki aşama çıktılarını değiştirme.
3. `work/stage-02-verified-inventory.md`, `work/stage-03-direct-revisions.md` ve `work/stage-04-crosscutting-revisions.md` tamamlanmış değilse dur.
4. Dış kaynak veya internet kullanma.
5. Bu aşamanın tek yazılabilir çıktısı `work/stage-05-final-content.md` dosyasıdır. Placeholder içeriğini tamamen değiştir.
6. Aşama tamamlanınca yalnız bu aşama çıktısını commit et. Önerilen commit mesajı: `Stage 5: integrate author-facing revision content`.
7. Aşama 6'ya geçme.

## Amaç

Şimdiye kadar hazırlanmış bütün doğrulanmış ve çözülebilir maddeleri:

- aynı pasajı tekrar etmeyecek biçimde tekilleştir,
- bilimsel ve dilsel yönleri tek çözümde birleştir,
- kitap sırasına yerleştir,
- yazarın anlayamayacağı iç kod ve teknik dili çıkar,
- “ne yapmalıyım?” sorusunu cevapsız bırakan maddeleri tamamla,
- Dördüncü Rapora girecek **tam içerik adayını** oluştur.

Bu aşamada esas görev yeni sorun aramak değil, mevcut doğrulanmış çözüm setini doğru biçimde bütünleştirmektir.

## Kaynak ve bağımlılık sırası

İçerik oluştururken şu sırayı kullan:

1. Aşama 2 — hangi sorunların gerçekten mevcut olduğunu belirleyen doğrulama kaydı,
2. Aşama 3 — yerel/bilimsel/dilsel doğrudan çözümler,
3. Aşama 4 — çapraz tarama ve Aşama 3'ün yerine geçen güncellenmiş çözümler,
4. güncel kitap nüshası — metin ve konum şüphesinde son hakem.

Aşama 4 açıkça bir Aşama 3 önerisinin yerine geçen daha kapsamlı çözüm verdiyse yalnız Aşama 4 çözümünü kullan.

## 1. Aynı pasajı tek maddeye indir

Aynı paragraf veya metin parçası farklı aşamalarda:

- bilimsel sorun,
- `değil/değildir` sorunu,
- tekrar,
- geçiş,
- dil/tashih

olarak ayrı ayrı ele alınmış olabilir. Yazarın aynı yeri birkaç kez değiştirmesini isteme. Bütün gerçek sorunları çözen **tek nihai öneri** oluştur.

Yalnız gerçekten farklı konumlarda ayrı değişiklik gerektiren sorunlar ayrı madde olarak kalsın.

## 2. Her yazar maddesinin zorunlu yapısı

Her gerçek düzeltme maddesi mümkün olduğunca şu dört soruyu eksiksiz yanıtlamalıdır:

1. **Kitabın neresinde?**
2. **Şu anda ne yazıyor?**
3. **Buradaki sorun ne?**
4. **Bunun yerine tam olarak ne yazılmalı veya ne yapılmalı?**

Tercih edilen biçim:

### [Sorunun açık adı]

**Bölüm/Başlık:** ...

**Sayfa:** ...

**Bulmak için:** “...” ile başlayan paragraf

**Mevcut metin:**
> “...”

**Sorun:**
Kısa, açık ve teknik olmayan açıklama.

**Önerilen düzeltme:**
> “...”

İki veya daha fazla mevcut parçanın birlikte değişmesi gerekiyorsa gerekli bütün parçaları göster ve birleşik nihai metni ver.

## 3. Soyut editör talimatı bırakma

Aşağıdaki ifadeler tek başına çözüm sayılmaz:

- kısalt,
- birleştir,
- yedir,
- taşı,
- yeniden yaz,
- daha ihtiyatlı kur,
- olumlu ifade et,
- geçiş ekle,
- kaynak kontrolü yap.

Proje dosyaları izin verdiği ölçüde işlemi bizzat gerçekleştir ve yazarın kullanacağı metni ver.

Bir ayrıntı güvenli biçimde çözülemiyorsa bunu açıkça **Kaynak sınırı** olarak işaretle; uydurma çözüm üretme.

## 4. Yazar raporuna girmeyecek içerikler

Aşağıdakileri bu içerik adayından çıkar:

- `CAND-*`, `VERIFIED`, `CHANGE` gibi iç denetim kodları,
- önceki raporların tarihçesi,
- “tamamlandı/kısmen tamamlandı” durum takibi,
- teknik Word/dizgi bilgileri,
- Heading, TOC, PAGEREF, RTL, bidi, run, OOXML, Zotero field vb.,
- yalnız istatistik veya kapsam kanıtı olarak tutulan tam envanterler,
- yazarın yapacağı işlem olmayan `KEEP` maddeleri,
- yayın kararı, yönetici özeti ve proje yönetimi dili.

## 5. Bilimsel güvenlik kontrolü

Her öneriyi şu ilkeler açısından yeniden oku:

- kırâatlerin aslî aktarım zemini telakki, müşâfehe, edâ, isnad ve rivâyettir;
- resm-i Osmânî bağımsız kırâat kaynağı değildir;
- resme uygunluk ile isnad sahihliği birbirinden ayrıdır;
- yazının ihtimal vermesi tek başına sahihlik değildir;
- kırâat, rivâyet, tarîk, vecih terminolojisi karıştırılmamalıdır;
- tarihsel rivâyet, klasik yorum ve yazar çıkarımı aynı kanıt düzeyinde sunulmamalıdır;
- sahâbe mushafları ile Osmânî mushafların statüsü ayrılmalıdır;
- yazım özelliklerine kaynakların desteklemediği mana/hikmet/i‘câz yüklenmemelidir.

Bir öneri kaynakların verdiğinden daha güçlü kesinlik üretiyorsa düzelt.

## 6. Dipnot, alıntı ve bibliyografik güvenlik

- Yeni kaynak veya dipnot ekleme.
- Mevcut dipnotun dayandığı iddiayı revizyonla değiştirme.
- Doğrudan alıntıyı üslup amacıyla yeniden yazma.
- Kaynakçada doğru ayrıntı proje dosyalarından kesinleşmiyorsa yeni bilgi uydurma.
- Açık bozuk ayrıntı cümlenin anlamı için zorunlu değilse güvenli biçimde çıkarılması önerilebilir.

## 7. Konum bilgisini sadeleştir

Nihai yazar maddesinde mümkün olduğunca:

- Bölüm/Başlık,
- sayfa,
- paragraf başlangıcı

bulunsun.

Sayfa Aşama 2'de güvenilir biçimde doğrulanamamışsa yanlış sayı üretme. Böyle durumlarda başlık + paragraf başlangıcını kullan ve sayfa alanını `—` bırak.

## 8. Tablo politikası

Bu aşamada esas biçim **madde bazlı açıklama**dır. Tablo yalnız gerçekten toplu görünüm sağlıyorsa kullanılabilir.

Muhtemel üç kısa tablo:

1. önemli bölümler arası çelişkilerin özeti,
2. önemli eksik/zayıf geçişlerin özeti,
3. çok tekrarlanan bazı anlatım kalıplarının kısa sıklık özeti.

Tablo hiçbir zaman ayrıntılı çözümün yerine geçmez. Tablodaki gerçek düzeltmeler ayrıca madde olarak bulunmalıdır.

## 9. Kitap sırasına göre düzenle

Yazar kitabıyla birlikte baştan sona ilerleyebilsin. İçeriği şu sırayla düzenle:

1. Önsöz
2. Giriş
3. Birinci Bölüm
4. İkinci Bölüm
5. Üçüncü Bölüm
6. Dördüncü Bölüm
7. Sonuç
8. Kitap Genelinde Tekrarlanan ve Kalıplaşmış Anlatımlar — yalnız bölüm içine doğal biçimde yerleştirilemeyen çapraz konular
9. Kaynakça ve Açık Bibliyografik Düzeltmeler

Aynı kitabın bölümünde çözülebilen `değil`, `Sonuç olarak` veya geçiş sorunu ayrıca 8. bölümde tekrar edilmesin.

## 10. Kapsama uzlaştırması

Aşama 2'de `VERIFIED`/`NEW-SOURCE` olarak taşınan her yazar-düzeltilebilir sorunun bu içerik adayında **tam olarak bir karşılığı** olmalıdır; şu istisnalar dışında:

- Aşama 3/4'te başka maddeyle birleştirildi,
- yazar için işlem gerektirmediği doğrulandı,
- kaynak sınırı nedeniyle güvenli çözüm üretilemedi.

Bu istisnaları iç denetim amacıyla dosyanın sonunda ayrı bir **Kapsam Uzlaştırma Özeti**nde listele. Bu özet Aşama 7'de nihai yazar raporuna taşınmayacaktır.

## Çıktı

`work/stage-05-final-content.md` dosyasını şu yapıyla oluştur:

1. `# Aşama 5 — Yazar-Odaklı Nihai İçerik Adayı`
2. `## Önsöz`
3. `## Giriş`
4. `## Birinci Bölüm`
5. `## İkinci Bölüm`
6. `## Üçüncü Bölüm`
7. `## Dördüncü Bölüm`
8. `## Sonuç`
9. `## Kitap Genelinde Tekrarlanan ve Kalıplaşmış Anlatımlar`
10. `## Kaynakça ve Açık Bibliyografik Düzeltmeler`
11. `## Kaynak Sınırı Nedeniyle Tam Çözülemeyen Maddeler`
12. `## Kapsam Uzlaştırma Özeti — Nihai Rapora Alınmayacak İç Denetim Bölümü`

Bu dosya Aşama 6'nın bağımsız son denetimine girecek **tam içerik adayı** olmalıdır. Kendi içinde tekrar, çelişki ve eksik alan kontrolü yap; commit et ve **dur**.