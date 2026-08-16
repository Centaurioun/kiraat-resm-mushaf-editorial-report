# V2 Ana Çalışma Envanteri

## Amaç ve sınır

Bu dosya, yazara gönderilecek yeni nihai raporun kendisi değildir. Önceki editoryal çalışmaları kaybetmeden, hangi bulgunun hangi sonraki işlem hattına gireceğini belirleyen ana yönlendirme envanteridir.

Bu V2 çalışma hattında eski `work/stage-01`–`stage-06` dosyaları ve `final/fourth-report.md` değiştirilmez. Bunlar provenance ve çözüm rezervuarı olarak korunur. Nihai V2 rapor daha sonra ayrı bir dosyada oluşturulacaktır.

Bağlayıcı güncel metin `source/manuscript/current/redaktorden_gelen.docx` dosyasıdır. `redaktorden_gelen_extracted.md` yalnız arama yardımcısıdır. Güncel metinle önceki rapor, Stage dosyası veya Google AI metni arasında uyuşmazlık olduğunda güncel DOCX esas alınacaktır.

## V2 için kaynak haritası

1. **Bağlayıcı güncel manuscript**
   - `source/manuscript/current/redaktorden_gelen.docx`
   - `source/manuscript/current/redaktorden_gelen_extracted.md`

2. **Zorunlu editoryal notlar**
   - `source/notes/duzeltilecekler.docx`

3. **Önceki kapsamlı çalışma**
   - `work/stage-01-final-inventory.md`
   - `work/stage-02-verified-inventory.md`
   - `work/stage-03-direct-revisions.md`
   - `work/stage-04-crosscutting-revisions.md`
   - `work/stage-05-final-content.md`
   - `work/stage-06-final-audited-content.md`

4. **Önceki raporlar**
   - `source/reports/` içindeki raporlar ve birleşik rapor
   - konuşmaya eklenen `kiraatlerin_rivayetinde_resm-i_mushaf_sorunlar.docx`; özellikle `Yer → İfade → Sorun → Önerilen düzeltme` kullanıcı deneyimi bakımından biçim modeli

5. **Google AI karşılaştırma havuzu**
   - `source/manuscript/google-ai/` altındaki bölüm bazlı DOCX/Markdown dosyaları
   - Bu metinler doğrudan yazara verilecek revizyon metni değildir. Yalnız bilgi, tarih, kaynak, yapı ve zenginleştirme adayı üretir.

## Önceki çalışma hakkında bağlayıcı sayısal durum

Stage 2, 183 aday kaydı güncel manuscriptle uzlaştırmış; 178 kaydı `VERIFIED`, 4 kaydı `MERGED`, 1 kaydı `RESOLVED` olarak kapatmıştır. Bu nedenle V2 çalışmasının temel aday evreni 178 doğrulanmış sorundur. V2 bu sorunları sıfırdan yeniden icat etmeyecek, fakat nihai rapora girmeden önce güncel metin üzerinde yeniden kontrol edecektir.

Stage 6 kendi iç denetiminde 178 sorunun 75 somut yazar maddesinde temsil edildiğini ve ayrıca 1 bibliyografik kaynak sınırı kaldığını bildirmiştir. Bu kapsama uzlaştırması yararlıdır; ancak V2 için tek başına yeterli kabul edilmez. Özellikle faktik doğruluk ve “İfade” alanının güncel manuscriptten birebir alınması ayrıca denetlenecektir.

## V2 yönlendirme etiketleri

Aynı aday birden fazla etikete sahip olabilir. Etiketler nihai yazara gösterilmeyecek, yalnız çalışma içindir.

