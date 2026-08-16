# V2 Aşama 3 — Google AI İçerik Triage ve Zenginleştirme Haritası

## Amaç

Bu aşamanın amacı `source/manuscript/google-ai/` altındaki bölüm dosyalarını yeni manuscript yerine geçirmek değildir. Amaç, bu dosyalarda bulunan bilgi, kaynak, örnek ve yapı önerilerini güncel canonical manuscript ile bölüm bölüm karşılaştırarak üç şeyi ayırmaktır:

1. Güncel manuscriptte zaten bulunan ve tekrar eklenmemesi gerekenler.
2. Gerçek bir boşluğu doldurabilecek, fakat bağımsız doğrulama ve yeniden yazım gerektirenler.
3. Kaynakların taşıdığından daha ileri giden, kavramsal olarak sorunlu veya yazarın üslubuna yabancı olduğu için kullanılmaması gerekenler.

Canonical metin olarak yalnız `source/manuscript/current/redaktorden_gelen_extracted.md` esas alınmıştır. Google AI dosyaları `GOOGLE-LEAD` statüsündedir. Aşama 2’de doğrulanan kişi, tarih, kronoloji ve kaynak kararları bağlayıcıdır.

Bu aşama author-facing final rapor değildir. Buradaki iç statü ve sınıflandırmalar final rapora aynen taşınmayacaktır.

## Karar anahtarı

- **ALREADY-PRESENT**: Google AI’nın önerdiği içerik güncel manuscriptte zaten yeterince bulunmaktadır.
- **USE-AS-FACT-LEAD**: Bilgi adayı yararlı olabilir; bağımsız kaynak doğrulaması ve yazar üslubunda yeniden yazım gerekir.
- **USE-AS-STRUCTURE-LEAD**: Bilgi değil, konuyu ayırma veya düzenleme biçimi yararlıdır.
- **RESEARCH-BEFORE-USE**: İddia potansiyel olarak değerlidir fakat doğrudan kaynak doğrulaması yapılmadan kullanılamaz.
- **REJECT-OVERCLAIM**: Kaynağın söylediğinden daha güçlü tarihsel, nedensel veya teleolojik sonuç kurulmuştur.
- **REJECT-STYLE**: İçerik doğru olsa bile mevcut kitabın dili ve terminoloji düzeyiyle uyumsuzdur.
- **CURRENT-MANUSCRIPT-FIX**: Google karşılaştırması, güncel manuscriptte fiilen bulunan ve final raporda düzeltilmesi gereken bir sorunu görünür kılmıştır.

# I. Genel sonuç

Google AI dosyalarının ana değeri **nihai metin üretmekte değil, araştırma ve sorun keşfi için aday havuz oluşturmaktadır**. Dosyaların önemli bir kısmı güncel manuscriptte zaten bulunan bilgileri çok daha ağır, modern teorik ve yer yer anakronik bir dille yeniden anlatmaktadır. Buna karşılık birkaç dosya, mevcut metinde gerçekten düzeltilmesi veya daha açık ayrılması gereken noktaları görünür hâle getirmiştir.

En önemli bulgu, Google AI’nın bazı problemli sentezlerinin güncel manuscripte de kısmen taşınmış olmasıdır. Bu nedenle V2 yalnız “Google’dan ne ekleyelim?” sorusuna cevap vermemeli; aynı zamanda “Google kaynaklı veya Google ile aynı mantığı taşıyan hangi mevcut cümleleri geri çekmeliyiz?” sorusunu da çözmelidir.

Google AI’dan doğrudan alınacak uzun paragraf bulunmamaktadır. Kabul edilebilecek unsurlar, bağımsız doğrulanmış küçük bilgi parçaları, örnekler ve bazı yapısal ayrımlardır.

# II. Bölüm bazlı karşılaştırma

## 1. `01.1-01.2_Islamdan_Once_Arap_Yazisinin_Durumu__Erken_Donemde_Kuranin_Yazi_ile_Iliskisi.md`

### Google AI’nın getirdiği başlıca unsurlar

- İslâm öncesi Hicaz’da yazının “çok sınırlı” olduğu görüşü ile “tamamen yok olmadığı” görüşünü karşılaştırarak orta bir sonuca ulaşma çabası.
- Varaka b. Nevfel, Kusay b. Kilâb, Muallakât, Abdülmuttalib’e nispet edilen senet ve Ubey b. Ka‘b gibi örneklerin genişletilmesi.
- Yazının İslâm’la birlikte “marjinal ticari araçtan kutsalın muhafızına” dönüştüğü yönünde geniş tarihsel yorum.

### Karar

**ALREADY-PRESENT + RESEARCH-BEFORE-USE + REJECT-STYLE**

Güncel manuscriptin temel yaklaşımı zaten yazının Hicaz’da tamamen bilinmeyen bir araç olmadığı, fakat kitlesel ve standart bir kullanım düzeyinde de bulunmadığı yönündedir. Google metninin uzun sosyal tarih anlatısı bu dengeyi anlamlı biçimde geliştirmemektedir.

Varaka, Kusay, Muallakât ve benzeri örnekler ancak birincil/sağlam ikincil kaynakta tam bağlamları doğrulanırsa kullanılabilir. Özellikle Muallakât’ın Kâbe’ye asılması gibi geleneksel anlatılar modern tarihsel kanıt seviyesinde sunulmamalıdır.

