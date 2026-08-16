# Fifth Report — Aşama 5 Son Kilitleme Denetimi

Bu dosya `final/fifth-report.md` için bağımsız kilitleme denetimidir. Nihai yazar raporu değildir. Amaç, Beşinci Rapor'un kullanıcının son talebini gerçekten kapatıp kapatmadığını; özellikle kırmızı `değil/değildir` evreni, mini-sonuçlar, yüksek öncelikli kalıplar, Ctrl+F kullanılabilirliği ve Fourth Report V2 ile uyum bakımından yeniden sınamaktır.

## 1. Denetim sonucu

**GENEL KARAR: NOT YET LOCKED — TWO REQUIRED HARDENINGS**

Beşinci Raporun içerik omurgası doğru ve büyük ölçüde tamamdır; ancak iki nokta kullanıcıya gönderilmeden önce düzeltilmelidir:

1. bazı `İfade` alanlarında üç nokta (`...`) kullanıldığı için bu alanlar gerçek Ctrl+F çıpası değildir;
2. yüksek öncelikli kalıplar (`Bu bağlamda`, `Bu çerçevede`, `göstermektedir`, `ortaya koymaktadır`, `anlaşılmaktadır`) çalışma aşamalarında tam taranmış olmakla birlikte final raporda her kullanım için açık bir `değiştir / koru / yapısal olarak çözüldü` hesabı görünmemektedir. Kullanıcının özellikle `Bu bağlamda / Bu çerçevede / göstermektedir / ortaya koymaktadır` grubunun neredeyse tamamının değiştirilmesi yönündeki son talebi nedeniyle bu kapsama ilişkin ayrıca kapatma defteri gereklidir.

Bu nedenle mevcut `final/fifth-report.md` içerik bakımından güçlü bir taslak finaldir; fakat henüz DOCX'e dönüştürülmemelidir.

## 2. Kırmızı `değil/değildir` kapsamı

**Başlangıç evreni:** 96 kırmızı paragraf / Word run düzeyinde 132 kırmızı parça. Searchable extraction'da 128 metinsel eşleşme.

Aşama 2, eski `KEEP` ve `ALREADY_RESOLVED_STAGE3` etiketlerini yeniden açmış; kitabın başından Sonuç bölümüne kadar `değil` ailesini yeniden taramıştır. Üç eski `KEEP` örneği de olumlu yapıya dönüştürülmüştür. 3.7–3.12 gibi Fourth Report V2 tarafından bütünüyle yeniden kurulacak alanlar mikro-cümleler yerine yapısal çözümle kapatılmış; doğrudan alıntı, hadis lafzı, âyet meali ve literal kaynak sözleri `ALINTI-KORU` sayılmıştır.

**Karar: PASS.**

Bu evrenin 96 ayrı yazar kartına dönüşmemesi kapsam eksikliği değildir; aynı paragraftaki birkaç kırmızı parça tek bitmiş paragrafla çözülebilir ve 3.7–3.12 gibi alanlarda Fourth Report V2'nin bölüm düzeyindeki yeniden yazımı bilinçli olarak tek çözüm kabul edilmiştir. Ancak nihai raporda doğrudan alıntı istisnası açık tutulmalıdır.

## 3. Mini-sonuç kapsamı

Aşama 3'te gerçek Sonuç bölümü dışında şu açık kapanış evreni yeniden açılmıştır:

- 14 `Sonuç olarak`;
- 3 `Netice itibarıyla`;
- 1 `Hülasa`;
- 4 `Bütün bu veriler...`;
- 1 `Bütün bunlar birlikte düşünüldüğünde...`.

Toplam 23 açık mini-sonuç/kapanış kümesi `SİL / YEDİR / GEÇİŞ / KORU-İÇERİK-YENİDEN-YAZ` mantığıyla karara bağlanmıştır. `Sonuç olarak` ifadesinin yalnız başka bir bağlaçla değiştirilmesi düzeltme sayılmamıştır.

Final raporda 1.4, 1.6.2, 1.7, 1.8, 1.10, 2.2.3, 2.4, 4.1, 4.2, 4.6, 4.7 ve kitap-geneli mini-sonuç kuralı yazar-facing çözüm olarak yer almaktadır.

**Karar: PASS.**

## 4. Yüksek öncelikli formül kapsamı

Aşama 1'de kilitlenen DOCX evreni:

| Kalıp | Kullanım |
|---|---:|
| `Bu bağlamda` | 16 |
| `Bu çerçevede` | 28 |
| `göstermektedir` | 120 |
| `ortaya koymaktadır` | 42 |
| `açıkça ortaya koymaktadır` | 7 |
| `anlaşılmaktadır` | 29 |

