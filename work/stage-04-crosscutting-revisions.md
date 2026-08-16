# Aşama 4 — Kitap Geneli Anlatım ve Geçiş Düzeltmeleri

Bu çalışma dosyası, Aşama 3’te bilinçli olarak sonraya bırakılan `CAND-161`–`CAND-167` kitap-geneli örüntülerini ve Stage 4 promptunda zorunlu tutulan tam kapsama taramalarını güncel kitap nüshası üzerinde uzlaştırır. Buradaki sayımlar hata sayısı değildir; yüksek sıklık tek başına müdahale gerekçesi sayılmamıştır. Aşama 3’te aynı pasaj için yeterli bir çözüm hazırlanmışsa yeni bir rakip metin üretilmemiş ve kayıt `ALREADY_RESOLVED_STAGE3` olarak kapatılmıştır.

## Değil/Değildir — Müdahale Gerektiren Kullanımlar

Üçüncü rapordaki kırmızı işaret envanteri ile güncel DOCX birlikte kontrol edildi. Redaktörün `değil/değildir` ailesini işaretlediği **96 ayrı paragraf** bulunmaktadır. Kırmızı biçimlendirme run düzeyinde parçalandığı için bu 96 paragrafta toplam **132 kırmızı `değil` ailesi parçası** görülmektedir. Karar birimi paragraftır.

Karar dağılımı:

- `CHANGE`: **8 paragraf**
- `KEEP`: **3 paragraf**
- `ALREADY_RESOLVED_STAGE3`: **85 paragraf**

`KEEP` verilen üç kullanım, kitabın ana tezindeki zorunlu karşıtlığı veya gerçek bir mukayeseyi açık biçimde kurmaktadır:

- **Giriş, P24:** “resm-i Osmânî’nin kırâatleri meydana getiren bağımsız bir kaynak olmadığıdır.” Kitabın merkezî ayrımını doğrudan kurduğu için korunabilir.
- **1.7, P151:** Deroche’ye nispet edilen “bir eksiklik veya hata değil, erken dönem Arap yazısının tabii özellikleridir” karşıtlığı, kaynağın değerlendirmesini açıklayan işlevli bir karşıtlıktır. Bu cümlenin çevresindeki daha güçlü yazar çıkarımları Aşama 3’te kaynak-iddia ayrımı kapsamında ayrıca sınırlandırılmıştır.
- **3.1, P285:** Şehir mushaflarının belirli yerlerde aynı yazımı taşımadığını ifade eden karşıtlık, şehir mushafları arasındaki yazım farklılığını açıklamak için anlamlıdır. Aşama 3’te gerçek/ihtimalî uygunluk ayrımı ayrıca düzeltilmiştir.

Aşağıdaki sekiz paragrafta ise negatif tanım yakın tekrar ve uzun karşıtlık zinciri oluşturduğu için doğrudan revizyon gerekir.

### Girişte şehir mushafları arasındaki farklılığı olumlu çekirdekle tanımlama

**İzlenen aday:** CAND-164  
**Bölüm/Başlık:** Giriş  
**Sayfa:** 2 ve devamı  
**Bulmak için:** “Bu yaklaşım, çalışmada kullanılan kavramlar arasında...” ile başlayan paragraf, P25.

**Mevcut metin:**
> Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, ortak mushaf otoritesinin bulunmadığını değil, aynı istinsah geleneği içinde bazı yazım farklılıklarının rivâyet edildiğini göstermektedir.

**Sorun:** Aynı paragraf zaten resm, resm-i mushaf, resm-i Osmânî, mushaf ve İmam Mushaf ayrımlarını olumlu tanımlarla kurmaktadır. Son cümlede yeniden “X’in bulunmadığını değil, Y’yi gösterir” kalıbına dönmek gereksizdir.

**Önerilen düzeltme:**
> Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, müşterek mushaf otoritesi içinde farklı yazım rivâyetlerinin bulunabildiğini göstermektedir.

### Ebû Ubeyde paragrafındaki tekrar ve çift negatif yapıyı kaldırma

**İzlenen adaylar:** CAND-161, CAND-164, CAND-165  
**Bölüm/Başlık:** 1.7. Resm-i Osmânî’nin Tanımı, Önemi ve Mahiyeti  
**Sayfa:** 27  
**Bulmak için:** “İlk dönem âlimlerinden Ebû Ubeyde el-Kâsım b. Sellâm...” ile başlayan paragraf, P139.

**Mevcut metin:**
> İlk dönem âlimlerinden Ebû Ubeyde el-Kâsım b. Sellâm (ö. 224/838), resm-i Osmânî terimini, daha sonraki âlimler gibi teknik bir başlık altında tanımlayan müstakil bir eser kaleme almamış olmakla beraber, Kur’an ilimlerine dair kaleme aldığı eserlerinde ortaya koyduğu yaklaşım, resm anlayışının erken ve kurucu safhasını oluşturmuştur. O, Osman mushaflarının yazımını bağımsız bir imlâ tercihi olarak değil, sahâbe nakline dayanan bağlayıcı bir metin geleneği olarak değerlendirmiştir. Bu yönüyle o, resm ilminin henüz kavramsallaşma sürecinde olduğu bir dönemde, daha sonra sistemleşecek olan temel prensipleri fiilen benimsemiş görünmektedir. Ebû Ubeyde, resm-i Osmânî’yi tanımlayan ilk isimlerden biri olmamakla beraber, Osman mushaflarının yazımının sahâbe nakline dayalı bağlayıcı bir metin geleneği olarak görmesiyle resm düşüncesinin erken dönem teorik temelini atmıştır.

