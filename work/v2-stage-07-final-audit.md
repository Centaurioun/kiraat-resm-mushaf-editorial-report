# V2 Aşama 7 — Nihai Rapor Öncesi Bağımsız Audit

## Amaç

Bu aşama `work/v2-stage-06-full-author-report-draft.md` dosyasını nihai rapora doğrudan terfi ettirmek için değil, bunu yapmanın güvenli olup olmadığını sınamak için yürütülmüştür.

Bağlayıcı metin `source/manuscript/current/redaktorden_gelen.docx` dosyasıdır. Aranabilir yardımcı metin `source/manuscript/current/redaktorden_gelen_extracted.md` dosyasıdır. V2 çalışma dalında `source/` değiştirilmediği için Aşama 2’de güncel manuscript üzerinde doğrulanan `CAND-*` kayıtları ile bu aşamadaki kaynak metin aynı canonical nüshaya dayanmaktadır.

Auditte şu ölçütler ayrı ayrı uygulanmıştır:

1. **Ctrl+F bulunabilirliği:** `İfade` alanı gerçekten güncel manuscriptte bulunan bir cümle veya pasaj mı?
2. **Uygulanabilirlik:** Öneri, yazarın ayrıca editoryal karar üretmesine gerek bırakmadan uygulanabilir mi?
3. **Kapsam:** Eski Aşama 2’de doğrulanan 178 gerçek sorundan herhangi biri V2 sıkıştırması sırasında sessizce kaybolmuş mu?
4. **Faktik güvenlik:** V2 Aşama 2’de doğrulanan kişi, tarih, âyet ve tarihsel mekanizma düzeltmeleri korunmuş mu?
5. **Kaynak güvenliği:** Kaynak görüşü, yazar çıkarımı ve sonraki yorum birbirine karışıyor mu?
6. **Üslup:** Öneri, kitabın mevcut akademik Türkçesine uyuyor mu; Google AI veya teknik audit dili sızmış mı?
7. **Bilgi kaybı:** Bir sorunu çözmek için doğru veya yararlı bilgi gereksiz yere siliniyor mu?
8. **Mükerrerlik:** Aynı editoryal işlem birden fazla rapor maddesinde gereksiz yere tekrar ediliyor mu?

# I. Genel karar

**Aşama 6 taslağı nihai rapora doğrudan taşınmaya hazır değildir.**

Bunun nedeni taslağın genel olarak zayıf olması değildir. Tersine, 75 maddenin önemli bölümü doğru yöne gitmiş ve V2 doğrulamalarını başarıyla içermiştir. Ancak bağımsız audit, iki ayrı sorun sınıfı ortaya çıkarmıştır:

- bazı maddelerde kullanıcı tarafından özellikle istenen **birebir `İfade` standardı** yeniden editoryal özet/parafraza dönmüştür;
- daha önemlisi, eski 178 sorunla kapsam uzlaştırması yapılırken bazı somut ve daha önce doğrulanmış düzeltmeler, daha geniş V2 maddeleri içinde temsil edildiği varsayılarak **sessizce görünmez hâle gelmiştir**.

Bu nedenle Aşama 6’daki `75` sayısı bir hedef veya üst sınır kabul edilmeyecektir. Nihai rapor 75’ten fazla madde içerebilir. Bir sorunun gerçekten uygulanabilir ayrı bir işlem olması, madde sayısını düşük tutmaktan daha önemlidir.

**Audit sonucu:** `PASS WITH REQUIRED REBUILD BEFORE FINAL`.

# II. Aşama 6’daki 75 maddenin durum sınıflandırması

## A. Büyük ölçüde korunabilecek 49 madde

Aşağıdaki maddelerde güncel manuscriptten ayırt edilebilir gerçek bir ifade/başlık verilmiş, sorun somutlaştırılmış ve öneri doğrudan uygulanabilir düzeydedir. Final üretiminde yalnız son dil, noktalama ve dipnot bağlamı kontrolü gerekir:

`1–35, 38, 40–44, 48, 50, 53, 56, 58, 63, 73, 75`.

Bu maddeler otomatik kopyalanmayacak; fakat yapısal olarak doğru final madde tipini temsil etmektedir.

## B. `İfade` alanı yeniden kurulması gereken 20 madde

Aşağıdaki maddelerde sorun ve öneri çoğunlukla kullanılabilir olmakla birlikte `İfade` alanı gerçek manuscript cümlesi yerine `...cümleler`, `...paragraflar`, `...kısımlar` gibi editoryal özet kullanmaktadır:

`36, 37, 39, 45, 46, 47, 49, 51, 54, 55, 57, 59, 60, 61, 62, 64, 65, 66, 67, 70`.

**Nihai işlem:** Her biri için canonical manuscriptten en az bir birebir Ctrl+F çıpası alınacak. Geniş yapısal sorunlarda birden fazla gerçek başlangıç cümlesi gösterilebilir. Yazarın “hangi paragraf?” sorusunu yeniden çözmesi istenmeyecektir.

## C. İçerik bakımından yeniden tasarlanması gereken 3 madde

### Madde 52 — 3.7–3.12 birleştirmesi

Mevcut V2 taslağı altı başlığı kısa bir dört-paragraflık metne dönüştürmektedir. Bu yaklaşım tekrarları azaltır; fakat mevcut 3.7–3.12’de bulunan kaynaklı ve birbirinden tamamen aynı olmayan malzemenin gereğinden fazla silinmesi riski vardır.

**Karar:** `SUBSTANTIVE-REBUILD`.

Yeni rapor, altı savunma halkasını korumayacak; fakat benzersiz kaynaklı malzemeyi de topluca silmeyecektir. Tek bir ana başlık altında en az şu ayrımlar korunacaktır:

1. tarihsel ve normatif süreklilik;
2. klasik resm/ilim geleneğinin korunması;
3. telakki-müşâfehe ve yazılı çerçevenin tamamlayıcılığı;
4. müşterek mushaf geleneği ve ümmet birliğiyle ilişki;
5. sınırlar: teleolojik tasarım, karşı-olgusal savlar ve doğrulanamayan modern örnekler kanıt olarak kullanılmayacak.

`Nebevî miras`, `selef fazileti`, `müşâfeheyi ihya`, `tek metin/tek hat/tek ümmet` gibi normatif-retorik dil ya müellif/gelenek görüşü olarak sınırlandırılacak ya da tekrar niteliğindeyse çıkarılacaktır.

### Madde 69 — `Kur’an` ev stili

Aşama 6 taslağındaki “ana metinde `Kur'an` yazımı tekleştirilmeli” kararı yanlıştır. Aşama 2’de güncel ana metnin baskın ve tercih edilen biçiminin **`Kur’an`** olduğu doğrulanmıştır.

**Nihai karar:** Ana metinde `Kur’an` kullanılacak. Sınırlı `Kur’ân` ve ASCII apostroflu `Kur'an` kullanımları `Kur’an` biçimine çekilecek. Bibliyografik başlıklar ve doğrudan alıntılar kendi özgün yazımları bakımından ayrıca değerlendirilecektir. `İmam Mushaf` özel terim olarak tekleştirilecektir.

### Madde 74 — farklı baskıların eşleştirilmesi

Aşama 6 V2 taslağı önceki çalışmada fiilen doğrulanmış baskı kararlarını yeniden soyut bir “eşleştirilsin” talimatına dönüştürmüştür. Bu geri adımdır.

**Finalde korunacak somut kararlar:**

- **İbn Ebû Dâvud, `Kitâbu’l-mesâhif`:** dipnot 2’de kullanılan Muhibbüddîn Abdüssübhân Vâiz tahkikli Beyrut 2002 baskısı tutulmalı; güncel dipnotlarda ayırt edilebilir kullanımı bulunmayan 2006 Selîm b. Îde’l-Hilâlî baskısı çıkarılmalıdır.
- **Ebû Dâvud Süleymân b. Necâh, `Muhtasaru’t-tebyîn`:** dipnot 109 Riyad 2000, dipnot 373 Medine 1999 baskısını kullanmaktadır; iki baskı da fiilen kullanıldığı için iki kayıt da korunmalıdır.
- **İbn Kuteybe, `Te’vîlu muhtelifi’l-hadîs`:** dipnot 8’de kullanılan Muhammed Zuhrî en-Neccâr tahkikli kayıt tutulmalı; güncel dipnotlarda ayırt edilebilir kullanımı bulunmayan 1999 Muhammed Muhyiddîn el-Asfar baskısı çıkarılmalıdır.
- **Ebû Şâme, `el-Murşidu’l-vecîz`:** 1993 baskısının kullanımı açıktır; 1975 baskısı ise kısa atıflar kesin eşleştirilmeden silinmemelidir. Bu işlem madde 75’teki tek açık bibliyografik kontrol olarak kalabilir.

## D. Bağımsız “sorun maddesi” olmaktan çıkarılacak 3 soyut madde

`68, 71, 72` numaralı maddeler kendi başlarına eski teknik rapor mantığına yaklaşmaktadır.

- **68:** `değil/değildir`, `Sonuç olarak`, `Nitekim` vb. için genel tarama talimatı finalde ayrı sorun olarak gösterilmeyecek. Somut problemli örnekler ilgili bölüm maddelerinde zaten düzeltilecek. Gerekirse rapor sonunda iki cümlelik “genel yazım notu” olarak kalabilir.
- **71:** ilk tam / sonraki kısa atıf kuralı genel bibliyografik ilke olarak kısa bir giriş notuna dönüştürülecek; yazarın düzelteceği somut örnekler varsa onların yanında gösterilecek.
- **72:** müellif artikeli / sûre artikeli kuralı da genel teknik talimat gibi ayrı numaralı sorun yapılmayacak. Somut tutarsızlıklar ve seçilen ev stili, kaynakça bölümünün kısa kullanım notunda verilecek.

# III. Aşama 6’da sessizce görünmez hâle gelen doğrulanmış düzeltmeler

Aşağıdaki kayıtlar Aşama 2’de canonical manuscript üzerinde doğrulanmış, bir kısmı eski Aşama 3/4’te doğrudan düzeltme metnine kadar ilerlemiş, fakat V2 Aşama 6’daki 75 maddede ya hiç görünmemiş ya da çok geniş bir madde altında yazarın uygulayacağı ayrı işlem olarak kaybolmuştur.

Bu bölüm, nihai rapor üretiminde **zorunlu geri-ekleme defteri** olarak kullanılacaktır.

## A. Önsöz/Giriş

Bu alanın temel sorunları V2 taslağında büyük ölçüde korunmuştur. Ek bir sessiz kapsam kaybı tespit edilmemiştir. Ancak madde 6 gibi çok-paragraflı değişikliklerde hangi güncel paragrafların tamamen değiştirileceği finalde açıkça belirtilecektir.

## B. Birinci Bölüm

### 1.1 — iki ayrı sentezi tekleştirme (`CAND-047`)

**Ctrl+F çıpaları:** `Bu farklı görüşler birlikte değerlendirildiğinde...` ve `Bütün bu veriler bir arada değerlendirildiğinde...`

İki kapanış aynı temel hükmü kurmaktadır. V2 madde 8 kanıt düzeylerini düzeltmekte, fakat iki sonuç paragrafının tekleştirilmesini açık işlem olarak göstermemektedir. Finalde bir tek sentez bırakılacaktır.

### 1.2 → 1.3 geçişindeki tekrar (`CAND-048`)

1.2’nin muhafaza modellerini kapatan paragrafıyla 1.3’ün ilk genel çerçevesi aynı bilgiyi yeniden kurmaktadır. Finalde 1.2 tek kısa kapanışla bitecek ve 1.3 doğrudan cem ihtiyacına geçecektir.