- **EXACT**: Güncel manuscriptten birebir aranabilir `İfade` çıkarılmalıdır. Stage 6’daki özet/parafraz `Mevcut metin` final için yeterli değildir.
- **FACT**: Kişi, tarih, eser, kronoloji, tarihsel mekanizma veya ağır bilimsel iddia bağımsız olarak doğrulanmalıdır.
- **SOURCE**: Mevcut dipnotun gerçekten önerilen cümleyi destekleyip desteklemediği kontrol edilmelidir.
- **GOOGLE-LEAD**: Google AI dosyasında yararlı olabilecek yeni bilgi, tarih, kaynak veya yapı önerisi vardır; hiçbir unsur doğrulanmadan kabul edilmeyecektir.
- **STYLE**: Akış, tekrar, mekanikleşen anlatım, `değil/değildir`, `Sonuç olarak`, bağlaç/yüklem tekrarı veya paragraf mimarisi sorunudur.
- **STRUCTURE**: Paragraf/bölüm birleştirme, taşıma, alt başlık mimarisi veya bölüm sınırı sorunudur.
- **BIB**: Dipnot, kaynakça, baskı, DOI, artikel, sûre adı veya ilk tam/sonraki kısa atıf sorunudur.
- **RECHECK-RESOLVED**: Önceki aşamada çözüldüğü söylenen, fakat kaynak manuscript değiştirilmediği için V2’de güncel DOCX üzerinde yeniden doğrulanması gereken maddedir.
- **NO-AUTHOR-ACTION**: Teknik Word/OOXML/dizgi meselesi veya gerçekten çözülmüş/kullanılması gerekmeyen kayıt. Nihai rapora alınmayacaktır.

# 1. Kapsam açısından korunacak ana sorun kümeleri

## 1.1 Önsöz ve Giriş

**Adaylar:** CAND-001–CAND-010, CAND-012.

**Ana sorunlar:** Önsöz ile Girişte ana tezin tekrarı, Girişte amaç-kapsam-yöntem-plan yoğunluğu, tarihsel niyetin aşırı kesinliği, telakki-müşâfehe-edâ-isnad-rivâyet dengesinin tam kurulamaması, son geçişin ikinci bir sonuç paragrafına dönüşmesi.

**V2 yönlendirmesi:** `EXACT + STYLE + STRUCTURE`; CAND-009 ayrıca `FACT + SOURCE`.

**Önemli kullanım kararı:** Stage 6 bu bölümlerde çoğu kez `Mevcut metin` alanında birebir alıntı yerine editoryal özet kullanmaktadır. V2 final raporunda bu kabul edilmeyecek. Her maddeye güncel manuscriptten Ctrl+F ile bulunabilecek gerçek başlangıç cümlesi veya gerekli tam pasaj konacaktır.

## 1.2 Birinci Bölüm: erken yazı, cem, istinsah ve mushaf sayısı

**Adaylar:** CAND-013–CAND-067.

Bu küme V2’nin en yüksek faktik doğrulama gerektiren alanlarından biridir.

### Doğrudan FACT/SOURCE önceliği taşıyanlar

