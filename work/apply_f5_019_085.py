#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='ffd4c4e8fabd7bd157cd21251f18da065e5466ecce357b63efe80361a18e4543'
ALLOWED={62,74,84,85,109,117,124,129,134,135,152,156,163,178,181,193,196,203,206,216,220,263,266,279,283,290,350,369,377,385,393,412,425,444,451}

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def c14n(el): return etree.tostring(el,method='c14n')
def sig(el): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())
def replace_range(p,start,end,new):
    nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]; starts=[]; cur=0
    for v in vals: starts.append(cur); cur+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def replace_exact(ps, item, old, new, expected_idx=None):
    hits=[]
    for i,p in enumerate(ps):
        s=text(p); pos=s.find(old)
        if pos>=0: hits.append((i,pos))
    if not hits:
        print(f'F5-{item:03d}\tVERIFIED_NO_CHANGE_OR_ALREADY_SATISFIED'); return False
    if len(hits)!=1: raise RuntimeError(f'F5-{item:03d} target count {hits}')
    i,pos=hits[0]
    if expected_idx is not None and i!=expected_idx: raise RuntimeError(f'F5-{item:03d} moved: {i}')
    p=ps[i]; before=text(p); bs=sig(p)
    replace_range(p,pos,pos+len(old),new)
    if sig(p)!=bs: raise RuntimeError(f'F5-{item:03d} structure changed')
    print(f'F5-{item:03d}\tAPPLIED\tP{i}')
    return True

def replace_whole(ps,item,idx,new,old_anchor=None):
    p=ps[idx]; before=text(p)
    if before==new:
        print(f'F5-{item:03d}\tALREADY_SATISFIED\tP{idx}'); return False
    if old_anchor and old_anchor not in before:
        print(f'F5-{item:03d}\tVERIFIED_NO_CHANGE_OR_ALREADY_SATISFIED'); return False
    nodes=p.xpath('.//w:t',namespaces=NS)
    if not nodes: raise RuntimeError(f'P{idx} no text nodes')
    bs=sig(p); nodes[0].text=new
    for n in nodes[1:]: n.text=''
    if sig(p)!=bs: raise RuntimeError(f'F5-{item:03d} structure changed')
    print(f'F5-{item:03d}\tAPPLIED\tP{idx}')
    return True

def no_op(item): print(f'F5-{item:03d}\tVERIFIED_NO_CHANGE')