### 1.3 — bozuk Zeyd b. Sâbit cümlesi (`CAND-049`)

**Ctrl+F çıpası:** `nedeninin yazı noktasındaki maharetli olduğunu gösterir`

Bu açık tamlama/yüklem bozukluğu V2 taslağında yoktur. Finalde gerçek cümle açılıp doğrudan tashih edilecektir.

### 1.4 — yazı ve hafıza dengesini düzeltme (`CAND-162`, eski Aşama 4 P82)

**Ctrl+F çıpası:** `Hz. Ebû Bekir döneminde gerçekleştirilen ilk cem faaliyetiyle birlikte Kur'an vahyinin tamamı yazılı malzeme üzerinden güvence altına alınmıştır.`

V2 taslağındaki madde 15 başka bağlamdaki `cem` sorununu çözüyor; bu ayrı cümle kaybolmuştur.

**Hazır düzeltme:**
> Hz. Ebû Bekir dönemindeki cem faaliyeti, vahyin yazılı kayıtları ile sahâbenin hafızasındaki aktarımın güvenilir bir derleme içinde bir araya getirilmesine yönelik bir tedbir olarak rivâyet edilmektedir. Hz. Ömer döneminde ise yeni bir istinsah faaliyetini gerektirecek ölçüde yaygın bir kırâat ihtilafının gündeme geldiğine dair aynı yoğunlukta rivâyet bulunmamaktadır.

### 1.4 — ikinci `Hülasa` kapanışını kaldırma (`CAND-052`)

1.4’te gerekçeler zaten sentezlenmişken `Hülasa...` ile ikinci kapanış kurulmaktadır. Finalde tek sonuç paragrafı bırakılacaktır.

### 1.4 → 1.5 geçişi (eski Aşama 4)

**Finale geri eklenecek hazır geçiş:**
> İstinsah kararının nasıl uygulandığını değerlendirebilmek için, çoğaltılan mushafların sayısı ve gönderildikleri merkezler üzerinde ayrıca durmak gerekir.

### 1.5 — çağdaş araştırmacıları mekanik sıra hâlinde vermeme (`CAND-054`)

V2 madde 26 “ortak analiz” genellemesini düzeltmektedir; fakat uzun `Zürkânî... Subhî es-Sâlih... Azamî... Hamîdullah...` dizisinin mekanik yapısı ayrıca sadeleştirilmelidir. Görüşler kişi kişi art arda sonuçlandırılmak yerine dayandıkları veri ve ihtiyat düzeyine göre gruplanacaktır.

### 1.5 → 1.6 geçişi (`CAND-055`)

Mushaf sayısı tartışmasından doğrudan kavramsal `resm` açıklamasına atlanmaktadır. Finalde kısa bir geçiş kurulacaktır.

### 1.6 başlangıcındaki üç meta-giriş (`CAND-039`)

**Ctrl+F çıpası:** `Resm-i Osmânî, Kur'an ilimleri içerisinde hem yazı tarihi hem de metnin korunması açısından merkezî bir kavramdır.`

Bunu izleyen “iki ana eksen” ve “öncelikle resm kelimesinin...” paragrafları aynı hazırlık işlevini tekrar etmektedir. Finalde tek giriş bırakılacaktır.

### 1.6.1 → 1.6.2 lügat tekrarını kaldırma (`CAND-057`)

1.6.2, `resm`in `iz/kalıntı` anlamını yeniden uzun biçimde anlatmamalı; doğrudan ıstılahî kullanıma geçmelidir.

### 1.6.2 sonundaki ikinci tanım özeti (`CAND-058`)

**Ctrl+F çıpası:** `Sonuç olarak Cürcânî ve Kastallânî'nin tanımları...`

Bu paragraf önceki iki tanımı yeniden özetlemektedir. Finalde önceki paragrafın sonuna yedirilecek veya kısaltılacaktır.

### 1.7 — Ebû Ubeyde, Dânî/Ebû Dâvud, Zerkeşî ve çağdaş araştırmacılar (eski Aşama 4’ün 4 ayrı düzeltme grubu)

V2 Aşama 6 bu dört doğrulanmış doğrudan revizyonu sessizce kaybetmiştir. Nihai rapora yeniden alınacaktır.

**Ebû Ubeyde çıpası:** `İlk dönem âlimlerinden Ebû Ubeyde el-Kâsım b. Sellâm...`

**Hazır metin:**
> İlk dönem âlimlerinden Ebû Ubeyde el-Kâsım b. Sellâm (ö. 224/838), resm-i Osmânî'yi daha sonraki literatürdeki teknik çerçevesiyle müstakil bir başlık altında tanımlamamıştır. Bununla birlikte Kur'an ilimlerine dair eserlerinde Osman mushaflarının yazımını sahâbe nakline dayanan bağlayıcı bir metin geleneği içinde değerlendirmesi, resm düşüncesinin erken safhası bakımından önemlidir. Bu yaklaşım, daha sonra sistemleşecek resm literatüründeki bazı temel kabullerin erken dönemdeki görünümünü yansıtmaktadır.

**Dânî çıpası:** `Resm-i Osmânî'nin müstakil bir ilim hâline gelmesinde Dânî'nin çalışmaları...`

**Hazır metin:**
> Resm-i Osmânî'nin müstakil bir inceleme alanı hâline gelmesinde Dânî'nin çalışmaları önemli bir yer tutmaktadır. Dânî, Osman mushaflarının yazım özelliklerini ve şehir mushafları arasında nakledilen farklılıkları sistematik biçimde kaydetmiştir. Böylece resm, belirli kuralları, örnekleri ve tasnif biçimleri bulunan teknik bir alan hâline gelmiştir. Dânî'nin yaklaşımı, farklı merkezlere nispet edilen yazım rivâyetlerini karşılaştırmalı biçimde ele alması bakımından özellikle önemlidir.