Varaka için Google’ın kesin `ö. 610` kullanımı Aşama 2 kararına aykırıdır. Kullanılacaksa `ö. 610 [?]` gibi ihtiyatlı biçim korunmalıdır.

### Yararlanılabilecek çekirdek

Gerekirse bölümün girişinde çok kısa bir denge cümlesi kurulabilir:

> İslâm öncesi Hicaz’da yazı toplumun tamamına yayılmış standart bir eğitim pratiği değildi; bununla birlikte ticaret, yazışma ve belirli dinî veya idarî çevrelerde kullanıldığına dair veriler, yazının bölgede bütünüyle bilinmediğini göstermektedir.

Bu cümle dahi finalde mevcut metinle tekrar oluşturuyorsa eklenmeyecektir.

## 2. `01.3_Kuranin_Mushaflastirilma_Ihtiyaci_ve_Tarihsel_Arka_Plan_A.md` ve `_B.md`

### Google AI’nın getirdiği başlıca unsurlar

- Hz. Peygamber dönemindeki `cem` ile Ebû Bekir dönemindeki resmî derleme arasında kavramsal ayrım.
- “İki şahit” meselesini iki farklı yorumla açıklama çabası.
- Tevbe 128–129 ile Ahzâb 23 rivayetlerini Ebû Bekir/Hz. Osman süreçleri bakımından ayırma.
- Mervân b. Hakem kronolojisinde bazı düzeltmeler.

### Karar

**USE-AS-STRUCTURE-LEAD + RESEARCH-BEFORE-USE + CURRENT-MANUSCRIPT-FIX**

Google dosyalarının en öğretici kusurlarından biri burada görülmektedir: biyografik düzeltme yaptığını iddia ettiği hâlde `Zeyd b. Sâbit’in kızı Hârice` ifadesini tekrar etmektedir. Aşama 2’de Hârice b. Zeyd’in Zeyd b. Sâbit’in **oğlu** olduğu doğrulanmıştır. Bu nedenle Google dosyası fact-check kaynağı değildir.

“İki şahit = yazılı belge + ezber” açıklaması tarihsel olayın tartışmasız yöntemi gibi sunulmamalıdır. Bu, kaynaklarda ve sonraki açıklamalarda bulunan yorumlardan biri olarak açıkça nispet edilmelidir. `bilimsel metin tenkidi kuralı`, `resmî orijinal belge`, `devlet arşivi`, `filolojik denetim` gibi çağdaş kurum dilini erken döneme doğrudan taşıyan ifadeler kullanılmamalıdır.

Tevbe 128–129 ile Ahzâb 23’ün hangi derleme/istinsah bağlamında anlatıldığı konusunda farklı rivayetlerin ayrılması yararlı olabilir. Ancak final önerisi, “iki farklı denetim yapıldığı için rivayetler uzlaşır” gibi yeni bir tarihsel mekanizma icat etmemelidir.

### Yararlanılabilecek çekirdek

- `cem` kelimesinin rivayet bağlamına göre ezberleme/toplama anlamlarının ayrılması.
- “İki şahit” hakkında birden fazla açıklama bulunduğunun belirtilmesi.
- Ahzâb 23 rivayetinin hangi döneme nispet edildiğinin kaynağa göre açık verilmesi.

## 3. `01.4_Resm-i_Mushafi_Cogaltmayi_Gerektiren_Sebepler.md`

### Google AI’nın getirdiği başlıca unsurlar

- Medine içindeki ve emsâr arasındaki okuyuş ihtilaflarını ayrı rivayet kanalları hâlinde düzenleme.
- Huzeyfe rivayetini istinsahın yakın sebebi olarak öne çıkarma.
- Sahâbe öğretim çevreleri, özel mushaflar ve fetih coğrafyasını tek neden zincirine bağlama.

### Karar

**ALREADY-PRESENT + USE-AS-STRUCTURE-LEAD + REJECT-OVERCLAIM**

Güncel manuscriptte Huzeyfe rivayeti, bölgesel öğretim çevreleri ve çoğaltma ihtiyacı zaten vardır. Google dosyasının yararlı tarafı, sebep türlerini ayırarak okunabilir hâle getirme fikridir. Fakat içerik “yıkıcı kıraat buhranı”, “devletin bekası”, “vizyoner devlet refleksi”, “askerî-idarî norm olarak dikte”, “teolojik sapma” gibi ifadelerle tarihsel malzemeyi dramatize etmektedir.

Sahâbe mushaflarındaki tefsirî notların yeni Müslümanlar tarafından vahiy sanıldığı gibi özel nedensel iddialar, tam kaynak gösterilmeden genelleştirilemez. Aynı şekilde farklı bölgelerin belirli bir sahâbî okuyuşunu “yegâne meşru metin” kabul ettiği yönündeki ifadeler klasik rivayetin ötesine taşmamalıdır.

### V2 yönü

Final metinde istinsah sebepleri **tek bir siyasi kriz teorisine indirgenmemeli**; kaynaklarda aktarılan okuyuş ihtilafı, coğrafî genişleme ve ortak yazılı referans ihtiyacı birbirini tamamlayan fakat ayrı kanıt düzeyleri olarak sunulmalıdır.

## 4. `01.5_Cogaltilan_Mushaflarin_Sayisi_ve_Gonderildikleri_Sehirler.md`

### Google AI’nın getirdiği başlıca unsur