Aşama 3 bu kalıpları kitap genelinde taramış ve üç temel çözüm kullanmıştır: kaynak sahibini özne yapmak, olguyu doğrudan söylemek, gerçek çıkarım gerekiyorsa kanıt düzeyini sınırlamak. Aşama 4 de yakın tekrar kümelerini ayrıca ele almıştır.

Bununla birlikte `final/fifth-report.md`, bu evrenin tamamını tek tek author-facing kartlara veya bir occurrence-ledger'a bağlamamaktadır. Finalde belirgin kümeler için bitmiş düzeltmeler ve ayrıca kitap-geneli kurallar vardır. Bu yaklaşım sıradan bir üslup raporu için yeterli olabilirdi; ancak kullanıcının son talebi daha katıdır: özellikle `Bu bağlamda`, `Bu çerçevede`, `göstermektedir` ve `ortaya koymaktadır` kullanımlarının neredeyse tamamı bağlam içinde yeniden kurulmalıdır.

**Karar: PARTIAL — REQUIRED HARDENING.**

Kilitlenmeden önce ayrı bir iç `occurrence ledger` oluşturulmalıdır. Her kullanım aşağıdaki statülerden birine bağlanmalıdır:

- `REWRITE-IN-FIFTH`: Fifth Report'ta bitmiş yeni cümle/paragraf var;
- `RESOLVED-BY-FOURTH`: Fourth Report V2 pasajı bütünüyle değiştirdiği için eski kullanım ortadan kalkıyor;
- `REMOVE-WITH-PARAGRAPH`: mini-sonuç veya tekrar paragrafıyla birlikte siliniyor;
- `KEEP-JUSTIFIED`: gerçek mantıksal veya kaynak aktarımı işlevi bulunduğu için bilinçli olarak kalıyor;
- `QUOTE/LITERAL`: doğrudan alıntının parçası.

`KEEP-JUSTIFIED` özellikle `Bu bağlamda / Bu çerçevede / göstermektedir / ortaya koymaktadır` grubunda istisna olmalı; korunuyorsa kısa gerekçe yazılmalıdır. Bu hesap final raporda aday/ID diliyle görünmek zorunda değildir; iç denetim dosyasında bulunması yeterlidir.

## 5. İkinci öncelikli kalıp ve ritim kapsamı

Aşama 4 şu evreni taramıştır:

- `Nitekim`: 90;
- `Dolayısıyla`: 49;
- `Böylece`: 79;
- `Bu noktada`: 8;
- `Bu yönüyle`: 9;
- `Bununla birlikte`: 32;
- `Diğer bir ifadeyle`: 8;
- `Başka bir ifadeyle`: 8;
- meta-anlatım (`dikkat çekici`, `önem arz etmektedir`, `vurgulamak gerekir` vb.);
- soyut `Bu durum / Bu yaklaşım / Bu süreç` özneleri;
- yakın `-maktadır/-mektedir` zincirleri.

Kullanıcının talebi bu grupta toplu yasak değil, AI-benzeri ritmi oluşturan kümelerin temizlenmesidir. Final rapordaki 89–93 numaralı kitap-geneli kararlar ve bölüm bazlı somut örnekler bu ölçütü karşılamaktadır.

**Karar: PASS.**

## 6. Ctrl+F / literal `İfade` denetimi

Fourth Report V2 için benimsenen kullanılabilirlik standardı Fifth Report için de geçerlidir: yazar `İfade` alanını Word'de aratarak ilgili yeri doğrudan bulabilmelidir.

Final Fifth Report'ta çok sayıda `İfade` alanı gerçek current-manuscript cümlesidir. Ancak bazı kartlarda çalışma notlarından kalan üç noktalı kısaltmalar hâlâ bulunmaktadır. Örnekler:

- madde 16: `... Kusay b. Kilâb'ın...`;
- madde 19: `... cem (toplama) ifadesi ...`;
- madde 33: `... bir eksiklik veya hata değil ...`;
- madde 42: `Sonuç olarak ... sınırlı kalmamış...`;
- madde 48: `Rivâyet sadece metin aktarımı değil...`;
- maddeler 49–51: bölüm cümleleri üç noktayla kısaltılmıştır;
- madde 53: `... yedi harfin tamamı üzerine değil...`;
- madde 54: `Netice itibarıyla ... değil...`;
- maddeler 55–59: bazı `İfade` alanları cümle sonunu üç noktayla kesmektedir;
- madde 62: Ferrâ paragrafı üç noktalı parçayla verilmiştir;
- madde 64: 3.7–3.12 için üç noktalı örnek çıpa kullanılmıştır;
- Dördüncü Bölüm ve Sonuç'ta da birkaç benzer kısaltılmış `İfade` vardır.