- CAND-013: İslâm öncesi yazı verilerinin kanıt düzeyleri.
- CAND-016: Varaka b. Nevfel çevresindeki tarih/çalışma notu; güncel metinde hâlen bulunup bulunmadığı ayrıca doğrulanacak.
- CAND-020: vahiy metinlerinin muhafazasına ilişkin iki modelin tarihsel kesinlik düzeyi.
- CAND-022: Hârice kimliği.
- CAND-024: Ebû Bekir suhufu ile yedi harf ilişkisi.
- CAND-025: Mervân b. Hakem’in niyetinin sonradan kurulan açıklamayla özdeşleştirilmesi.
- CAND-028: Taberî ölüm tarihi/tekrar notu.
- CAND-029: `التابوت` örneğinde lehçe, telaffuz ve imlâ ayrımı.
- CAND-032, CAND-033: İbn Ebû Dâvud ve Suyûtî ölüm tarihi tekrar notları.
- CAND-034: mushaf sayısının 1.5 ve 4.1 arasında çelişkili sunumu.
- CAND-035: Yemen/Bahreyn/Mısır/el-Cezîre cümlesinin bağlamın tersini söylemesi.
- CAND-036: çağdaş araştırmacılara ortak “altı mushaf” kanaati yüklenmesi.
- CAND-037: Amr b. Kays ölüm tarihi.
- CAND-038: Muhammed Hamîdullah’ın bozuk ölüm tarihi.
- CAND-040: Kastallânî tekrar/tarih notu.
- CAND-043: Bâkıllânî’nin bozuk tarih kaydı.
- CAND-044: Ca‘berî ölüm tarihi. Stage 2 güncel metinde `832/1428` biçimini kaydetmiştir; Google AI dosyası bunu `732/1332` olarak düzeltme iddiasındadır. Bu madde V2’de mutlaka bağımsız doğrulanacaktır ve mevcut Stage 3/6 metni otomatik kullanılmayacaktır.
- CAND-046: Zerkeşî–İbnü’l-Cezerî kronoloji ilişkisi.
- CAND-050: arza-i âhire ile Osmânî istinsah arasında fazla kesin mekanizma kurulması.
- CAND-053: Ebû Şâme için `665/1276` ve `665/1267` çelişkisi.
- CAND-056: sözlük anlamından tarihsel terimleşme teorisi çıkarılması.
- CAND-060: Muâviye’ye nispet edilen yazı talimatı rivâyetinin kanıt değeri.
- CAND-064: hazfin “bilinçli/hikmetli tercih” olarak tanımlanması.
- CAND-067: Motzki, Sinai ve Déroche gibi çağdaş araştırmacıların görüşlerinin kitabın tezine olduğundan güçlü bağlanması.

### Ana STRUCTURE/STYLE önceliği taşıyanlar

CAND-015, 017, 019, 026, 027, 031, 039, 041, 042, 045, 047, 048, 051, 052, 054, 055, 057, 058, 059, 061, 062, 065 ve 066.

Bu adaylarda önceki Stage 3 çözümleri önemli bir rezervuardır; ancak final V2 maddesi gerçek `İfade` alıntısı kullanılarak yeniden kurulacaktır.

## 1.3 İkinci Bölüm: kırâatlerin rivâyet mantığı

**Adaylar:** CAND-068–CAND-082 ve CAND-113 ile ilişkili çapraz terminoloji.

**Temel karar:** Önceki analizde bu bölüm kitabın teorik omurgasına göre yetersiz bulunmuştur. Ancak V2’de “bölümü büyütmek” başlı başına hedef değildir. Yalnız gerçekten eksik kalan kavram ayrımları, manuscriptteki mevcut akışı bozmadan ve kaynakla doğrulanarak eklenmelidir.

**Özellikle korunacak ayrımlar:**

- kırâat / rivâyet / tarîk / vecih;
- telakki / müşâfehe / edâ;
- imamın okuyuşun kurucusu değil nispet ve aktarım merkezi olması;
- sözlü aktarımın aslîliği ile yazılı kaydın tamamlayıcı rolünün birlikte korunması;
- resme uygunluğun rivâyetin yerine geçmemesi.

**V2 yönlendirmesi:** CAND-068, 069, 070, 073, 076, 079 ve 082 `EXACT + FACT/SOURCE`; diğerleri ağırlıkla `EXACT + STYLE/STRUCTURE`.

Google AI’nın 2.1–2.3 dosyaları bu bölüm için `GOOGLE-LEAD` olarak değerlendirilecektir. Özellikle yeni terminoloji ve ölüm tarihleri otomatik kabul edilmeyecek; Google metninin `epistemolojik havza`, `kanonizasyon`, `konsonantal plastiklik` gibi yazarın üslubuna yabancı dili final metne taşınmayacaktır.

## 1.4 Üçüncü Bölüm: en yüksek bilimsel redaksiyon riski

**Adaylar:** CAND-083–CAND-116.

Bu küme, tarihsel veri ile klasik hikmet/i‘câz yorumu arasındaki sınır bakımından V2’nin en kritik bilimsel alanıdır.

### FACT/SOURCE zorunlu adaylar

