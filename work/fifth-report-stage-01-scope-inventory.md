# Fifth Report — Aşama 1
## Kapsam, bağlayıcı redaksiyon kuralları ve dil envanteri

Bu dosya Fifth Report için bağlayıcı çalışma sözleşmesi ve başlangıç envanteridir. Nihai yazar raporu değildir. Amaç, Fourth Report V2’de bilimsel/faktik ve yapısal olarak büyük ölçüde çözülen kitabın, özellikle yazarın kırmızıyla işaretlediği `değil/değildir` ailesi, gereksiz mini-sonuçlar ve kalıplaşmış akademik/AI-benzeri anlatım açısından ayrı ve eksiksiz bir son redaksiyon katmanından geçirilmesidir.

## 1. Çalışma zemini

- Çalışma dalı: `editorial/fifth-report`
- Başlangıç dalı: `editorial/author-report-v2`
- Canonical manuscript: `source/manuscript/current/redaktorden_gelen.docx`
- Searchable extraction: `source/manuscript/current/redaktorden_gelen_extracted.md`
- Zorunlu notlar: `source/notes/duzeltilecekler.docx`
- Önceki çapraz tarama: `work/stage-04-crosscutting-revisions.md`
- Fourth Report V2: `final/fourth-report-v2.md`

`source/`, `prompts/`, eski Stage çıktıları ve Fourth Report V2 bu aşamada değiştirilmez. Fifth Report yeni bir ek rapor hattıdır.

## 2. Fifth Report’un sınırı

Fifth Report yeni bilimsel tez üretmez. Yeni tarihsel/faktik araştırma yalnız bir dil düzeltmesi mevcut bilimsel anlamı değiştirme riski taşıdığında zorunlu hâle gelirse yapılır. Normal çalışma alanı şunlardır:

1. yazar/redaktör tarafından kırmızıyla işaretlenmiş bütün `değil/değildir` kullanımları;
2. `Sonuç olarak`, `Netice itibarıyla`, `Hülasa` ve benzeri gereksiz ara sonuçlar;
3. `Bu bağlamda`, `Bu çerçevede`, `göstermektedir`, `ortaya koymaktadır`, özellikle `açıkça ortaya koymaktadır` kalıpları;
4. yakın tekrar ve formülaik kullanım oluşturduğu yerlerde `Nitekim`, `Dolayısıyla`, `Böylece`, `Bu noktada`, `Bu yönüyle`, `Bununla birlikte`, `anlaşılmaktadır` ve benzeri anlatım kalıpları;
5. uzun `-maktadır/-mektedir` zincirleri ve aynı paragrafta tekrar eden soyut gönderme yapıları (`Bu durum`, `Bu yaklaşım`, `Bu süreç` vb.);
6. Fourth Report V2 ile dilsel çakışma ve rakip düzeltme kontrolü.

## 3. Bağlayıcı redaksiyon kuralları

### 3.1. `değil/değildir` ailesi

Önceki Aşama 4 taramasında güncel DOCX üzerinde kırmızı işaretlenmiş **96 ayrı paragraf** ve bu paragraflarda run düzeyinde **132 kırmızı `değil` ailesi parçası** tespit edilmiştir. Önceki karar dağılımı 8 `CHANGE`, 3 `KEEP`, 85 `ALREADY_RESOLVED_STAGE3` idi.

Fifth Report için bu eski karar dağılımı nihai karar değildir. Kullanıcının son talebi daha sıkıdır: kırmızı işaretlenmiş bütün kullanımlar yeniden ele alınacak ve yazarın doğrudan kullanabileceği daha doğal bir cümle üretilecektir.

Bağlayıcı kurallar:

- `değildir` → `olmamaktadır` gibi mekanik eş anlamlı ikamesi yapılmaz.
- `yalnız/sadece ... değil, aynı zamanda ...` kalıbı mümkün olduğunda olumlu ve doğrudan bir cümle yapısına çevrilir.
- Kitabın ana tezindeki gerekli karşıtlık bile mümkünse olumlu iki cümleyle yeniden kurulur. Örnek ilke: `Resm-i Osmânî kırâatlerin kaynağı değildir` yerine `Kırâatlerin kaynağı rivâyet geleneğidir; resm-i Osmânî ise ... tamamlayıcı ölçüdür.`
- Doğrudan alıntının lafzı sırf bu amaçla değiştirilmez. Sorun doğrudan alıntı içindeyse cümlenin dış çerçevesi yeniden kurulur veya alıntı korunarak açıklama sadeleştirilir.
- Her kırmızı kullanım Fifth Report çalışma envanterinde ayrı ayrı izlenir. Aynı paragraftaki birkaç kırmızı parça tek nihai cümle/paragrafla çözülebilir, fakat hiçbir işaretli kullanım kapsam dışı bırakılamaz.

### 3.2. `Sonuç olarak` ve ara sonuçlar

Önceki tam taramada **Sonuç bölümü dışında 14 adet `Sonuç olarak`** kullanımı tespit edilmiştir. Önceki dağılım 1 `KEEP-SYNTHESIS`, 1 `CHANGE-TRANSITION`, 12 `ALREADY_RESOLVED_STAGE3` idi. Ayrıca Sonuç bölümü dışında `Bütün bu veriler...` ile başlayan **4 ayrı kapanış paragrafı** tespit edilmiştir.

Fifth Report’ta bütün bu noktalar yeniden açılır. Varsayılan çözüm `Sonuç olarak` ifadesini başka bir bağlaçla değiştirmek değildir.

Her kullanım için şu kararlar arasından biri verilir:

- `SİL`: paragraf yalnız önceki iki-üç paragrafı tekrar özetliyorsa;
- `YEDİR`: gerçekten gerekli tek çıkarım önceki paragrafın sonuna eklenebiliyorsa;
- `GEÇİŞ`: paragraf bir sonraki alt başlığa köprüye dönüştürülebiliyorsa;
- `KORU-İÇERİK/YENİDEN-YAZ`: gerçek analitik sentez varsa içerik korunur fakat `Sonuç olarak` formülü zorunlu değildir.

Gerçek `Sonuç` bölümü, kitabın genel nihai sentez yeri olarak korunur.

### 3.3. Yüksek öncelikli kalıplar

Önceki güncel-nüsha taramasındaki sayımlar:

| Kalıp | Kullanım |
|---|---:|
| `Bu bağlamda` | 16 |
| `Bu çerçevede` | 28 |
| `göstermektedir` | 120 |
| `ortaya koymaktadır` | 42 |
| `açıkça ortaya koymaktadır` | 7 |
| `anlaşılmaktadır` | 29 |

Bu sayılar tek başına hata sayısı değildir; ancak Fifth Report’ta önceki Fourth Report yaklaşımından daha sıkı bir eşik uygulanacaktır.

- `Bu bağlamda` ve `Bu çerçevede` korunmak için gerçekten daha önce kurulmuş somut bir bağlam/çerçeveye ihtiyaç duyar. İşlevsiz kullanımlar çıkarılır.
- `göstermektedir` ve `ortaya koymaktadır` için toplu eş anlamlı değiştirme yapılmaz. Cümlenin delil işlevi yeniden kurulur.
- `açıkça ortaya koymaktadır` varsayılan olarak yüksek riskli kabul edilir. Kaynak gerçekten bu kesinlikte değilse doğrudan aktarım, sınırlı çıkarım veya daha ölçülü yüklem kullanılır.
- `göstermektedir` → `işaret etmektedir` toplu dönüşümü yasaktır; bu yalnız yeni bir kalıp üretir.
- Mümkün olduğunda soyut sonuç fiili yerine olgunun kendisi doğrudan söylenir.

### 3.4. İkinci öncelikli kalıplar

Önceki güncel-nüsha taramasındaki sayımlar:

| Kalıp | Kullanım |
|---|---:|
| `Nitekim` | 90 |
| `Dolayısıyla` | 49 |
| `Böylece` | 79 |
| `Bu noktada` | 8 |
| `Bu yönüyle` | 9 |
| `Bununla birlikte` | 32 |

