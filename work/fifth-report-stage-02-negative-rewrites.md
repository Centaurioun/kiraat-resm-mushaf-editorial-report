# Fifth Report — Aşama 2
## Kırmızı `değil/değildir` kullanımlarının yeniden yazımı

Bu dosya Fifth Report’un ikinci çalışma aşamasıdır. Nihai yazar raporu değildir. Amaç, redaktörün güncel DOCX üzerinde kırmızıyla işaretlediği `değil/değildir` ailesini, önceki Stage 3 ve Fourth Report V2’deki bilimsel düzeltmeleri kaybetmeden, doğal ve doğrudan Türkçe cümlelere dönüştürmektir.

## 1. Kapsam ve sayım uzlaştırması

Önceki DOCX tabanlı tam taramada **96 ayrı kırmızı paragraf** ve bu paragraflarda run düzeyinde **132 kırmızı `değil` ailesi parçası** tespit edilmişti. Searchable Markdown extraction üzerinde yapılan yeni tam metin taramasında `değil` ailesinin **128 metinsel eşleşmesi** görülmektedir. Bu iki sayı birbiriyle çelişmez: Word’de bir kelime veya yapı renk/biçimlendirme nedeniyle birden fazla run’a bölünebilir; Markdown extraction ise yalnız metinsel görünümü taşır.

Aşama 2’nin karar birimi tek tek Word run’ı değil, ilgili **cümle/paragrafın nihai yeniden yazımıdır**. Aynı paragrafta birden fazla kırmızı parça varsa bunların tamamı tek doğal paragrafla çözülebilir. Önceki karar dağılımındaki `ALREADY_RESOLVED_STAGE3` veya `KEEP` etiketleri bu aşamada kapanış sebebi sayılmamıştır. Fourth Report V2’de daha güvenli bilimsel bir paragraf zaten hazırlanmışsa Fifth Report o bilimsel anlamı esas alır ve negatif/formülaik yapıyı ayrıca temizler.

Karar türleri:

- **DOĞRUDAN-YENİDEN-YAZ:** mevcut negatif yapı olumlu/doğrudan cümleyle değiştirilir.
- **YAPISAL-OLARAK-ÇÖZÜLÜR:** aynı paragraf Fourth Report V2’de bütünüyle değiştirildiği için yeni rakip cümle üretilmez; Fifth Report, Fourth Report’un bilimsel çekirdeğini daha doğal dille kullanır.
- **ALINTI-KORU:** doğrudan alıntı, âyet meali veya kaynak sahibinin lafzı sırf `değil/değildir` içerdiği için değiştirilmez.

## 2. Bağlayıcı yazım ilkesi

Bu aşamada `değildir → olmamaktadır`, `değil → aksine`, `sadece değil → bunun yanında` gibi toplu sözcük ikameleri yapılmamıştır. Cümlenin düşünce yapısı yeniden kurulmuştur. Özellikle kitabın ana tezi mümkün olduğunda şu olumlu sırayla ifade edilmiştir:

> Kırâatlerin aslî kaynağı telakki, müşâfehe, edâ, isnad ve rivâyet geleneğidir. Resm-i Osmânî ise rivâyetle sabit okuyuşların müşterek mushaf yazısıyla ilişkisini belirleyen tamamlayıcı bir ölçüdür.

Bu yapı, `Resm kırâatlerin kaynağı değildir` türündeki gerekli bilimsel ayrımı korur; ancak kitabın geneline yayılan negatif tanım ritmini azaltır.

# Giriş

## G-01 — Cem ile istinsahın negatif karşıtlıkla tanımlanması

**Mevcut ifade:**
> Hz. Peygamber'in vefatından sonra gerçekleştirilen cem ile Hz. Osman dönemindeki istinsah ise aynı işlem değildir.

**Önerilen düzeltme:**
> Hz. Peygamber'in vefatından sonra gerçekleştirilen cem ile Hz. Osman dönemindeki istinsah, farklı amaç ve şartlarda yürütülen iki ayrı uygulamadır.

## G-02 — Araştırma sorularının negatif zincirle birbirine bağlanması

**Mevcut ifadeler:**
> Bu sorular birbirinden bağımsız değildir.
>
> Şehir mushaflarına ait rivâyetler yalnız erken dönem yazı tarihine, çağdaş baskılar da yalnız matbaa tarihine ait veriler değildir.

**Önerilen düzeltme:**
> Bu sorular birbirine bağlıdır. Osmânî mushafların ortak başvuru metni hâline gelme süreci, resm-i Osmânî'ye uygunluğun kabul ölçüsüne dönüşmesini; kırâatin rivâyet mantığı ise bu ölçünün sınırlarını açıklamaktadır. Şehir mushaflarına ait rivâyetler erken dönem yazı tarihinin yanında okuyuşların yazılı aktarımı hakkında, çağdaş baskılar ise resm ve zapt tercihlerinin kırâatlerin dolaşımına etkisi hakkında veri sunmaktadır.

## G-03 — Kitabın ana tezinin `değildir` ile kurulması

**Mevcut ifadeler:**
> Kitabın hareket noktası, resm-i Osmânî'nin kırâatleri meydana getiren bağımsız bir kaynak olmadığıdır.
>
> Resm-i Osmânî'ye uygunluk, bu bütün içinde okuyuşu üreten değil, rivâyetle gelen okuyuşun ortak mushaf geleneğindeki kabul alanını belirleyen bir ölçüdür.

**Önerilen düzeltme:**
> Kırâatlerin aslî kaynağı telakki, müşâfehe, edâ ve isnada dayanan rivâyet geleneğidir. Resm-i Osmânî'ye uygunluk ise rivâyetle gelen okuyuşun ortak mushaf geleneğindeki kabul alanını belirleyen ölçülerden biridir.

Bu metin, önceki Aşama 4’te `KEEP` verilen Giriş P24 kullanımını da kullanıcının son talebi doğrultusunda olumlu yapıya dönüştürür.

## G-04 — Resm, resm-i mushaf ve resm-i Osmânî ayrımının negatif kalıpla kurulması

**Mevcut ifade:**
> Bu sebeple her mushaf yazısı resm-i Osmânî olmadığı gibi, resm-i mushaf ile resm-i Osmânî de bütün bağlamlarda birbirinin yerine kullanılamaz.

**Önerilen düzeltme:**
> Resm-i mushaf daha geniş bir inceleme alanını, resm-i Osmânî ise Hz. Osman döneminde çoğaltılan mushaflara nispet edilen tarihsel yazım geleneğini ifade eder; iki terim bağlama göre ayrı kullanılmalıdır.

## G-05 — Şehir mushaflarındaki farklılığın `X değil Y` yapısıyla açıklanması

**Mevcut ifade:**
> Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, ortak mushaf otoritesinin bulunmadığını değil, aynı istinsah geleneği içinde bazı yazım farklılıklarının rivâyet edildiğini göstermektedir.

**Önerilen düzeltme:**
> Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, müşterek mushaf otoritesi içinde farklı yazım rivâyetlerinin de bulunduğunu belirtmektedir.

## G-06 — Kırâatin negatif tanımla açılması

**Mevcut ifade:**
> Kırâat, dil bakımından mümkün olan her seslendirme anlamına gelmez.

**Önerilen düzeltme:**
> Kırâat, güvenilir rivâyet yoluyla nakledilen ve kırâat geleneği içinde kabul gören okuyuşları ifade eder.

## G-07 — Kırâat, rivâyet, tarîk ve vecih ayrımında `aynı düzeyde değildir`

**Mevcut ifade:**
> Bir kırâat imamına nispet edilen genel okuyuş sistemi, bu okuyuşun belirli bir râvi üzerinden aktarılan rivâyeti ve râviden sonraki nakil kollarını gösteren tarîklerle aynı düzeyde değildir.

**Önerilen düzeltme:**
> Kırâat, rivâyet, tarîk ve vecih aktarım zincirinin farklı düzeylerini gösteren terimlerdir: kırâat imama, rivâyet râviye, tarîk râviden sonraki nakil koluna, vecih ise ilgili rivâyet veya tarîk içindeki edâ seçeneğine işaret eder.

## G-08 — Resme uygunluğun negatif tanımı

**Mevcut ifade:**
> Resm-i Osmânî'ye uygunluk, her durumda harflerin okuyuşu birebir göstermesi anlamına gelmez.

**Önerilen düzeltme:**
> Resm-i Osmânî'ye uygunluk doğrudan veya ihtimalî biçimde gerçekleşebilir.

## G-09 — Sahih/meşhur/âhâd/şâz kategorilerinde negatif tanım

**Mevcut ifadeler:**
> Sahih, meşhur, âhâd ve şâz nitelemeleri de tek bir ölçünün farklı dereceleri değildir.
>
> Şâz bir rivâyetin tefsîrî veya dilsel değeri bulunabilmesi, onun bağlayıcı bir kırâat kabul edilmesiyle aynı mesele değildir.

**Önerilen düzeltme:**
> Sahih, meşhur, âhâd ve şâz nitelemeleri farklı değerlendirme boyutlarını ifade eder. Şâz bir rivâyetin tefsîrî veya dilsel bilgi değeri ile bağlayıcı kırâat statüsü ayrı ayrı değerlendirilmelidir.

## G-10 — Bağlayıcılık ile tevkîfîliğin negatif ilişkiyle ayrılması

**Mevcut ifade:**
> Resm-i Osmânî'nin sonraki mushaf geleneğinde bağlayıcı kabul edilmesi, bütün yazım ayrıntılarının doğrudan vahiy tarafından belirlendiğinin tartışmasız biçimde kabul edildiği anlamına gelmez.

**Önerilen düzeltme:**
> Resm-i Osmânî'nin sonraki mushaf geleneğindeki bağlayıcılığı ile bütün yazım ayrıntılarının tevkîfî olduğu görüşü ayrı meselelerdir.

## G-11 — Yazım örneklerinin `yalnız ... değil` yapısı

**Mevcut ifade:**
> Yazım örnekleri yalnız şekil bakımından değil, bağdaştıkları veya dışladıkları kırâat ihtimalleri açısından ele alınmaktadır.

