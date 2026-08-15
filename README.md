# Kırâatlerin Rivayetinde Resm-i Mushaf’ın Etkisi — Dördüncü Rapor Çalışma Deposu

Bu depo, **Kırâatlerin Rivayetinde Resm-i Mushaf’ın Etkisi** adlı kitap için hazırlanacak yazar odaklı **Dördüncü Akademik Redaksiyon ve Düzeltme Raporu**nun kontrollü üretim sürecini izlemek için oluşturulmuştur.

## Temel amaç

Nihai rapor, teknik editörlük jargonu veya geçmiş raporların tarihçesini değil, yazarın doğrudan uygulayabileceği düzeltmeleri içerecektir. Her somut maddede mümkün olduğunca şu zincir tamamlanacaktır:

**Bölüm/Başlık → Sayfa → Bulmak için paragraf başlangıcı → Mevcut metin → Sorun → Önerilen düzeltme**

Yazarın bilgisayar ve Word kullanım bilgisinin sınırlı olabileceği kabul edilir. Bu nedenle nihai rapor, “birleştir/kısalt/taşı” gibi soyut editör talimatları yerine mümkün olduğunca işlemi uygulanmış hazır metin sunacaktır.

## Kaynak önceliği

1. `source/manuscript/current/redaktorden_gelen.docx` — güncel ve bağlayıcı kitap nüshası.
2. `source/manuscript/current/redaktorden_gelen_extracted.md` — arama ve metin karşılaştırması için aynı nüshanın metin çıkarımı.
3. `source/notes/duzeltilecekler.docx` — redaktör/yazar düzeltme notları.
4. `source/reports/` — daha önce hazırlanmış üç rapor ve birleşik rapor.
5. `source/manuscript/archive/` — yalnız karşılaştırma gerektiğinde kullanılacak eski nüsha.

`combined-report.docx`, ilk üç raporun birleşik sürümüdür; bağımsız dördüncü bulgu kaynağı gibi sayılmamalıdır.

## Yedi aşamalı iş akışı

Promptlar `prompts/` klasöründedir ve sırayla uygulanmalıdır. Bir aşama tamamlanmadan sonraki aşama çalıştırılmamalıdır.

- **Stage 1:** rapor bulgularını süzme ve tekilleştirilmiş aday sorun envanteri
- **Stage 2:** aday sorunları güncel kitapta doğrulama ve kesin konumlandırma
- **Stage 3:** doğrulanmış yerel/bilimsel/dilsel sorunlar için doğrudan kullanılabilir düzeltme metinleri
- **Stage 4:** kitap genelindeki `değil/değildir`, `Sonuç olarak`, tekrar, kalıplaşmış anlatım ve geçiş sorunlarının sistematik çözümü
- **Stage 5:** bütün çözümlerin tekilleştirilmesi ve yazar-odaklı tam içerik adayının oluşturulması
- **Stage 6:** içerik adayının bağımsız son denetimi, kapsam uzlaştırması ve düzeltilmiş son içerik paketinin hazırlanması
- **Stage 7:** denetimden geçmiş içerikten nihai yazar-facing Dördüncü Raporun Markdown olarak oluşturulması

**Word/DOCX üretimi bu yedi aşamanın dışında tutulur.** `final/fourth-report.md` kullanıcı tarafından onaylandıktan sonra aynı içerikten ayrıca DOCX üretilecektir.

## Aşama çıktıları

- Stage 1 → `work/stage-01-final-inventory.md`
- Stage 2 → `work/stage-02-verified-inventory.md`
- Stage 3 → `work/stage-03-direct-revisions.md`
- Stage 4 → `work/stage-04-crosscutting-revisions.md`
- Stage 5 → `work/stage-05-final-content.md`
- Stage 6 → `work/stage-06-final-audited-content.md`
- Stage 7 → `final/fourth-report.md`

Aşama 1-6 dosyaları iç çalışma ve izlenebilirlik içindir. Yazarın göreceği nihai Markdown yalnız `final/fourth-report.md` dosyasıdır.

## Önemli sınırlar

- Dış kaynak kullanılmaz; kullanıcı açıkça izin vermedikçe yalnız proje dosyaları esas alınır.
- Kaynaklarda bulunmayan tarih, kişi, eser, rivâyet, kırâat vechi veya bibliyografik ayrıntı üretilmez.
- Güncel kitap nüshası doğrudan değiştirilmez; bu depo rapor üretimi içindir.
- `source/` altındaki kanıt dosyaları değiştirilemez.
- Aynı pasaj üç eski raporda birkaç kez ele alınmışsa nihai raporda mümkün olduğunca tek düzeltme maddesine indirgenir.
- Teknik Word/dizgi sorunları yazar-facing rapora alınmaz; gerektiğinde önceki teknik raporlarda tutulur.
- Nihai Markdown onaylandıktan sonra üretilecek Word dosyasının içeriği bu Markdown ile aynı olmalıdır; Word aşaması yeni akademik revizyon turu değildir.

## Dal kullanımı

- `main` — kabul edilmiş bootstrap ve kaynak tabanı
- `editorial/fourth-report` — prompt geliştirmeleri, aşama çıktıları ve nihai Markdown rapor

Her aşama ayrı commit ile kaydedilmelidir. Kaynak dosyalar değiştirilmemelidir.