Bu grupta blanket deletion uygulanmaz. Müdahale özellikle şu durumlarda zorunludur:

- aynı sayfa veya yakın paragraflarda kümelenme;
- bağlacın gerçek bir mantıksal ilişki kurmaması;
- paragraf başlangıçlarının algoritmik ritim oluşturması;
- aynı işlevin farklı bağlaçlarla art arda tekrarlanması;
- önceki cümleyi gereksiz biçimde yeniden adlandıran `Bu durum / Bu yaklaşım / Bu süreç` yapılarıyla birleşmesi.

## 4. Fourth Report V2 ile çakışma kuralı

Fifth Report, Fourth Report V2’yi geçersiz kılan bağımsız bir bilimsel rapor değildir. Fourth Report V2’deki bilimsel/faktik düzeltmeler korunur.

Aynı cümle iki raporda da müdahale gerektiriyorsa:

1. önce Fourth Report V2’deki bilimsel/faktik düzeltme esas alınır;
2. sonra Fifth Report o nihai anlamı daha doğal ve kalıpsız bir Türkçeyle yeniden kurar;
3. Fifth Report içinde Fourth Report’un eski ve Fifth Report’un yeni iki rakip metni yan yana bırakılmaz;
4. author-facing Fifth Report gerekirse `Fourth Report’taki ilgili bilimsel düzeltme korunarak cümle aşağıdaki biçimde yazılabilir` şeklinde açıklar.

Bu kural özellikle `değil/değildir`, `göstermektedir`, `ortaya koymaktadır` ve mini-sonuçların Fourth Report maddeleriyle kesiştiği yerlerde uygulanacaktır.

## 5. Fifth Report üretim hattı

### Aşama 1 — Kapsam ve envanter

Bu dosya. Amaç çalışma evrenini ve sayımları kilitlemektir.

### Aşama 2 — Bütün kırmızı `değil/değildir` kullanımlarının yeniden yazımı

- 96 paragrafın tamamı güncel DOCX ile yeniden eşleştirilecek.
- Her paragraf için exact searchable `İfade` çıkarılacak.
- Her kullanım için bitmiş alternatif cümle/paragraf üretilecek.
- Önceki `KEEP` verilen üç paragraf da kullanıcının son talebi gereği yeniden yazılacak; gerekli anlam korunacak.
- Doğrudan alıntı içeren örneklerde alıntı lafzı korunacak.

Çıktı: `work/fifth-report-stage-02-negative-rewrites.md`

### Aşama 3 — Ara sonuçlar ve yüksek öncelikli kalıplar

- Sonuç bölümü dışındaki 14 `Sonuç olarak` yeniden değerlendirilecek.
- `Bütün bu veriler...` ile başlayan dört kapanış ayrıca kontrol edilecek.
- `Bu bağlamda`, `Bu çerçevede`, `göstermektedir`, `ortaya koymaktadır`, `açıkça ortaya koymaktadır` kullanımları kitap boyunca cümle bazında taranacak.
- Aynı paragrafta birden fazla hedef kalıp varsa tek doğal yeniden yazım üretilecek; madde sayısı yapay biçimde artırılmayacak.

Çıktı: `work/fifth-report-stage-03-conclusions-and-high-priority-formulas.md`

### Aşama 4 — İkinci öncelikli kalıplar ve ritim denetimi

- `Nitekim`, `Dolayısıyla`, `Böylece`, `Bu noktada`, `Bu yönüyle`, `Bununla birlikte`, `anlaşılmaktadır` ve benzeri yapılar yakın tekrar/kümelenme bakımından kontrol edilecek.
- Uzun `-maktadır/-mektedir` zincirleri ve soyut gönderme cümleleri incelenecek.
- Her değişiklik yeni bir eş anlamlı klişe üretip üretmediği bakımından tekrar denetlenecek.

Çıktı: `work/fifth-report-stage-04-secondary-formulas-and-rhythm.md`

