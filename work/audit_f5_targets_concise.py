#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys, re
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='ffd4c4e8fabd7bd157cd21251f18da065e5466ecce357b63efe80361a18e4543'
TARGETS={
19:'Zira söz konusu rivâyetlerde geçen cem (toplama) ifadesi yazılı malzemelerin fiziki olarak bir araya getirilmesi değil, Kur\'an\'ın ezberlenmesi anlamında açıklanmıştır.',
20:'Dolayısıyla "iki şâhit" ezber ve yazı bütünlüğünü ifade etmektedir.',
21:'Dolayısıyla Hz. Ebû Bekir ile Hz. Osman dönemleri arasında bir çelişki değil, şartlara göre şekillenmiş iki farklı tedbir söz konusudur.',
22:'Hülasa, istinsah kararı, vahyin aslını değiştirme veya yeni bir metin oluşturma girişimi değildir.',
23:'Bu bağlamda hâfız sahâbîler yeni Müslüman olan topluluklara Kur\'an öğretmek üzere farklı merkezlere gönderilmiştir.',
24:'Dolayısıyla Hz. Osman döneminde gerçekleştirilen istinsah faaliyeti, tarihsel ve toplumsal zemin üzerinde ortaya çıkmıştır.',
25:'Böylece toplam altı nüshanın varlığı ihtimalî kuvvet kazanmaktadır.',
26:'Böylece resm bir izden ziyade, belirli bir düzen içinde çizilmiş harfler bütünü anlamını kazanmıştır.',
27:'Sonuç olarak Cürcânî ve Kastallânî\'nin tanımları, resmin ıstılâhî çerçevesini iki temel prensip üzerine oturtur ve bunları, temsil ve uygunluk olarak belirler.',
28:'O, Osman mushaflarının yazımını bağımsız bir imlâ tercihi olarak değil, sahâbe nakline dayanan bağlayıcı bir metin geleneği olarak değerlendirmiştir.',
29:'Diğer bir ifadeyle Dânî\'ye göre resm, sadece kelimelerin nasıl yazıldığını değil, hangi mushaf merkezinde hangi yazımın tercih edildiğini inceleyen karşılaştırmalı bir alandır.',
30:'Mushaf yazımında esas olan dilcilerin kıyas yoluyla ulaştıkları imlâ kuralları değil, güvenilir nakille sabit olmuş yazım geleneğidir.',
31:'Diğer bir ifadeyle resm alanında belirleyici olan şey kıyas değil, rivâyet ve nakildir.',
32:'Sonuç olarak işaret edilen hususlar, resm-i Osmânî\'nin doğasını net bir biçimde ortaya koymaktadır.',
33:'Ona göre ilk dönem mushaflarında görülen noktasızlık ve harekesizlik, bazı harflerin düşmesi veya farklı yazım şekilleri, bir eksiklik veya hata değil, erken dönem Arap yazısının tabii özellikleridir.',
34:'Sonuç olarak rivâyetle ilgili kaynaklar birlikte değerlendirildiğinde şu tablo ortaya çıkmaktadır:',
35:'Nitekim İmâm Mâlik\'ten nakledilen rivâyetlerde, mushafın insanların sonradan benimsediği yazı biçimine göre değil, ilk yazıldığı şekil üzere yazılması gerektiği belirtilmiş',
36:'Ona göre bu rivâyetin, Hz. Peygamber\'e nispeti sabit kalacak derecede sahih değildir ve bu sebeple delil olarak kullanılması doğru değildir.',
37:'Bu bağlamda bütün resm kuralları aynı derecede işlevsel değildir.',
38:'Vurgulamak gerekir ki, bu altı imlâ özelliği birlikte değerlendirildiğinde şu önemli sonuçlar ortaya çıkmaktadır:',
39:'Bu düşürme rastgele bir eksiltme değildir; erken mushaf yazım geleneğine bağlı, kurallı ve çoğu zaman hikmetli bir tercihtir.',
40:'Erken dönem mushaflarında hemzenin çoğu zaman müstakil bir harf olarak gösterilmemesi Osmânî mushaf yazımının hem teknik hem de tarihî karakterini anlamak bakımından önem arz etmektedir.',
41:'Ziyâde, resm-i Osmânî\'nin temel yazım kurallarından biri olmakla beraber, hazf kadar yaygın ve belirleyici değildir.',
42:'Sonuç olarak Hz. Osman döneminde gerçekleştirilen istinsah faaliyetleri, yalnızca mushafların çoğaltılmasıyla sınırlı kalmamış',
43:'Diğer bir ifadeyle kırâat Kur\'an lafızlarının güvenilir rivâyetlerle nakledilmiş ve okunmuş biçimleri demektir.',
44:'Ancak kırâat sadece "farklı okuma" anlamına gelmemektedir.',
45:'Kur\'an sadece yazıya geçirilmiş bir metinden ibaret olmayıp, aynı zamanda okunarak aktarılan bir kitaptır.',
46:'Kırâat ilmini anlamanın en sağlam yollarından biri, onu sadece "farklı okuyuşlar" meselesi olarak değil, rivâyet, sened ve ilmî otorite üzerine kurulmuş bir aktarım düzeni olarak ele almaktır.',
47:'Bu durum kırâat ilminin baştan itibaren yazılı değil, birebir öğretim geleneği içinde geliştiğini göstermektedir.',
48:'Bu yüzden kırâat ilminde rivâyet, sadece metin aktarımı değil, aynı zamanda okuyuş biçimini aktarma işidir.',
49:'Bu bağlamda İbnü\'l-Cezerî, kırâat ilmini tanımlarken onun Kur\'an kelimelerinin edâ keyfiyetlerini ve bu keyfiyetlerdeki ihtilafı nakleden imamlar yoluyla bilme ilmi olduğunu Tâceddîn Subkî\'den',
50:'Mesela "Âsım (ö. 127/745) kırâati" denildiğinde burada sadece Âsım\'ın tercih ettiği okuyuş biçimi değil',
51:'Çünkü kırâat ilmi, sadece farklılıkları kaydeden bir alan değil, aynı zamanda hangi okuyuşun güvenilir sayılacağını',
52:'Sonuç olarak kırâatlerde otorite ekseni Kur\'an\'ın doğru okuyuşunu koruyan çok yönlü bir ilmî geleneği ifade eder.',
53:'Klasik literatürde bu konuda öne çıkan ilk görüş Hz. Osman\'ın insanları yedi harfin tamamı üzerine değil, ihtilafı ortadan kaldıracak bir harf üzerine topladığı görüşüdür.',
54:'Netice itibarıyla resm-i mushaf, klasik tefsîr ve kırâat geleneğinde sadece Kur\'an\'ın yazılı biçimi olarak değil',
55:'Kırâat geleneğinde bu husus, resm-i Osmânî\'nin sıradan bir yazım biçimi değil, kırâatlerin rivâyetini koruyan özel bir sistem olduğunu gösteren temel delillerden biri olduğunu daha önce de zikretmiştik.',
56:'Böylece yazım tercihi, yalnızca şekle ilişkin bir farklılık olmaktan çıkmakta, doğrudan edatın cümle içindeki nahivsel görevini ve anlam yönelimini de göstermektedir.',
57:'Sözü edilen örnekler resm-i mushaf\'ın yalnızca imlâya ilişkin bir tercih olmadığını, aynı zamanda anlamı yönlendiren ve nahivsel ayrımları belirginleştiren bir işaretleme sistemi olduğunu göstermektedir.',
58:'Normal kıyasa göre kapalı "ta" ile yazılması beklenen bazı kelimelerin mushaflarda açık "ta" ile yazılması, âlimler tarafından sadece yazım farkı olarak değerlendirilmemiş, lehçe izi olarak değerlendirilmiştir.',
59:'Bu sebeple kaynaklarda mushaf hattının bazı yerlerde bir kelimenin sadece o andaki telaffuz şeklini değil, onun aslî yapısını',
60:'Diğer bir ifadeyle resm-i Osmânî, lafzın işitilen tarafını kaydettiği kadar âyetin hitap gücünü de resm üzerinde muhafaza etmektedir.',
61:'Diğer bir ifadeyle mushaf hattı bazı yerlerde kelimenin nasıl okunacağından ziyade o kelimenin cümle içinde hangi türden bir yapı kurduğunu da okuyucuya hissettirmektedir.',
62:'Söz konusu örneklerden hareketle şu önemli neticeye varılabilir: Nahiv âlimleri için resm-i mushaf sadece sıradan bir imlâ mirası değildir.',
63:'Bu bağlamda resm-i mushaf\'ı, sadece tarihi bir yazım biçimi olarak değil, metnin korunmuşluğunu ve kırâatlerin meşruiyetini destekleyen bir zemin olarak değerlendirmek gerekir.',
64:'Resm-i Osmânî\'ye Bağlılığın Hata ve Tahriften Koruyucu İşlevi',
65:'Bu bakımdan resm-i Osmânî, kırâatlerin asıl kaynağı olarak görülmeyip, sahih rivâyetleri yazı düzeyinde sabitleyen ve onları müşterek bir çerçeve içinde koruyan tamamlayıcı bir unsur olarak öne çıkmaktadır.',
66:'Kırâat vecihlerinin naklinde aslî dayanak, yazılı metinden önce telakki ve müşâfehedir.',
67:'Bütün bunlar birlikte düşünüldüğünde Osmânî resmin kırâat vecihlerinin rivâyet ve naklinde üç yönlü bir rol üstlendiği söylenebilir.',
68:'Bu yönüyle Osmânî resm, sahâbe mushaflarından gelen okuyuş çeşitliliğini nihai mushaf otoritesi bakımından ayıklayan',
69:'Bu noktada dikkat çekici olan husus, söz konusu tasarrufun sahâbenin genel mutabakatı içinde gerçekleşmiş olmasıdır.',
70:'Sonuç olarak bu veriler birlikte değerlendirildiğinde, sahâbe mushaflarının yakılması meselesinin, Kur\'an tarihindeki en önemli birleştirici adımlardan biri olduğu görülmektedir.',
71:'Bütün bu veriler ışığında, resm-i Osmânî\'ye aykırı kırâat vecihlerinin mensuh ve şâz sayılması meselesinin',
72:'Bu sebeple meşhur kırâat imamlarının tercihleri, rivâyet malzemesi içinden yapılmış serbest seçimler değildir;',
73:'Bu çerçevede vakıf, salt fonetik bir tercihten öte, yazı ile okuyuş arasında kurulan disiplinli ilişkinin görünür tezahürlerinden biri hâline gelmektedir.',
74:'Bu noktada Dânî\'nin, emsâr mushaflarında farklılık gösteren harflerin tamamının Hz. Osman\'ın yazdırdığı imam mushaftan istinsah edilen nüshalarda bulunduğunu',
75:'Bu çerçevede denilebilir ki Osmânî mushafların hecâsına dair rivâyetler, yalnız yazı tarihine ilişkin malumat sunan tali veriler değildir.',
76:'Çağdaş Basılı Mushaflarda Resm-i Osmânî\'nin Korunması ve Klasik Kaynaklara Dayalı Yazım Geleneği',
77:'Bu çerçevede çağdaş mushaf neşirlerinde resm-i Osmânî\'nin korunması üç temel amaca hizmet etmektedir.',
78:'Bütün bu veriler birlikte değerlendirildiğinde, çağdaş matbu mushaflarda resm-i Osmânî\'nin korunmasının gelişigüzel bir tercih olmadığı açıkça anlaşılmaktadır.',
79:'Başka bir ifadeyle, mushafın hangi kırâat rivâyetine göre düzenlendiği meselesi sadece yazım tekniğine dair bir tercih olarak kalmamış;',
80:'Bütün bu veriler, matbu mushafların sadece mevcut okuyuşları pasif biçimde yansıtan araçlar olmadığını göstermektedir.',
81:'Bununla birlikte mevcut veriler, istinsahın yeni bir Kur\'an metni oluşturma girişimi olmadığını;',
82:'Yazının bir okuyuşu mümkün kılması, o okuyuşun sahih olduğunu göstermemektedir.',
83:'Resme uygunluk tek başına yeterli değildir.',
84:'Resm-i Osmânî\'nin normatif bağlayıcılığı, onun bütün ayrıntılarının tartışmasız biçimde tevkîfî olduğu iddiasıyla özdeş değildir.',
85:'Sonuç olarak resm-i Osmânî, kırâati doğuran bağımsız kaynak değil, rivâyet yoluyla nakledilen kırâatlerin ortak yazılı sınırıdır.'}
GLOBAL=['Sonuç olarak','Netice itibarıyla','Hülasa','Bütün bu veriler','Bütün bunlar birlikte düşünüldüğünde','Bu bağlamda','Bu çerçevede','göstermektedir','ortaya koymaktadır','açıkça ortaya koymaktadır','anlaşılmaktadır','Nitekim','Dolayısıyla','Böylece','Bu noktada','Bu yönüyle','Bununla birlikte','Diğer bir ifadeyle','Başka bir ifadeyle','dikkat çekici','önemlidir','önem arz etmektedir','Vurgulamak gerekir','vurgulamak gerekir','Bu durum','Bu yaklaşım','Bu süreç']
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def txt(e): return ''.join(e.xpath('.//w:t/text()',namespaces=NS))
def norm(s):
    return s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('‐','-').replace('‑','-').replace('–','-').replace('—','-').lower()