**Sorun:** Aynı fikir paragrafın ikinci ve son cümlesinde yeniden kuruluyor. “Bağımsız imlâ tercihi değil...” karşıtlığı da bu tekrarı güçlendiriyor; ayrıca “kurucu safha/teorik temel” ifadeleri kaynağın söylediğinden daha ileri bir yazar sonucu izlenimi verebilir.

**Önerilen düzeltme:**
> İlk dönem âlimlerinden Ebû Ubeyde el-Kâsım b. Sellâm (ö. 224/838), resm-i Osmânî’yi daha sonraki literatürdeki teknik çerçevesiyle müstakil bir başlık altında tanımlamamıştır. Bununla birlikte Kur’an ilimlerine dair eserlerinde Osman mushaflarının yazımını sahâbe nakline dayanan bağlayıcı bir metin geleneği içinde değerlendirmesi, resm düşüncesinin erken safhası bakımından önemlidir. Bu yaklaşım, daha sonra sistemleşecek resm literatüründeki bazı temel kabullerin erken dönemdeki görünümünü yansıtmaktadır.

### Dânî ve Ebû Dâvud paragraflarında negatif tanım zincirini azaltma

**İzlenen adaylar:** CAND-161, CAND-164, CAND-166  
**Bölüm/Başlık:** 1.7  
**Sayfa:** 27  
**Bulmak için:** Dânî ile başlayan P142 ve “Dânî’nin talebesi olarak bilinen Ebû Dâvud...” ile başlayan P144.

**Mevcut metindeki problemli yapılar:**
> ... dağınık gözlemlerden oluşan bir bilgi alanı olmaktan çıkarak...  
> ... “mutlak tek biçimlilik” değil, “nakille sabitlenmiş...”  
> ... yalnızca mushaf farklılıklarını kaydeden bir alan olmaktan çıkmış...  
> Mushaf yazımında esas olan dilcilerin kıyas yoluyla ulaştıkları imlâ kuralları değil, güvenilir nakille sabit olmuş yazım geleneğidir.

**Sorun:** İki ardışık paragraf aynı gelişmeyi art arda “bir şey olmaktan çıkma” ve “X değil Y” kalıplarıyla anlatıyor. Dânî’nin karşılaştırmalı kaydı ile Ebû Dâvud’un ayrıntılandırıcı rolü doğrudan olumlu tanımlarla verilebilir.

**P142 için önerilen düzeltme:**
> Resm-i Osmânî’nin müstakil bir inceleme alanı hâline gelmesinde Dânî’nin çalışmaları önemli bir yer tutmaktadır. Dânî, Osman mushaflarının yazım özelliklerini ve şehir mushafları arasında nakledilen farklılıkları sistematik biçimde kaydetmiştir. Böylece resm, belirli kuralları, örnekleri ve tasnif biçimleri bulunan teknik bir alan hâline gelmiştir. Dânî’nin yaklaşımı, farklı merkezlere nispet edilen yazım rivâyetlerini karşılaştırmalı biçimde ele alması bakımından özellikle önemlidir.

**P144 için önerilen düzeltme:**
> Dânî’nin talebesi Ebû Dâvud Süleymân b. Necâh, hocasının çizdiği çerçeveyi ayrıntılı kurallar, örnekler ve uygulamalarla geliştiren önemli resm âlimlerinden biridir. Onun çalışmalarında mushaf yazımının temel başvuru zemini, güvenilir nakille aktarılan Osman mushaflarının yazım geleneğidir. Bu yaklaşım, kıyasî imlâ ile mushaf yazımının ayrı ölçütler çerçevesinde değerlendirildiğini göstermektedir.

### Zerkeşî paragrafındaki art arda olumsuz karşıtlıkları tek açıklamaya indirme

**İzlenen adaylar:** CAND-161, CAND-164, CAND-166, CAND-167  
**Bölüm/Başlık:** 1.7  
**Sayfa:** 27  
**Bulmak için:** “Zerkeşî ise, mushaf yazımını ele alırken...” ile başlayan uzun paragraf, P145.

**Mevcut metin:**
> ... sadece filolojik veya gramer temelli bir tercih olmadığını...  
> ... değiştirmeyi değil, olduğu gibi korumayı esas almıştır.  
> Mushaf yazımında ölçü ... teorik kurallar değil, sahâbeden gelen yazı pratiğidir.  
> ... belirleyici olan şey kıyas değil, rivâyet ve nakildir.  
> ... “yanlış” kabul edilmez...

**Sorun:** Aynı karşıtlık beş farklı biçimde tekrarlanıyor. Paragraf bu nedenle uzuyor ve resmin normatif değerine ilişkin çıkarımı kaynak aktarımından daha güçlü gösteriyor.

**Önerilen düzeltme:**
> Zerkeşî, Osman mushaflarında benimsenen yazım biçiminin dilcilerin kıyas yoluyla belirlediği standart imlâ kurallarıyla her zaman örtüşmediğine dikkat çeker. Onun aktardığı çerçevede mushaf hattının ölçüsü, sonraki kıyasî imlâdan ziyade sahâbe döneminden nakledilen yazım uygulamasıdır. Elif hazifleri, harf ziyadeleri ve vasl-fasl örneklerinin sonraki mushaflarda korunması da bu tarihsel aktarımın devamı olarak değerlendirilmiştir. Bu sebeple resm-i Osmânî’nin normatif değeri açıklanırken kıyasî imlâ ile nakledilmiş mushaf yazımı arasındaki farkın korunması yeterlidir; her yazım farklılığına ayrıca özel ve bilinçli bir amaç yüklenmemelidir.