**Önerilen düzeltme:**
> Yazım örnekleri, şekil özellikleriyle birlikte bağdaştıkları veya dışladıkları kırâat ihtimalleri açısından ele alınmaktadır.

## G-12 — Literatür katkısının negatif tanımla kurulması

**Mevcut ifade:**
> Kitabın literatüre sağlamayı hedeflediği katkı, resm ilmi ile kırâat ilmini bütünüyle yeni kavramlarla açıklamak değil, çoğu zaman ayrı başlıklar altında incelenen meseleleri ortak bir problem etrafında buluşturmaktır.

**Önerilen düzeltme:**
> Kitabın literatüre hedeflediği katkı, çoğu zaman ayrı başlıklar altında incelenen resm ve kırâat meselelerini ortak bir problem etrafında birlikte değerlendirmektir.

## G-13 — Resm-i Osmânî'nin `yalnız eski imlâ değil` kalıbıyla tanımlanması

**Mevcut ifade:**
> Resm-i Osmânî yalnız eski bir imlâ sistemi olarak değil, rivâyetle nakledilen okuyuşların ortak yazılı sınırlarını belirleyen bir ölçü olarak incelenmektedir.

**Önerilen düzeltme:**
> Resm-i Osmânî, tarihsel bir yazım geleneği olmasının yanında rivâyetle nakledilen okuyuşların ortak yazılı sınırlarını belirleyen bir ölçü olarak incelenmektedir.

## G-14 — Girişin kapanışındaki negatif araştırma sorusu

**Mevcut ifade:**
> Bu yapı içinde araştırmanın temel sorusu, yazı ile sözlü rivâyetten hangisinin üstün olduğu değildir.

**Önerilen düzeltme:**
> Araştırmanın temel sorusu, rivâyet yoluyla sabit okuyuşlarla bunların ortak mushaf yazımı içindeki kabul ve aktarımı arasındaki ilişkinin nasıl kurulduğudur.

**Uzlaştırma notu:** Fourth Report V2, Girişin son paragrafını doğrudan Birinci Bölüme geçişe dönüştürmektedir. Nihai Fifth Report’ta iki rakip metin verilmeyecek; Fourth Report’taki geçiş tercih edilirse bu madde o geçiş içinde çözülmüş sayılacaktır.

# Birinci Bölüm

## 1.1 — İslâm'dan Önce Arap Yazısının Durumu

### B1-01 — Hatîb el-Bağdâdî'ye nispet edilen negatif hüküm

**Mevcut ifade:**
> Ona göre İslâm'ın ilk dönemlerinde Araplar yazı konusunda yeterli yetkinliğe sahip değildi.

**Önerilen düzeltme:**
> Hatîb el-Bağdâdî, İslâm'ın ilk dönemlerinde Araplar arasında yazı yetkinliğinin sınırlı olduğunu düşünmektedir.

### B1-02 — Yazının bilinmesi/kullanılması ayrımında negatif sonuç

**Mevcut ifade:**
> Yazının toplumun tamamına yayılmamış olması, onun bilinmediği veya kullanılmadığı anlamına gelmez.

**Önerilen düzeltme:**
> Yazının toplumun tamamına yayılmamış olması, belirli çevrelerde bilindiği ve kullanıldığı yönündeki verilerle birlikte değerlendirilmelidir.

### B1-03 — Yazının yaygınlığına ilişkin çift negatif sentez

**Mevcut ifade:**
> İslâm öncesi Arap toplumunda yazı, yaygın ve sistemli bir uygulama değildi; ancak tamamen yabancı olunan bir kabiliyet de değildi.

**Önerilen düzeltme:**
> İslâm öncesi Arap toplumunda yazı toplum geneline yayılmış sistemli bir uygulama hâline gelmemişti; buna karşılık belirli çevrelerde biliniyor ve pratik ihtiyaçlar için kullanılıyordu.

### B1-04 — Teknik/toplumsal dönüşümde `sadece ... değil`

**Mevcut ifade:**
> Bu süreç Arap yazısının sadece teknik yönden değil, aynı zamanda toplumsal ve kültürel dönüşümünü de beraberinde getirmiştir.

**Önerilen düzeltme:**
> Bu süreç, Arap yazısında teknik gelişmenin yanında toplumsal ve kültürel bir dönüşümü de beraberinde getirmiştir.

### B1-05 — Kurumsal kullanımın negatif kurulması

**Mevcut ifade:**
> Bu veriler yazının kurumsal anlamda pratiğinin olmadığını, ancak toplumsal hayatın bazı alanlarında fonksiyonel olduğunu otaya koymaktadır.

**Önerilen düzeltme:**
> Bu veriler, yazının toplum geneline yayılmış kurumsal bir pratik hâline gelmediğini, buna karşılık belirli toplumsal alanlarda işlev gördüğünü düşündürmektedir.

### B1-06 — Sözlü/yazılı dolaşımın negatif karşıtlığı

**Mevcut ifade:**
> ... yazının sadece sözlü değil, zaman zaman yazılı olarak dolaşımda olduğunu düşündürmektedir.

**Önerilen düzeltme:**
> Zuheyr gibi bazı şairlerin yazıyı bildiklerine dair bilgiler, güçlü sözlü kültürün yanında yazılı dolaşımın da bulunduğunu düşündürmektedir.

### B1-07 — Bölüm sonu `hiç bilinmediğini söylemek mümkün değildir`

**Mevcut ifade:**
> Bütün bu veriler bir arada değerlendirildiğinde İslâm öncesi Arap toplumunda yazının hiç bilinmediğini söylemek mümkün değildir.

**Önerilen düzeltme:**
> Bütün bu veriler, İslâm öncesi Arabistan'da yazının belirli çevrelerde bilindiğini ve kullanıldığını; buna karşılık toplum geneline yayılmış sistemli bir uygulamaya dönüşmediğini düşündürmektedir.

## 1.2 — Erken Dönemde Kur'an'ın Yazı ile İlişkisi

### B1-08 — Yazının sözlü aktarıma `alternatif değil` diye tanımlanması

**Mevcut ifade:**
> Böylece yazı, sözlü aktarımın karşısına konumlanan bir alternatif değil, onunla birlikte işleyen tamamlayıcı bir faktör olarak müesseseleşmeye başlamıştır.

**Önerilen düzeltme:**
> Yazı, sözlü aktarımla birlikte işleyen tamamlayıcı bir unsur olarak giderek daha belirgin bir konum kazanmıştır.

### B1-09 — `Ne salt sözlü ne de ... tamamen yazılı` ve `sadece teknik metin değil` zinciri

**Mevcut ifadeler:**
> Bu serüven Kur'an'ın ne salt sözlü ne de baştan itibaren tamamen yazılı bir metin olduğunu göstermektedir.
>
> ... sadece teknik bir metin değil, aynı zamanda İslâm toplumunun bilgi, otorite ve hafıza anlayışının bir yansıması olmuştur.

**Önerilen düzeltme:**
> Kur’an'ın aktarımında sözlü rivâyet ile yazılı kayıt erken dönemden itibaren birlikte işleyen iki unsur olmuştur. Kitaplaşma süreci, teknik metinleşmenin yanında İslâm toplumundaki bilgi, otorite ve hafıza ilişkileriyle de bağlantılıdır.

### B1-10 — Kaydın başlangıç tarihindeki negatif bilgi

**Mevcut ifade:**
> Kur'an vahyinin ne zaman kayda geçirilmeye başlandığı hususunda kesin ve tarihsel olarak net bir bilgiye sahip değiliz.

**Önerilen düzeltme:**
> Kur’an vahyinin ne zaman kayda geçirilmeye başlandığını kesin biçimde belirleyen tarihsel bir veri bulunmamaktadır.

### B1-11 — Mekkî kaydın kapsamı

**Mevcut ifade:**
> ... bu kayıt faaliyetinin kapsamını, sürekliliğini ve bütün Mekkî vahyi içerip içermediğini kesin biçimde belirlemeye elverişli değildir.

**Önerilen düzeltme:**
> Mevcut bilgiler, bu kayıt faaliyetinin kapsamı, sürekliliği ve bütün Mekkî vahyi içerip içermediği konusunda kesin bir sonuca imkân vermemektedir.

### B1-12 — Hz. Peygamber döneminde yazılı kayıt için çift negatif yapı

**Mevcut ifadeler:**
> Yazılı vahiy metinlerinin Hz. Peygamber döneminde bir araya getirilmemiş olmasının, vahyin o dönemde yazıya geçirilmediği anlamına gelmediğini...
>
> Kur'an'ın yazıya geçirilmesi nüzûl sonrasında ortaya çıkmış bir mesele değildir.

**Önerilen düzeltme:**
> Hz. Peygamber döneminde tek bir kitap hâlinde derleme yapılmamış olsa da vahyin farklı yazı malzemeleri üzerine kaydedildiği rivâyet edilmektedir. Hâris el-Muhâsibî de yazılı kaydı nüzûl dönemine ait bir uygulama olarak değerlendirmektedir.

### B1-13 — Merkezî arşiv karşıtlığı

**Mevcut ifade:**
> Bu aktarım Kur'an'ın yazılı malzemesinin merkezî bir arşivde değil, farklı sahâbîlerin elinde muhafaza edildiği yönündeki yaklaşımı desteklemektedir.

**Önerilen düzeltme:**
> Bu aktarım, yazılı vahiy malzemesinin farklı sahâbîlerin ellerinde muhafaza edildiği yönündeki yaklaşımı desteklemektedir.

## 1.3–1.4 — Cem ve istinsah

### B1-14 — Hz. Peygamber dönemindeki `cem`in yalnız hafızaya indirgenmesi

**Mevcut ifade:**
> ... cem (toplama) ifadesi yazılı malzemelerin fiziki olarak bir araya getirilmesi değil, Kur'an'ın ezberlenmesi anlamında açıklanmıştır.

**Önerilen düzeltme:**
> Söz konusu rivâyetlerdeki cem ifadesi bazı âlimler tarafından Kur’an'ın ezberlenmesi anlamında yorumlanmış; bunun yanında nüzûl döneminde vahyin yazılı kaydının da bulunduğu bilinmektedir.

