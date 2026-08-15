# AŞAMA 7 — Yazar İçin Nihai Dördüncü Raporun Markdown Olarak Oluşturulması

Bu aşama, ilk altı aşamada hazırlanıp Aşama 6'da bağımsız son denetimden geçirilmiş içeriği **tek, yazar-facing nihai Dördüncü Rapor** hâline getirir. Bu aşamada Word/DOCX üretme.

## Çalışma sözleşmesi

1. `AGENTS.md` dosyasını önce oku ve bağlayıcı kabul et.
2. Yalnız `editorial/fourth-report` dalında çalış. `main`, `source/`, `prompts/` ve `work/` altındaki önceki aşama çıktılarını değiştirme.
3. `work/stage-06-final-audited-content.md` tamamlanmış değilse veya iç denetim makbuzunda Aşama 7'ye geçmeye engel ciddi açık sorun belirtilmişse dur ve kullanıcıya bildir.
4. Dış kaynak veya internet kullanma.
5. Bu aşamanın tek yazılabilir çıktısı `final/fourth-report.md` dosyasıdır. Placeholder içeriğini tamamen değiştir.
6. Aşama tamamlanınca yalnız `final/fourth-report.md` dosyasını commit et. Önerilen commit mesajı: `Stage 7: assemble final author-facing fourth report`.
7. Bu aşamada DOCX, PDF veya başka format üretme.

## Esas kaynak

Nihai raporun içerik kaynağı öncelikle:

`work/stage-06-final-audited-content.md`

olacaktır.

Aşama 6 dosyasındaki **“İç Denetim Makbuzu — Aşama 7'ye Aktarılmayacak”** bölümünü nihai rapora koyma.

Bir ifade Aşama 6 içeriğinde açıkça bozuk, eksik veya güncel kitapla çelişkili görünürse yeni araştırma başlatma. Önce Aşama 6'nın ilgili kaydını ve güncel kitap nüshasını kontrol et. Güvenli biçimde çözülemeyen maddede tahmin üretme; gerekirse final raporda kaynak sınırını sade biçimde belirt.

## Ana amaç

Yazarın başka hiçbir rapora bakmadan kitabını baştan sona düzeltebileceği, sade ve doğrudan uygulanabilir bir rapor oluştur.

Her gerçek düzeltme mümkün olduğunca şu soruları cevaplasın:

1. **Kitabın neresinde?**
2. **Şu anda ne yazıyor?**
3. **Sorun ne?**
4. **Bunun yerine ne yazılmalı veya ne yapılmalı?**

Yazarın bilgisayar ve Word bilgisinin sınırlı olduğunu varsay.

## Raporun başlığı

# Kırâatlerin Rivayetinde Resm-i Mushaf’ın Etkisi
## Yazar İçin Nihai Düzeltme ve Redaksiyon Raporu

## Kısa kullanım açıklaması

Raporun başında en fazla birkaç paragrafla şunu açıkla:

- raporda yalnız hâlen düzeltilmesi veya geliştirilmesi önerilen yerlerin bulunduğunu,
- her maddede mümkün olduğunca bölüm/sayfa/paragraf başlangıcı, mevcut metin, sorun ve hazır düzeltme verildiğini,
- teknik Word/dizgi meselelerinin bilinçli olarak bu rapora alınmadığını,
- önerilerin kitabın mevcut kaynak ve ilmî çerçevesi içinde hazırlandığını.

Önceki üç raporun tarihçesini anlatma.

## Ana düzen

Raporu kitap sırasına göre oluştur:

1. `# Önsözde Yapılması Önerilen Düzeltmeler`
2. `# Girişte Yapılması Önerilen Düzeltmeler`
3. `# Birinci Bölümde Yapılması Önerilen Düzeltmeler`
4. `# İkinci Bölümde Yapılması Önerilen Düzeltmeler`
5. `# Üçüncü Bölümde Yapılması Önerilen Düzeltmeler`
6. `# Dördüncü Bölümde Yapılması Önerilen Düzeltmeler`
7. `# Sonuç Bölümünde Yapılması Önerilen Düzeltmeler`
8. `# Kitap Genelinde Tekrarlanan ve Kalıplaşmış Anlatımlar`
9. `# Kaynakça ve Açık Bibliyografik Düzeltmeler`

Boş kalan ana bölüm varsa sırf şablon gereği ekleme; o bölümde yazarın yapacağı gerçek bir işlem yoksa atlanabilir.

## Her düzeltme maddesinin biçimi

Tercih edilen biçim:

### [Sorunun açık ve doğal adı]

**Bölüm/Başlık:** ...

**Sayfa:** ...

**Bulmak için:** “...” ile başlayan paragraf

**Mevcut metin:**
> “...”

**Sorun:**
Sorunu birkaç açık cümleyle anlat.