**Ebû Dâvud çıpası:** `Dânî'nin talebesi olarak bilinen Ebû Dâvud Süleymân b. Necâh...`

**Hazır metin:**
> Dânî'nin talebesi Ebû Dâvud Süleymân b. Necâh, hocasının çizdiği çerçeveyi ayrıntılı kurallar, örnekler ve uygulamalarla geliştiren önemli resm âlimlerinden biridir. Onun çalışmalarında mushaf yazımının temel başvuru zemini, güvenilir nakille aktarılan Osman mushaflarının yazım geleneğidir. Bu yaklaşım, kıyasî imlâ ile mushaf yazımının ayrı ölçütler çerçevesinde değerlendirildiğini göstermektedir.

**Zerkeşî çıpası:** `Zerkeşî ise, mushaf yazımını ele alırken önemli bir ilkeye dikkat çeker.`

**Hazır metin:**
> Zerkeşî, Osman mushaflarında benimsenen yazım biçiminin dilcilerin kıyas yoluyla belirlediği standart imlâ kurallarıyla her zaman örtüşmediğine dikkat çeker. Onun aktardığı çerçevede mushaf hattının ölçüsü, sonraki kıyasî imlâdan ziyade sahâbe döneminden nakledilen yazım uygulamasıdır. Elif hazifleri, harf ziyadeleri ve vasl-fasl örneklerinin sonraki mushaflarda korunması da bu tarihsel aktarımın devamı olarak değerlendirilmiştir. Bu sebeple resm-i Osmânî'nin normatif değeri açıklanırken kıyasî imlâ ile nakledilmiş mushaf yazımı arasındaki farkın korunması yeterlidir; her yazım farklılığına ayrıca özel ve bilinçli bir amaç yüklenmemelidir.

**Çağdaş araştırmacılar:** el-Azamî, Zürkânî, Motzki, Sinai ve Déroche’ye atfedilen değerlendirmeler ayrı ayrı kaynağın söylediği düzeyde tutulacak; yazarın ana tezi bu isimlerin ortak sonucu gibi sunulmayacaktır. Eski Aşama 4’te hazırlanmış üç kısa paragraf final üretiminde rezervuar olarak kullanılacaktır.

### 1.7 — üç ayrı ara sonucu tekleştirme (`CAND-059`)

1.7 içindeki birden fazla `Sonuç olarak`/ara sentez tek bölüm kapanışına indirilecektir.

### 1.8 — tevkîfîlik ile normatif bağlılığı en başta ayırma (`CAND-041`, `CAND-042`)

Bölümün temel sorusu tartışmanın ortasında yeniden başlatılmaktadır. Final önerisi, başta şu ayrımı kuracaktır: `Resmin tarihsel olarak tevkîfî kabul edilmesi` ile `sonraki mushaf yazımında bu resme bağlı kalınması gerektiği görüşü` aynı iddia değildir.

### 1.8 — Muâviye rivâyetinin kanıt değerini tutarlı sunma (`CAND-060`)

Aynı rivâyet önce tevkîfîliğin delili gibi güçlü biçimde verilip sonra zayıf/uydurma değerlendirmeleri aktarılmaktadır. Finalde rivayetin tartışmalı kanıt değeri ilk zikredildiği yerde açıkça belirtilecek; sonraki değerlendirmeler bunu tekrar etmeyecektir.

### 1.9 başlangıcı — resm-i mushaf / resm-i Osmânî eşitliğini bozma (`CAND-061`)

**Ctrl+F çıpası:** `Resm-i Mushaf (resm-i Osmânî), Kur'an metninin...`

Bu eşitleme, Girişte kurulan kavramsal ayrımla çelişmektedir. Finalde resm-i mushaf daha geniş alan, resm-i Osmânî belirli tarihsel yazım çerçevesi olarak ayrılacaktır.

### 1.9 girişindeki erken sonuç (`CAND-062`)

İmlâ özellikleri açıklanmadan önce `erken dönem İslâm toplumunun Kur'an metnini hem yazı hem kırâat düzeyinde koruma çabasının ürünü` şeklinde geniş niyet sonucu verilmemelidir.

### 1.9.1 — fasl/vasl tanımındaki açık parantez bozukluğu (`CAND-063`)

**Ctrl+F çıpası:** `ayrı yazılması fasl).`

Doğrudan tashih edilmelidir.

### 1.9.1 Hazf — ikinci kapanış (`CAND-065`)

**Ctrl+F çıpası:** `Sonuç olarak hazf, resm-i Osmânî'nin en yaygın...`

Hazf örnekleri tamamlandıktan sonra aynı işlevleri yeniden sıralayan bu mini-sonuç kısaltılacaktır.

### 1.9.2 — üç kapanışı tek senteze indirme (`CAND-066`)

V2 madde 35 doğru sentezi vermektedir; finalde bu yeni paragraf gerçekten mevcut son üç paragrafın yerine konacak ve bunun uygulama sınırı açıkça yazılacaktır.

### 1.10 → İkinci Bölüm geçişi (eski Aşama 4)

**Finale geri eklenecek hazır geçiş:**
> Resm-i Osmânî'nin kırâatlerin değerlendirilmesinde yazılı bir ölçü hâline gelmesi, bu ölçünün sözlü rivâyet düzeni içindeki yerini ayrıca açıklamayı gerekli kılar. İkinci bölüm bu sebeple kırâatlerin rivâyet mantığına yönelmektedir.

## C. İkinci Bölüm

### 2.1 sonunu 2.2’ye geçişe dönüştürme (`CAND-071`, `CAND-072`)

**Ctrl+F çıpası:** `Netice itibarıyla kırâat kavramı...`

2.1’in rivâyet/sened açıklamalarını tekrar eden kapanışı kısaltılıp 2.2’ye bağlanacaktır.

### 2.2.1 — yanlış yazı/sözlü dikotomisini düzeltme (`CAND-073`)