### Çağdaş araştırmacılar kümesindeki üç ardışık negatif formülü yeniden kurma

**İzlenen adaylar:** CAND-067, CAND-161, CAND-164, CAND-165, CAND-166  
**Bölüm/Başlık:** 1.7  
**Sayfa:** 27 ve devamı  
**Bulmak için:** P148–P150; el-Azamî, Zürkânî, Motzki ve Sinai’nin aktarıldığı ardışık paragraflar.

**Mevcut metindeki problemli yapılar:**
> ... yalnızca çoğaltma işi değil, aynı zamanda metnin birliğini sağlama girişimidir de.  
> ... metni değiştiren değil, mevcut güvenilir rivâyeti sabitleyen...  
> ... kırâat farklılıklarını tamamen ortadan kaldırmak için değil...  
> ... sözlü geleneği ortadan kaldıran değil...

**Sorun:** Üç ardışık paragraf farklı kaynakları aktarırken aynı “X değil Y” formülünü tekrarlıyor ve bazı yerlerde tarihsel niyeti kaynakların açık tespitinden daha kesin bir dille kuruyor.

**P148 için önerilen düzeltme:**
> Çağdaş araştırmacılar Hz. Osman dönemindeki istinsah faaliyetini, mushafların çoğaltılmasının yanı sıra müşterek bir yazılı çerçevenin oluşmasıyla ilişkilendirmiştir. el-Azamî, bu süreci güvenilir sahâbe nüshaları üzerinden ortak bir yazı standardının kurulması çerçevesinde değerlendirir. Bu değerlendirme, mevcut rivâyetin müşterek mushaf geleneği içinde sabitlenmesine vurgu yapmaktadır.

**P149 için önerilen düzeltme:**
> Günümüz Kur’an tarihi çalışmalarında Osmânî mushafların yazı iskeletinin, rivâyetle nakledilen bazı farklı okuyuşlarla bağdaşabildiğine dikkat çekilmektedir. Zürkânî ve el-Azamî de resmin belirli kırâat vecihlerine imkân veren yönlerini vurgulamaktadır. Bu değerlendirmelerde resm-i Osmânî, rivâyet edilen okuyuşların müşterek mushaf yazısıyla bağdaşma alanını belirleyen bir çerçeve olarak ele alınmaktadır.

**P150 için önerilen düzeltme:**
> Harald Motzki ve Nicolai Sinai gibi çağdaş araştırmacılar da erken İslâm toplumunda sözlü aktarım güçlü konumunu korurken yazılı kayıtların giderek daha belirgin bir rol üstlendiğine dikkat çekmektedir. Bu değerlendirme, sözlü aktarım ile yazının erken metin aktarımında birlikte işleyen unsurlar olarak ele alınmasına imkân vermektedir.

### Değil/değildir kapsam defteri

Aşağıdaki 85 paragraf, Aşama 3’te aynı pasaj için hazırlanmış revizyonun ilgili negatif kalıbı da ortadan kaldırması veya yeniden kurması nedeniyle `ALREADY_RESOLVED_STAGE3` olarak kapatıldı:

`P32, P35, P51, P54, P59, P61, P62, P66, P70, P80, P132, P134, P141, P146, P174, P175, P176, P177, P199, P200, P202, P215, P218, P226, P227, P232, P234, P236, P237, P238, P239, P241, P242, P243, P244, P247, P250, P255, P256, P257, P258, P259, P261, P264, P266, P267, P268, P270, P271, P272, P273, P282, P289, P290, P292, P293, P294, P295, P296, P300, P302, P303, P304, P310, P317, P319, P322, P325, P326, P327, P337, P342, P347, P348, P351, P362, P364, P375, P376, P388, P393, P398, P401, P434, P450, P453`.

Bu liste Aşama 5’te yeni madde üretmek için değil, kapsamın kaybolmadığını göstermek içindir.

## Sonuç Olarak ve Gereksiz Ara Sonuçlar

Güncel kitapta **Sonuç başlığı dışında 14 adet** `Sonuç olarak` kullanımı bulunmaktadır. Bunların tamamı yeniden kontrol edildi.

Karar dağılımı:

- `KEEP-SYNTHESIS`: **1**
- `CHANGE-TRANSITION`: **1**
- `MERGE`: **0**
- `DELETE`: **0**
- `ALREADY_RESOLVED_STAGE3`: **12**

### Korunabilecek gerçek sentez

**1.8, P172 — `KEEP-SYNTHESIS`**

Bu paragraf, tevkîfîlik tartışmasında önceki rivâyet ve isnad değerlendirmesini sınırlı bir sonuca bağlıyor. Alt başlığın gerçek sentez işlevini taşıdığı için sırf `Sonuç olarak` kalıbını ortadan kaldırmak amacıyla silinmemelidir. Aşama 5’te aynı başlıkta başka kapanışlar azaltıldığında bu tek sentezin korunması yeterlidir.

### 2.2’den 2.3’e ara sonucu geçişe dönüştürme