Farklı rivayetleri birleştirerek “beş bölgesel nüsha + Hz. Osman’ın şahsî/İmam Mushafı = toplam altı ana resmî akış” sonucuna ulaşması.

### Karar

**REJECT-OVERCLAIM + CURRENT-MANUSCRIPT-FIX**

Bu dosya V2 açısından en kritik Google dosyalarından biridir. Aşama 2’de farklı klasik sayım geleneklerinden yeni bir tek “doğru idari model” üretmenin güvenli olmadığı kararlaştırılmıştır. Buna rağmen güncel manuscriptte de aynı sentez açık biçimde bulunmaktadır:

> `Mevcut rivâyetler ışığında, Osmânî mushafları en kuvvetli ihtimalle şu şekilde tasnif etmek mümkündür: Halifenin yanında kalan "İmam Mushaf" ile birlikte Medine, Mekke, Şam, Kûfe ve Basra'ya gönderilen beş nüsha bulunmaktadır. Böylece toplam altı nüshanın varlığı ihtimalî kuvvet kazanmaktadır.`

ve devamında:

> `tarihsel ve rivâyet analizi bakımından en güçlü kanaat "İmam Mushaf" ile birlikte toplam altı nüshanın yazıldığı yönündedir.`

Daha sonra bölüm bunu “çağdaş araştırmacıların önemli bir kısmının ortak kanaati” düzeyine yükseltmektedir. Bu hüküm, kaynakların farklı sayım ilkelerini tek modele dönüştürdüğü için final raporda değiştirilmelidir.

### Güvenli yön

- Dânî’nin dört nüsha görüşü kendi ifadesiyle verilir.
- Dânî’nin başka bağlamlarda Mekke mushafına da atıf yapması ayrıca kaydedilebilir; bu veri otomatik olarak “Dânî gerçekte beş diyordu” sonucuna çevrilmez.
- Beş, yedi, sekiz, dokuz vb. rivayetler sahiplerine nispet edilir.
- `Medine mushafı`, `İmam Mushaf` ve `Hz. Osman’ın yanında kalan nüsha` kavramlarının her kaynakta aynı şeyi ifade ettiği varsayılmaz.
- Sonuç cümlesi kesin sayı üretmek yerine rivayet ihtilafını korur.

### Önerilecek final yönü

> Kaynaklarda istinsah edilen mushafların sayısı ve gönderildikleri merkezler konusunda farklı rivayetler bulunmaktadır. Dânî dört nüsha görüşünü daha sahih kabul ederken başka kaynaklarda beş, yedi, sekiz ve daha yüksek sayılar da nakledilmiştir. Bu sebeple farklı rivayetlerin dayandığı sayım biçimleri ayrıştırılmadan tek bir kesin sayı vermek isabetli değildir.

Bu metin final raporda mevcut kaynaklarla sayfa/kaynak düzeyinde yeniden kurulacaktır.

## 5. `01.6_Resm-i_Osmaninin_Kavramsal_Cercevesi_ve_Tarihsel_Olusumu.md`

### Google AI’nın getirdiği başlıca unsurlar

- `resm` kelimesinin lügavî “iz/eser” anlamıyla teknik mushaf yazımı arasında tarihsel bir terimleşme çizgisi kurma.
- Cevherî’yi bu teknik dönüşümün açık tanığı gibi sunma.
- Kavramı “ortografi kanonu”, “epistemolojik/ontolojik çerçeve”, “dogmatik yazı disiplini” olarak teorileştirme.

### Karar

**ALREADY-PRESENT + SOURCE-MISMATCH + REJECT-STYLE + CURRENT-MANUSCRIPT-FIX**

Güncel manuscriptte lügavî/ıstılahî ayrım zaten geniş biçimde bulunmaktadır. Google’ın teorik genişletmesi ek değer üretmemektedir.

Daha önemlisi, güncel manuscriptte şu cümle yer almaktadır:

> `Cevherî (ö. 400/1009), "iz" ve "yazı" anlamına gelen resm kelimesinin zamanla Kur'an yazımına özgü teknik bir terime dönüştüğünü ve erken dönem mushaf pratiğinin sistemleşmesiyle yakından ilgili olduğunu belirtmiş...`

Aşama 2’de bu atıf `SOURCE-MISMATCH` olarak değerlendirilmiştir. Cevherî’nin sözlük açıklaması lügavî anlamı destekleyebilir; fakat Kur’an yazımına özgü terimleşmenin tarihini Cevherî’nin bizzat kurduğu söylenemez. Ayrıca Google’ın `393/1003` kesin ölüm tarihi güvenli bulunmamış; TDV’nin `400/1009’dan önce` ihtiyatı esas alınmıştır.

### Yararlanılabilecek çekirdek

- Lügavî anlam ile resm ilminin sonraki teknik kullanımını birbirinden ayırmak.
- Terimleşmeyi tek bir sözlük müellifine nispet etmek yerine resm literatürünün gelişimi üzerinden göstermek.

`Yazı sesin ontolojik izi`, `vahyin ses iskeletinin ebediyen sabitlenmesi`, `dogmatik ortografi kanonu` gibi Google ifadeleri kullanılmayacaktır.

## 6. `01.7_Resm-i_Osmaninin_Tanimi_Onemi_ve_Mahiyeti.md`

### Google AI’nın getirdiği başlıca unsurlar