**Ctrl+F çıpası:** `Kırâatlerin aktarımı baştan itibaren yazılı değil, sözlü...`

Bu cümle kitabın ana teziyle uyuşmamaktadır. Final önerisi sözlü telakki ve edânın aslî rolünü koruyacak; fakat yazılı mushaf ve kayıtların tamamlayıcı varlığını inkâr etmeyecektir.

### 2.3 — Birinci Bölüm tarih tekrarını kısaltma (`CAND-077`)

Yedi harf ve Osmânî istinsahın tarihsel gelişimi Birinci Bölümde uzun biçimde anlatılmıştır. 2.3 yalnız rivâyet mantığı için gerekli kısa hatırlatmayı koruyacaktır.

### 2.3 sonunu 2.4’e bağlama (`CAND-078`)

**Ctrl+F çıpası:** `Sonuç olarak Osmânî mushaf ile yedi harf meselesi...`

V2 madde 41’in ihtiyatlı görüşler paragrafı korunabilir; fakat bunun sonunda 2.4’teki müşterek başvuru metni meselesine açık bir geçiş eklenmelidir.

### 2.4 — karşı-olgusal `resm ortak hâle gelmemiş olsaydı` (`CAND-079`)

Bu tür cümleler gözlenmiş tarihsel sonuçlar üzerinden yeniden kurulacak; kanıtlanamayan alternatif tarih senaryosu kullanılmayacaktır.

### 2.4 → Üçüncü Bölüm geçişi (`CAND-081`)

Finalde şu işlev korunacaktır: teorik çerçeveden hazf, ziyâde, ibdâl, vasl-fasl gibi somut resm örneklerine geçildiği açıkça belirtilecektir.

### Kırâat / rivâyet / tarîk / vecih (`CAND-082`)

Girişte ayrım artık açıkça bulunduğundan İkinci Bölüme yeni uzun teorik kutu eklenmeyecektir. Final raporda yalnız yanlış veya belirsiz kullanımlar somut cümleleriyle gösterilecektir.

## D. Üçüncü Bölüm

### 3.1 — `daha önce de zikretmiştik` meta-göndermesini kaldırma (`CAND-099`)

Bölümün yeni açılışı V2 madde 43 ile tekleştirilecek; eski meta-gönderme taşınmayacaktır.

### 3.1 — `otuz üç adet` uzun listesinin türlerini ayırma (`CAND-097`)

**Ctrl+F çıpası:** `Bu kelimeler otuz üç adet olup...`

Liste içindeki bütün örnekler aynı tür resm-kırâat ilişkisi gibi sunulmamalıdır. Finalde ya türler açıkça ayrılacak ya da genelleyici giriş cümlesi sınırlandırılacaktır.

### 3.3 → 3.4 geçişi (`CAND-102`)

Fonetik/hareke tartışmasından mana ve hikmet yorumlarına geçerken kanıt düzeyinin değiştiği açıkça söylenecektir. Böylece okur, tarihsel-imlâî açıklamadan klasik yorum literatürüne geçtiğini görecektir.

### 3.4 — `anlam işaretleme sistemi` sonucunu kaldırma (`CAND-103`, `CAND-104`)

Hikmet örnekleri tamamlanmadan resmin bir `anlam işaretleme sistemi` olduğu sonucuna varılmayacak. V2 madde 48’in yeni başlık/giriş metni kullanılacak; ara sentez örneklerden önce gelmeyecektir.

### 3.5 — çift kapanışı tekleştirme (`CAND-105`)

Son iki sentez paragrafı aynı işi yapmaktadır. Tek kapanış bırakılacaktır.

### 3.6 — İbn Haldûn’a verilen savunmacı cevabı kanıt düzeyine çekme (`CAND-087`)

**Ctrl+F çıpaları:** `İbn Haldûn'un bu yaklaşımı resm-i mushaf'ın hüccet değerini zayıflatma tehlikesi taşımaktadır.` ve `Çağdaş resm-i Osmânî literatüründe İbn Haldûn'a karşı geliştirilen cevaplar...`

İbn Haldûn’un tarihsel açıklaması, ona verilen klasik/çağdaş cevaplar ve kitabın değerlendirmesi birbirinden ayrılacaktır. `Kur'an'ın korunmuşluğu vaadi mushaf kitâbetinin gelişigüzel hata zincirine bırakılmadığını ima eder` gibi teolojik savunmalar tarihsel kanıtın yerine geçirilmeyecektir.

### 3.6 — açılış ve iç sıralama (`CAND-107`, `CAND-108`)

Ahmed b. Hanbel, tevkîfîlik, kırâat sıhhati, hikmet, nahiv, İbn Haldûn ve i‘câz aynı çizgide zikzaklı ilerlememelidir. Finalde bölüm şu sıraya çekilecektir:

1. bağlayıcılık meselesi;
2. tevkîfî/ictihâdî ve tarihsel köken tartışması;
3. dil/nahiv ve resm ilişkisi;
4. hikmet/i‘câz yorumları;
5. İbn Haldûn’un eleştirisi ve sonraki cevapların kanıt değeri;
6. kısa ve ihtiyatlı sentez.

### 3.6 — `üç ana çizgi` sayım hatası (`CAND-106`)

**Ctrl+F çıpası:** `Sonuç olarak resm-i mushaf etrafındaki tartışmalar üç ana çizgide toplanmaktadır:`

Mevcut cümle ardından iki çizgi saymaktadır. Finalde ya gerçekten üç yaklaşım açıkça sayılacak ya da `başlıca yaklaşımlar` denilerek hatalı sayı kaldırılacaktır.

### 3.7 sonundaki modern imlâ görüşleri (`CAND-110`)

Resm-i Osmânî ile modern imlâ arasında üç görüş tasnifi, hata/tahrif başlığının sonuna iliştirilmemeli; bağlayıcılık tartışmasının yürütüldüğü 3.6 içine taşınmalıdır. Bu kaynaklı ve özgün malzeme, 3.7–3.12 birleştirmesi sırasında kaybedilmemelidir.