**Karar:** `CHANGE-TRANSITION`  
**Bölüm/Başlık:** 2.2.3 Otorite Ekseni → 2.3 Osmânî Mushaf ve Yedi Harf Meselesi  
**Sayfa:** 49–50  
**Bulmak için:** P251, “Sonuç olarak kırâatlerde otorite ekseni...”

**Mevcut metin:**
> Sonuç olarak kırâatlerde otorite ekseni Kur’an’ın doğru okuyuşunu koruyan çok yönlü bir ilmî geleneği ifade eder. Bu geleneğin merkezinde Peygamberî öğretim, sahâbî aktarımı, kırâat imamlarının güvenilirliği, râvilerin sürekliliği, mushaf yazısıyla kurulan denge ve ilim çevrelerinin kabulü yer alır.

**Sorun:** Otorite ekseni önceki paragraflarda zaten tanımlanmıştır. Burada ikinci bir özet yerine 2.3’teki sözlü aktarım–müşterek mushaf ilişkisine geçiş daha işlevlidir.

**Önerilen düzeltme:**
> Kırâatlerde otoritenin bu çok katmanlı yapısı, sözlü aktarımın müşterek mushaf yazısıyla nasıl ilişkilendiği sorusunu gündeme getirir. Bu ilişki, yedi harf ile Osmânî mushaf meselesinde daha belirgin hâle gelmektedir.

### Aşama 3’te zaten çözülen 12 kullanım

`P134, P141, P146, P152, P177, P186, P219, P261, P274, P322, P338, P407` için Aşama 3’te doğrudan kısaltma, tek sentez, bölüm birleştirme veya geçiş metni hazırlanmıştır. Aşama 5 bu on iki yerde Aşama 3 çözümünü esas almalı ve ayrı bir `Sonuç olarak` maddesi üretmemelidir.

### `Bütün bu veriler...` ile başlayan dört kapanış

Sonuç bölümü dışında `Bütün bu veriler` ile başlayan **4 paragraf** bulunmaktadır: P57, P416, P455 ve P472. Dördü de Aşama 3’te sırasıyla 1.1 sentezi, 4.3 kabul ölçütleri, 4.6 modern neşir sentezi ve 4.7 tek kapanış düzenlemeleri içinde ele alınmıştır. Bu nedenle Aşama 4’te yeni rakip metin üretilmemiştir.

## Kalıplaşmış ve Mekanikleşen Anlatım Örnekleri

### Sıklıklar: yalnız tarama göstergesi

Sonuç başlığından önceki güncel ana metinde kesin sayılabilen bazı kullanımlar şöyledir:

| Kalıp | Kullanım |
|---|---:|
| `Nitekim` | 90 |
| `Dolayısıyla` | 49 |
| `Bu bağlamda` | 16 |
| `Bu çerçevede` | 28 |
| `Bu noktada` | 8 |
| `Bu yönüyle` | 9 |
| `Bununla birlikte` | 32 |
| `Böylece` | 79 |
| `göstermektedir` | 120 |
| `ortaya koymaktadır` | 42 |
| `anlaşılmaktadır` | 29 |
| `açıkça ortaya koymaktadır` | 7 |
| `klasik` | 36 |

Bu sayılar tek başına sorun değildir. Müdahale, aynı işlevin yakın paragraflarda tekrarlandığı, bağlacın gerçek mantıksal ilişki kurmadığı veya yüklemin kanıtı gereğinden güçlü gösterdiği yerlerle sınırlandırılmıştır.

### Girişte uzun tarihsel çerçeveyi kısaltma

**İzlenen adaylar:** CAND-162, CAND-165, CAND-166  
**Bölüm/Başlık:** Giriş  
**Sayfa:** 2 ve devamı  
**Bulmak için:** P20, “Problemin tarihsel zemini, İslâm öncesi Arap yazısından...”

**Mevcut metin:**
> Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan Kur’an’ın cem ve istinsah süreçlerine uzanmaktadır. Ana metinde değerlendirilen veriler, İslâm öncesi dönemde yazının ne bütünüyle bilinmeyen ne de toplumun tamamına yayılmış sistemli bir uygulama olduğunu göstermektedir. Vahyin nüzûlüyle yazının kullanım alanı genişlemiş; Kur'an'ın kayda geçirilmesi, sözlü aktarımı tamamlayan ve onun güvenilirliğini pekiştiren bir muhafaza vasıtası olarak gelişmiştir. Hz. Peygamber’in vefatından sonra gerçekleştirilen cem ile Hz. Osman dönemindeki istinsah ise aynı işlem değildir. Cem, dağınık yazılı malzemenin ve hafızadaki aktarımın güvenilir bir derleme içinde bir araya getirilmesine; istinsah, mevcut sahifeler esas alınarak mushaf nüshalarının çoğaltılmasına yönelmiştir. Kaynaklarda heyetin yapısı, mushafların sayısı ve gönderildikleri şehirler hakkında farklı rivâyetler bulunmakla birlikte, istinsah faaliyetinin öncelikli amacının ihtilafların toplumsal ayrışmaya dönüşmesini önleyecek ortak bir mushaf metni oluşturmak olduğu anlaşılmaktadır.

**Sorun:** Paragraf Girişte tarihsel gelişimi ayrıntılı biçimde önceden özetliyor; art arda karşıtlıklar ve sonuç yüklemleri kullanıyor. Son cümle ayrıca tarihsel niyeti “öncelikli amaç” olarak kesinleştiriyor.