### B1-15 — Yedi harfin `vücûb değil ruhsat` kalıbıyla anlatılması

**Mevcut ifade:**
> ... yedi harfin korunmasının vücûb değil ruhsat alanına girdiği...

**Önerilen düzeltme:**
> İbnü'l-Cezerî'ye göre yedi harf, ümmete tanınmış bir ruhsat ve kolaylık alanıdır.

### B1-16 — Ebû Bekir/Osman uygulamalarının `çelişki değil` yapısı

**Mevcut ifade:**
> Dolayısıyla Hz. Ebû Bekir ile Hz. Osman dönemleri arasında bir çelişki değil, şartlara göre şekillenmiş iki farklı tedbir söz konusudur.

**Önerilen düzeltme:**
> Hz. Ebû Bekir ve Hz. Osman dönemlerindeki uygulamalar, farklı tarihsel şartlarda ortaya çıkan iki ayrı tedbir olarak değerlendirilmelidir.

### B1-17 — 1.4'teki `Hülasa ... değildir` kapanışı

**Mevcut ifade:**
> Hülasa, istinsah kararı, vahyin aslını değiştirme veya yeni bir metin oluşturma girişimi değildir.

**Karar:** **YAPISAL-OLARAK-ÇÖZÜLÜR.** Fourth Report V2 bu mini-sonucu kaldırıp 1.5'e geçişe dönüştürmektedir. İçerik gerekirse şu tek cümlede korunabilir:
> İstinsah kararı, mevcut sahifeler esas alınarak müşterek mushaf nüshalarının çoğaltılması ve okuyuş ihtilaflarının sınırlandırılması amacıyla alınmış bir tedbir olarak rivâyet edilmektedir.

### B1-18 — Sahâbe mushaflarındaki açıklayıcı kayıtlar

**Mevcut ifade:**
> Bu ilaveler, Kur'an metninin bir parçası olmayıp...

**Önerilen düzeltme:**
> Bu ilaveler açıklayıcı notlar niteliğindedir; zamanla bazı kimseler tarafından kırâat olarak algılanmış ve ilgili sahâbîlere nispet edilmiştir.

## 1.6–1.7 — Resm kavramı ve resm literatürü

### B1-19 — Yazı ile ses ilişkisinin negatif tanımı

**Mevcut ifade:**
> Yazı sesin aynısı değil, onun kabul edilmiş ve kurallı görsel karşılığıdır.

**Önerilen düzeltme:**
> Yazı, sesin kabul edilmiş ve kurallı görsel karşılığı olarak değerlendirilir.

### B1-20 — `Sadece sözün kaydı değil`

**Mevcut ifade:**
> Böylece yazı, sadece sözün kaydı değil, onun korunmuş ve düzenlenmiş hâli olarak ortaya çıkar.

**Önerilen düzeltme:**
> Bu tanımlarda yazı, sözü kalıcı ve düzenlenmiş bir biçimde temsil eden araç olarak açıklanmaktadır.

### B1-21 — Ebû Ubeyde paragrafındaki negatif formül

**Mevcut ifade:**
> O, Osman mushaflarının yazımını bağımsız bir imlâ tercihi olarak değil, sahâbe nakline dayanan bağlayıcı bir metin geleneği olarak değerlendirmiştir.

**Önerilen düzeltme:**
> Ebû Ubeyde, Osman mushaflarının yazımını sahâbe nakline dayanan bir metin geleneği içinde değerlendirmiştir.

### B1-22 — Dânî paragrafındaki negatif zincir

**Mevcut ifadeler:**
> ... “mutlak tek biçimlilik” değil, “nakille sabitlenmiş...”
>
> ... resm, sadece kelimelerin nasıl yazıldığını değil...

**Önerilen düzeltme:**
> Dânî, Osman mushaflarının yazım özelliklerini ve şehir mushafları arasında nakledilen farklılıkları sistematik biçimde kaydetmiştir. Onun yaklaşımında resm, kelimelerin yazım biçimleriyle birlikte farklı mushaf merkezlerine nispet edilen yazım rivâyetlerini de inceler.

### B1-23 — Ebû Dâvud'da kıyas/nakil karşıtlığı

**Mevcut ifade:**
> Mushaf yazımında esas olan dilcilerin kıyas yoluyla ulaştıkları imlâ kuralları değil, güvenilir nakille sabit olmuş yazım geleneğidir.

**Önerilen düzeltme:**
> Ebû Dâvud'un yaklaşımında mushaf yazımının temel başvuru zemini, güvenilir nakille aktarılan Osman mushaflarının yazım geleneğidir.

### B1-24 — Zerkeşî paragrafındaki art arda negatif karşıtlıklar

**Mevcut küme:**
> ... sadece filolojik veya gramer temelli bir tercih olmadığını...
>
> ... değiştirmeyi değil, olduğu gibi korumayı...
>
> ... teorik kurallar değil, sahâbeden gelen yazı pratiğidir.
>
> ... belirleyici olan şey kıyas değil, rivâyet ve nakildir.
>
> ... “yanlış” kabul edilmez...

**Önerilen düzeltme:**
> Zerkeşî, Osman mushaflarında benimsenen yazım biçiminin dilcilerin kıyas yoluyla belirlediği standart imlâ kurallarıyla her zaman örtüşmediğine dikkat çeker. Onun aktardığı çerçevede mushaf hattının ölçüsü, sonraki kıyasî imlâdan ziyade sahâbe döneminden nakledilen yazım uygulamasıdır. Elif hazifleri, harf ziyadeleri ve vasl-fasl örneklerinin sonraki mushaflarda korunması da bu tarihsel aktarımın devamı olarak değerlendirilmiştir.

### B1-25 — 1.7 sonuç paragrafındaki `değil` zinciri

**Mevcut ifade:**
> ... bu yazım sistemi dilbilgisel düşünselin ürünü değil... belirleyici otorite filolojik kurallar değil...

**Önerilen düzeltme:**
> Bu anlatımda resm-i Osmânî, sahâbe döneminden nakledilen tarihsel mushaf yazımı olarak ele alınmakta; normatif değerinin dayanağı da bu yazım uygulamasının güvenilir nakille aktarılması şeklinde açıklanmaktadır.

### B1-26 — Çağdaş araştırmacılar kümesindeki tekrarlanan `değil` formülleri

**Mevcut yapılar:**
> ... yalnızca çoğaltma işi değil...
>
> ... metni değiştiren değil...
>
> ... kırâat farklılıklarını tamamen ortadan kaldırmak için değil...
>
> ... sözlü geleneği ortadan kaldıran değil...

**Önerilen düzeltme:**
> Çağdaş araştırmacılar Hz. Osman dönemindeki istinsah faaliyetini, mushafların çoğaltılmasının yanında müşterek bir yazılı çerçevenin oluşmasıyla ilişkilendirmiştir. el-Azamî bu süreci mevcut güvenilir rivâyetin müşterek mushaf geleneği içinde sabitlenmesi çerçevesinde değerlendirir. Bazı çağdaş çalışmalar, Osmânî mushafların farklı rivâyetlerle bağdaşabilen sınırlı bir yazılı çerçeve sunduğunu vurgular. Erken dönem üzerine yapılan çalışmalar da sözlü aktarım ile yazılı kayıtların birlikte işlediği bir aktarım düzenine dikkat çekmektedir.

### B1-27 — Déroche'ye nispet edilen `eksiklik veya hata değil`

**Mevcut ifade:**
> ... bir eksiklik veya hata değil, erken dönem Arap yazısının tabii özellikleridir.

**Önerilen düzeltme:**
> Déroche, noktasızlık, harekesizlik ve bazı yazım farklılıklarını erken Arap yazısının doğal özellikleri çerçevesinde değerlendirmektedir.

Bu kullanım önceki Aşama 4’te `KEEP` sayılmıştı; Fifth Report kullanıcının son talebi doğrultusunda kaynak nispetini koruyarak pozitif yapıya dönüştürür.

## 1.8–1.10 — Tevkîfîlik ve resm kuralları

### B1-28 — Doğrudan Bâkıllânî alıntısı

**Mevcut alıntı parçası:**
> ... özel bir resm dayatılmış değildir.

**Karar:** **ALINTI-KORU.** Bu cümle doğrudan alıntının lafzıdır. Sırf kırmızı `değildir` içerdiği için değiştirilmez. Çevresindeki yazar cümleleri sadeleştirilebilir.

### B1-29 — İmâm Mâlik'in görüşünün `değil` ile aktarılması

**Mevcut ifade:**
> ... mushafın insanların sonradan geliştirdiği imlâ ile değil, “ilkyazım üzere” yazılması gerektiğini belirtmiştir.

**Önerilen düzeltme:**
> İmâm Mâlik, mushafın “ilk yazım üzere” yazılması gerektiğini belirtmiştir.

### B1-30 — Albânî değerlendirmesindeki çift negatif

**Mevcut ifade:**
> ... sahih değildir ve bu sebeple delil olarak kullanılması doğru değildir.

**Önerilen düzeltme:**
> Albânî, rivâyeti zayıf hatta uydurma kabul ettiği için delil değeri taşımadığı sonucuna varmaktadır.

### B1-31 — Resm-i Osmânî'nin `sadece imlâ tercihi değil` tanımı

**Mevcut ifade:**
> Bu yazım sistemi, sadece bir imlâ tercihi değil, erken dönem Kur'an aktarımının yazıdaki sabitlenmiş hâlidir.

**Önerilen düzeltme:**
> Bu yazım sistemi, erken dönem Kur’an aktarımının yazılı biçimde sabitlenen tarihsel görünümünü temsil etmektedir.

### B1-32 — Resm farklılıklarının `gelişigüzel değil` diye tanımlanması

**Mevcut ifade:**
> Bu farklılıklar gelişigüzel değil, sistemli ve takip edilebilir bir yapı arz etmektedir.

**Önerilen düzeltme:**
> Bu farklılıklar kaynaklarda belirli başlıklar altında tasnif edilen düzenli yazım özellikleri olarak ele alınmıştır.

### B1-33 — Resm kurallarının işlev farklılığı

**Mevcut ifade:**
> ... bütün resm kuralları aynı derecede işlevsel değildir.