- Ebû Ubeyd, İbn Ebû Dâvud, Dânî ve Ebû Dâvud Süleymân b. Necâh üzerinden resm literatürünün gelişimini aşamalı anlatma.
- Dânî’nin şehir mushafları arasındaki farklılıkları kaydetmesinin “mutlak tek biçimlilik” anlayışına karşı önemini vurgulama.
- Resm ile kıraat ilişkisinde bazı yazım biçimlerinin birden fazla sahih okuyuşla bağdaşabildiğini öne çıkarma.

### Karar

**ALREADY-PRESENT + USE-AS-STRUCTURE-LEAD + REJECT-OVERCLAIM**

Güncel manuscriptte bu tarihsel çizginin büyük kısmı zaten vardır. Google metnindeki `kurucu safha`, `disiplinin anayasası`, `sarsılmaz`, `dogmatik`, `grafik plastisite`, `archetypus`, `resmî skriptoryum` gibi kavramlar eklenmeyecektir.

Bölümün gerçekten korunmaya değer fikri, Dânî’nin resm literatüründe şehir mushafları arasındaki sınırlı farklılıkları kaydetmesinin, resm-i Osmânî’yi “her nüshada harf harf mutlak tek biçimlilik” şeklinde anlamayı zorlaştırmasıdır. Bu fikir güncel manuscriptte zaten iyi ölçüde bulunmaktadır ve tekrar genişletilmemelidir.

### Kaynak sınırı

`Dânî mushaf yazımındaki bazı özelliklerin farklı sahih kıraatleri taşımak üzere bilinçli biçimde korunduğunu söyledi` gibi amaç yükleyen cümleler, Dânî’nin ilgili pasajı açıkça bu niyeti kurmadıkça yumuşatılmalıdır. Güvenli ifade, bazı resm biçimlerinin nakledilmiş birden fazla okuyuşla bağdaşabildiğini söylemektir.

## 7. `01.8_Resm-i_Osmani_Tevkifi_mi_Ictihadi_mi.md`

### Google AI’nın getirdiği başlıca unsurlar

- Tevkîfîlik ile “Osmânî resme bağlı kalma” yükümlülüğünü birbirinden ayırma.
- Muâviye’ye nispet edilen ayrıntılı yazı talimatı rivayetinin delil değerini sorgulama.
- Zeyd b. Sâbit’e nispet edilen kontrol rivayeti ile harf harf imlâ talimatı iddiasını ayırma.

### Karar

**USE-AS-STRUCTURE-LEAD + ALREADY-PRESENT + RESEARCH-BEFORE-USE**

Bu Google dosyasının yapısal olarak en yararlı katkısı, şu iki sorunun ayrı tutulmasıdır:

1. Mushaf yazımında Osmânî resme bağlı kalmak gerekir mi?
2. Bu yazımın bütün ayrıntıları doğrudan Hz. Peygamber tarafından tevkîfî olarak belirlenmiş midir?

Güncel manuscript bu ayrımı büyük ölçüde zaten yapmaktadır. Bu nedenle Google paragrafı eklenmemeli, mevcut bölüm kısaltılıp kaynak güvenliği artırılmalıdır.

Muâviye’ye nispet edilen “hokkayı eğ, kalemi...” rivayeti, tevkîfîlik için güçlü kanıt gibi kullanılmamalıdır. Google’ın Albânî üzerinden “kesin mevzû” sonucu da tek başına yeterli değildir; klasik hadis kaynaklarındaki isnad değerlendirmesi ayrıca kontrol edilmelidir.

Zeyd b. Sâbit rivayeti metnin Hz. Peygamber’e okunup kontrol edildiği yönünde veri sağlayabilir; buradan bütün ortografik ayrıntıların nebevî talimatla belirlendiği sonucu çıkarılmamalıdır.

### Güncel manuscriptte doğrudan düzeltilecek mekanik kayıt

`Bâkıllânî (ö. 403/10113 daha önce geçtiyse silinsin)` biçimindeki çalışma notu ve yazım hatası author-facing final raporda doğrudan düzeltilecektir.

## 8. `01.9_Resm-i_Mushafin_Temel_Ozellikleri.md`

### Google AI’nın getirdiği başlıca unsurlar

- Hazf, ziyâde, hemze, ibdâl, vasl ve fasl için örnekleri düzenleme.
- Bazı hazflerin kırâatle, bazılarının genel erken yazı geleneğiyle ilişkili olabileceğini ayırma.
- Ca‘berî ölüm tarihini `732/1332` olarak düzeltme.

### Karar

**USE-AS-FACT-LEAD + REJECT-OVERCLAIM + CURRENT-MANUSCRIPT-FIX**

Bu dosya örnek havuzu olarak yararlı, açıklama dili bakımından ise yüksek risklidir. `grafik iskelet`, `morfo-fonetik esneklik`, `kaligrafik tescil`, `Hicaz paleografi okulu`, `paleografik inertia`, `muazzam grafik plastiklik`, `deha`, `kusursuzca` gibi ifadelerin hiçbiri V2 metnine alınmamalıdır.

Daha önemli sorun teleolojidir. Google metni hazf ve diğer yazım özelliklerini sık sık “çoklu kıraatleri barındırmak için bilinçli tasarlanmış mekanizma” olarak açıklamaktadır. Güncel manuscriptte de bunun daha yumuşak fakat hâlâ fazla güçlü örnekleri vardır:

> `Bu tespit Osman mushaflarının hazırlanışında yazı ile okuyuş arasında bilinçli bir uyum gözetildiğini ortaya koymaktadır.`

