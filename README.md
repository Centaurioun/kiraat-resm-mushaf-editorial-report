# Kırâatlerin Rivayetinde Resm-i Mushaf’ın Etkisi — Dördüncü Rapor Çalışma Deposu

Bu depo, **Kırâatlerin Rivayetinde Resm-i Mushaf’ın Etkisi** adlı kitap için hazırlanacak yazar odaklı **Dördüncü Akademik Redaksiyon ve Düzeltme Raporu**nun altı aşamalı üretim sürecini izlemek için oluşturulmuştur.

## Temel amaç

Nihai rapor, teknik editörlük jargonu veya geçmiş raporların tarihçesini değil, yazarın doğrudan uygulayabileceği düzeltmeleri içerecektir. Her somut maddede mümkün olduğunca şu zincir tamamlanacaktır:

**Bölüm/Başlık → Sayfa → Bulmak için paragraf başlangıcı → Mevcut metin → Sorun → Önerilen düzeltme**

## Kaynak önceliği

1. `source/manuscript/current/redaktorden_gelen.docx` — güncel ve bağlayıcı kitap nüshası.
2. `source/manuscript/current/redaktorden_gelen_extracted.md` — arama ve metin karşılaştırması için aynı nüshanın metin çıkarımı.
3. `source/notes/duzeltilecekler.docx` — redaktör/yazar düzeltme notları.
4. `source/reports/` — daha önce hazırlanmış üç rapor ve birleşik rapor.
5. `source/manuscript/archive/` — yalnız karşılaştırma gerektiğinde kullanılacak eski nüsha.

## Altı aşama

Promptlar `prompts/` klasöründedir ve sırayla uygulanmalıdır. Bir aşama tamamlanmadan sonraki aşama çalıştırılmamalıdır.

- Stage 1: üç raporun süzülmesi ve tekilleştirilmiş sorun envanteri
- Stage 2: sorunların güncel kitapta doğrulanması
- Stage 3: kitap sırasına göre doğrudan düzeltme metinleri
- Stage 4: kitap geneline yayılan anlatım ve geçiş sorunları
- Stage 5: tekilleştirme, bilimsel güvenlik ve kullanılabilirlik kontrolü
- Stage 6: nihai yazar raporunun oluşturulması

## Çalışma dosyaları

Aşama çıktıları `work/` altında tutulur. Bunlar GitHub sürüm geçmişinin ana izleme yüzeyidir. Nihai içerik `final/` altında toplanır.

## Önemli sınırlar

- Dış kaynak kullanılmaz; kullanıcı açıkça izin vermedikçe yalnız proje dosyaları esas alınır.
- Kaynaklarda bulunmayan tarih, kişi, eser, rivâyet, kırâat vechi veya bibliyografik ayrıntı üretilmez.
- Güncel kitap nüshası doğrudan değiştirilmez; bu depo rapor üretimi içindir.
- Nihai Word dosyası, onaylanmış son Markdown içeriğinden üretilecektir.