**Önerilen düzeltme:**
> Resm kurallarının kırâatlerle ilişkisi örneğe göre değişir.

### B1-34 — Hazfin `rastgele değildir` formülü

**Mevcut ifade:**
> Bu düşürme rastgele bir eksiltme değildir; erken mushaf yazım geleneğine bağlı, kurallı ve çoğu zaman hikmetli bir tercihtir.

**Önerilen düzeltme:**
> Hazf, lafızda bulunan bazı harflerin mushaf yazısında gösterilmemesidir. Bu özellik resm-i Osmânî'de düzenli biçimde görülen yazım uygulamalarından biridir. Bütün hazf örneklerinin aynı sebeple ortaya çıktığı veya kırâat farklılığını koruma amacı taşıdığı söylenemez; bazı örnekler erken yazı geleneğiyle açıklanırken bazı yazımlar rivâyetle sabit birden fazla okuyuşla bağdaşabilmektedir.

### B1-35 — Vaslın etkisinin negatif karşılaştırmayla verilmesi

**Mevcut ifade:**
> ... etkisi hazf kadar güçlü değildir.

**Önerilen düzeltme:**
> Vaslın kırâatlerle ilişkisi hazfe göre daha sınırlı görünmektedir.

### B1-36 — Geçerli okuyuşun `yazıya değil` diye açıklanması

**Mevcut ifade:**
> ... hangi okumanın geçerli olduğu yazıya değil, nakledilen kırâate ve bağlama bakılarak belirlendiğinden...

**Önerilen düzeltme:**
> Geçerli okuyuş nakledilen kırâat ve bağlam üzerinden belirlenir; vasl yazımı ise bazı örneklerde sınırlı bir yazılı imkân sunar.

### B1-37 — Faslın negatif tanımı

**Mevcut ifade:**
> Bu durum resm-i Osmânî'nin her durumda kelimeleri zorunlu olarak birleştiren bir yazı sistemi olmadığını göstermektedir.

**Önerilen düzeltme:**
> Fasl örnekleri, resm-i Osmânî'de kelime sınırlarının farklı biçimlerde gösterilebildiğini belirtir.

### B1-38 — Ziyâdenin `hazf kadar yaygın değildir` yapısı

**Mevcut ifade:**
> Ziyâde, hazf kadar yaygın görülen bir uygulama değildir.

**Önerilen düzeltme:**
> Ziyâde, hazfe kıyasla daha sınırlı görülen resm özelliklerinden biridir.

### B1-39 — 1.9.2'de resmin `yalnızca bir yazım biçimi değil` olarak tanımlanması

**Mevcut ifade:**
> ... resm-i Osmânî yalnızca bir yazım biçimi değil...

**Önerilen düzeltme:**
> Bazı mushaf yazımları rivâyetle sabit birden fazla okuyuşla bağdaşabilmektedir.

### B1-40 — `Resm-i Osmânî keyfî bir yazım değildir`

**Mevcut ifade:**
> Resm-i Osmânî, keyfî bir yazım değildir.

**Önerilen düzeltme:**
> Resm-i Osmânî, kaynaklarda belirli yazım özellikleri ve rivâyetlerle takip edilen tarihsel bir mushaf geleneği olarak ele alınmaktadır.

### B1-41 — `Yalnızca bir imlâ standardı değil`

**Mevcut ifade:**
> ... yalnızca bir imlâ standardı değil, aynı zamanda kırâat geleneğini muhafaza eden...

**Önerilen düzeltme:**
> Bazı mushaf yazımları, rivâyetle sabit birden fazla okuyuşla bağdaşabilecek bir harf yapısı sunmaktadır.

### B1-42 — `Amacı sadece yazım birliğini sağlamak değil`

**Mevcut ifade:**
> ... amacı sadece yazım birliğini sağlamak değil, sahâbeden gelen okuyuş geleneğini de korumaktır.

**Önerilen düzeltme:**
> Osmânî istinsahın yazılı birlik sağlaması ile bazı nakledilmiş okuyuşların resmle bağdaşabilmesi ayrı fakat ilişkili iki husustur.

### B1-43 — İbn Mücâhid tasnifinin `ilk defa ortaya çıkmış değildir`

**Mevcut ifade:**
> Ancak onun bu çalışması ilk defa ortaya çıkmış değildir.

**Önerilen düzeltme:**
> İbn Mücâhid'in tasnifi, kendisinden önce oluşan kırâat birikimini sistemleştiren önemli aşamalardan biridir.

### B1-44 — Ebû Ubeyde'de `re'y ile değil, rivâyetle`

**Mevcut ifade:**
> Ona göre kırâat, re'y ile değil, rivâyetle bilinen bir alandır.

**Önerilen düzeltme:**
> Ebû Ubeyde'nin yaklaşımında kırâatin dayanağı rivâyettir.

### B1-45 — Kabul ölçülerinin `sadece rivâyet zincirini değil`

**Mevcut ifade:**
> Bu âlimler, sahih kırâatlerin belirlenmesinde sadece rivâyet zincirini değil, aynı zamanda mushaf yazısının da dikkate alınması gerektiğini vurgulamışlardır.

**Önerilen düzeltme:**
> Bu âlimler, rivâyet zincirinin yanında mushaf yazısına uygunluğu da dikkate almışlardır.

### B1-46 — 1.10 mini-sonucundaki negatif tanım

**Mevcut ifade:**
> ... resm-i mushaf, klasik tefsîr ve kırâat geleneğinde sadece Kur'an'ın yazılı biçimi olarak değil, hangi okuyuşun kırâat kapsamında kabul edileceğini belirleyen bağlayıcı bir ölçü olarak işlev görmüştür.

**Karar:** **YAPISAL-OLARAK-ÇÖZÜLÜR.** Aşama 3 mini-sonuç taramasında bu paragraf ayrıca ele alınacaktır. İçerik korunacaksa:
> Klasik kırâat ve tefsîr geleneğinde resm-i mushaf, Kur’an'ın yazılı biçiminin yanında okuyuşların kabulünde başvurulan ölçülerden biri olarak işlev görmüştür.

# İkinci Bölüm

## 2.1 — Kırâat Kavramı

### B2-01 — `Sadece farklı okuma` / `yalnızca fonetik değil` zinciri

**Mevcut ifadeler:**
> Ancak kırâat sadece “farklı okuma” anlamına gelmemektedir.
>
> ... yalnızca fonetik okuyuşları içine alan bir mesele değil, aynı zamanda...

**Önerilen düzeltme:**
> Kırâat, Kur’an kelimelerinin edâ biçimlerini ve bu biçimlerdeki farklılıkların rivâyetini konu edinen geniş bir ilim alanıdır.

### B2-02 — `Dilde mümkün olan her okuyuş değil`

**Mevcut ifade:**
> Dolayısıyla kırâat, dilde mümkün olan her okuyuş değil, güvenilir yollarla aktarılan ve Kur'an kırâati içinde yer bulan okuyuş olarak değerlendirilmiştir.

**Önerilen düzeltme:**
> Kırâat, güvenilir yollarla nakledilmiş ve kırâat geleneği içinde yer bulmuş okuyuşları ifade eder.

### B2-03 — Kur’an'ın `sadece yazıya geçirilmiş metin` karşıtlığı

**Mevcut ifade:**
> Kur'an sadece yazıya geçirilmiş bir metinden ibaret olmayıp, aynı zamanda okunarak aktarılan bir kitaptır.

**Önerilen düzeltme:**
> Kur’an'ın aktarımında yazılı metne, okunarak öğretilen sözlü edâ geleneği eşlik etmiştir.

### B2-04 — Kırâat ilminin amacında negatif tanım

**Mevcut ifade:**
> ... kırâat ilmi sadece farklılıkları kaydetmek için ortaya çıkmamıştır; asıl amacı sahih okuyuşu sahih olmayanından ayırt etmektir.

**Önerilen düzeltme:**
> Kırâat ilmi, farklı okuyuşları kaydetmenin yanında sahih kabul edilen okuyuşları diğerlerinden ayırmaya yönelik ölçüler de geliştirmiştir.

## 2.2 — Rivâyet, Sened ve Otorite

### B2-05 — 2.2 açılışındaki `sadece ... değil`

**Mevcut ifade:**
> Kırâat ilmini anlamanın en sağlam yollarından biri, onu sadece “farklı okuyuşlar” meselesi olarak değil, rivâyet, sened ve ilmî otorite üzerine kurulmuş bir aktarım düzeni olarak ele almaktır.

**Önerilen düzeltme:**
> Kırâat ilmi, okuyuş farklılıklarını rivâyet, sened ve ilmî otorite üzerinden takip eden bir aktarım düzenidir. Temel soru, bir okuyuşun nasıl nakledildiği, kimden alındığı ve hangi ölçülerle kabul gördüğüdür.

### B2-06 — Rivâyetin negatif tanımı

**Mevcut yapılar:**
> Kırâat yalnızca ... değildir.
>
> Temel soru ... değil...

**Önerilen düzeltme:**
> Rivâyet, bir okuyuşun kimden alındığını, nasıl aktarıldığını ve hangi yollarla güven kazandığını gösteren aktarım hattıdır. Bir okuyuşun kırâat sayılması için dil bakımından mümkün olması yeterli görülmez; güvenilir bir nakil hattına dayanması gerekir.

### B2-07 — Mekkî b. Ebû Tâlib'de `re'y ile değil`

**Mevcut ifade:**
> ... re'y ile değil, telakki ve semâ yoluyla...

**Önerilen düzeltme:**
> Mekkî b. Ebû Tâlib, kırâatlerin telakki ve semâ yoluyla öğrenildiğini vurgular.

### B2-08 — `Baştan itibaren yazılı değil`

**Mevcut ifade:**
> Bu durum kırâat ilminin baştan itibaren yazılı değil, birebir öğretim geleneği içinde geliştiğini göstermektedir.

**Önerilen düzeltme:**
> Kırâatlerin aktarımında aslî zemin telakki, müşâfehe ve edâya dayanan sözlü rivâyettir. Kur’an'ın yazılı kaydı ve mushaf geleneği ise rivâyet edilen okuyuşların müşterek metinle ilişkisini gösteren tamamlayıcı bir çerçeve sağlamıştır.