> `Diğer bir ifadeyle kelimedeki bazı harflerin bilinçli olarak düşürülmesi demektir.`

> `Bu düşürme rastgele bir eksiltme değildir; erken mushaf yazım geleneğine bağlı, kurallı ve çoğu zaman hikmetli bir tercihtir.`

Bu cümleler tarihsel yazı özelliği, sonraki resm âlimlerinin açıklaması ve yazarın işlevsel yorumu arasındaki sınırı bulanıklaştırmaktadır.

### Bağlayıcı düzeltmeler

- Ca‘berî `832/1428` → **732/1332**.
- `أُوْلُوا` örneği için Bakara **2/268 değil 2/269**.
- `وَوَصَّى / وَأَوْصَى` örneği Bakara **2/85 değil 2/132**.
- `بِأَيْيْدٍ` için “fonetik zorunluluktan dolayı” ifadesi açık bir kaynak olmadan kullanılmamalıdır.
- Hemzenin bugünkü biçimde görünmemesini `nokta ve hareke sistemi henüz gelişmemişti` gibi tek nedenli bir anlatımla açıklamak yerine, erken Arap yazısındaki işaretleme pratiklerinin farklı gelişim çizgileri olduğu söylenmelidir.
- Erken Arapçada ayırt edici noktaların 20’li hicrî yıllarda kullanıldığını gösteren epigrafik veriler nedeniyle `noktalama henüz yoktu` türü genellemelerden kaçınılmalıdır.

### Kabul edilecek temel ilke

> Resm kurallarının kırâatlerle ilişkisi aynı düzeyde değildir. Bazı yazım biçimleri erken Arap yazı geleneğiyle açıklanabilirken bazıları rivâyet yoluyla sabit birden fazla okuyuşla bağdaşabilmektedir. Bir yazımın teorik olarak birden fazla okuyuşa imkân vermesi, bu okuyuşların sahihliğini tek başına göstermez.

Bu ilke kitabın ana tezine uygundur ve final V2’de korunmalıdır.

## 9. `02.1_Kiraat_Kavrami_ve_Rivayet_Temelli_Yapisi.md`

### Google AI’nın getirdiği başlıca unsurlar

- Kırâati serbest dilsel ihtimallerden ayırma.
- Telakki, müşâfehe ve senedi merkezileştirme.
- İbn Mücâhid’in yedi kıraat seçimini “kanonizasyon” ve kurumsal denetim diliyle açıklama.

### Karar

**ALREADY-PRESENT + REJECT-STYLE + LIMITED-ENRICHMENT**

Güncel manuscriptin 2.1 bölümü zaten Google’ın doğru çekirdeğinin hemen tamamını daha doğal bir dille ifade etmektedir: kırâat dilde mümkün her okuyuş değildir; rivayet, işitme ve telakki önemlidir; yazı tek başına edâyı belirlemez.

Google’ın `epistemolojik havza`, `kutsal metinsel şahit`, `kanonik kodifikasyon`, `anayasal usul`, `sarsılmaz üçlü formül`, `devasa ve muhafazakâr disiplin` gibi dili kullanılmamalıdır.

İbn Mücâhid’in faaliyeti `devletin idari kontrolü ve ulemanın icma süzgeciyle yürütülen en radikal adım` biçiminde anlatılmamalıdır. Scholar Gateway’de yapılan hedefli arama da bu kadar güçlü “devlet kontrolü” formülünü doğrudan taşıyan uygun bir kaynak sağlamamıştır. Bu nedenle bu iddia Google’dan alınmayacaktır.

### Gerçek zenginleştirme adayı

Kırâat terminolojisinde **kırâat – rivâyet – tarîk – vecih** hiyerarşisini çok kısa ve teknik bir paragrafla açıklamak yararlı olabilir. Güncel manuscript 2.2’de imam–râvi–tarîk ayrımını zaten kurmaktadır; eksik olan nokta `vecih`in de doğru düzeyde tanımlanması ve bu terimlerin birbirinin yerine kullanılmamasıdır. Bu ekleme Google metninden değil, doğrudan kırâat kaynaklarından doğrulanarak hazırlanmalıdır.

## 10. `02.2_Kiraatlerde_Rivayet_Sened_ve_Otorite_Ekseni.md`

### Google AI’nın getirdiği başlıca unsurlar

- Rivâyet, sened ve otoriteyi ayrı başlıklar hâlinde kurma.
- Âsım–Hafs–Şu‘be örneği üzerinden aktarım katmanlarını açıklama.
- Yazının tek başına med, hemze, idğam vb. edâ ayrıntılarını belirleyemeyeceğini vurgulama.

### Karar

**ALREADY-PRESENT + REJECT-OVERCLAIM + LIMITED-ENRICHMENT**

Güncel 2.2 bölümü bu unsurları zaten ayrıntılı biçimde içermektedir. Google metninin `formal stemma`, `resmî rivayet`, `ilim akademileri`, `kurumsal ispat disiplini`, `adalet ve zabtı en katı metin tenkidiyle sorgulama` gibi ifadeleri, kırâat senedini hadis tenkidi veya modern stemmatolojiyle gereğinden fazla özdeşleştirmektedir.

### Güncel manuscriptte iyileştirme gerektiren ifade

> `Mesela "Âsım (ö. 127/745) kırâati" denildiğinde burada sadece Âsım'ın tercih ettiği okuyuş biçimi değil...`