### 3.10 — `tam fonetik yazı olsaydı müşâfehe zayıflardı` karşı-olgusu (`CAND-112`)

**Ctrl+F çıpası:** `Şayet Kur'an lafızlarının tamamı telaffuza tam uygun biçimde yazılmış olsaydı...`

Bu varsayım tarihsel kanıt olarak kullanılamaz. Bunun yerine gözlenen durum ifade edilecektir: okuyuş ayrıntıları telakki ve edâ yoluyla aktarılmış, yazı bu aktarımın tamamlayıcı çerçevesi olmuştur.

### 3.11 — `modern imlâya geçilirse vecihler zayi olur` nedenselliği (`CAND-115`)

Yazım değişikliğinin belirli vecihlerin yazıdaki görünürlüğünü veya resmle bağdaşma biçimini etkileyebilmesi ile kırâat rivâyetinin kendisinin ortadan kalkması birbirinden ayrılacaktır. Kırâatlerin sözlü nakil zeminiyle çelişen `zayi olur` kesinliği kullanılmayacaktır.

### 3.12 → Dördüncü Bölüm geçişi (`CAND-116`)

Birleştirilen 3.7’nin sonuna, normatif bağlılık tartışmasından resmin kırâatlerin tespiti/tahdidi ve uygulamadaki kullanımına geçildiğini açıkça belirten kısa köprü eklenecektir.

## E. Dördüncü Bölüm

### 4.1 — tarihsel tekrarları kısaltma (`CAND-051`, `CAND-135`)

Ebû Bekir cemi, Huzeyfe olayı, Osmânî istinsah ve mushaf sayısı Birinci Bölümde ayrıntılı biçimde anlatılmıştır. 4.1 bu malzemeyi yalnız kendi `tespit/tahdit` argümanı için gerekli ölçüde hatırlatmalıdır.

### 4.1 — `Kırâat sünnettir` örneğinde kanıt dilini düşürme (eski Aşama 4 P385)

**Ctrl+F çıpası:** `Kırâat vecihlerinin naklinde aslî dayanak...`

**Hazır düzeltme:**
> “Kırâat sünnettir.” sözü ile Ebû Amr b. el-A‘lâ’dan nakledilen ifade, kırâat aktarımında rivâyet ve telakkinin merkezî konumuna işaret etmektedir.

### 4.1 → 4.2 geçişi (`CAND-136`)

Müşterek Osmânî mushaf çerçevesinden sahâbe şahsî mushaflarına geçerken bu iki malzemenin aynı normatif statüde olmadığı tek cümleyle belirtilmelidir.

### 4.2 — resmi `ayıklayan kurucu otorite` yapmama (`CAND-137`)

**Ctrl+F çekirdeği:** sahâbe mushafları bağlamında `ayıklayan` / `kurucu bir otorite` ifadeleri.

Seçme/ayıklama fiili resme verilmemelidir. Aktör tarihsel istinsah, müşterek mushaf kabulü ve sonraki ilmî değerlendirme sürecidir; resm bu süreçte yazılı ölçüdür.

### 4.2 — İbn Mes‘ûd’un psikolojisini kesinleştirmeme (`CAND-138`)

`öfke`, `kırgınlık`, `geçici tepki` gibi ifadeler kaynak açıkça bu psikolojik gerekçeyi vermiyorsa yazar hükmü yapılmayacaktır. Tarihsel tavır ve nakledilen sözler aktarılacak, niyet ayrıca yorum olarak sınırlandırılacaktır.

### 4.2 — tarihsel tanıklık/normatif otorite tekrarını ve çift kapanışı tekleştirme (`CAND-139`, `CAND-140`)

V2 madde 55’in kategori ayrımı kullanılabilir; fakat finalde mevcut 4.2’nin ilgili tekrar bloklarının gerçekten hangi paragraf aralığının yerine geçeceği gösterilmelidir.

### 4.3 — şâz kategorisini tek çizgiye indirmeme (`CAND-141`, `CAND-142`)

Resme aykırı, âhâd, mensuh olduğu ileri sürülen veya önceki ruhsat alanıyla ilişkilendirilen okuyuşlar tek kategori gibi anlatılmayacaktır. Her örnek kendi kaynak/statü bağlamında verilecek ve her örneğin sonunda `resmin merkezî konumu` sonucu yeniden tekrarlanmayacaktır.

### 4.3 → 4.4 geçişi (`CAND-143`)

Kabul/sahihlik tartışması ile kabul edilmiş okuyuşlar arasındaki tercih, tevcîh ve vakıf tartışmasının farklı düzeyler olduğu açıkça belirtilmelidir.

### 4.4 — imamları kurucu seçici gibi anlatmama (`CAND-144`)

**Ctrl+F çıpası:** `Kırâat imamları kendilerine ulaşan farklı okuyuşlar arasından...`

Tercih kavramı, imamların mevcut rivâyetlerden bağımsız yeni okuyuşlar oluşturduğu izlenimini vermeyecek biçimde rivâyet ve nispet bağlamında yeniden kurulacaktır.

### 4.4 — vakıf türlerini ayırma (`CAND-124`)

**Ctrl+F çıpası:** `Resm, vakıf uygulamalarında da doğrudan belirleyici...`

Mana temelli vakıf-ibtidâ, resmle ilişkili yazılı kelime sınırı ve rivâyet/edâya özgü vakıf uygulamaları aynı nedensellik içinde toplanmayacaktır.

### 4.5 — `her yazımın hikmeti` görüşünü kaynağa nispet etme (`CAND-146`)

**Ctrl+F çekirdeği:** `Zeyd b. Sâbit'in yazdığı her şeyin bir hikmet ve ince sır...`