**Önerilen düzeltme:**
> Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan cem ve istinsah süreçlerine uzanmaktadır. Vahyin yazıya geçirilmesi sözlü aktarımı tamamlayan bir kayıt işlevi görmüş; Hz. Ebû Bekir dönemindeki cem ile Hz. Osman dönemindeki istinsah ise farklı ihtiyaçlara cevap veren iki ayrı uygulama olarak rivâyet edilmiştir. Kaynaklarda istinsah heyeti, mushafların sayısı ve gönderildikleri merkezler konusunda farklı aktarımlar bulunduğundan, bu sürecin ayrıntıları ihtiyatla değerlendirilmelidir.

### 1.4 açılışında yazı ve hafıza ilişkisindeki aşırı kesinliği azaltma

**İzlenen aday:** CAND-162  
**Bölüm/Başlık:** 1.4. Resm-i Mushaf’ı Çoğaltmayı Gerektiren Sebepler  
**Sayfa:** 16  
**Bulmak için:** P82, “Hz. Ebû Bekir döneminde gerçekleştirilen ilk cem faaliyetiyle...”

**Mevcut metin:**
> Hz. Ebû Bekir döneminde gerçekleştirilen ilk cem faaliyetiyle birlikte Kur’an vahyinin tamamı yazılı malzeme üzerinden güvence altına alınmıştır. Bu faaliyet, vahyin kaybolma ihtimaline karşı alınmış tedbir niteliğinde olup metnin korunmasını hedeflemektedir. Mevcut rivâyetler, Hz. Ömer döneminde ise yeni bir istinsah faaliyetini gerekli kılacak ölçüde yaygın bir kırâat ihtilafının gündeme gelmediğine işaret etmektedir.

**Sorun:** İlk cümle korunmayı yalnız yazılı malzeme üzerinden açıklıyor ve kitabın sözlü-yazılı tamamlayıcılık yaklaşımıyla uyuşmuyor. Paragrafın temel işlevi, Ebû Bekir dönemindeki cem ile Osman dönemindeki istinsahı ayırmaktır.

**Önerilen düzeltme:**
> Hz. Ebû Bekir dönemindeki cem faaliyeti, vahyin yazılı kayıtları ile sahâbenin hafızasındaki aktarımın güvenilir bir derleme içinde bir araya getirilmesine yönelik bir tedbir olarak rivâyet edilmektedir. Hz. Ömer döneminde ise yeni bir istinsah faaliyetini gerektirecek ölçüde yaygın bir kırâat ihtilafının gündeme geldiğine dair aynı yoğunlukta rivâyet bulunmamaktadır.

### 1.4’te ihtilafın mahiyetini daha ihtiyatlı ve kısa anlatma

**İzlenen adaylar:** CAND-162, CAND-166  
**Bölüm/Başlık:** 1.4  
**Sayfa:** 16 ve devamı  
**Bulmak için:** P95, “Bu rivâyetler, o dönemde Müslümanlar arasında kırâate yönelik ihtilafların...”

**Mevcut metin:**
> Bu rivâyetler, o dönemde Müslümanlar arasında kırâate yönelik ihtilafların çok vahim bir noktaya geldiği, çözüm bulunmadığı takdirde Müslümanlar arasında bölünmelere ve ayrışmaya dönüşebileceğine dair ciddi bir endişe doğurduğunu göstermektedir. Burada dikkat edilmesi gereken nokta, ihtilafın metnin varlığı ve bütünlüğünden çok, lafzi farklılıklar ve yazım özellikleri üzerine yoğunlaşmış olmasıdır. Anlam çoğu durumda korunmakla birlikte, farklı lehçe ve kırâat uygulamaları yeni Müslüman olan topluluklar nezdinde zaman zaman şüphe uyandırabilmiştir. Arap lehçelerine aşina olmayanlar, bu farklılıkların ruhsat kaynaklı olduğunu kavrayamamış; bunu metinsel bir çelişki olarak algılayabilmiştir.

**Sorun:** “Çok vahim”, “anlam çoğu durumda korunmuştur” ve yeni Müslüman toplulukların algısına ilişkin zincir, rivâyetlerden çıkarılabilecek sonucun kapsamını gereğinden fazla genişletiyor.

**Önerilen düzeltme:**
> Rivâyetler, farklı okuyuşların özellikle yeni fethedilen bölgelerde ihtilaf konusu hâline gelmesinin ciddi bir endişe doğurduğunu aktarmaktadır. Buradaki mesele, Kur’an metninin varlığından ziyade okuyuş farklılıklarının nasıl anlaşılacağı ve müşterek bir mushaf çerçevesi içinde nasıl sınırlandırılacağıyla ilgilidir. Bu sebeple istinsah faaliyetine götüren şartlar, rivâyetlerin açıkça aktardığı ihtilaf örnekleri üzerinden değerlendirilmelidir.

### `açıkça ortaya koymaktadır` kalıbında kanıt düzeyini iki yerde düşürme

Güncel metinde `açıkça ortaya koymaktadır` tam kalıbı **7 kez** geçmektedir. Bunların beşi Aşama 3’te ilgili paragrafın yeniden yazılmasıyla zaten giderilmiştir: P316, P364, P387, P404 ve P429. İki kullanım için ek düzeltme gerekir.

#### 1.2’de rivâyetin gösterdiği sınırı aşmama

**Bölüm/Başlık:** 1.2  
**Sayfa:** 10–11  
**Bulmak için:** P63, “Bu ve bunun gibi rivâyetler...”