- CAND-083: çoklu kırâatle bağdaşmanın istinsah heyetinin bilinçli tasarım amacı gibi sunulması.
- CAND-084: resmin bilinçli ses/hareke işaretleme sistemi gibi anlatılması.
- CAND-085: ziyâde ve hazfin “ince manaya delaleti” başlığının sonucu peşinen kabul etmesi.
- CAND-086: yazım farkının anlam farkını zorunlu işaret ettiği varsayımı.
- CAND-087: İbn Haldûn’a verilen savunmacı cevabın kanıt dili.
- CAND-093: İsrail/Afrika’da tahrif edilmiş mushaf anlatısı; ağır dış doğrulama gerektirir.
- CAND-098: şâzlık ile resme aykırılığın tek nedensellik çizgisinde sunulması.
- CAND-100: yedi harf ile lehçenin eşitlenmesi riski.
- CAND-103: resmin “anlam işaretleme sistemi” hâline getirilmesi ve hikmet/i‘câz yorumlarının tarihsel veriyle eşitlenmesi.
- CAND-112: tam fonetik yazı olsaydı müşâfehenin zayıflayacağı karşı olgusu.
- CAND-114: İsrail anlatısında niyet/kasıt atfı.
- CAND-115: modern imlâya geçişte kırâat vecihlerinin “zayi olacağı” şeklindeki aşırı nedensellik.

### STRUCTURE/STYLE ağırlıklı adaylar

CAND-088–CAND-092, CAND-094–CAND-097, CAND-099, CAND-101, CAND-102, CAND-104–CAND-111 ve CAND-116.

**Özel yapısal konu:** CAND-109 ve ilişkili adaylarda 3.7–3.12 başlıklarının aynı “resme bağlılığın gerekçeleri” işlevini tekrar ettiği tespit edilmiştir. Stage 6’daki birleştirme önerisi doğrudan kopyalanmayacak; önce her başlığın güncel manuscriptte vazgeçilmez özgün malzeme taşıyıp taşımadığı kontrol edilecektir.

## 1.5 Dördüncü Bölüm: uygulama, sahâbe mushafları, şâz kırâat ve matbu mushaflar

**Adaylar:** CAND-117–CAND-156.

### FACT/SOURCE zorunlu adaylar

- CAND-117 ve CAND-137: resmin kurucu/seçici aktör gibi sunulması.
- CAND-119: sahâbe mushafı farklılıklarının tefsirî kayıt/neshedilmiş okuyuş gibi tek kategoriye yaklaştırılması.
- CAND-120: İbn Şenbûz olayının “resme aykırılık = şâzlık/ceza” biçiminde sadeleştirilmesi.
- CAND-124: vakıf türlerinin birbirine karışması.
- CAND-125: İbn Mu‘âz el-Cühenî’nin bozuk ölüm tarihi.
- CAND-126: resm rivâyetlerinin “kurucu zemin” şeklinde sunulması.
- CAND-128: Hâlid b. Ebü’l-Heyyâc kimlik belirsizliği.
- CAND-130: Hinkelmann/Marracci/Mevlây Osman ve sonraki baskı kronolojisi.
- CAND-131: “ilk resmî Osmanlı mushafı” ve 1873/1874 kesinliği.
- CAND-132: `Mevlây Osman (?)` kimliği.
- CAND-133: basılı mushafların belirli rivâyetleri yaygınlaştırmasını tek yönlü neden-sonuçla açıklama.
- CAND-138: İbn Mes‘ûd’un tavrını psikolojik niyetle kesinleştirme.
- CAND-141: şâz kavramının tek etikete indirgenmesi.
- CAND-144: kırâat imamlarının kurucu seçiciler gibi anlaşılması.
- CAND-146 ve CAND-148: “her yazımın hikmeti vardır” ve “son derece bilinçli ve işlevsel” türü geniş sonuçlar.
- CAND-150: nokta/hareke yokluğunu farklı kırâat vecihlerini koruma amacıyla açıklama.

### Biyografik/not temizliği, ancak önce doğrulama gerekenler