Bu görüş yazar sonucu gibi bırakılmayacak; görüş sahibine nispet edilerek, tarihsel yazım sebebini kanıtlamadığı açıkça belirtilecektir.

### 4.5 — sonucu tasniften önce vermeme (`CAND-147`)

**Ctrl+F çıpası:** `Bu çerçevede denilebilir ki...`

Genel hüküm üçlü tasniften önce geliyorsa sonraya taşınacak veya tasnif sonunda gerekli olmadığı için kaldırılacaktır.

### 4.5 — `son derece bilinçli ve işlevsel` genellemesini daraltma (`CAND-148`)

Üç örnek türünden bütün resm-i Osmânî’ye ortak tarihsel niyet çıkarılmayacaktır. V2 madde 60’ın daha ihtiyatlı çerçevesi uygulanacaktır.

### 4.6 — Dânî/Ebû Dâvud ve modern neşir tekrarlarını tek paragrafta toplama (`CAND-151`, `CAND-152`)

Aynı kaynak işlevi dört kez sonuçlandırılmamalıdır. Finalde tek sentez paragrafı bırakılacak, ardından 4.7’ye geçilecektir.

### 4.7 — `ilk resmî` mutlaklığını yeniden kontrol etme (`CAND-131`)

1873 karar / 1874 basım ayrımı güncel manuscriptte zaten düzeltilmiştir ve tekrar sorun yapılmayacaktır. Buna karşılık aynı pasajda `ilk` veya `ilk resmî` mutlaklığı kalmışsa bağlı kaynağın ifade düzeyine çekilecektir.

### 4.7 — neşir ile belirli rivâyetin yaygınlaşmasını tek nedene bağlamama (`CAND-133`)

Matbu mushafların etkisi, bölgesel öğretim geleneği, resmî neşir tercihleri ve rivâyet aktarımıyla birlikte ele alınacaktır.

### 4.7 — 1889 Teftîş-i Mesâhif cümlesindeki özne-yüklem bozukluğu (`CAND-134`)

**Ctrl+F çıpası:** `1889'da kurulan Teftîş-i Mesâhif-i Şerîfe Meclisinin`

Mevcut cümle tam olarak açılıp öznesi ve yüklemi uyumlu olacak şekilde doğrudan tashih edilecektir.

### 4.7 — mikro-yapı ve çift sonuç (`CAND-154`, `CAND-155`, `CAND-156`)

Bölüm şu işlev sırasına çekilecektir:

1. matbu mushaf tarihine kısa giriş;
2. erken baskılar ve tarihsel kronoloji;
3. bölgesel/kırâat rivâyetlerine göre baskılar;
4. Osmanlı/Türkiye denetim ve neşir tecrübesi;
5. tek ihtiyatlı sonuç.

Türkiye örneğinden önce `Bütün bu veriler...` ile bölüm kapatılmayacak; sonrasında ikinci genel sonuç da oluşturulmayacaktır.

## F. Sonuç

V2 maddeler 65–67 içerik bakımından doğru yöndedir; fakat `İfade` alanları gerçek manuscript alıntılarıyla değiştirilecektir. Matbu mushafların belirli rivâyetleri `standartlaştırdığı` ifadesi tek yönlü nedensellik taşımayacak şekilde neşir, öğretim, bölgesel gelenek ve kurumlarla birlikte anlatılacaktır.

## G. Kitap geneli dil ve kalıplaşmış anlatım

Eski Aşama 4’ün taraması kapsam kanıtı olarak korunacaktır:

- kırmızı `değil/değildir` ailesi bulunan 96 paragraf: 8 gerçek değişiklik, 3 korunacak kullanım, 85 önceki doğrudan revizyon içinde çözülmüş;
- Sonuç bölümü dışındaki 14 `Sonuç olarak`: 1 gerçek sentez, 1 geçişe dönüştürülecek kullanım, 12 önceki revizyon içinde çözülmüş;
- kırmızı uzunluk nedeniyle incelenen 29 blok: 26’sı eski Aşama 3 revizyonlarında çözülmüş, 3’ü eski Aşama 4’te somut düzeltmeye dönüştürülmüş.

Bu sayılar **final rapora konmayacaktır**. Final raporda yalnız somut cümle/paragraf düzeltmeleri yer alacaktır. `Kalıplaşmış anlatım` terimi kullanılacak; `formüle anlatım` kullanılmayacaktır.

# IV. Faktik ve terminolojik son kontrol kararları

Final üretimde aşağıdaki kararlar bağlayıcıdır:

- Ca‘berî: `732/1332`.
- Hârice b. Zeyd: Zeyd b. Sâbit’in **oğlu**, `100/718-19`.
- Mervân b. Hakem: `65/685`.
- Ebû Şâme: `665/1267`.
- Muhammed Hamîdullah: `2002`.
- Varaka b. Nevfel ilk kullanımda tarih korunacaksa: `ö. 610 [?]`.
- Cevherî: tarih gerekiyorsa `ö. 400/1009’dan önce`; sözlük kaydı yalnız lügavî anlam için kullanılacak.
- Mehdevî: ilk kullanımda gerekiyorsa `440/1048-49 [?]`.
- İbn Mu‘âz el-Cühenî: `442/1050`.
- Sehâvî: `643/1245`.
- Amr b. Kays: bu çalışma hattında Basra’ya gönderildiği aktarılan kişinin kimliğiyle güvenli biyografik ölüm tarihi tam eşleştirilemediğinden `ö. ?` çıkarılacak; **yeni tarih eklenmeyecek**.
- `أُوْلوُا`: Bakara `2/269`.
- `وَوَصَّى / وَأَوْصَى`: Bakara `2/132`.
- `سَأُوْرِيكُمْ`: el-Enbiyâ `21/37`.
- `بِأَيْيْدٍ`: ez-Zâriyât `51/47`; kaynak açıkça söylemiyorsa `fonetik zorunluluktan dolayı` gerekçesi eklenmeyecek.
- Ana metin ev stili: **`Kur’an`**.
- Tarihsel özel terim: **`İmam Mushaf`**.
- `resm-i mushaf` ile `resm-i Osmânî` bağlama göre ayrılacak; otomatik eş anlamlı kullanılmayacak.
- `kırâat`, `rivâyet`, `tarîk`, `vecih` birbirinin yerine kullanılmayacak.
- telakki, müşâfehe ve edâ aynı kavram gibi kullanılmayacak.