### Aşama 5 — Uzlaştırma ve nihai Fifth Report

- Aşama 2–4 kapsamı birbirine karşı uzlaştırılacak.
- Fourth Report V2 ile rakip/çelişkili öneri bırakılmayacak.
- Aynı cümle farklı taramalarda yakalanmışsa tek author-facing çözüm bırakılacak.
- Hiçbir kırmızı `değil/değildir` paragrafı kapsam dışında kalmayacak.
- Nihai rapor kitap sırasını izleyecek.

Final author-facing biçim:

**Yer**  
**İfade**  
**Sorun**  
**Önerilen düzeltme**

Nihai Markdown: `final/fifth-report.md`

DOCX üretimi ayrıca ve final Markdown kilitlendikten sonra yapılacaktır.

## 6. Kilitli başlangıç envanteri

| Grup | Kesin başlangıç evreni | Fifth Report yaklaşımı |
|---|---:|---|
| Kırmızı `değil/değildir` paragrafı | 96 paragraf / 132 kırmızı parça | Tamamı yeniden yazım için açılacak |
| `Sonuç olarak` (gerçek Sonuç bölümü dışında) | 14 | Tamamı yeniden değerlendirilecek; çoğunda sil/yedir/geçiş öncelikli |
| `Bütün bu veriler...` kapanışı | 4 | Mini-sonuç olarak ayrıca kontrol |
| `Bu bağlamda` | 16 | Tam tarama; işlevsizlerin büyük kısmı çıkarılacak |
| `Bu çerçevede` | 28 | Tam tarama; işlevsizlerin büyük kısmı çıkarılacak |
| `göstermektedir` | 120 | Tam tarama; doğal cümle yeniden kurulacak |
| `ortaya koymaktadır` | 42 | Tam tarama; yüksek öncelikli sadeleştirme |
| `açıkça ortaya koymaktadır` | 7 | Tam tarama; varsayılan yüksek risk |
| `anlaşılmaktadır` | 29 | Tam tarama içinde sonuç-fiili kontrolü |
| `Nitekim` | 90 | Yakın tekrar/kümelenme odaklı |
| `Dolayısıyla` | 49 | Yakın tekrar/kümelenme odaklı |
| `Böylece` | 79 | Yakın tekrar/kümelenme odaklı |
| `Bu noktada` | 8 | Yakın tekrar/kümelenme odaklı |
| `Bu yönüyle` | 9 | Yakın tekrar/kümelenme odaklı |
| `Bununla birlikte` | 32 | Yakın tekrar/kümelenme odaklı |

## 7. Sayım ve kapsam notu

Yukarıdaki sayımlar `work/stage-04-crosscutting-revisions.md` içinde güncel DOCX üzerinde yapılmış tam taramanın kayıtlarıdır. `source/` dosyaları o aşamadan bu yana değiştirilmediği için Fifth Report başlangıç evreni olarak kullanılabilir. Buna rağmen author-facing bir madde yazılmadan önce ilgili cümle canonical DOCX / searchable extraction üzerinde yeniden doğrulanacaktır.

Önceki Aşama 4’te `değil/değildir`, `Sonuç olarak`, uzun kırmızı blok ve `açıkça ortaya koymaktadır` taramalarında 116 benzersiz paragrafın Aşama 3 çözümüyle kapsandığı belirtilmişti. Fifth Report bu nedenle `ALREADY_RESOLVED_STAGE3` etiketini kapanış sebebi saymayacaktır. Kullanıcının son talebi gereği özellikle kırmızı `değil/değildir` evreni yeniden author-facing düzeltmeye dönüştürülecektir.

## 8. Aşama 1 kapanış kararı

Kapsam kilitlendi. Fifth Report için yeni bir geniş araştırma planına ihtiyaç yoktur. Sıradaki iş doğrudan üretimdir: 96 kırmızı `değil/değildir` paragrafının tamamını güncel manuscript üzerinde tek tek bulmak, Fourth Report V2 ile çakışmasını kontrol etmek ve her biri için nihai doğal Türkçe alternatif üretmek.