CAND-118, CAND-122, CAND-123, CAND-125, CAND-127, CAND-128, CAND-129, CAND-132 ve CAND-160 ile ilişkili somut kayıtlar.

V2 ilkesi: doğru bilgi bulunabiliyorsa yalnız silmek yerine düzeltmek; kişi/tarih daha önce doğru biçimde verilmişse sonraki tekrarda tarihi kaldırmak; doğrulanamıyorsa yeni bilgi uydurmamak.

### STRUCTURE/STYLE ağırlıklı adaylar

CAND-135, 136, 139, 140, 142, 143, 145, 147, 149, 151–156 ve bu bölümü Birinci Bölüm tarih tekrarından ayıran CAND-051.

## 1.6 Sonuç

**Adaylar:** CAND-157–CAND-159.

- CAND-157 `FACT + SOURCE`: matbu mushafların rivâyet standardizasyonundaki etkisi tek yönlü ve fazla kesin kuruluyor.
- CAND-158 `EXACT + STYLE`: resmin uygunluk ölçüsü ve kabul şartları birbirine yakın paragraflarda tekrar ediliyor.
- CAND-159 `EXACT + STRUCTURE`: nihai sonuç ile ileri araştırma önerisi aynı paragrafta toplanıyor.

## 1.7 Kitap geneli anlatım ve ev stili

**Adaylar:** CAND-161–CAND-167, CAND-169, CAND-170 ve CAND-171.

Stage 4’ün tam taramaları değerli iç kanıt olarak korunacaktır. Ancak nihai V2 rapor “bütün `değil`leri değiştirin” veya “bütün `göstermektedir`leri değiştirin” türü mekanik talimat vermeyecektir.

Önceki sayımlar:

- redaktör işaretli `değil/değildir` ailesi: 96 paragraf;
- Sonuç bölümü dışındaki `Sonuç olarak`: 14 kullanım;
- `göstermektedir`: 120;
- `ortaya koymaktadır`: 42;
- `anlaşılmaktadır`: 29;
- `açıkça ortaya koymaktadır`: 7.

Bu sayılar yalnız tarama kapsamı kanıtıdır; “hata sayısı” değildir. V2 final rapora yalnız gerçek bağlam sorunu bulunan kullanımlar girecektir.

CAND-169 ve CAND-170 için kitap genelindeki `İmam Mushaf` ve `Kur’an` yazımı finalden önce tekrar taranacaktır. CAND-171’de gerçek/ihtimalî resme uygunluk ayrımının örneklerde gerçekten görünür olup olmadığı kaynakla birlikte yeniden kontrol edilecektir.

## 1.8 Dipnot ve kaynakça

**Adaylar:** CAND-172–CAND-178, CAND-180, CAND-181; CAND-179/182/183 daha önce bunlarla birleştirilmiştir.

- CAND-172–174: dipnotlarda kalmış çalışma notları. `EXACT + BIB`.
- CAND-175: ilk tam, sonraki kısa atıf düzeni. `BIB`.
- CAND-176: aynı dipnotta farklı kaynakları ayırma biçimi. `BIB`.
- CAND-177: müellif adlarındaki artikel/ev stili. `BIB`.
- CAND-178: sûre adlarında artikel kullanımı. `BIB`.
- CAND-180: aynı eserin farklı baskılarının fiilî kullanımına göre ayrıştırılması. `BIB + SOURCE`.
- CAND-181: iki bozuk DOI. `BIB + FACT`.

Stage 6’da CAND-180’in bir bölümü ilk tam dipnotlarla çözülmüş; Ebû Şâme’nin 1975/1993 baskıları arasında tek kaynak sınırı bırakılmıştır. V2 bu sonucu da kaynakça ve ilk tam dipnotlarla yeniden kontrol edecektir.

# 2. Google AI dosyalarının V2’deki kullanım biçimi

Google AI metinlerinin tamamı `GOOGLE-LEAD` statüsündedir. Doğrudan “önerilen düzeltme” olarak kullanılmayacaktır.

## 2.1 Bölüm bazlı fırsatlar