### B2-09 — `Kitap sayfasında duran teori değil`

**Mevcut ifade:**
> Kırâat ... kitap sayfasında duran bir teori değil...

**Önerilen düzeltme:**
> Kırâat, hocadan alınan, talebenin uygulamayla öğrendiği ve aynı aktarım disiplini içinde sonraki nesle naklettiği bir ilimdir.

### B2-10 — `Sadece harfleri değil / sadece metin aktarımı değil`

**Mevcut yapılar:**
> ... nakledilen şey sadece kelimenin harfleri değil...
>
> Rivâyet sadece metin aktarımı değil...

**Önerilen düzeltme:**
> Rivâyette kelimenin harfleriyle birlikte ses değeri ve edâ biçimi de aktarılır.

### B2-11 — Senedin `tali ayrıntı değil` diye tanımlanması

**Mevcut yapı:**
> ... bir alan değildir ... tali ayrıntı değil...

**Önerilen düzeltme:**
> Kırâat ilmi, okuyuş biçimleriyle birlikte bu okuyuşların kimden alındığını, hangi yolla aktarıldığını ve nakil güvenilirliğini de inceler. Bu nedenle sened, ilmin temel unsurlarından biridir.

### B2-12 — Âsım kırâatinin negatif açıklaması

**Mevcut ifade:**
> Mesela “Âsım kırâati” denildiğinde burada sadece Âsım'ın tercih ettiği okuyuş biçimi değil...

**Önerilen düzeltme:**
> Mesela “Âsım kırâati” denildiğinde Âsım'a nispet edilen okuyuş bütünü ile bu okuyuşun Hafs ve Şu‘be gibi râviler aracılığıyla sonraki nesillere nasıl aktarıldığı birlikte anlaşılır. Bu nispet, ilgili rivâyet ve öğretim geleneğinin Âsım'ın adı etrafında tanınıp nakledildiğine işaret eder.

### B2-13 — `Yalnızca lafızla değil / rey ile değil`

**Mevcut yapılar:**
> ... yalnızca lafızla değil...
>
> ... rey ile değil, nakille...

**Önerilen düzeltme:**
> Bu tanım, lafzın yanı sıra onun güvenilir aktarımını da merkeze alır. Ebû Şâme de kırâat bilgisinin nakle dayandığını vurgular.

### B2-14 — Sened ve Hafs rivâyetinde negatif tanımlar

**Mevcut yapılar:**
> Sened sadece genel bir silsile değil...
>
> Hafs rivâyeti ... tek tip ... değil...

**Önerilen düzeltme:**
> Sened, imam-râvi-tarîk ayrımıyla ayrıntılanan çok katmanlı bir aktarım düzenidir. “Hafs rivâyeti” ifadesi de râviden sonraki farklı tarîkleri içeren bu nakil yapısı içinde anlaşılmalıdır.

### B2-15 — Otoritenin negatif formüllerle kurulması

**Mevcut yapılar:**
> Kırâat ilmi ... sadece farklılıkları kaydeden alan değil...
>
> Bu dönemde sadece okuyuşu bilen kimseler değil...
>
> ... sadece râvi değil...
>
> ... şahsî kanaatlerinden değil...
>
> ... yalnız kendi dönemlerinde değil...

**Önerilen düzeltme:**
> Kırâat ilmi, farklı okuyuşları kaydetmenin yanında bunların güvenilirlik, kabul ve öğretim otoritesini de değerlendiren köklü bir ilim geleneğidir. Bu dönemde okuyuşu bilen kurrânın yanı sıra belirli öğretim geleneklerini temsil eden imamlar öne çıkmıştır. İbn Âmir, İbn Kesîr, Âsım, Ebû Amr, Hamza, Nâfi‘ ve Kisâî gibi isimler rivâyet ve öğretim geleneklerinin merkezî imamları hâline gelmiştir. Otoriteleri güvenilir hocalardan okuyuş almaları, talebe yetiştirmeleri ve okuyuşlarının ilmî çevrelerde kabul görmesiyle ilişkilidir.

## 2.3–2.4 — Yedi harf, kırâat ve tefsîr

### B2-16 — Osmânî istinsahın `yalnızca yazım birliği değildir` formülü

**Mevcut yapı:**
> ... yalnızca yazım birliğini sağlama işi değildir...
>
> ... yalnızca mevcut metni çoğaltmak için değil...

**Önerilen düzeltme:**
> Osmânî istinsah, müşterek mushafların çoğaltılmasıyla birlikte okuyuş ihtilaflarını ortak bir yazılı çerçeveye bağlayan tarihsel bir uygulama olarak değerlendirilmiştir.

### B2-17 — Birinci yedi harf görüşündeki negatif kalıplar

**Mevcut yapılar:**
> ... yedi harfin tamamı üzerine değil...
>
> ... Kur'an'ın terk edilmesine değil...
>
> ... “daraltma” değil koruma ve birleştirme...

**Önerilen düzeltme:**
> Bir görüşe göre Hz. Osman, ümmeti ihtilafı azaltacak müşterek bir harf etrafında toplamıştır. Taberî bu uygulamayı Kur’an'ın korunmasına ve ümmetin müşterek bir harf etrafında toplanmasına yönelik bir tedbir olarak değerlendirir. İbn Abdilberr'e nispet edilen değerlendirme de uygulamanın koruma ve birleştirme yönünü öne çıkarır.

### B2-18 — İkinci yedi harf görüşündeki `tamamını değil`

**Mevcut ifade:**
> ... Osmânî mushafın yedi harfin tamamını değil, onlardan mushaf yazısının kaldırabildiği kısmı koruduğu...

**Önerilen düzeltme:**
> Başka bir görüş, Osmânî mushafların yedi harfle ilişkisini mushaf yazısının taşıyabildiği vecihlerin korunması üzerinden açıklamaktadır.

### B2-19 — Yedi harf bölümünün bilimsel nihai sentezi

**Karar:** Bu bölümdeki çok sayıdaki `değil` cümlesi Fourth Report V2’de daha kapsamlı ve bilimsel bir paragrafla değiştirilmiştir. Nihai Fifth Report’ta aşağıdaki çekirdek esas alınacaktır:
> Osmânî mushaflarla yedi harf arasındaki ilişkinin nasıl anlaşılacağı konusunda klasik kaynaklarda farklı görüşler bulunmaktadır. Bir kısım âlimler Hz. Osman'ın ümmeti belirli bir harf üzerinde topladığını, bir kısmı ise mushaf resminin taşıdığı ölçüde birden fazla vechin korunduğunu ifade etmiştir. Bu görüşlerin her biri kendi kaynak ve yorum bağlamı içinde değerlendirilmelidir. Kırâatlerin aktarımında telakki ve rivâyet belirleyici olmaya devam etmiş; resm ise nakledilen okuyuşların ortak mushaf yazısıyla bağdaşma sınırını göstermiştir.

### B2-20 — 2.4'teki negatif anlatım zinciri

**Mevcut yapılar:**
> Artık mesele farklı kırâatlerin bulunması değil...
>
> ... sadece kırâat ilmini değil, tefsîr ilmini...
>
> ... şahsî sahife ... değil...
>
> ... kırâat farklılıklarının tümü değil...
>
> ... artık Kur'an kırâati değil...
>
> Zemahşerî ... sadece bir rivâyet meselesi olarak değil...
>
> ... yoruma karşı değil...
>
> ... sınırlayan değil...
>
> ... tefsîr geleneğinin dağılmasını değil...
>
> Tefsîr, sadece bir anlam açıklaması değil...

**Önerilen düzeltme:**
> Bu aşamada odak, farklı kırâatlerin müşterek mushaf çerçevesi içindeki konumunun değerlendirilmesine kaymıştır. Mushaf yazısının ortaklaşması kırâat ilminin yanında tefsîr çalışmalarının metinsel zeminini de etkilemiştir. Hz. Osman döneminden sonra müfessirlerin temel yazılı başvuru zemini müşterek mushaf hattı olmuştur. Tefsirde esas alınan kırâatler, sahih rivâyetle nakledilen ve mushaf hattıyla bağdaşan okuyuşlar arasından değerlendirilmiş; sahih kırâat şartlarını taşımadığı kabul edilen bazı rivâyetler ise açıklayıcı veya tefsirî malzeme olarak kullanılmıştır. Zemahşerî ve başka müfessirler kırâat farklılıklarını rivâyet boyutunun yanında belâgat ve nahiv açısından da ele almıştır. Müşterek mushaf hattı, bu yorumların üzerinde yürütüldüğü ortak yazılı zemini sağlamıştır.

# Üçüncü Bölüm

## 3.1 — Çoklu kırâat ve resm

### B3-01 — Resmin `sıradan yazım değil` diye tanımlanması

**Mevcut ifade:**
> ... resm-i Osmânî'nin sıradan bir yazım biçimi değil, kırâatlerin rivâyetini koruyan özel bir sistem olduğunu...

**Önerilen düzeltme:**
> Bazı resm biçimleri, rivâyetle sabit birden fazla kırâatle bağdaşabilmesi bakımından kırâat-resm ilişkisini incelemek için önemli örnekler sunmaktadır.

### B3-02 — Şehir mushaflarındaki farklı resmlerin negatif cümlesi

**Mevcut yapı:**
> ... hepsinde aynı biçimde değil, farklı mushaflarda farklı resmlerle...

**Önerilen düzeltme:**
> Bazı kelimeler, farklı Osman mushaflarında farklı resmlerle nakledilmiştir.

Bu kullanım önceki Aşama 4’te `KEEP` sayılmıştı; Fifth Report’ta anlam korunarak olumlu yapıya çevrilmiştir.

## 3.2 — Lehçe yorumları

### B3-03 — `Yalnızca bir yazım biçimi değildir`

**Mevcut ifade:**
> Resm-i Osmânî yalnızca bir yazım biçimi değildir.

**Önerilen düzeltme:**
> Resm-i Osmânî, tarihsel mushaf yazımının yanında erken Arap dili ve kırâat rivâyetleriyle ilişkili veriler de taşımaktadır.