`tercih ettiği okuyuş` ifadesi imamın okuyuşu üreten/icat eden kişi olduğu izlenimi verebilir. Daha güvenli ifade `Âsım’a nispet edilen ve ondan nakledilen okuyuş` veya bağlama göre `Âsım’ın naklettiği kırâat` olacaktır.

### Gerçek zenginleştirme adayı

İmamın bir okuyuşun **mucidi değil, kendisine nispet edilen aktarım/öğretim geleneğinin merkez şahsiyeti** olduğunun bir cümleyle açıklanması, kitabın ana tezi bakımından yararlıdır.

## 11. `02.3_Osmani_Mushaf_ve_Yedi_Harf_Meselesi.md`

### Google AI’nın getirdiği başlıca unsurlar

- Yedi harf ile Osmânî mushaf ilişkisini birkaç klasik görüş halinde ayırma.
- Taberî’ye nispet edilen “bir harf üzerinde toplama” görüşü ile, mushaf resminin taşıdığı ölçüde birden fazla unsurun korunmuş olduğu görüşünü karşılaştırma.
- Son aşamada bu görüşlerden birini “en tutarlı” çözüm olarak seçme.

### Karar

**USE-AS-STRUCTURE-LEAD + REJECT-OVERCLAIM + CURRENT-MANUSCRIPT-FIX**

Farklı klasik yaklaşımları açıkça ayırmak yararlıdır. Ancak Google’ın `metinsel daraltma`, `grafik uzlaşma`, `sivil parçalanma`, `kurumsal kurtarma operasyonu`, `cerrahi ayıklama`, `mükemmel grafik plastiklik` dili kullanılmayacaktır.

Daha önemlisi güncel manuscript de tartışmayı yer yer hakem gibi sonuçlandırmaktadır:

> `Doğruya yakın olan, mushafın ihtilafa yol açan fazlalıkları ayıklayıp, sahih ve taşınabilir çeşitliliği koruyan bir çerçeve sunduğunu söylemektir.`

Bu cümle, klasik görüşleri aktarmaktan çıkıp tarihsel mekanizmayı kesinleştiren bir senteze dönüşmektedir. Aynı sorun bölümün sonuç paragrafında da görülmektedir.

### V2 yönü

- Yedi harf ile kanonik kırâatler özdeşleştirilmemelidir.
- “Osmânî mushaf yedi harften şunları korudu” şeklindeki mekanizma, doğrudan tarihsel veri değil, klasik açıklama/görüş düzeyinde sunulmalıdır.
- Taberî, Mekkî, Dânî, Ebû Şâme, İbnü’l-Cezerî ve diğerlerinin görüşleri kendi bağlamlarında ayrı ayrı verilmelidir.
- Yazarın sentezi olacaksa “bu görüşler birlikte değerlendirildiğinde...” gibi ihtiyatlı bir dille kurulmalı; “doğruya yakın olan budur” şeklinde tartışmayı kapatan ifade kullanılmamalıdır.
- Resm bir okuyuşu **üretmez**. Yazı, önceden rivayetle nakledilen okuyuşların bir kısmıyla bağdaşabilir veya onları yazı bakımından sınırlandırabilir.

### Güvenli çekirdek ifade

> Osmânî mushaflar ile yedi harf arasındaki ilişkinin nasıl anlaşılacağı konusunda klasik kaynaklarda farklı görüşler bulunmaktadır. Bu görüşlerin bir kısmı mushafların yedi harften birini esas aldığına, bir kısmı ise resmin taşıdığı ölçüde birden fazla vechi muhafaza ettiğine yönelir. Bu tartışma, sahih kırâatlerin doğrudan mushaf yazısından üretildiği anlamına gelmez; kırâatlerin aktarımında rivâyet ve telakki belirleyici olmaya devam eder.

# III. Google AI’dan gerçekten yararlanılabilecek kısa liste

Aşağıdaki noktalar, **Google metni olarak değil, bağımsız araştırma görevleri olarak** V2’nin sonraki aşamalarına taşınmaya değerdir:

1. **İslâm öncesi yazı:** “sınırlı fakat mevcut” dengesini modern epigrafik verilerle destekleme; mevcut bölüm tekrar etmiyorsa kısa bir güncelleme.
2. **İki şahit meselesi:** Birden fazla açıklama bulunduğunu açıkça ayırma; hiçbirini tartışmasız tarihsel yöntem diye sunmama.
3. **Mushaf sayısı:** Farklı klasik rivayetleri sahiplerine göre vermek; `İmam/Medine/halifenin nüshası` ayrımlarından yeni kesin sayı üretmemek.
4. **Resm kavramı:** Lügavî anlam ile teknik resm literatürünün teşekkülünü ayırmak; terimleşmeyi Cevherî’ye yanlış biçimde yüklememek.
5. **Resm kuralları:** Hazf, ziyâde, hemze, ibdâl, vasl ve faslın kırâatlerle aynı düzeyde ilişkili olmadığını açıklaştırmak.
6. **Erken noktalama:** Noktaların “henüz icat edilmediği” anlatısını bırakmak; yazı pratiği ile Kur’an nüshalarındaki kullanım yoğunluğunu ayırmak.
7. **Kırâat terminolojisi:** Kırâat – rivâyet – tarîk – vecih ayrımını kısa ve doğru bir terminoloji kutusu/paragrafıyla netleştirmek.
8. **İmamın rolü:** İmamı okuyuşun mucidi değil, kendisine nispet edilen rivâyet/öğretim hattının merkez otoritesi olarak açıklamak.
9. **Sözlü ve yazılı aktarım:** Rivâyet/telakki ile resm-i mushafı rakip iki açıklama gibi değil, farklı işlevler gören tamamlayıcı aktarım katmanları olarak kurmak.
10. **Yedi harf–Osmânî mushaf:** Klasik görüş ayrılığını korumak; tek bir mekanik ilişkiyi tarihsel gerçek diye ilan etmemek.