### 01.1–01.2

Olası yarar: kişi tarihleri, İslâm öncesi yazı örnekleri, erken vahiy-yazı ilişkisine ek kaynak adayları.

Risk: metin güçlü ve kesin tarihsel ifadeler üretmekte; “kesin olarak doğrulamaktadır”, “vahim/radikal dönüşüm”, “kutsalın muhafızı” gibi yazarın mevcut akademik sesinden uzak söylem kullanmaktadır. Bu nedenle yalnız bilgi ve kaynak ipucu alınabilir.

### 01.3 A/B

Olası yarar: Mervân b. Hakem, Hârice, cem, iki şahit, suhufun akıbeti gibi faktik düğümlere araştırma ipucu.

Risk: “resmî devlet komisyonu”, “filolojik denetim”, “ana nüsha”, “resmî arşiv” gibi modern kurumsal kavramlarla erken süreci fazla sistematik yeniden inşa etme eğilimi.

### 01.4

Olası yarar: Taberî ve sahâbe tarihleri, istinsah gerekçeleri, çalışma notlarının temizliği.

Risk: kıraat ihtilaflarını dramatik siyasi kriz ve devlet refleksi diliyle aşırı nedenselleştirme.

### 01.5

Olası yarar: mushaf sayısı ve merkezler konusundaki farklı rivâyetleri karşılaştırmak için kaynak adayları.

Risk: Google metni sonunda belirli bir “5 şehir + 1 şahsî = 6” sentezini gereğinden kesin kurmakta ve bazı araştırmacılara/klasik kaynaklara stemmatolojik sonuçlar yükleyebilmektedir. Bu bölüm yalnız hedefli kaynak doğrulamasına başlangıç noktası olacaktır.

### 01.6

Olası yarar: Cevherî gibi biyografik kayıtlar ve resm teriminin sözlük/ıstılah ayrımı için kaynak ipuçları.

Risk: sözlük anlamından “ontolojik”, “dogmatik”, “kanonik” tarih teorisi üretme eğilimi. CAND-056 bakımından özellikle dikkatli kullanılacaktır.

### 01.7

Olası yarar: Ebû Ubeyde, Dânî, Ebû Dâvud gibi isimlerin resm literatüründeki yerini karşılaştırmak için kaynak adayları.

Risk: “kurucu safha”, “sarsılmaz”, “dogmatik prensip”, “teorik temel” gibi kaynakların açıkça söylemeyebileceği güçlü tarih anlatısı.

### 01.8

Olası yarar: tevkîfîlik/ictihâdîlik tartışmasında kaynak, kişi ve tarih adayları; Ebû Şâme tarihinin yeniden kontrolü.

Risk: delil hiyerarşisini çok kesin ve polemikçi kurabilen dil; bazı hadis değerlendirmeleri bağımsız doğrulanmadan alınmayacaktır.

### 01.9

Olası yarar: özellikle Ca‘berî tarihindeki düzeltme iddiası ve resm kuralları için yeni kaynak adayları.

Risk: “archetypus”, “ortografik kanon”, “grafik plastiklik”, “bilinçli düşürme”, “stratejik kural” gibi hem yazar üslubuna yabancı hem de tarihsel niyet yükleyen söylem. Bu metin faktik ipucu dışında doğrudan kullanılamaz.

### 02.1–02.3

Olası yarar: kırâat/rivâyet/sened/otorite/yedi harf alanında yeni kaynak ve terminoloji adayları.

Risk: “epistemolojik havza”, “anayasal usul”, “kanonize edilmiş”, “konsonantal plastiklik”, “mutlak filtre” gibi aşırı teorik ve homojen AI dili. Ayrıca okuyuşların kanonlaşması ve yedi harf ilişkisi konusunda kaynakların taşıdığından güçlü sonuçlar üretme riski yüksektir.

## 2.2 Google AI kabul testi

Bir Google AI unsuru ancak aşağıdaki dört koşulun tamamını geçerse V2 nihai raporda kullanılabilir:

1. Güncel manuscriptte gerçekten bir boşluğu, hatayı veya geliştirme fırsatını karşılamalıdır.
2. İddia güvenilir kaynakla doğrulanmalıdır.
3. Mevcut dipnot veya eklenecek kaynak iddiayı doğrudan desteklemelidir.
4. Metin Google AI’nın kelime dünyasıyla değil, yazarın mevcut doğal akademik Türkçesiyle yeniden yazılmalıdır.

# 3. Eski “sorunlar” raporunun V2’deki rolü

Konuşmaya eklenen `kiraatlerin_rivayetinde_resm-i_mushaf_sorunlar.docx` iki ayrı işlevle kullanılacaktır:

1. **Biçim standardı:** `Yer → İfade → Sorun → Önerilen düzeltme`.
2. **Aday sorun kaynağı:** Eski raporda bulunan her sorun güncel manuscriptte yeniden aranır; çözülmüş olan final rapora alınmaz.

Özellikle eski rapordaki `İfade` alanının birebir alıntı kullanması V2 için zorunlu kullanıcı deneyimi standardıdır. Yazarın Ctrl+F bilmesi veya paragraf kimliği çözmesi beklenmeyecektir; rapordaki ifade doğrudan aranabilir olmalıdır.

Eski raporda teknik Word/Heading/RTL/OOXML/Zotero alanları gibi yazarın düzeltemeyeceği konular V2 final rapora taşınmayacaktır.

# 4. Stage 3–6’dan doğrudan kopyalanabilecekler ve yeniden kurulması gerekenler

## 4.1 Doğrudan yararlanılabilir rezervuar

Stage 3 ve Stage 6’daki aşağıdaki çözüm türleri güçlü başlangıç malzemesidir:

- açık çalışma notunun kaldırıldığı yerler;
- iki paragrafın gerçekten birleştirilmiş yeni biçimi;
- mekanik `değil/değildir` kullanımının olumlu ve doğal cümleyle değiştirildiği yerler;
- `Sonuç olarak` ara kapanışının gerçek geçiş cümlesine dönüştürüldüğü yerler;
- resmin fail/kurucu aktör yapılmasını engelleyen rivâyet ve ilmî değerlendirme odaklı cümleler;
- sonuç paragraflarındaki tekrarı azaltan kısa sentezler.

Bunların hiçbiri otomatik final değildir; güncel exact ifade ve kaynak güvenliği kontrolünden sonra yeniden kullanılacaktır.

## 4.2 Yeniden kurulması zorunlu maddeler

Aşağıdaki Stage 6 madde türleri final V2’ye doğrudan taşınmayacaktır:

- `Mevcut metin:` alanı gerçek alıntı yerine “paragraf şu konuları birkaç kez kurmaktadır” biçiminde özet olan maddeler;
- sayfa aralığı çok geniş olup tek bir uygulanabilir editoryal işlem tanımlamayan maddeler;
- birbiriyle ilgisiz faktik hata + dil sorunu + yapı sorununu tek dev maddede birleştiren maddeler;
- doğru tarih araştırılabilecekken problemli tarihi yalnız silen çözümler;
- dış kaynak yasağı nedeniyle “kaynak sınırı” denmiş fakat bugün hedefli doğrulamayla çözülebilecek maddeler;
- Google AI’nın sonradan eklenen bölüm dosyalarındaki yararlı bilgi adaylarını hiç değerlendirmemiş maddeler.

# 5. V2’de ilk önce doğrulanacak yüksek riskli düğümler

Aşağıdaki sıra Phase 2 doğrulamasının öncelik sırasıdır:

1. **Ca‘berî ölüm tarihi ve tekrarları** — mevcut Stage 3/6 çözümünde yanlış tarih bırakılmış olma riski açık.
2. **Ebû Şâme ölüm yılı** — `1276/1267` iç çelişkisi.
3. **Hârice kimliği** — “Zeyd b. Sâbit’in kızı” / “Hârice b. Zeyd” çatışması.
4. **Amr b. Kays, Hamîdullah, Bâkıllânî, Taberî, Kastallânî, Mehdevî, Ebû Amr, İbn Mu‘âz, Sehâvî, Hâlid b. Ebü’l-Heyyâc, Ebü’l-Fadl el-Huzâ‘î, Mevlây Osman ve diğer çalışma notlu kişiler.**
5. **Mushaf sayısı ve gönderildiği merkezler** — toplam nüsha / gönderilen nüsha / İmam-Medine ayrımı ayrı ayrı kurulacak.
6. **Yedi harf – Ebû Bekir suhufu – arza-i âhire – Osmânî istinsah** — tarihsel rivâyet ile sonraki usûlî yorum katmanları ayrılacak.
7. **Muâviye’ye yazı talimatı rivâyeti ve tevkîfîlik delilleri.**
8. **Üçüncü Bölümde hazf/ziyâde, mana, hikmet ve i‘câz yorumları.**
9. **İsrail/Afrika tahrif anlatısı.**
10. **Sahâbe mushafları ve şâz kırâat tasnifi.**
11. **Matbu mushaf/Osmanlı baskı kronolojisi, “ilk resmî” nitelemeleri ve Mevlây Osman kimliği.**
12. **Kahraman ve Maşalı DOI kayıtları ile Ebû Şâme baskı eşleştirmesi.**

# 6. Final V2 maddesinin değişmez sözleşmesi

Yazara girecek her somut madde mümkün olduğunca şu biçimi kullanacaktır:

### [Açık sorun başlığı]

**Yer:** [bölüm/alt başlık ve güvenilir sayfa]

**İfade:**
> [güncel manuscriptten birebir, Ctrl+F ile bulunabilecek cümle veya gerekli pasaj]

**Sorun:**
[Bu ifadenin neden değiştirilmesi gerektiğinin kısa, doğal ve anlaşılır açıklaması. Kaynak görüşü ile editör yorumu ayrılır.]

**Önerilen düzeltme:**
> [yazarın doğrudan kullanabileceği tamamlanmış metin]

Yalnız gerçekten yeni veya değiştirilmiş bir bilgi için gerekirse:

**Ek kaynak önerisi (APA 7):** [doğrulanmış künye]

Bir paragraf tamamen çıkarılacaksa “silinsin” denmekle yetinilmeyecek; hangi paragrafın çıkarılacağı ve çıkarıldıktan sonra geçişin nasıl olacağı gösterilecektir.

# 7. Nihai rapora alınmayacaklar

- gerçekten çözülmüş eski sorunlar;
- yalnız olumlu değerlendirmeler;
- Word Heading, TOC, PAGEREF, RTL, bidi, run, OOXML ve benzeri üretim/dizgi teknikleri;
- ham kırmızı run/karakter envanterleri;
- iç denetim kodları (`CAND-*`, `VERIFIED`, `CHANGE`, `KEEP` vb.);
- Stage tarihçesi ve proje yönetimi dili;
- yazarın uygulayacağı somut işlem oluşturmayan istatistikler;
- Google AI’nın yalnız daha ağır terminolojiyle yaptığı üslup dönüşümleri.

# 8. Phase 1 sonucu ve Phase 2 giriş koşulu

Bu envanter Phase 1 yönlendirme katmanını tamamlar. Eski 178 doğrulanmış sorun korunmuştur; hiçbirinin sıfırdan yeniden keşfedilmesi gerekmemektedir. Buna karşılık Stage 6’nın 75 maddesi final kabul edilmemiştir. Bundan sonraki aşamada özellikle yüksek riskli faktik düğümler doğrulanacak ve her nihai önerinin kaynak sınırı yeniden belirlenecektir.

Phase 2’de henüz bütün final rapor yazılmayacaktır. Çıktı, doğrulanmış kişi/tarih/kronoloji/kaynak kararları ile hangi Google AI bilgi adaylarının kullanılabilir olduğuna ilişkin kaynaklı bir doğrulama dosyası olacaktır.