**Mevcut ifade:**
> Bu ve bunun gibi rivâyetler, Medine döneminde vahyin yazıyla tespitinin düzenli bir uygulama hâline geldiğini açıkça ortaya koymaktadır.

**Önerilen düzeltme:**
> Bu rivâyetler, Medine döneminde vahyin yazıyla kaydedilmesinin düzenli bir uygulama olarak aktarıldığına işaret etmektedir.

**Not:** Aynı paragraftaki ikinci ve üçüncü gerekçenin birleştirilmesi Aşama 3’te CAND-019 kapsamında ayrıca çözülmüştür.

#### 4.1’de iki rivâyeti gereğinden güçlü genellememek

**Bölüm/Başlık:** 4.1  
**Sayfa:** 87  
**Bulmak için:** P385, “Kırâat vecihlerinin naklinde aslî dayanak...”

**Mevcut ifade:**
> ... “Kırâat sünnettir.” sözü ile Ebû Amr b. el-A’lâ’nın ... ifadesi, bu anlayışı açıkça ortaya koymaktadır.

**Önerilen düzeltme:**
> ... “Kırâat sünnettir.” sözü ile Ebû Amr b. el-A’lâ’dan nakledilen ifade, kırâat aktarımında rivâyet ve telakkinin merkezî konumuna işaret etmektedir.

### `klasik` nitelemesine ilişkin tarama sonucu

Sonuç başlığından önce `klasik` kelimesi **36 kez** geçmektedir. Bunların önemli bölümü `klasik kaynaklar`, `klasik kırâat usûlü`, `klasik müfessirler` veya belirli isimlerin hemen ardından gelen karşılaştırmalar gibi bağlamı açık kullanımlardır. Sırf kelimenin sıklığı nedeniyle toplu bir değişiklik yapılmamıştır. Aşama 3’te yeniden yazılan 1.5, 1.7, 2.1–2.4 ve 3.4–3.12 pasajları, belirsiz `klasik/modern` karşıtlıklarının önemli kısmını zaten gidermektedir. Aşama 5’te `klasik` için ayrıca genel bir yazar talimatı üretmek yerine yalnız ilgili Aşama 3 ve 4 revizyonları kullanılmalıdır.

### Kırmızı uzun bloklara ilişkin tarama sonucu

Üçüncü raporda kırmızı içerik uzunluğu yüksek olduğu için ayrıca incelenen **29 blok** yeniden kontrol edildi. Uzunluk tek başına hata kabul edilmedi.

- **26 blok:** Aşama 3’te ilgili bölümün doğrudan revizyonu içinde yeterli biçimde çözüldü (`ALREADY_RESOLVED_STAGE3`).
- **3 blok:** Yukarıda ayrıca düzeltildi: P20, P82 ve P95.

Bu nedenle Aşama 5’te “uzun paragraf” adıyla bağımsız bir toplu talimat oluşturulmamalıdır; yalnız bu üç somut yeni düzeltme ve Aşama 3’teki ilgili çözümler kullanılmalıdır.

## Paragraf Açılış ve Kapanış Tekrarları

Yakın açılış kümeleri `Nitekim`, `Bu çerçevede`, `Bu noktada`, `Bununla birlikte` ve benzeri ifadeler üzerinden tarandı. Büyük kümelerin çoğu Aşama 3’te tamamen yeniden yapılandırılan 3.4–3.12, 4.2–4.7 ve Giriş pasajları içinde zaten ortadan kalkmaktadır. Yalnız 4.7’de hem açılış kalıbı hem de tarihsel nedensellik bakımından ek düzeltme gerektiren bir çift paragraf kaldı.

### 4.7’de `Nitekim / Bununla birlikte` zincirini ve nokta-hareke nedenini yeniden kurma

**İzlenen adaylar:** CAND-165, CAND-166  
**Bölüm/Başlık:** 4.7. Kırâat Rivâyetlerine Göre Düzenlenen Basılı Mushafların Yaygınlaşması ve Etkileri  
**Sayfa:** 109 ve devamı  
**Bulmak için:** P459–P460; “Nitekim İbn Kesîr’in de işaret ettiği üzere...” ve hemen ardından “Bununla birlikte Osmânî mushaflarının ilk şeklinde...”

**Mevcut sorun:** İki paragraf art arda bağlaçla açılıyor. İkinci paragraf nokta ve harekenin bulunmamasını doğrudan farklı kırâatleri taşıma amacıyla açıklıyor; bu, erken Arap yazısının tarihsel özelliklerine niyet yüklemektedir.

**Bu iki paragrafın başlangıcı yerine önerilen biçim:**
> Erken mushaf yazısında nokta ve hareke sistemlerinin bugünkü biçimiyle bulunmaması, dönemin Arap yazısının genel özellikleriyle birlikte değerlendirilmelidir. Yazının bu yapısı bazı kelimelerde birden fazla rivâyet edilmiş okuyuşla bağdaşabilmiştir; ancak bu durum nokta ve harekenin özellikle farklı kırâatleri korumak amacıyla terk edildiğini tek başına göstermez. Sonraki dönemlerde zapt işaretlerinin gelişmesi, mushafların belirli okuyuş rivâyetlerine göre daha ayrıntılı biçimde düzenlenmesine imkân vermiştir.