**Önerilen düzeltme:**
> “...”

İki veya daha fazla metin parçası birlikte değişecekse gerekli bütün mevcut parçaları göster ve ardından tek birleşik öneriyi ver.

Bir paragraf tamamen çıkarılacaksa bunu açıkça söyle; yalnız “sil” demek yerine hangi paragrafın neden çıkarıldığını göster. Çıkarma sonrasında geçiş gerekiyorsa yeni geçiş metnini de ver.

## Dil ve kullanıcı deneyimi

Nihai raporda şu tür teknik dil bulunmamalıdır:

- `CAND-*`, `VERIFIED`, `CHANGE`, `KEEP`,
- Heading, TOC, PAGEREF,
- RTL, bidi, run, OOXML,
- Zotero field,
- kapatma matrisi, sınıf C/D/E,
- paragraf kimlikleri,
- render/PDF prova dili.

“Formülaik anlatım” yerine **kalıplaşmış anlatım** veya **mekanikleşen anlatım** kullan.

Sorun açıklamaları kısa, doğal ve akademik Türkçeyle yazılsın. Yazarın teknik editörlük bilgisi olduğu varsayılmasın.

## Meta bilgiler çıkarılacak

Nihai rapora şunları taşıma:

- “Birinci raporda...”, “İkinci raporda...”, “Üçüncü raporda...”
- “Aşama 1/2/3...”
- “tamamlandı/kısmen tamamlandı” durumları,
- iç denetim kodları,
- kapsam makbuzları,
- ham sayım ve takip tabloları,
- yayın kararı veya proje yönetimi açıklamaları.

Yazar yalnız mevcut kitapta neyi nasıl düzelteceğini görmelidir.

## Tablo politikası

Tablo sayısını minimumda tut. Tablo yalnız bir bakışta karşılaştırma gerçekten yararlıysa kullanılabilir. Uzun envanter veya teknik takip tabloları oluşturma.

Bir tablo korunursa, tablodaki yazarın işlem yapacağı her gerçek sorun ayrıntılı düzeltme maddesinde de açıklanmış olmalıdır. Tablo çözümün yerine geçmez.

## Bilimsel ve kaynak güvenliği

Nihai metinde:

- yeni tarih, kişi, eser, kaynak, rivâyet, kırâat vechi veya bibliyografik ayrıntı üretme;
- resm-i Osmânî'yi bağımsız kırâat kaynağı gibi sunma;
- resme uygunluk ile isnad sahihliğini karıştırma;
- yazının teorik ihtimalini sahihlik gibi gösterme;
- tarihsel rivâyeti tartışmasız olay gibi kesinleştirme;
- klasik yorum ile yazar çıkarımını birbirine karıştırma;
- kaynakların desteklemediği mana/hikmet/i‘câz iddiası ekleme.

Kaynak sınırı nedeniyle güvenli bir tam düzeltme verilemiyorsa bunu sade biçimde belirt; tahmin üretme.

## Dipnot ve alıntı güvenliği

Nihai rapor yeni dipnot üretmez. Mevcut dipnotun desteklediği iddiayı genişletme. Doğrudan alıntıları üslup amacıyla değiştirme. Önerilen metin mevcut dipnotların konumunu etkiliyorsa, yazarın anlayacağı kısa bir notla hangi mevcut dipnotun ilgili cümlede korunması gerektiğini belirt.

## Son kalite kontrolü

`final/fourth-report.md` dosyasını yazmadan önce ve yazdıktan sonra şu kontrolleri yap:

- aynı pasaj iki kez düzeltiliyor mu?
- önerilen metin gerçekten mevcut metnin yerine konabilir mi?
- “birleştir/kısalt/taşı” gibi işlemler uygulanmış mı, yoksa yazara mı bırakılmış?
- sayfa numarası güvenilir mi; değilse yanlış sayı yerine `—` kullanılmış mı?
- bölüm/başlık ve paragraf başlangıcı yeri bulmaya yeterli mi?
- teknik terim veya iç denetim kodu sızmış mı?
- Aşama 6'nın kaynak sınırı uyarıları kaybolmuş mu?
- öneriler arasında yeni çelişki oluşmuş mu?
- rapor yazarın kitabı baştan sona takip edebileceği sırada mı?

## Çıktı ve durma koşulu

`final/fourth-report.md` dosyasını tamamen oluştur, kendi içinde son kez oku ve commit et.

Son kullanıcıya yalnız:

- Aşama 7'nin tamamlandığını,
- nihai Markdown dosyasının yolunu,
- toplam somut düzeltme maddesi sayısını,
- açık kaynak sınırı maddesi varsa sayısını,
- dosyanın henüz DOCX'e dönüştürülmediğini

kısaca bildir.

**DOCX oluşturma. Dur.**