### B3-04 — `Sadece yazım farkı değil, lehçe izi`

**Mevcut yapı:**
> ... sadece yazım farkı olarak değerlendirilmemiş, lehçe izi olarak...

**Önerilen düzeltme:**
> Bazı klasik açıklamalarda açık “ta” ile yazılan örnekler lehçe özellikleriyle ilişkilendirilmiştir.

### B3-05 — Standart dil / tarihî çeşitlilik karşıtlıkları

**Mevcut yapılar:**
> ... yalnız standart dil kurallarını değil...
>
> ... gelişigüzel değil...
>
> ... dil malzemesini sadeleştiren değil...

**Önerilen düzeltme:**
> Bu yorumlarda mushaf yazısının standartlaşan dil kurallarıyla birlikte erken Arapçaya nispet edilen bazı özellikleri de yansıttığı kabul edilmiştir. İlgili yazım farklılıkları erken dil kullanımlarıyla açıklanmaya çalışılmış; resm-i Osmânî tarihî dil çeşitliliğine ait bazı izleri koruyan bir yazım geleneği olarak değerlendirilmiştir.

### B3-06 — `Amacı sadece kelimeyi açık yazmak değil`

**Mevcut ifade:**
> ... amacı sadece kelimeyi en açık biçimde yazmak değil...

**Önerilen düzeltme:**
> Kıyasî imlâ ile resm-i Osmânî arasındaki fark, bazı lehçe ve kırâat özelliklerinin tarihsel mushaf yazısında görünür kalmasıyla ilişkilendirilmiştir.

## 3.3 — Harekenin/harfin aslı

### B3-07 — `Teknik imlâ sistemi değildir`

**Mevcut ifade:**
> Resm-i Osmânî, Kur'an lafzını yalnızca yazıyla sabitleyen teknik bir imlâ sistemi değildir...

**Önerilen düzeltme:**
> Resm-i Osmânî, Kur’an lafzının tarihsel yazım biçimi olarak kırâat ve dil özellikleriyle birlikte değerlendirilmiştir.

### B3-08 — `Sadece o andaki telaffuz değil` ve `sadece sesin biçimi değil`

**Önerilen düzeltme:**
> Bazı kaynaklar, belirli yazımların telaffuzun yanında harf veya harekenin kökensel yapısıyla da ilişkilendirildiğini belirtmektedir. Bu yorumda yazı, ses biçiminin yanında kelimenin tarihî ve sarfî yapısıyla da ilişkilendirilmektedir.

### B3-09 — `Amaç yalnızca okuyuşu kaydetmek değil`

**Önerilen düzeltme:**
> Bu açıklamada yazım, okuyuşun yanında harekenin yapısal kökeniyle de ilişkilendirilmektedir.

### B3-10 — `Kârî sadece yazıma bakarak değil`

**Önerilen düzeltme:**
> Doğru edâ, kârînin hocadan telakki ettiği rivâyet yoluyla öğrenilir; resm ise belirli örneklerde bu aktarımı destekleyen yazılı veriler sunar.

### B3-11 — `Ne tamamen ... ne de ...`

**Önerilen düzeltme:**
> Resm, ses değerlerinin bir kısmını açıkça gösterirken bir kısmını telakki ve rivâyete bırakan tarihsel bir yazım yapısına sahiptir.

### B3-12 — `Harekenin değil, harfin aslını` ve `yalnızca iskeleti değil`

**Önerilen düzeltme:**
> Bu örnekler kaynaklarda çoğunlukla harfin aslını gösteren yazımlar arasında ele alınır. Bazı klasik yorumlarda resm, kelimenin harf iskeletiyle birlikte yapısal kökenine dair işaretler de taşır.

## 3.4–3.6 — Mana/hikmet, vasl-fasl ve eleştirel yaklaşımlar

### B3-13 — Hazf ve ziyâdeye yüklenen anlamlarda negatif tekrarlar

**Mevcut yapılar:**
> ... sıradan bir gelişten değil...
>
> ... sadece harf düşmesi değil...
>
> ... yalnızca kelimenin nasıl okunacağını gösteren unsur değildir...
>
> ... sadece tek imlâ farklılıkları üzerinden okumak yeterli değildir...
>
> ... tamamı her âlim tarafından ... değildir.

**Önerilen düzeltme:**
> Bazı klasik müellifler, hazf ve ziyâde gibi yazım biçimleriyle kelimenin anlamı veya bağlamı arasında yorum ilişkileri kurmuştur. Merrâkuşî'nin bazı açıklamalarında hazf fiilin sürati, kolaylığı veya etkisinin çabuk gerçekleşmesiyle; bazı ziyâde örnekleri ise hitabın kuvveti veya anlam vurgusuyla ilişkilendirilmiştir. Bu yorumların kapsamı ve ağırlığı müellifler arasında değişmektedir. İlgili açıklamalar klasik yorumlar olarak aktarılmalı; resmin bütünü için genel bir “anlam işaretleme sistemi” sonucuna dönüştürülmemelidir.

### B3-14 — 3.5'teki vasl-fasl negatif zinciri

**Mevcut yapılar:**
> Bu yazım farkı yalnızca yazıma dair bir tercih değildir...
>
> ... yeni bir soru değil...
>
> cevabı “evet” veya “hayır” değil...
>
> yüzüstü ... kimsenin değil...
>
> ... yalnız görünüşe ait bir farklılık olmaktan çıkmakta...

**Önerilen düzeltme:**
> Bazı klasik açıklamalarda vasl ve fasl farkı, nahivsel işlev ve anlam ilişkileriyle birlikte yorumlanmıştır. İlgili istifham yapısı iki hâl arasında mukayese ve tercih kurmakta; cevap da iki seçenekten hangisinin kastedildiğini belirlemektedir. Âyet, yüzüstü yürüyen kimse ile dosdoğru yol üzerinde yürüyen kimseyi karşılaştırır ve ikinci durumu doğru yol ile ilişkilendirir. Bu yorumlar, vasl ve fasl biçimlerinin dil ve tefsir değerlendirmelerinde nasıl kullanıldığını gösterir; tarihsel yazım sebebi ayrıca ele alınmalıdır.

### B3-15 — 3.6'da nahivcilerin `sıradan imlâ mirası değildir` formülü

**Mevcut ifade:**
> Nahiv âlimleri için resm-i mushaf sadece sıradan bir imlâ mirası değildir.

**Önerilen düzeltme:**
> Nahiv âlimleri mushaf hattını, dilin mümkün gördüğü vecihler arasında değerlendirmeye katılan yazılı verilerden biri olarak kullanmıştır.

### B3-16 — İbn Haldûn paragrafındaki negatif hükümler

**Mevcut yapılar:**
> ... tam sağlamlık ... ulaşmış değildir...
>
> ... ilmî zaruretten değil...
>
> ... ilmî değil keyfî...

**Önerilen düzeltme:**
> İbn Haldûn, erken Arap yazısını henüz gelişme aşamasında bulunan bir yazı geleneği olarak tasvir eder. Mushaf yazımındaki bazı farklılıkları erken yazının tarihsel şartlarıyla ilişkilendirir ve sonraki bazı hikmet açıklamalarını sahâbeyi yazı konusundaki eksiklikten tenzih etme eğilimiyle bağlantılı görerek eleştirir.

### B3-17 — İbn Haldûn'a cevapların negatif savunma dili

**Mevcut yapılar:**
> ... resm-i mushaf'ı sadece tarihî bir yazım biçimi olarak değil...
>
> ... mümkün değildir...

**Önerilen düzeltme:**
> Sonraki resm literatüründe İbn Haldûn'un görüşüne, resmin sahâbe uygulamasıyla nakledilmesi, mushaf geleneğindeki süreklilik ve bağlayıcılık düşüncesi üzerinden çeşitli cevaplar verilmiştir. Bu cevaplar normatif bağlılığın gerekçelerini açıklamak bakımından önemlidir; erken yazım biçimlerinin tarihsel sebebini tek başına belirleyen kanıtlar olarak kullanılmamalıdır.

### B3-18 — Debbâğ ve hikmet yorumlarındaki negatif formüller

**Mevcut yapılar:**
> ... sadece teknik yazım farklılıkları sayılmaması...
>
> ... rastgele imlâ ayrıntıları değildir...

**Önerilen düzeltme:**
> Debbâğ'a nispet edilen görüş, kıyasa aykırı görünen bazı yazım özelliklerini mana incelikleri ve bağlamsal işaretlerle ilişkilendirir. Bu açıklamalar ilgili müellifin yorumları olarak aktarılmalıdır.

### B3-19 — 3.6 kapanışında tarihsel/normatif düzeylerin negatif ayrımı

**Önerilen düzeltme:**
> Resm-i mushaf tartışmaları tarihsel köken, sonraki bağlayıcılık ve yazım özelliklerine yüklenen anlam/hikmet yorumları olmak üzere ayrı düzeylerde ele alınmalıdır. Normatif bağlılık, her yazım ayrıntısına özel bir hikmet veya mucizevî anlam yüklemeyi gerektirmez.

## 3.7–3.12 — Yapısal olarak Fourth Report V2 tarafından değiştirilecek alan

Bu altı başlıkta çok sayıda kırmızı `değil/değildir`, `yalnız/sadece ... değil`, `ne ... ne de ...` yapısı bulunmaktadır. Fifth Report burada cümle cümle rakip çözümler üretmeyecektir; çünkü Fourth Report V2 bu alanı **“Resm-i Osmânî'ye Bağlılığın Gerekçeleri ve Sınırları”** başlığı altında yeniden kurmaktadır. Mevcut negatif yapılar arasında şunlar bulunmaktadır:

> resm-i Osmânî'ye bağlılık, sadece tarihî bir sadakat olarak değil...
>
> mushafın insanların sonradan geliştirdiği imlâ ile değil...
>
> manevi yorum klasik muhafaza çizgisinden tamamen kopuk değildir...
>
> teknik imkânlar ... tasfiye etmek için değil...
>
> yazının değeri, sadece görsel biçiminden ibaret değil...
>
> Arap dili ve yazı esaslarını bilmek ... tek başına yeterli değildir...
>
> hadis lafzı olarak değil, ilmî bir kaide olarak...
>
> olumsuz güçlük olarak değil, bilinçli yönlendirme...
>
> Kur'an sadece yazıya geçirilmiş bir kitap olmayıp...
>
> burada söz konusu olan şey yalnızca harflerin nasıl yazıldığı meselesi değildir...
>
> kaygı sadece görsel çeşitlilik değildir...
>
> ümmetin birliği yalnızca yazı birliğine indirgenebilecek dar bir mesele değildir...
>
> ne tek başına yeterli bir birlik ilkesi ne de önemsiz bir yazım ayrıntısı...

**Fifth Report için bağlayıcı yeni çekirdek:**
> Osmânî mushafların müşterek yazılı gelenek hâline gelmesi, resme bağlılığın tarihsel ve normatif zeminini oluşturmuştur. Kur’an'ın okunma biçimi telakki, müşâfehe, edâ ve isnad yoluyla aktarılmış; resm-i Osmânî bu sözlü aktarımın müşterek yazılı çerçevesi olarak işlev görmüştür. Klasik resm literatürü, tarihsel yazım rivâyetlerini ve şehir mushaflarına nispet edilen farklılıkları koruyan bir bilgi birikimi sunmaktadır. Bu literatürün devamlılığı, her yazım ayrıntısına özel bir teolojik anlam yüklenmesini gerektirmez. Resme bağlılığın birlik ve ortak hafıza boyutu ise yazının ümmet birliğini tek başına kurduğu iddiası yerine, müşterek mushaf geleneğinin tarihî ve kültürel sürekliliğe katkısı şeklinde ifade edilmelidir.

Bu karar, söz konusu altı başlıktaki kırmızı negatif yapıların Fourth Report’un bilimsel revizyonuyla çelişen ayrı ayrı cümle önerilerine dönüşmesini engeller.

# Dördüncü Bölüm

## 4.1 — Tespit ve tahdit

### B4-01 — Resmin `asıl kaynak görülmeyip` diye tanımlanması

**Mevcut ifade:**
> ... resm-i Osmânî, kırâatlerin asıl kaynağı olarak görülmeyip...

**Önerilen düzeltme:**
> Kırâatlerin asıl kaynağı rivâyettir; resm-i Osmânî ise sahih rivâyetlerin müşterek mushaf yazısıyla ilişkisini değerlendirmede tamamlayıcı bir unsurdur.

### B4-02 — `Asıl dayanak mushaf nüshaları değil`

**Mevcut ifade:**
> ... kırâat vecihlerinin naklinde asıl dayanağın mushaf nüshaları değil, telakki ve müşâfehe olduğunu...

**Önerilen düzeltme:**
> Kırâat vecihlerinin naklinde aslî dayanak telakki ve müşâfehedir; mushaf nüshaları bu sözlü öğretimin yazılı çerçevesini sağlar.

### B4-03 — Uygunluğun `mutlak birebir eşleşme olmayıp`

**Önerilen düzeltme:**
> Mushaf ile bölgesel okuyuş arasındaki uygunluk her örnekte birebir gerçekleşmez; kaynaklar bazı durumlarda çoğunluğa dayalı veya ihtimalî bir bağdaşmadan söz etmektedir.

### B4-04 — Mushaf ve mukrî birlikteliğinin `yalnız ... değil`

**Mevcut ifade:**
> ... Hz. Osman'ın mushafları yalnız metin birliğini sağlamak için göndermediğini, aynı zamanda ... muallimleri tayin ederek...

**Önerilen düzeltme:**
> Hz. Osman'ın mushaflarla birlikte mukrîler göndermesi, yazılı nüsha ile öğretim faaliyetinin birlikte yürütüldüğünü belirtmektedir.

### B4-05 — Mushafların `yalnız ilmî değil, tarihî` değeri

**Önerilen düzeltme:**
> Bu mushaflar ilmî başvuru değerinin yanında tarihî ve sembolik önem de kazanmıştır.

## 4.2 — Sahâbe mushafları

### B4-06 — Geçmişte var olan rivâyet / müşterek mushaf karşıtlığı

**Mevcut ifade:**
> ... esas alınan şey, sadece bir rivâyetin geçmişte var olmuş olması değil, ümmetin ... hangi lafız üzerinde birleştiğidir.

**Önerilen düzeltme:**
> Değerlendirmede, bir rivâyetin geçmişteki varlığının yanında müşterek mushaf metnindeki konumu da dikkate alınmıştır.

### B4-07 — Sahâbe nakline güvensizlik karşıtlığı

**Mevcut ifade:**
> ... ortak mushafın dışında bırakılması, sahâbenin nakline güvensizlikten değil...

**Önerilen düzeltme:**
> Sahâbe mushaflarındaki farklı rivâyetlerin müşterek mushafın dışında kalması, sonraki normatif mushaf otoritesinin Osmânî istinsah etrafında şekillenmesiyle ilişkilendirilmelidir.

### B4-08 — `Ortadan kaldırılan şey Kur'an'ın kendisi olmayıp`

**Önerilen düzeltme:**
> Tedavülden kaldırılan nüshalar, müşterek mushaf otoritesi dışında kalan şahsî sahife ve mushaflardır.

### B4-09 — `Yalnız yeni mushaf göndermekten ibaret değildir`

**Önerilen düzeltme:**
> Hz. Osman dönemindeki uygulama, müşterek mushafların çoğaltılmasıyla birlikte bunların dışında dolaşan şahsî nüshaların tedavülden kaldırılmasını da kapsamıştır.

### B4-10 — `Şahsî ve tek taraflı karar olarak görülmediğini`

**Önerilen düzeltme:**
> Hz. Ali'ye nispet edilen söz, uygulamanın sahâbenin genel mutabakatıyla ilişkilendirildiğini belirtmektedir.

### B4-11 — `Sadece halifenin idarî tercihi olmayıp`

**Önerilen düzeltme:**
> Bu aktarımda resm-i Osmânî, halifenin idarî kararının yanında sahâbenin fiilî mutabakatıyla güçlenen müşterek mushaf otoritesi olarak sunulmaktadır.

## 4.3–4.4 — Kabul, tercih, tevcîh ve vakıf

### B4-12 — İmamların tercihlerini negatif kalıplarla açıklayan küme

**Mevcut yapılar:**
> ... meselenin yalnız râvi sayısıyla ilgili olmadığını...
>
> ... nakledilmiş olmasıyla sınırlı değildir...
>
> ... serbest seçimler değildir...

**Önerilen düzeltme:**
> Mekkî'nin yorumunda kırâat tercihinde râvi sayısının yanı sıra mushaf hattı ve genel kabul de dikkate alınmaktadır. İmamların tercihleri, kendilerine ulaşan rivâyet ve öğretim geleneği içinde değerlendirilmelidir.

### B4-13 — Dil ve resm ilişkisindeki negatif tanımlar

**Mevcut yapılar:**
> dil mutlak hâkim unsur ... değildir...
>
> resm ... dili dışlayan ... olmaktan öte...

**Önerilen düzeltme:**
> Bu kaynaklarda dil verileri, mushaf hattı ve rivâyetle birlikte değerlendirilmektedir. Resm verisi, dilsel ihtimallerin müşterek mushaf çerçevesi içindeki konumunu belirlemeye katkı sağlar.

### B4-14 — `Resm sadece kabul şartı değildir`

**Önerilen düzeltme:**
> Resm verisi bazı kaynaklarda kabul ölçüsünün yanında tercih ve tevcîh gerekçesi olarak da kullanılmaktadır.

### B4-15 — Zeccâc, Semîn el-Halebî ve İbn Hâleveyh kümesi

**Önerilen düzeltme:**
> Zeccâc, Semîn el-Halebî ve İbn Hâleveyh'in bazı açıklamalarında mushaf hattı, belirli okuyuşların tercihi veya tevcîhi için başvurulan verilerden biri olarak kullanılmaktadır. Bu kullanım, rivâyetin yerine geçen bağımsız bir ölçü anlamına gelmez; resm, nakil ve dil verileriyle birlikte değerlendirilir.

### B4-16 — Vakıf alanındaki negatif kalıplar

**Mevcut yapılar:**
> ... yalnız kırâat vecihlerinin kabulü ... sınırlı kalmamış...
>
> vakıf ... sadece ses icrasıyla ilgili ... değil...

**Önerilen düzeltme:**
> Resm verisinin kullanıldığı alanlar arasında bazı vakıf ve edâ uygulamaları da bulunmaktadır. Vakıf ve ibtidâ öncelikle mana, nahiv ve rivâyetle ilişkilidir; vasl-fasl ve kelime sınırları gibi bazı yazım özellikleri belirli örneklerde ek veri sağlar.

## 4.5 — Resm rivâyetleri ve yazım özellikleri

### B4-17 — `Hiçbir şey hikmetsiz değildir` görüşü

**Mevcut ifade:**
> ... onun yazdığı hiçbir şey hikmetsiz ve ince bir illetten yoksun değildir.

**Karar:** Bu ifade kaynakta bir görüş olarak aktarılmaktadır. Yazarın genel hükmüne dönüştürülmemelidir.

**Önerilen düzeltme:**
> Bazı resm müellifleri Zeyd b. Sâbit'e nispet edilen yazım özelliklerine hikmet açıklamaları yüklemiştir. Bu yorumlar ilgili müelliflere nispet edilerek aktarılmalıdır.

### B4-18 — Ebû Amr'da `kendi bölgesindeki mushaf değil`

**Önerilen düzeltme:**
> Ebû Amr, söz konusu okuyuşunu Medine mushaflarında gördüğü yazımla ilişkilendirmiştir.

### B4-19 — `İlişkinin tek boyutlu olmadığı`

**Önerilen düzeltme:**
> Bu rivâyet, kırâat ile mushaf resminin birden fazla merkezdeki yazım rivâyetleri üzerinden ilişkilendirilebildiğini belirtmektedir.

### B4-20 — Resm rivâyetlerinin `tali veri değildir` biçiminde tanımlanması