**Uygulama notu:** Bu yeni açılıştan sonra 4.7’deki belirli rivâyetlerin bölgesel yayılışına ilişkin somut örnekler korunabilir. Aynı tarihsel açıklamayı “Nitekim” ve “Bununla birlikte” ile yeniden başlatan iki giriş cümlesi kullanılmamalıdır.

## Eksik veya Zayıf Geçişler

Önceki raporlarda belirlenmiş **26 önemli geçiş noktası** Aşama 3 çözümleriyle birlikte yeniden kontrol edildi.

Karar dağılımı:

- **Aşama 3’te yeterli biçimde çözülmüş:** 22
- **Aşama 4’te ek revizyon gereken:** 3
- **Mevcut hâli korunabilecek:** 1 (`4.7 → Sonuç`; Sonuç bölümü zaten bağımsız açılabildiği için zorunlu ek geçiş gerekmiyor)

Aşama 4’te ek revizyon gereken üç geçiş şöyledir.

### 1.4’ten 1.5’e istinsah gerekçesinden nüsha sayısına geçiş

**Bölüm/Başlık:** 1.4 → 1.5  
**Sayfa:** 16 → 20  
**Sorun:** 1.4 istinsahı gerektiren şartları sonuçlandırdıktan sonra 1.5 doğrudan nüsha sayısına geçiyor.

**1.4’ün sonuna önerilen geçiş:**
> İstinsah kararının nasıl uygulandığını değerlendirebilmek için, çoğaltılan mushafların sayısı ve gönderildikleri merkezler üzerinde ayrıca durmak gerekir.

### 1.10’dan İkinci Bölüme yazılı ölçüden rivâyet mantığına geçiş

**Bölüm/Başlık:** 1.10 → İkinci Bölüm  
**Sayfa:** 40 → 45  
**Sorun:** Birinci Bölüm resme uygunluğun ölçü niteliğini açıklayarak kapanıyor; İkinci Bölüm ise kırâat rivâyetini yeni bir başlangıç gibi açıyor. İki bölümün neden ardışık olduğu tek cümleyle görünür hâle getirilebilir.

**1.10’un sonuna önerilen geçiş:**
> Resm-i Osmânî’nin kırâatlerin değerlendirilmesinde yazılı bir ölçü hâline gelmesi, bu ölçünün sözlü rivâyet düzeni içindeki yerini ayrıca açıklamayı gerekli kılar. İkinci bölüm bu sebeple kırâatlerin rivâyet mantığına yönelmektedir.

### 2.2’den 2.3’e otorite ekseninden Osmânî mushafa geçiş

Bu geçiş, yukarıdaki P251 `Sonuç olarak` düzeltmesiyle aynıdır. Aşama 5’te iki ayrı madde oluşturulmamalıdır.

**Önerilen tek metin:**
> Kırâatlerde otoritenin bu çok katmanlı yapısı, sözlü aktarımın müşterek mushaf yazısıyla nasıl ilişkilendiği sorusunu gündeme getirir. Bu ilişki, yedi harf ile Osmânî mushaf meselesinde daha belirgin hâle gelmektedir.

### Aşama 3’te çözülen geçişlerin kapsam kaydı

Aşağıdaki geçişler Aşama 3’teki doğrudan metinlerle yeterli biçimde karşılanmıştır ve Aşama 5’te yeniden çoğaltılmamalıdır:

- Giriş içi işlev sırası
- Giriş → Birinci Bölüm
- 1.1 içi
- 1.1 → 1.2
- 1.2 → 1.3
- 1.3 → 1.4
- 1.5 → 1.6
- 1.6.1 → 1.6.2
- 1.6.2 → 1.7
- 1.9 → 1.9.1
- 1.9.1 → 1.9.2
- 2.1 → 2.2
- 2.3 → 2.4
- 2.4 → Üçüncü Bölüm
- 3.3 → 3.4
- 3.5 → 3.6
- 3.12 → Dördüncü Bölüm
- 4.1 → 4.2
- 4.3 → 4.4
- 4.5 → 4.6
- 4.6 → 4.7
- 4.7 içi Türkiye örneğine geçiş

`4.7 → Sonuç` geçişi için ek cümle zorunlu görülmemiştir.

## Metinde Kalmış Çalışma Notları

Aşama 2 ve önceki raporlarda izlenen açık yazar/redaktör/yayınevi notları yeniden kontrol edildi. Aşama 3; B1-04 “ikinci maddeye yedirecektiniz” notunu, müellif ölüm tarihleriyle ilgili `daha önce geçti mi/silinsin` notlarını, `(?)` kayıtlarını, 4.2’deki “burası daha önce düzeltilmemiş...” notunu ve dipnot 32/41/105’teki çalışma notlarını somut çözümlerle ele almıştır.

- Önceki raporlarda izlenen **22 çalışma-notu kaydı** Aşama 3 çözümlerinde temsil edilmektedir.
- Aşama 4 taramasında bunlara ek, çözümsüz bırakılmış yeni bir çalışma notu tespit edilmemiştir.
- `CAND-180` çalışma notu değildir; farklı baskıların dipnot-kaynakça eşleştirmesi tamamlanmadan güvenle kapatılamayan bibliyografik kaynak sınırıdır ve Aşama 5’e taşınmalıdır.

## Aşama 3 Çözümlerinin Yerine Geçen Revizyonlar

Aşama 4 taramasında Aşama 3’teki belirli bir öneriyi iptal edip onun yerine geçmesi gereken rakip bir revizyon tespit edilmemiştir.

**Yerine geçen revizyon sayısı: 0.**