# IV. Google AI’dan kesinlikle taşınmayacak dil ve düşünme kalıpları

Aşağıdaki kelime ve kalıplar, yalnız tek tek sözcük sorunu değildir; çoğu zaman metnin kaynak düzeyini de olduğundan güçlü gösteren bir anlatım biçiminin işaretidir:

- `epistemolojik havza`
- `ontolojik sütun / ontolojik bel kemiği`
- `anayasal usul`
- `kurumsal kurtarma operasyonu`
- `metinsel cerrahi`
- `devrimsel işlev`
- `mükemmel grafik uzlaşma`
- `grafik plastisite / konsonantal plastiklik`
- `morpho-phonetic / morfo-fonetik esneklik` (zorunlu teknik bağlam dışında)
- `archetypus / stemma / recension` (yazarın mevcut terminolojisi yerine gösteriş amaçlı kullanım)
- `resmî skriptoryum`
- `ilim akademisi / kırâat akademisi`
- `devlet arşivi` (erken dönem için kaynak açıkça böyle bir kurumu tarif etmiyorsa)
- `muazzam`, `sarsılmaz`, `deha`, `kusursuzca`, `radikal`, `yıkıcı`, `vizyoner`
- `kesin olarak kanıtlamaktadır` (kaynak yalnız ihtimal/yorum taşıyorsa)
- `tam bilimsel konsensüs`
- her resm özelliğine `bilinçli olarak çoklu kırâati koruma amacı` yükleyen cümleler

# V. Güncel manuscriptte Google karşılaştırmasıyla görünür hâle gelen yüksek öncelikli düzeltmeler

Bu maddeler sonraki author-facing üretim aşamasında exact quote + önerilen metin formatına dönüştürülecektir.

## 1. Altı mushaf sentezi

Güncel manuscript farklı rivayetlerden tek bir `en güçlü / en makul altı nüsha` modeli üretmektedir. Bu hüküm kaldırılmalı veya açık bir araştırmacı görüşüne nispet edilmelidir. Aşama 2’de bağımsız olarak doğrulanmış Dânî verisi dört nüsha görüşünü açıkça nakletmektedir.

## 2. Cevherî’ye terimleşme tarihi nispeti

Cevherî lügavî `resm` anlamı için kullanılabilir. Teknik Kur’an yazımı teriminin tarihsel dönüşümünü Cevherî’nin bizzat açıkladığı biçimindeki cümle yeniden kurulmalıdır.

## 3. Resm özelliklerine amaç yükleme

`bilinçli uyum`, `hikmetli tercih`, `kırâat amacı` gibi ifadeler kaynak düzeyine göre daraltılmalıdır. İşlevsel uyumluluk ile tarihsel niyet birbirinden ayrılmalıdır.

## 4. 1.9 faktik düzeltmeleri

- Ca‘berî: 732/1332.
- Bakara 2/268 → 2/269 (`أُوْلُوا`).
- Bakara 2/85 → 2/132 (`وَوَصَّى / وَأَوْصَى`).
- `fonetik zorunluluktan dolayı` gibi gerekçeler kaynaklanmadıkça çıkarılmalı.

## 5. Kırâat imamını üretici gibi gösteren ifade

`Âsım’ın tercih ettiği okuyuş` yerine, bağlama göre `Âsım’a nispet edilen`, `Âsım’dan nakledilen` veya `Âsım’ın rivâyet ettiği` gibi aktarım merkezli dil kullanılmalıdır.

## 6. Yedi harf bölümünde yazarın tek modeli doğruya en yakın diye seçmesi

Görüşler ayrı kaynak katmanları halinde verilmelidir. Yazar sentezi, sahih kırâatlerin yazıdan üretildiği izlenimini vermemelidir.

## 7. Tevkîfîlik bölümündeki çalışma notu ve kaynak düzeyi

`Bâkıllânî (ö. 403/10113 daha önce geçtiyse silinsin)` gibi açık editoryal kalıntı düzeltilmeli. Muâviye ve Zeyd rivayetlerinin delil değeri, tevkîfîlik sonucundan ayrı değerlendirilmelidir.

# VI. Modern akademik kaynakların bu aşamadaki işlevi

Aşama 2’de seçilen modern çalışmalar bu triage kararlarını destekleyen arka plan olarak kullanılabilir:

- **van Putten (2019):** ortak ortografik özelliklerin erken yazılı Uthmânî arketip tartışmasındaki önemi. Kitapta “yazı yalnız pasifti” gibi aşırı bir sözlü aktarım modelini dengelemek için yararlı.
- **van Putten (2022):** kanonik kırâatlerin rasmle genel uyumu yanında istisnaların bulunması. `resm = her kanonik okuyuşu kusursuz biçimde önceden kodlayan sistem` iddiasını sınırlar.
- **Sidky (2023):** bölgesel kıraat gelenekleri ve sözlü aktarımın erkenliği. Kırâatlerin yalnız yazıdaki belirsizliklerden üretildiği modelin yetersizliğini gösteren modern karşılaştırma için yararlı.
- **Ghabban & Hoyland (2008):** 24/644–45 tarihli Zuhayr yazıtı ve erken ayırt edici noktalar. `noktalama o tarihte bilinmiyordu` genellemesini düzeltmek için doğrudan önemlidir.