# V. Google AI malzemesinin final üretimdeki sınırı

Aşama 3’te belirlenen karar değişmemiştir:

- Google AI’dan doğrulanmış tarih/kişi düzeltmesi, kaynak ipucu veya gerçekten yeni bilgi alınabilir.
- Google AI cümlesi doğrudan final öneriye kopyalanmayacaktır.
- `grafik plastisite`, `archetypus`, `epistemolojik havza`, `kanonizasyon`, `muazzam`, `sarsılmaz`, `deha`, `kurucu anayasa` ve benzeri yazarın mevcut diline yabancı terim/retorik final metne taşınmayacaktır.
- Google AI’nın `altı mushaf en güçlü sentezdir` gibi kaynaklardan daha ileri sonuçları kullanılmayacaktır.

# VI. Nihai rapor üretim sözleşmesi

Bir sonraki aşamada oluşturulacak `final/fourth-report-v2.md` için aşağıdaki şartlar zorunludur:

1. Kitap sırası korunacak: Önsöz → Giriş → Birinci → İkinci → Üçüncü → Dördüncü → Sonuç → gerekli kısa dipnot/kaynakça bölümü.
2. Her normal bulguda **Yer → İfade → Sorun → Önerilen düzeltme** bulunacak.
3. `İfade` güncel manuscriptten birebir alınacak. Parafraz/özet `İfade` olarak kullanılamaz.
4. Yapısal sorunlarda birden çok gerçek başlangıç cümlesi verilebilir; hangi pasajın hangi öneriyle değişeceği açıkça söylenecek.
5. “Kısaltın”, “birleştirin”, “geçiş ekleyin”, “yumuşatın” diye bırakılmayacak; yeni metin fiilen yazılacak.
6. Bir sorun doğru bilgi bulunarak çözülebiliyorsa bilgi silinmeyecek. Yalnız doğrulanamayan ayrıntı çıkarılabilir.
7. Sayfa numarası yardımcı konum olarak kalacak; Ctrl+F çıpasının yerine geçmeyecek.
8. `CAND-*`, Stage, PASS, audit, matrix, run, heading, OOXML, Zotero field gibi iç/teknik terimler yazara gösterilmeyecek.
9. Finalde frekans tabloları ve büyük envanter tabloları olmayacak.
10. Aynı sorun sırf eski envanterde ayrı kodla bulunduğu için ikinci kez raporlanmayacak; ancak ayrı Ctrl+F/uygulama işlemi gerektiriyorsa ayrı madde olacaktır.
11. 75 madde sınırı yoktur. Kapsam kaybını önlemek için final madde sayısı doğal olarak belirlenecektir.
12. Önerilen yeni cümlede mevcut dipnotun taşıyamayacağı yeni iddia oluşuyorsa dipnot ya daraltılacak ya ek kaynak açıkça önerilecektir.
13. Kaynaklı klasik hikmet/yorum malzemesi tamamen silinmek yerine gerektiğinde `X’e göre...` biçiminde doğru epistemik statüye çekilecektir.
14. Üçüncü Bölümde tekrar azaltılırken benzersiz kaynaklı içerik korunacak; savunmacı/vaaz üslubu ve teleolojik genellemeler ayıklanacaktır.
15. Final üretim bittikten sonra, her `İfade` için canonical extract üzerinde yeniden arama kontrolü yapılacaktır.

# VII. Audit makbuzu

- Aşama 6 taslağındaki yazar-facing madde: **75**.
- Büyük ölçüde korunabilir: **49**.
- `İfade` çıpası yeniden kurulması gereken: **20**.
- İçerik bakımından esaslı yeniden tasarlanması gereken: **3** (`52, 69, 74`).
- Soyut/genel not hâline dönüştürülecek: **3** (`68, 71, 72`).
- Eski 178 sorunla karşılaştırmada, V2 Aşama 6’nın daha geniş maddeleri altında sessizce görünmez olmuş çok sayıda somut editoryal işlem yeniden tespit edilmiş ve yukarıdaki geri-ekleme defterine kaydedilmiştir.
- Özellikle eski Aşama 4’ün 14 ek düzeltme grubundan V2 Aşama 6’da görünmeyenler geri alınmıştır.
- `Kur’an` ev stili hatası yakalanmıştır.
- Farklı baskılar için eski Aşama 6’da doğrulanmış somut kararların V2’de soyutlaşması yakalanmış ve geri yüklenmiştir.
- 3.7–3.12’nin aşırı sıkıştırılması sonucu oluşabilecek bilgi kaybı riski yakalanmıştır.
- Amr b. Kays için kimlik eşleştirilmeden yeni ölüm tarihi eklenmemesi kararı korunmuştur.

## Nihai readiness kararı

**Aşama 6 dosyası olduğu hâliyle final değildir.**

Ancak bu audit sonunda eksik/gizlenmiş işlemler, hatalı ev stili kararı, soyutlaşan bibliyografik kararlar ve aşırı yapısal sıkıştırma açık bir onarım planına bağlanmıştır. Bir sonraki aşama yeni bir araştırma veya yeniden keşif aşaması olmayacaktır; bu audit defterini uygulayarak doğrudan nihai yazar raporunu üretme aşaması olacaktır.

**Karar: FINAL ÜRETİME HAZIR, ANCAK AŞAMA 7 ONARIMLARI UYGULANMADAN AŞAMA 6 TERFİ ETTİRİLEMEZ.**