Bu üç noktalar kullanıcıya 'yer bulma' kolaylığı sağlamaz; ayrıca raporun başındaki `İfade alanları mevcut nüshada aranabilir metinlerdir` vaadiyle çelişir.

**Karar: FAIL — REQUIRED HARDENING.**

Kilitlenmeden önce her üç noktalı `İfade` alanı current searchable extraction'daki gerçek, kesintisiz bir cümle veya yeterince ayırt edici literal cümle parçasıyla değiştirilmelidir. Gerekirse tüm uzun cümle yerine ilk tam cümle kullanılabilir; önemli olan üç noktasız ve Ctrl+F ile bulunabilir olmasıdır.

## 7. Önerilen düzeltmelerde hedef kalıpların yeniden üretilmesi

Final metinde büyük ölçüde başarılı bir kalıp temizliği vardır. Bununla birlikte birkaç önerilen düzeltme yeniden `göstermektedir`, `işaret etmektedir`, `belirtmektedir`, `teyit etmektedir` gibi rapor yüklemlerine dönmektedir. Bunların hepsi yanlış değildir; ancak kullanıcının özellikle `göstermektedir / ortaya koymaktadır` ailesini agresif biçimde azaltma talebi nedeniyle kilitleme öncesinde bir son tarama yapılmalıdır.

Özellikle şu ilke uygulanmalıdır:

- `... ilişkilendirildiğini göstermektedir` → mümkünse `... ilişkilendirilmiştir`;
- `Bu rivâyetler ... göstermektedir` → doğrudan olgu veya kaynak öznesi;
- `... işaret etmektedir` yalnız gerçekten sınırlı kanıt ilişkisi gerekiyorsa;
- yeni metinde bir hedef kalıbın çıkarılması, başka hedef kalıbın otomatik olarak eklenmesiyle sonuçlanmamalıdır.

**Karar: MINOR HARDENING.**

## 8. Fourth Report V2 ile çakışma denetimi

Fifth Report, Dördüncü Rapor'un bilimsel/faktik çerçevesini açıkça üst norm olarak tanımlamaktadır. Aşama 2–4'te özellikle şu alanlarda Fourth Report V2 esas alınmıştır:

- yedi harf ve arza-i âhire;
- resmin kırâatleri üretmediği ilkesi;
- hazf/ziyâde ve teleolojik amaç atfı;
- tevkîfîlik ile normatif bağlılığın ayrılması;
- sahâbe mushafları;
- resmin seçen/ayıklayan/kurucu fail gibi kullanılmaması;
- matbu mushafların yaygınlaşma etkisinin tek neden gibi sunulmaması;
- 3.7–3.12'nin mikro düzeltmeler yerine bölüm düzeyinde yeniden kurulması.

Final raporda bu konularda Fourth Report V2'yi açıkça zayıflatan veya eski daha iddialı metni yeniden canlandıran bir öneri tespit edilmemiştir.

**Karar: PASS.**

## 9. Yapılacak son işlem

Fifth Report'u kilitlemek için yeni bilimsel araştırma veya yeni geniş editoryal tarama gerekmemektedir. Yalnız iki kapatma işlemi yapılacaktır:

1. **Ctrl+F hardening:** final rapordaki bütün üç noktalı / kısaltılmış `İfade` alanlarını exact current-manuscript çıpasıyla değiştirmek ve önerilen metinlerde yeniden oluşan yüksek öncelikli sonuç fiillerini mümkün olduğunca doğrudanlaştırmak.
2. **High-priority occurrence ledger:** `Bu bağlamda`, `Bu çerçevede`, `göstermektedir`, `ortaya koymaktadır`, `açıkça ortaya koymaktadır`, `anlaşılmaktadır` evrenindeki her kullanımı `REWRITE / RESOLVED-BY-FOURTH / REMOVE / KEEP-JUSTIFIED / QUOTE` statüsüne bağlamak. Final yazar raporuna yalnız gerçekten yazarın uygulaması gereken ek maddeler taşınacak; iç ledger final raporda görünmeyecektir.

Bu iki işlem tamamlandıktan sonra `final/fifth-report.md` yeniden denetlenecek ve ancak bundan sonra DOCX'e dönüştürülecektir.