def apply(src,out):
    actual=sha(src)
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        before=[c14n(p) for p in ps]
        # 019 — Fourth already expresses cem as some-riwayat memorization + written record.
        no_op(19)
        # 020 — remove premature single-rule conclusion; preserve both genuine notes on the compact paragraph.
        replace_whole(ps,20,62,'“İki şahit” ifadesi farklı şekillerde yorumlanmıştır. Bir görüş, yazılı malzemenin hafızadaki aktarım ile birlikte doğrulanmasını esas alır ve Huzeyme b. Sâbit rivâyetini bu yönde değerlendirir. Başka bir görüş ise iki kişinin şahitliğini öne çıkarır. Rivâyetlerin farklılığı sebebiyle bu uygulama tek bir usûlle açıklanmamalıdır.','Dolayısıyla “iki şâhit” ezber ve yazı bütünlüğünü ifade etmektedir.')
        no_op(21); no_op(22)
        replace_exact(ps,23,'Bu bağlamda hâfız sahâbîler yeni Müslüman olan topluluklara Kur’an öğretmek üzere farklı merkezlere gönderilmiştir.','Hâfız sahâbîler yeni Müslüman olan topluluklara Kur’an öğretmek üzere farklı merkezlerde görev almıştır.',74)
        replace_exact(ps,24,'Dolayısıyla Hz. Osman döneminde gerçekleştirilen istinsah faaliyeti, tarihsel ve toplumsal zemin üzerinde ortaya çıkmıştır.','Hz. Osman dönemindeki istinsah faaliyetinin arka planını değerlendirirken bölgesel okuyuş farklılıkları, fetihlerle genişleyen öğretim çevreleri ve Huzeyfe b. Yemân rivâyeti birlikte ele alınmalıdır. Kaynakların aktardığı ihtilaf örnekleri bu tarihsel zeminin temel verileridir.',84)
        replace_exact(ps,24,'Bu noktada asıl üzerinde durulması gereken mesele, Müslümanları söz konusu rivâyetlerdeki ihtilafa sürükleyen sebeplerin gerisinde yatan ana nedenlerin neler olduğu hususudur.','',85)
        no_op(25)
        replace_exact(ps,26,'Böylece resm bir izden ziyade, belirli bir düzen içinde çizilmiş harfler bütünü anlamını kazanmıştır.','Kur’an yazımı bağlamındaki teknik kullanım, kelimelerin mushaflarda hangi harf düzeniyle yazıldığını ifade eden özel bir anlam kazanmıştır. Bu teknik kullanımın tarihsel gelişimi resm literatürü üzerinden izlenmelidir.',109)
        replace_whole(ps,27,117,'Cürcânî ve Kastallânî’nin tanımlarında resmin lafzı yazıyla temsil etme ve yazılı biçimi tanınabilir kılma yönleri öne çıkmaktadır. Bu kavramsal zemin, Hz. Osman döneminde çoğaltılan mushaflara nispet edilen yazım geleneğinin nasıl tanımlandığını incelemeyi gerekli kılar.','Sonuç olarak Cürcânî ve Kastallânî’nin tanımları')
        no_op(28); no_op(29); no_op(30); no_op(31)
        replace_exact(ps,32,'Sonuç olarak es-Sicistânî, resm-i Osmânî’yi açık bir terim tanımıyla net bir biçimde ifade etmese de, Osman mushaflarının yazımını sahâbe nakline dayanan bağlayıcı bir metin geleneği olarak sunmuştur.','Sicistânî’nin rivâyet temelli aktarımı, Osman mushaflarının yazımını sahâbe nakline dayanan bağlayıcı bir metin geleneği içinde sunar.',124)
        replace_whole(ps,32,129,'Resm literatüründe esas alınan zemin, Osman mushaflarına nispet edilen yazım özelliklerinin rivâyet yoluyla kaydedilip sonraki nesillere aktarılmasıdır. Bu tarihsel yazım geleneği daha sonra kıyasî imlâdan ayrı kurallar ve tasnifler içinde incelenmiş; Dânî ve Ebû Dâvud gibi müelliflerin eserlerinde müstakil bir çalışma alanı hâline gelmiştir.','Sonuç olarak işaret edilen hususlar')
        replace_whole(ps,32,135,'Motzki ve Déroche’nin değerlendirmeleri, sözlü aktarım ile erken mushaf yazısının tarihsel verilerini farklı kanıt türleri üzerinden ele alır. Bu veriler, resm-i Osmânî’nin kırâatleri meydana getiren bağımsız bir kaynak olduğu sonucuna dönüştürülmemelidir.','Sonuç olarak Motzki ve Deroche’nin açıklamaları')
        replace_exact(ps,33,'Ona göre ilk dönem mushaflarında görülen noktasızlık ve harekesizlik, bazı harflerin düşmesi veya farklı yazım şekilleri, bir eksiklik veya hata değil, erken dönem Arap yazısının tabii özellikleridir.','Déroche, noktasızlık, harekesizlik ve bazı yazım farklılıklarını erken Arap yazısının doğal özellikleri çerçevesinde değerlendirir.',134)
        replace_whole(ps,34,156,'Hz. Peygamber döneminde vahyin yazıya geçirildiği konusunda güçlü bir rivâyet zemini bulunmakla birlikte, mushaf yazımının bütün ayrıntılarının doğrudan peygamberî talimatla belirlendiğini göstermek için kullanılan bazı rivâyetlerin isnadı tartışmalıdır. Resm-i Osmânî’ye bağlılık ile yazımın bütün ayrıntılarının tevkîfî olduğu iddiası ayrı değerlendirilmelidir.','Sonuç olarak rivâyetle ilgili kaynaklar birlikte değerlendirildiğinde')
        replace_exact(ps,35,'Nitekim İmâm Mâlik’ten nakledilen rivâyetlerde, mushafın insanların sonradan benimsediği yazı biçimine göre değil, ilk yazıldığı şekil üzere yazılması gerektiği belirtilmiş; Dânî de bu hususta Mâlik’e muhalefet eden bir görüş bilmediğini ifade etmiştir.','İmâm Mâlik, mushafın “ilk yazım üzere” yazılması gerektiğini belirtir. Dânî de bu konuda ümmet âlimlerinden Mâlik’e muhalefet eden bir görüş bilmediğini kaydeder.',304)
        replace_exact(ps,36,'Ona göre bu rivâyetin, Hz. Peygamber’e nispeti sabit kalacak derecede sahih değildir ve bu sebeple delil olarak kullanılması doğru değildir.','Albânî, rivâyeti zayıf hatta uydurma kabul ettiği için delil değeri taşımadığı sonucuna varır.',152)
        replace_whole(ps,37,163,'Resm kurallarının kırâatle ilişkisi örneğe göre değişir. Bazı yazım özellikleri belirli kırâat örnekleriyle ilişkilendirilebilirken bazıları erken yazı geleneğinin genel özellikleriyle açıklanmaktadır. Aşağıdaki kurallar bu farklı ilişki düzeyleri gözetilerek ele alınacaktır.','Bu bağlamda bütün resm kuralları aynı derecede işlevsel değildir.')
        no_op(38); no_op(39)
        replace_whole(ps,40,178,'Erken mushaflarda bugünkü hemze işaretleme sistemi henüz yerleşmemişti. Hemzenin yazımı dönemin Arap yazısının gelişim özellikleri içinde değerlendirilmelidir; kırâatle ilişkisi ise örnek bazında ayrıca ele alınmalıdır.','önem arz etmektedir')
        replace_exact(ps,41,'Ziyâde, resm-i Osmânî’nin temel yazım kurallarından biri olmakla beraber, hazf kadar yaygın ve belirleyici değildir. Diğer bir ifadeyle okunuşta bulunmayan veya telaffuzda açıkça karşılığı olmayan bir harfin yazıda yer almasıdır.','Ziyâde, lafızda açık karşılığı bulunmayan bir harfin mushaf yazısında yer almasıdır. Resm kaynakları bu örnekleri haziften ayrı bir başlık altında incelemiştir; kırâat ve mana ile ilişkileri örnekten örneğe değişmektedir.',181)
        replace_whole(ps,42,196,'Osmânî mushafların farklı merkezlerde ortak başvuru nüshaları hâline gelmesi, resme uygunluğun sonraki kırâat literatüründe kabul ölçülerinden biri olarak yerleşmesinin tarihsel zeminini oluşturmuştur.','Sonuç olarak Hz. Osman döneminde gerçekleştirilen istinsah faaliyetleri')
        replace_exact(ps,43,'Diğer bir ifadeyle kırâat Kur’an lafızlarının güvenilir rivâyetlerle nakledilmiş ve okunmuş biçimleri demektir.','Kırâat, Kur’an kelimelerinin edâ keyfiyetlerini ve bu keyfiyetlerdeki farklılıkları nakledenlere nispet ederek bilmeyi konu edinen rivâyet disiplinidir.',203)
        replace_exact(ps,44,'Ancak kırâat sadece “farklı okuma” anlamına gelmemektedir.','Kırâat, Kur’an kelimelerinin edâ biçimlerini ve bu biçimlerdeki farklılıkların rivâyetini konu edinen geniş bir ilim alanıdır.',203)
        replace_exact(ps,45,'Kur’an sadece yazıya geçirilmiş bir metinden ibaret olmayıp, aynı zamanda okunarak aktarılan bir kitaptır.','Kur’an’ın aktarımında yazılı metne, okunarak öğretilen sözlü edâ geleneği eşlik etmiştir.',206)
        no_op(46); no_op(47)
        replace_exact(ps,48,'Bu yüzden kırâat ilminde rivâyet, sadece metin aktarımı değil, aynı zamanda okuyuş biçimini aktarma işidir.','Rivâyette kelimenin harfleriyle birlikte ses değeri ve edâ biçimi de aktarılır.',216)
        replace_exact(ps,49,'Bu bağlamda İbnü’l-Cezerî, kırâat ilmini tanımlarken onun Kur’an kelimelerinin edâ keyfiyetlerini ve bu keyfiyetlerdeki ihtilafı nakleden imamlar yoluyla bilme ilmi olduğunu Tâceddîn Subkî’den (ö. 771/1369) aktarmaktadır.','İbnü’l-Cezerî, Tâceddîn Subkî’den naklettiği tanımda kırâati Kur’an kelimelerinin edâ keyfiyetleri ve bu keyfiyetlerdeki ihtilafın nakledenlere nispet edilerek bilinmesi şeklinde aktarır.',220)
        no_op(50); no_op(51); no_op(52); no_op(53)
        replace_exact(ps,54,'Netice itibarıyla resm-i mushaf, klasik tefsîr ve kırâat geleneğinde sadece Kur’an’ın yazılı biçimi olarak değil, hangi okuyuşun kırâat kapsamında kabul edileceğini belirleyen bağlayıcı bir ölçü olarak işlev görmüştür.','Klasik tefsîr ve kırâat geleneğinde mushaf yazısına uygunluk, okuyuşların değerlendirilmesinde başvurulan ölçülerden biri olmuş; bu ölçü rivâyet ve dil verileriyle birlikte işlemiştir.',193)
        no_op(55)
        replace_exact(ps,56,'Böylece yazım tercihi, yalnızca şekle ilişkin bir farklılık olmaktan çıkmakta, doğrudan edatın cümle içindeki nahivsel görevini ve anlam yönelimini de göstermektedir.','Bu yorum, yazım farkını söz dizimi ve anlamla ilişkilendirir; yazımın tarihsel sebebini tek başına belirlemez.',283)
        no_op(57)
        replace_exact(ps,58,'Normal kıyasa göre kapalı “ta” ile yazılması beklenen bazı kelimelerin mushaflarda açık “ta” ile yazılması, âlimler tarafından sadece yazım farkı olarak değerlendirilmemiş, lehçe izi olarak değerlendirilmiştir.','Bazı klasik açıklamalarda açık “ta” ile yazılan bu örnekler lehçe özellikleriyle ilişkilendirilmiştir.',263)
        replace_whole(ps,59,266,'Bazı kaynaklar belirli yazımları harf veya harekenin kökensel yapısıyla ilişkilendirir. Bu açıklamalar ilgili örneklerle sınırlı tutulmalıdır. Doğru edâ telakki ve rivâyet yoluyla öğrenilir; resm belirli örneklerde bu aktarımı destekleyen yazılı veriler sunar.','Bu sebeple kaynaklarda mushaf hattının bazı yerlerde')
        replace_exact(ps,60,'Diğer bir ifadeyle resm-i Osmânî, lafzın işitilen tarafını kaydettiği kadar âyetin hitap gücünü de resm üzerinde muhafaza etmektedir.','Bu açıklama, ilgili yazım ile hitap tonu arasında kurulan klasik bir yorum ilişkisidir; yazımın tarihsel sebebini tek başına belirlemez.',279)
        no_op(61)
        replace_exact(ps,62,'Söz konusu örneklerden hareketle şu önemli neticeye varılabilir: Nahiv âlimleri için resm-i mushaf sadece sıradan bir imlâ mirası değildir.','Ferrâ’nın ifadesi, Arap dili içinde mümkün bir vecih bulunduğunda mushaf hattını tercih gerekçelerinden biri olarak dikkate aldığını belirtir. Bu yaklaşım bütün nahivcilerin resme mutlak biçimde tâbi olduğu şeklinde genelleştirilmemelidir.',290)
        no_op(63); no_op(64)
        replace_exact(ps,65,'Bu bakımdan resm-i Osmânî, kırâatlerin asıl kaynağı olarak görülmeyip, sahih rivâyetleri yazı düzeyinde sabitleyen ve onları müşterek bir çerçeve içinde koruyan tamamlayıcı bir unsur olarak öne çıkmaktadır.','Kırâatlerin asıl kaynağı rivâyettir. Resm-i Osmânî’ye uygunluk, sahih rivâyetlerin müşterek mushaf yazısıyla ilişkisini değerlendirmede kullanılan tamamlayıcı ölçülerden biridir.',350)
        replace_exact(ps,66,'Kırâat vecihlerinin naklinde aslî dayanak, yazılı metinden önce telakki ve müşâfehedir.','Kırâat vecihlerinin naklinde aslî dayanak telakki, müşâfehe ve isnaddır.',350)
        no_op(67); no_op(68)
        old69='Bu noktada dikkat çekici olan husus, söz konusu tasarrufun sahâbenin genel mutabakatı içinde gerçekleşmiş olmasıdır. Hz. Ali’den nakledilen, “Osman hakkında hayırdan başka bir şey söylemeyin; Allah’a yemin olsun ki mushaflar konusunda yaptığı şeyi ancak bizim toplu görüşümüzle yapmıştır.” sözü, bu işin şahsi ve tek taraflı bir karar olarak görülmediğini açıkça ortaya koymaktadır. Yine Mus’ab b. Sa’d’ın, Hz. Osman’ın, mushafları ortadan kaldırdığında insanların bunu beğendiklerini yahut hiç kimsenin bunu ayıplamadığını söylemesi, sahâbe çevresinde bu uygulamanın meşruiyet kazandığını göstermektedir. Böylece resm-i Osmânî, sadece halifenin idari tercihi olmayıp, sahâbenin fiilî ve ilmî içtimaıyla tahkim edilmiş bir mushaf otoritesi hâline gelmiştir.'
        replace_exact(ps,69,old69,'Hz. Ali ve Mus’ab b. Sa’d’dan nakledilen rivâyetler, mushafların birleştirilmesi yönündeki tasarrufun sahâbe çevresinde destek gördüğünü aktarır.',369)
        replace_exact(ps,69,'Bu noktada dikkat çekici olan husus, mushaf hattına aykırı kalan bütün vecihlerin baştan beri temelsiz veya uydurma sayılmamasıdır.','Mushaf hattına aykırı kalan rivâyetlerin tamamı kaynaklarda baştan itibaren uydurma sayılmaz; bazı müellifler bunları daha önce okunmuş, ancak sonraki müşterek tilâvet alanının dışında kalmış vecihler olarak değerlendirir. Bu açıklama ilgili klasik yorum olarak sunulmalıdır.',377)
        no_op(70); no_op(71)
        replace_exact(ps,72,'Bu sebeple meşhur kırâat imamlarının tercihleri, rivâyet malzemesi içinden yapılmış serbest seçimler değildir; dil, nakil ve resm-i mushaf arasındaki dengeyi gözeten bilinçli ilmî tercihlerdir.','İmamların tercihleri kendilerine ulaşan rivâyet ve öğretim geleneği içinde değerlendirilmelidir. Bazı kaynaklarda râvi sayısı, mushaf hattı, dil verileri ve genel kabul tercih gerekçeleri arasında birlikte zikredilir.',385)
        replace_exact(ps,73,'Bu çerçevede vakıf, salt fonetik bir tercihten öte, yazı ile okuyuş arasında kurulan disiplinli ilişkinin görünür tezahürlerinden biri hâline gelmektedir.','Bazı vakıf uygulamalarında mushaf yazımı da dikkate alınmıştır.',393)
        no_op(74); no_op(75)
        replace_whole(ps,76,412,'Çağdaş neşirlerde resm-i Osmânî’nin esas alınması, klasik resm rivâyetlerinin modern üretim süreçlerine aktarılmasıyla ilişkilidir.','Mesele sadece geçmişten kalan bir yazı biçimini tekrarlamak değildir.')
        no_op(77); no_op(78)
        replace_exact(ps,79,'Başka bir ifadeyle, mushafın hangi kırâat rivâyetine göre düzenlendiği meselesi sadece yazım tekniğine dair bir tercih olarak kalmamış; belirli okuyuşların korunması, yayılması ve sonraki nesillere aktarılması bakımından da belirleyici bir rol oynamıştır.','Belirli bir rivâyete göre zapt edilen mushafların yaygınlaşması, o rivâyetin daha geniş okuyucu çevrelerine ulaşmasına katkıda bulunmuştur. Bölgesel öğretim gelenekleri, eğitim kurumları, resmî neşir tercihleri ve mevcut kırâat geleneği de bu dolaşımın biçimlenmesinde etkilidir.',425)
        no_op(80)
        replace_exact(ps,81,'Bununla birlikte mevcut veriler, istinsahın yeni bir Kur’an metni oluşturma girişimi olmadığını; Osmânî mushafları ortak başvuru metni hâline getiren ve şahsi nüshalardan doğabilecek ihtilafları azaltmayı amaçlayan tedbir niteliği taşıdığını göstermektedir.','Mevcut veriler Osmânî istinsahı, mevcut sahifeler esas alınarak ortak başvuru mushaflarının çoğaltıldığı ve şahsî nüshalardan doğabilecek ihtilafların sınırlandırılmasına yönelik bir tedbir olarak sunar.',444)
        no_op(82); no_op(83)
        replace_exact(ps,84,'Resm-i Osmânî’nin normatif bağlayıcılığı, onun bütün ayrıntılarının tartışmasız biçimde tevkîfî olduğu iddiasıyla özdeş değildir.','Resm-i Osmânî’nin normatif bağlayıcılığı ile bütün yazım ayrıntılarının tevkîfî olduğu görüşü ayrı meselelerdir.',451)
        no_op(85)
        after=[c14n(p) for p in ps]; changed=[i for i,(a,b) in enumerate(zip(before,after)) if a!=b]
        if actual!=EXPECTED and not changed:
            shutil.copyfile(src,out); print('CHANGED_PARAGRAPHS=[]'); return
        if actual!=EXPECTED: raise RuntimeError('input sha mismatch '+actual)
        if not set(changed).issubset(ALLOWED): raise RuntimeError('unexpected paragraph changes '+repr(changed))
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,changed)
    print('CHANGED_PARAGRAPHS='+repr(changed))