Bu kaynaklar klasik İslâmî açıklamaların yerine geçirilmeyecek; klasik kaynakların söylediği ile çağdaş tarihsel/paleografik araştırmanın gösterdiği şey ayrı katmanlar halinde tutulacaktır.

Scholar Gateway’de bu aşamada yapılan iki hedefli tarama, özellikle Ghabban–Hoyland’ın erken noktalama tartışmasını yeniden destekledi. Buna karşılık İbn Mücâhid’in faaliyetini `devlet kontrolü` şeklinde tanımlamayı doğrudan taşıyan yeterince özel ve güçlü bir sonuç elde edilmedi. Bu nedenle Google AI’nın “devletin idari kontrolü + icma süzgeci” formülü **kanıtlanmış kabul edilmedi**.

# VII. `Qiraat Book` Zotero collection için kaynak planı

Kullanıcının belirttiği `Qiraat Book` collection, özellikle şu dört başlıkta değerli bir Türkçe ikincil literatür katmanı oluşturabilir:

1. kırâat–rivâyet–tarîk–vecih terminolojisi;
2. resm-i Osmânî ve kırâat kabul ölçüleri;
3. yedi harf ile Osmânî mushaf ilişkisine dair Türkçe literatürdeki görüş tasnifleri;
4. Türkiye’de resmü’l-mushaf literatürü ve Dânî/Ebû Dâvud çalışmaları.

Ancak bu turda ZotSeek/Zotero Local bağlantısına doğrudan çağrı yapıldığında mevcut host `This conversation does not support developer MCPs` hatası verdi. Bu nedenle collection **taranmış gibi kabul edilmeyecek** ve içeriği hakkında tahminde bulunulmayacaktır.

Bağlantı erişilebilir hâle geldiğinde yöntem şu olacaktır:

- önce ZotSeek ile collection içindeki Türkçe çalışmalar geniş semantik taramadan geçirilecek;
- gerçekten ilgili makaleler seçildikten sonra Zotero Local Library ile exact metadata ve gerekli PDF pasajları doğrulanacak;
- yalnız doğrudan ilgili ve metindeki belirli bir düzeltme/zenginleştirmeyi taşıyan çalışmalar finalde ek kaynak önerisine dönüşecek;
- “collection içinde olduğu için” kaynak eklenmeyecek.

# VIII. Aşama 3’ün bağlayıcı kararları

1. Google AI **yeniden yazım kaynağı değil, araştırma lead havuzudur**.
2. Google’ın ana fikirlerinin büyük bölümü güncel manuscriptte zaten vardır; tekrar ekleme kitabı şişirecektir.
3. Google’ın en büyük riski üsluptan önce **epistemik kesinlik artışıdır**: rivayet → tarihsel gerçek, işlev → bilinçli amaç, ihtimal → kesin mekanizma dönüşmektedir.
4. Güncel manuscriptte de Google’a benzeyen bazı sentezler bulunduğundan, yalnız yeni ekleri reddetmek yetmez; mevcut cümleler de kaynak düzeyine çekilmelidir.
5. En yüksek öncelikli mevcut düzeltmeler: **altı mushaf sentezi, Cevherî source mismatch, 1.9’daki teleolojik resm açıklamaları, Ca‘berî ve ayet numaraları, yedi harf bölümünün tek modele bağlanması**.
6. Bölüm 2 için gerçek yeni katkı, uzun teorik paragraflar değil; **kırâat–rivâyet–tarîk–vecih terminolojisinin netleştirilmesi ve imamın üretici değil aktarım merkezi olduğunun açıklanmasıdır**.
7. Sözlü aktarım ile yazılı resm birbirine rakip açıklamalar gibi kurulmayacak; farklı işlev gören iki aktarım katmanı olarak değerlendirilecektir.
8. Resmin teorik olarak bir okuyuşu mümkün kılması, o okuyuşun sahihliğini kanıtlamaz; sahihlik rivâyet ve kabul ölçüleriyle belirlenir.
9. Yedi harf tartışması klasik görüş ihtilafı olarak korunacak; tek bir mekanik tarihsel modele dönüştürülmeyecektir.
10. `Qiraat Book` collection erişilebildiğinde hedefli Türkçe literatür taraması yapılacak; şu an erişim olmadığı için hiçbir kaynak varmış gibi yazılmayacaktır.

## Aşama sonucu

**PASS — LIMITED ENRICHMENT, MAJOR PROSE REJECTION.**

Google AI dosyaları yararlı bir fact/source/gap discovery katmanı sağlamış, fakat nihai metin olarak güvenilir bulunmamıştır. V2’ye taşınmaya değer katkılar sınırlı ve somuttur: birkaç faktik düzeltme, bazı tartışmaları görüşler halinde ayırma, teknik kırâat terminolojisini netleştirme ve resm–rivâyet ilişkisinde niyet/işlev ayrımını güçlendirme. Bir sonraki aşamada bu kararlar, güncel manuscriptteki exact ifadeler üzerinden author-facing düzeltme adaylarına dönüştürülecektir.