**Önerilen düzeltme:**
> Resm rivâyetleri, mushaf kelimelerinin hangi biçimde yazıldığını ve şehir mushafları arasında nakledilen farklılıkları belirlemek bakımından önemlidir. Bu veriler kırâatlerin rivâyet kaynağının yerine geçmez; okuyuşların yazılı mushaf geleneğiyle ilişkisini değerlendirmeye imkân veren tamamlayıcı malzeme sunar.

### B4-21 — el-Kürdî'de `hakikatte esaslı ihtilaf değildir`

**Önerilen düzeltme:**
> Muhammed Tâhir el-Kürdî bu farklılıkları, kırâat vecihlerindeki gerçek okuyuş farkından ayrılan görünüşe ilişkin yazım farkları olarak değerlendirmektedir.

### B4-22 — `İhtilaf üretmeye yönelik unsur olmaktan çok`

**Önerilen düzeltme:**
> Kaynaklarda bazı şehir mushafı farklılıkları, ayrı okuyuşların farklı yazılı biçimlerle ilişkilendirilmesi çerçevesinde açıklanmıştır.

### B4-23 — `Kaba sınırlama değildir`

**Önerilen düzeltme:**
> Aynı yazım biçiminin rivâyetle sabit birden fazla okuyuşla bağdaşabildiği örnekler de bulunmaktadır.

## 4.6–4.7 — Modern neşir

### B4-24 — `Mesele sadece geçmişten kalan yazıyı tekrarlamak değildir`

**Önerilen düzeltme:**
> Çağdaş neşirlerde resm-i Osmânî'nin esas alınması, klasik resm rivâyetlerinin modern üretim süreçlerine aktarılmasıyla ilişkilidir.

### B4-25 — `Şahsî kanaatlere göre değil`

**Önerilen düzeltme:**
> Modern mushaf neşrinde yazım tercihleri Dânî ve Ebû Dâvud gibi klasik resm kaynakları esas alınarak ilmî bir yöntem içinde belirlenmiştir.

### B4-26 — `İhtisardan maksat yüzeysel kısaltma değildir`

**Önerilen düzeltme:**
> Eserdeki ihtisar, tefsîr, ahkâm ve i‘râb bahislerinin ayıklanarak resm meselesine yoğunlaşılması şeklinde gerçekleştirilmiştir.

### B4-27 — Mushaf istinsahının `yalnız çoğaltma faaliyeti değildir` biçimi

**Önerilen düzeltme:**
> Mushaf istinsahı tarih boyunca çoğaltma faaliyetiyle birlikte hat ve yazı geleneği içinde gelişmiştir.

### B4-28 — Türkiye'de basımın `sadece teknik matbaa işi değildir` biçimi

**Önerilen düzeltme:**
> Türkiye'de mushaf basımı, teknik üretimin yanında ilmî ve dinî denetime tabi özel bir neşir alanı olarak düzenlenmiştir.

### B4-29 — Türkiye basım tarihinin `sadece kurumlar ve izinler` karşıtlığı

**Önerilen düzeltme:**
> Türkiye'deki mushaf basım tarihi, kurum ve izin süreçlerinin yanında imlâ tercihlerinin tarihî seyri bakımından da incelenmelidir.

# Sonuç

## S-01 — Osmânî istinsahın `yeni metin değildir` yapısı

**Mevcut yapı:**
> ... istinsahın yeni bir Kur'an metni oluşturma girişimi olmadığını...

**Önerilen düzeltme:**
> Mevcut veriler, Osmânî istinsahı ortak başvuru mushaflarının çoğaltılması ve şahsî nüshalardan doğabilecek ihtilafların sınırlandırılması yönünde bir tedbir olarak sunmaktadır.

## S-02 — Yazı ihtimali ile sahihlik ayrımı

**Mevcut ifade:**
> Yazının bir okuyuşu mümkün kılması, o okuyuşun sahih olduğunu göstermemektedir.

**Önerilen düzeltme:**
> Yazının bir okuyuşla bağdaşması yalnız yazılı uygunluğu gösterir; okuyuşun sahihliği telakki, isnad ve edâ yoluyla belirlenir.

## S-03 — `Resme uygunluk tek başına yeterli değildir`

**Önerilen düzeltme:**
> Kırâatlerin kabulünde rivâyetin güvenilirliği, Arap dilinde bir veche sahip olması ve resm-i Osmânî'ye uygunluk birlikte değerlendirilir.

## S-04 — `Yazım verileri tek ve mutlak belirleyici değildir`

**Önerilen düzeltme:**
> Yazım verileri, rivâyet, dil ve mana verileriyle birlikte yönlendirici bir işlev üstlenmektedir.

## S-05 — Sahâbe mushaflarının normatif statüsü

**Mevcut ifade:**
> ... aynı normatif düzeye yerleştirmeyi gerektirmez.

**Önerilen düzeltme:**
> Sahâbe mushafları tarihsel tanıklık değeri taşırken normatif mushaf otoritesi Osmânî mushaflar etrafında şekillenmiştir.

## S-06 — Normatif bağlayıcılık ile tevkîfîlik

**Mevcut ifade:**
> Resm-i Osmânî'nin normatif bağlayıcılığı, onun bütün ayrıntılarının tartışmasız biçimde tevkîfî olduğu iddiasıyla özdeş değildir.

**Önerilen düzeltme:**
> Resm-i Osmânî'nin normatif bağlayıcılığı ile bütün yazım ayrıntılarının tevkîfî olduğu görüşü ayrı meselelerdir.

## S-07 — Klasik resm geleneğinin `yalnız erken dönem tarihine ait değildir` biçimi

**Önerilen düzeltme:**
> Klasik resm geleneği çağdaş mushaf neşirlerinde de başvuru zemini olmayı sürdürmüştür.

## S-08 — Nihai `bağımsız kaynak değil` cümlesi

**Mevcut ifade:**
> Sonuç olarak resm-i Osmânî, kırâati doğuran bağımsız kaynak değil, rivâyet yoluyla nakledilen kırâatlerin ortak yazılı sınırıdır.

**Önerilen düzeltme:**
> Son tahlilde kırâatlerin kaynağı rivâyet geleneğidir. Resm-i Osmânî, rivâyet yoluyla nakledilen okuyuşların ortak yazılı sınırını belirleyen tamamlayıcı çerçevedir.

## S-09 — `Ne dar kalıp ne sınırsız alan` karşıtlığı

**Mevcut yapı:**
> ... tek bir okuyuşu ... dar bir fonetik kalıp olmadığı gibi, sınırsız ... alanı da değildir.

**Önerilen düzeltme:**
> Bu çerçeve, sahih rivâyetle sabit okuyuşların bir kısmını açık biçimde gösterir, bir kısmıyla ise ihtimal yoluyla bağdaşır; böylece yazılı birlik ile sınırlandırılmış okuyuş çeşitliliği birlikte korunabilir.

# Doğrudan alıntı ve literal metin koruma listesi

Aşağıdaki `değil/değildir` örnekleri Fifth Report’ta sırf üslup gerekçesiyle değiştirilmemelidir:

1. **Bâkıllânî doğrudan alıntısı:** `özel bir resm dayatılmış değildir.`
2. **Hadis lafzı:** `Kim benim sünnetimden yüz çevirirse benden değildir.`
3. **Kaynakta doğrudan aktarılan hukukî/normatif ifade:** `... yazılması câiz değildir.` türündeki doğrudan alıntılar.
4. **Âyet meali veya alıntılanmış çeviri:** `Hıristiyanlar doğru yolda değillerdir / Yahudiler doğru yolda değillerdir.` gibi alıntı içi kullanımlar.
5. Başka bir âlimin açıkça tırnak içinde verilen sözü; burada cümlenin dışındaki yazar anlatımı sadeleştirilebilir, alıntı lafzı korunur.

# Kapsam uzlaştırması

- Word tabanlı önceki envanter: **96 kırmızı paragraf / 132 kırmızı run parçası**.
- Önceki karar dağılımı: 85 `ALREADY_RESOLVED_STAGE3`, 8 `CHANGE`, 3 `KEEP`.
- Fifth Report yaklaşımı: 85 eski Stage3 paragrafı yeniden kapatılmış sayılmamış; ilgili Stage3/Fourth Report bilimsel çözüm blokları bu dosyadaki olumlu yeniden yazımların dayanağı olarak kullanılmıştır.
- Önceki 3 `KEEP` kullanımından Girişteki ana tez, Déroche nispeti ve 3.1 şehir mushafı karşılaştırması da bu aşamada yeniden yazılmıştır.
- 3.7–3.12 arasındaki çok sayıdaki negatif cümle, Fourth Report V2’nin bölüm düzeyindeki yeniden kuruluşu tarafından **YAPISAL-OLARAK-ÇÖZÜLÜR** sayılmıştır; bu alanda yazarın önüne aynı pasaj için iki rakip metin çıkarılmayacaktır.
- Direct quotation / âyet meali / literal kaynak sözü olan örnekler **ALINTI-KORU** statüsündedir.
- Searchable extraction üzerinde kitap başından Sonuç bölümünün sonuna kadar `değil` ailesi tam metin olarak taranmıştır. Extraction’daki 128 metinsel eşleşme ile Word’deki 132 kırmızı run parçası arasındaki fark biçimlendirme/run yapısından kaynaklanmaktadır; kaynak dosyalar bu çalışma sırasında değiştirilmemiştir.

# Aşama 2 kapanış kararı

Kırmızı `değil/değildir` evreni için Fifth Report’un dil politikası ve bitmiş yeniden yazım çekirdekleri oluşturulmuştur. Nihai Fifth Report’ta bunlar kitap sırasına göre `Yer → İfade → Sorun → Önerilen düzeltme` kartlarına dönüştürülecek; aynı cümlenin Fourth Report V2’de bilimsel bir revizyonu varsa Fifth Report yalnız o revizyonun nihai, kalıpsız dilini verecektir.

Sıradaki aşama, gerçek `Sonuç` bölümü dışındaki bütün mini-sonuçları ve yüksek öncelikli formülleri (`Bu bağlamda`, `Bu çerçevede`, `göstermektedir`, `ortaya koymaktadır`, `açıkça ortaya koymaktadır`, `anlaşılmaktadır`) cümle/paragraf düzeyinde yeniden yazmaktır.