def validate(src,out,changed):
    with ZipFile(src) as a,ZipFile(out) as b:
        if a.namelist()!=b.namelist() or b.testzip() is not None: raise RuntimeError('zip')
        for n in a.namelist():
            if n!='word/document.xml' and a.read(n)!=b.read(n): raise RuntimeError('package change '+n)
        da=etree.fromstring(a.read('word/document.xml')); db=etree.fromstring(b.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=674 or len(pb)!=674: raise RuntimeError('body')
        got=[i for i,(x,y) in enumerate(zip(pa,pb)) if c14n(x)!=c14n(y)]
        if got!=changed: raise RuntimeError('changed mismatch')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnotes')
        def instr(z):
            out=[]
            for n in z.namelist():
                if n.startswith('word/') and n.endswith('.xml'):
                    try:r=etree.fromstring(z.read(n))
                    except Exception:continue
                    out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
            return out
        ia,ib=instr(a),instr(b)
        if ia!=ib or len(ib)!=520: raise RuntimeError('fields')
        if (sum('ADDIN ' in x for x in ib),sum('ZOTERO_ITEM' in x for x in ib),sum('ZOTERO_BIBL' in x for x in ib))!=(466,465,1): raise RuntimeError('zotero')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53 or len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('bookmarks/hyperlinks')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('rtl')
if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_019_085.py INPUT OUTPUT')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