def quoted_ranges(s):
    out=[]
    # curly quotes
    pos=0
    while True:
        a=s.find('“',pos)
        if a<0: break
        b=s.find('”',a+1)
        if b<0: break
        out.append((a,b+1)); pos=b+1
    # straight quote pairs
    pts=[m.start() for m in re.finditer('"',s)]
    for a,b in zip(pts[0::2],pts[1::2]): out.append((a,b+1))
    return out
def inquote(s,a,b): return any(a>=x and b<=y for x,y in quoted_ranges(s))
if len(sys.argv)!=3: raise SystemExit('usage: audit_f5_targets_concise.py INPUT OUTPUT')
src=Path(sys.argv[1]); out=Path(sys.argv[2]); got=sha(src)
if got!=EXPECTED: raise RuntimeError(f'input sha mismatch {got}')
with ZipFile(src) as z:
    d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
    if len(ps)!=674: raise RuntimeError(len(ps))
    texts=[txt(p) for p in ps]; norms=[norm(s) for s in texts]
    print('SPECIFIC_TARGETS')
    for n,a in TARGETS.items():
        na=norm(a); hits=[i for i,s in enumerate(norms) if na in s]
        print(f'F5-{n:03d}\tHITS={hits}')
    print('GLOBAL_PATTERNS')
    for phrase in GLOBAL:
        np=norm(phrase); rec=[]
        for i,s in enumerate(norms):
            st=0
            while True:
                j=s.find(np,st)
                if j<0: break
                rec.append((i,inquote(texts[i],j,j+len(np)))); st=j+len(np)
        compact=','.join(f'{i}{"Q" if q else ""}' for i,q in rec)
        print(f'PATTERN\t{phrase}\tCOUNT={len(rec)}\t{compact}')
    # author negatives outside obvious quotes, paragraph-level unique indices
    for needle in ['değildir','değil']:
        idx=[]
        for i,s in enumerate(norms):
            st=0; found=False
            while True:
                j=s.find(needle,st)
                if j<0: break
                if not inquote(texts[i],j,j+len(needle)): found=True
                st=j+len(needle)
            if found: idx.append(i)
        print(f'AUTHOR_NEGATIVE\t{needle}\tPARAS={idx}')
shutil.copyfile(src,out)
if sha(out)!=got: raise RuntimeError('copy mismatch')
print('BYTE_IDENTICAL_COPY=PASS')