Bu aşamadaki 14 yeni/ek düzeltme grubu, Aşama 3’ün kapsamına eklenen veya Aşama 3’te bilinçli olarak kitap-geneli taramaya bırakılmış meseleleri somutlaştıran önerilerdir. Aynı pasaj için Aşama 3’te zaten yeterli metin bulunan yerlerde yeni metin oluşturulmamıştır.

## Kapsam ve Sayım Özeti

### CAND-161–CAND-167 kapanış durumu

- **CAND-161 (`klasik`):** Güncel ana metindeki 36 kullanım tarandı. Sıklık tek başına hata sayılmadı; belirsizleşen kullanımların önemli kısmı Aşama 3’te yeniden yazılan pasajların içinde çözüldü. Yeni toplu “klasik kelimesini değiştir” talimatı üretilmedi.
- **CAND-162 (uzun kırmızı bloklar):** 29 blok kontrol edildi; 26’sı Aşama 3’te çözülmüş, 3’ü Aşama 4’te doğrudan revize edilmiştir.
- **CAND-163 (`Sonuç olarak` ve ara sonuçlar):** Sonuç bölümü dışındaki 14 kullanımın tamamı karara bağlandı; 1 `KEEP-SYNTHESIS`, 1 `CHANGE-TRANSITION`, 12 `ALREADY_RESOLVED_STAGE3`.
- **CAND-164 (`değil/değildir`):** 96 ayrı paragrafın tamamı karara bağlandı; 8 `CHANGE`, 3 `KEEP`, 85 `ALREADY_RESOLVED_STAGE3`.
- **CAND-165 (bağlaç/açılış tekrarları):** Sıklıklar güncel metinden yeniden sayıldı; yalnız yakın tekrar veya işlev bozukluğu olan yerlerde müdahale edildi. Aşama 4’te 4.7 P459–P460 kümesi için yeni doğrudan çözüm üretildi; diğer büyük kümeler Aşama 3 bölüm revizyonlarının içinde çözülmüştür.
- **CAND-166 (sonuç fiilleri):** `göstermektedir` 120, `ortaya koymaktadır` 42, `anlaşılmaktadır` 29 kez geçmektedir. Toplu eş anlamlı değişimi yapılmadı; P20, P95, P63 ve P385 gibi bağlamda gerçekten sorun oluşturan yerler doğrudan yeniden kuruldu.
- **CAND-167 (`açıkça ortaya koymaktadır`):** 7 kullanım incelendi; 5’i Aşama 3’te zaten çözülmüş, 2’si Aşama 4’te doğrudan yumuşatılmıştır.

### Geçiş kapsamı

- Kontrol edilen önemli geçiş: **26**
- Aşama 3’te yeterli biçimde çözülmüş: **22**
- Aşama 4’te ek değişiklik gereken: **3**
- Ek müdahale gerektirmeyen: **1**

### Aşama 3 ile çakışma kontrolü

Paragraf bazında `değil/değildir`, `Sonuç olarak`, uzun kırmızı blok ve `açıkça ortaya koymaktadır` taramalarında **116 benzersiz güncel kitap paragrafı** Aşama 3 çözümüyle zaten kapsanmış olduğundan yeni yazar maddesine dönüştürülmedi. Bu 116 sayısına geçiş noktaları dâhil değildir; böylece aynı pasajın farklı taramalarda iki kez sayılması önlenmiştir.

### Aşama 5’e taşınacak yeni/ek düzeltmeler

Aşama 4, Aşama 3’teki çözümleri çoğaltmadan **14 yeni/ek düzeltme grubu** üretmiştir:

1. Giriş P25 negatif tanım
2. 1.7 P139 Ebû Ubeyde
3. 1.7 P142–P144 Dânî/Ebû Dâvud
4. 1.7 P145 Zerkeşî
5. 1.7 P148–P150 çağdaş araştırmacılar
6. 2.2 P251 ara sonuç → geçiş
7. Giriş P20 uzun/kalıplaşmış tarihsel çerçeve
8. 1.4 P82 yazı-hafıza dengesini düzeltme
9. 1.4 P95 ihtilaf anlatısını ihtiyatlılaştırma
10. 1.2 P63 `açıkça ortaya koymaktadır` düzeltmesi
11. 4.1 P385 `açıkça ortaya koymaktadır` düzeltmesi
12. 4.7 P459–P460 açılış ve tarihsel nedensellik düzeltmesi
13. 1.4 → 1.5 geçişi
14. 1.10 → İkinci Bölüm geçişi

2.2 → 2.3 geçişi 6 numaralı P251 düzeltmesiyle aynı editoryal işlemdir ve ikinci kez sayılmamıştır.

Bu 14 grubun **9’u** esas olarak kalıplaşmış anlatım/negatif tanım/sonuç yüklemi veya yakın açılış tekrarını; **5’i** uzunluk, tarihsel ihtiyat veya bölüm geçişini düzeltmektedir.

### Açık kalan kaynak sınırı

Aşama 4 sonunda yeni bir kaynak belirsizliği üretilmemiştir. Aşama 3’ten devreden **CAND-180**, farklı baskıların dipnot-kaynakça eşleştirmesi yapılmadan güvenle kapatılamadığı için Aşama 5’te açık kaynak sınırı olarak korunmalıdır.

**Aşama 4 sınırı:** Bu dosya kitap-geneli anlatım ve geçiş taramasını kapatır. Aşama 5 başlatılmamıştır.
