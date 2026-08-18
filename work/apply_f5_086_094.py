#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys, re
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED='869aefdec0d5fe046176e09e690d0e7d928ab53566b641fa6ace912bda31160e'
QNEG_298='“Bugün mushafın, imamların ilkyazım ıstılâhı üzere yazılması câiz değildir; zira bu, cahillerin hataya düşmesine yol açabilir.”'
QNEG_302='“Kim benim sünnetimden yüz çevirirse benden değildir.”'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def text(e): return ''.join(e.xpath('.//w:t/text()',namespaces=NS))
def c14n(e): return etree.tostring(e,method='c14n')
def sig(e): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in e.iter())
def quote_ranges(s):
    out=[]; pos=0
    while True:
        a=s.find('“',pos)
        if a<0: break
        b=s.find('”',a+1)
        if b<0: break
        out.append((a,b+1)); pos=b+1
    pts=[m.start() for m in re.finditer('"',s)]
    for a,b in zip(pts[0::2],pts[1::2]): out.append((a,b+1))
    return out
def inquote(s,a,b): return any(a>=x and b<=y for x,y in quote_ranges(s))
def replace_range(p,start,end,new):
    nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]; starts=[]; cur=0
    for v in vals: starts.append(cur); cur+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start<st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end<=st+len(v))
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def replace_outside(p,old,new):
    changed=0
    while True:
        s=text(p); qs=quote_ranges(s); hits=[]; st=0
        while True:
            j=s.find(old,st)
            if j<0: break
            if not any(j>=a and j+len(old)<=b for a,b in qs): hits.append(j)
            st=j+len(old)
        if not hits: break
        j=hits[-1]; replace_range(p,j,j+len(old),new); changed+=1
    return changed

def replace_exact_in_p(ps,idx,old,new):
    p=ps[idx]; s=text(p); pos=s.find(old)
    if pos<0: return False
    replace_range(p,pos,pos+len(old),new); return True

def replace_whole_p(ps,idx,new,anchor):
    p=ps[idx]; s=text(p)
    if s==new: return False
    if anchor not in s: return False
    nodes=p.xpath('.//w:t',namespaces=NS)
    if not nodes: raise RuntimeError('no text P'+str(idx))
    nodes[0].text=new
    for n in nodes[1:]: n.text=''
    return True

def log(item,changed): print(f'F5-{item:03d}\t'+('APPLIED' if changed else 'VERIFIED_NO_CHANGE_OR_ALREADY_SATISFIED'))

def apply(src,out):
    actual=sha(src)
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        before=[c14n(p) for p in ps]
        if QNEG_298 not in text(ps[298]) or QNEG_302 not in text(ps[302]): raise RuntimeError('quote-negative precondition')

        # F5-086 — remove remaining mini-conclusion outside the Fourth-approved P49 synthesis.
        c86=replace_whole_p(ps,161,'Resm-i Osmânî’nin kıyasî yazımdan ayrılan özellikleri, erken mushaf yazısının tarihsel yapısı ve rivâyetle korunan okuyuşlarla ilişkisi birlikte değerlendirilerek açıklanmalıdır. Bu kuralların tümüne tek bir amaç yüklenmemeli; her özellik kendi tarihsel ve rivâyet bağlamında incelenmelidir.','Sonuç olarak resm-i Osmânî’nin kıyasî yazımdan ayrılışı')
        log(86,c86)

        # F5-087 — remove algorithmic framing and expose the real grammatical subject.
        c87=0
        for p in ps[:457]:
            for old in ['Bu bağlamda, ','Bu bağlamda ','Bu çerçevede, ','Bu çerçevede ']: c87+=replace_outside(p,old,'')
        log(87,c87>0)

        # F5-088 — source/inference statements in simple present; remove emphatic certainty marker.
        c88=0
        for p in ps[:457]:
            for old,new in [('açıkça ortaya koymaktadır','ortaya koyar'),('ortaya koymaktadır','ortaya koyar'),('göstermektedir','gösterir'),('anlaşılmaktadır','anlaşılır')]: c88+=replace_outside(p,old,new)
        log(88,c88>0)

        # F5-089 — reduce repetitive transition machinery; retain Bununla birlikte where it marks a real caution/contrast.
        c89=0
        for p in ps[:457]:
            for old in ['Nitekim, ','Nitekim ','Dolayısıyla, ','Dolayısıyla ','Böylece, ','Böylece ','Bu noktada, ','Bu noktada ','Bu yönüyle, ','Bu yönüyle ']: c89+=replace_outside(p,old,'')
        log(89,c89>0)

        # F5-090 — remove rephrasing labels; the substantive proposition remains directly stated.
        c90=0
        for p in ps[:457]:
            for old in ['Diğer bir ifadeyle, ','Diğer bir ifadeyle ','Başka bir ifadeyle, ','Başka bir ifadeyle ']: c90+=replace_outside(p,old,'')
        log(90,c90>0)

        # F5-091 — remove overt authorial attention labels; recast 'important' statements where their function is explicit.
        c91=0
        for p in ps[:457]:
            c91+=replace_outside(p,'dikkat çekici','öne çıkan')
        manual91={
          122:('Bununla birlikte Kur’an ilimlerine dair eserlerinde Osman mushaflarının yazımını sahâbe nakline dayanan bir metin geleneği içinde değerlendirmesi, resm düşüncesinin erken safhası bakımından önemlidir.','Kur’an ilimlerine dair eserlerinde Osman mushaflarının yazımını sahâbe nakline dayanan bir metin geleneği içinde değerlendirmesi, resm düşüncesinin erken safhasını izlemeye imkân verir.'),
          125:("Dânî'nin yaklaşımı, farklı merkezlere nispet edilen yazım rivâyetlerini karşılaştırmalı biçimde ele alması bakımından özellikle önemlidir.","Dânî'nin yaklaşımı, farklı merkezlere nispet edilen yazım rivâyetlerini karşılaştırmalı biçimde ele alır."),
          190:('Ona göre okuyuşun Arapça bakımından güçlü dayanağa sahip olması önemlidir.','Ona göre okuyuşun Arapça bakımından güçlü bir dayanağa sahip olması gerekir.'),
          280:('Bu örnek, resm-i mushaf’ın sadece tehdit ve heybet ifade eden âyetlerden ibaret olmayıp; rahmet ve af bağlamında da ince mana delaletleri taşıyabildiğini göstermesi bakımından ayrıca önemlidir.','Bu örnek, resm-i mushaf yazımının rahmet ve af bağlamında da mana yorumlarıyla ilişkilendirildiğini gösterir.'),
          295:('Bu cevaplar, resme bağlılığın normatif gerekçelerini açıklamak bakımından önemlidir; ancak erken yazım biçimlerinin tarihsel sebebini tek başına belirleyen kanıtlar olarak değerlendirilmemelidir.','Bu cevaplar, resme bağlılığın normatif gerekçelerini açıklar; ancak erken yazım biçimlerinin tarihsel sebebini tek başına belirleyen kanıtlar olarak değerlendirilmemelidir.'),
          306:('Bu değerlendirme resm-i Osmânî meselesinin klasik gelenekte sadece güçlü bir ittiba çağrısı etrafında şekillenmediğini, aynı zamanda bu ittibanın hükmi derecesinin de tartışıldığını göstermesi bakımından önemlidir.','Bu değerlendirme, klasik gelenekte resm-i Osmânî’ye ittibanın yanı sıra bu ittibanın hükmî derecesinin de tartışıldığını gösterir.'),
          357:('Mushaflar İslâm beldelerine ulaştığında Müslümanların bunlardan harf harf, kelime kelime yeni nüshalar çıkarmaları ve kendi mushaflarını bunlarla karşılaştırmaları da ayrıca önemlidir.','Mushaflar İslâm beldelerine ulaştığında Müslümanların bunlardan harf harf, kelime kelime yeni nüshalar çıkarmaları ve kendi mushaflarını bunlarla karşılaştırmaları, ortak mushaf metninin başvuru niteliğini yansıtır.'),
          361:('Sahâbe döneminde Kur’an’ın yazıya geçirilmesi, vahyin korunmasına yönelik tedbirlerin erken safhada devreye girdiğini göstermesi bakımından son derece önemlidir.','Sahâbe dönemindeki yazılı kayıtlar, vahyin korunmasına yönelik tedbirlerin erken safhada devreye girdiğine işaret eder.'),
          372:('Sahâbeye nispet edilen mushaf rivâyetleri, erken Kur’an aktarımında bulunan okuyuş, tertip ve yazım çeşitliliğini incelemek bakımından önemlidir.','Sahâbeye nispet edilen mushaf rivâyetleri, erken Kur’an aktarımındaki okuyuş, tertip ve yazım çeşitliliğine ilişkin tarihsel veri sağlar.'),
          395:('Bu tespit, kırâat ilminde dil kıyası ile mushaf resmi karşı karşıya geldiğinde, belirli durumlarda yazı geleneğinin üstün tutulabildiğini göstermesi bakımından son derece önemlidir.','Bu tespit, kırâat ilminde dil kıyası ile mushaf resmi karşı karşıya geldiğinde belirli durumlarda yazı geleneğinin üstün tutulabildiğine işaret eder.'),
          400:('Resm rivâyetleri, mushaf kelimelerinin hangi biçimde yazıldığını ve şehir mushafları arasında nakledilen yazım farklılıklarını belirlemek bakımından önemlidir.','Resm rivâyetleri, mushaf kelimelerinin hangi biçimde yazıldığını ve şehir mushafları arasında nakledilen yazım farklılıklarını belirlemek için temel kaynak malzemesi sağlar.'),
          415:('Bu bilgi, mushaf naklinin ne kadar yoğun bir yazı faaliyeti içinde sürdürüldüğünü ve bu süreçte yazım farklılıklarının ortaya çıkmasının neden bütünüyle önlenemediğini göstermesi bakımından önemlidir.','Bu bilgi, mushaf naklinin yoğun bir yazı faaliyeti içinde sürdüğünü ve bu süreçte yazım farklılıklarının neden bütünüyle önlenemediğini açıklamaya katkı sağlar.'),
          427:('Bu tespit, daha sonraki dönemlerde matbu mushafların neden özellikle belirli kırâat rivâyetleri etrafında yoğunlaştığını anlamak bakımından oldukça önemlidir.','Bu tespit, daha sonraki dönemlerde matbu mushafların belirli kırâat rivâyetleri etrafında yoğunlaşmasını açıklamaya katkı sağlar.')
        }
        for idx,(old,new) in manual91.items(): c91+=int(replace_exact_in_p(ps,idx,old,new))
        log(91,c91>0)

        # F5-092 — replace selected abstract subjects with the actual event/evidence/institution named in context.
        c92=0
        m92={
          73:('Bu durum Medine merkezli eğitim ortamında dahi kırâat farklılıklarının tartışma ve inkâra dönüştüğünü','Huzeyfe rivâyeti, Medine merkezli eğitim ortamında dahi kırâat farklılıklarının tartışma ve inkâra dönüştüğünü'),
          84:('Bu durum Kur’an’ın yazılı bir ölçüye bağlanması','Kırâat ihtilaflarının yaygınlaşması, Kur’an’ın yazılı bir ölçüye bağlanması'),
          95:('Bu durum Yemen ve Bahreyn’e mushaf gönderildiği yönündeki rivâyetlerin zayıf olabileceği ihtimalini','Somut kayıtların yokluğu, Yemen ve Bahreyn’e mushaf gönderildiği yönündeki rivâyetlerin zayıf olabileceği ihtimalini'),
          160:('Bu durum resm-i Osmânî’nin yalnızca görsel bir imlâ sistemi değil, aynı zamanda kırâat geleneğini gözeten esnek bir yazı yapısı olduğunu','Bu örnekler, resm-i Osmânî’nin bazı rivâyetle sabit okuyuşlarla bağdaşabilen esnek bir yazı yapısı sunduğunu'),
          174:('Bu durum resm-i Osmânî’nin her durumda kelimeleri zorunlu olarak birleştiren bir yazı sistemi olmadığını','Vasl ve fasl örnekleri, resm-i Osmânî’nin her durumda kelimeleri zorunlu olarak birleştiren bir yazı sistemi olmadığını'),
          208:('Bu durum, kırâat ilminin zamanla daha disiplinli bir ölçü sistemine kavuştuğunu','Dil, rivâyet ve mushaf hattının birlikte değerlendirilmesi, kırâat ilminin zamanla daha disiplinli bir ölçü sistemine kavuştuğunu'),
          226:('Bu durum, kırâat otoritesinin baştan itibaren hem kişiler hem de ilim çevreleri tarafından geliştiğini','İmamlar, râviler ve öğretim çevreleri arasındaki aktarım ağı, kırâat otoritesinin kişiler ve ilim çevreleri üzerinden geliştiğini'),
          241:('Bu durum resmin tefsîrde sessiz ama güçlü bir zemin oluşturduğunu','Ortak mushaf metni, resmin tefsîrde yazılı bir referans zemini oluşturduğunu'),
          256:('Bu durum yazının okuyuşu bütünüyle belirlediğini değil, belirli okuyuşların ortak harf iskeleti içinde karşılık bulabildiğini','Bu örnekler, yazının okuyuşu bütünüyle belirlemediğini; belirli okuyuşların ortak harf iskeleti içinde karşılık bulabildiğini'),
          289:('Bu durum İslâm geleneğinde resm-i mushaf için tek bir açıklama şeklinin olmadığını','Kaynaklardaki farklı açıklamalar, İslâm geleneğinde resm-i mushaf için tek bir açıklama şeklinin olmadığını'),
          311:('Bu durum, resm-i Osmânî’ye bağlılığın yalnız yazıyı korumaktan ibaret görülmediğini','Bu rivâyet ve yorumlar, resm-i Osmânî’ye bağlılığın yalnız yazıyı korumaktan ibaret görülmediğini'),
          352:('Bu durum, resmin okuyuşları seçen bağımsız bir özne olduğunu değil, rivâyet edilen okuyuşların müşterek yazılı çerçeveyle uyumunun değerlendirilmesine katkı sağladığını','Bu örnekler, resmin okuyuşları seçen bağımsız bir özne olmadığını; rivâyet edilen okuyuşların müşterek yazılı çerçeveyle uyumunun değerlendirilmesine katkı sağladığını'),
          387:('Bu durum, resm-i Osmânî’nin kırâat ilminde dili dışlayan bir ilke olmaktan öte, onu kendi sınırları içinde yönlendiren bir otorite olarak işlediğini','İbn Hâleveyh’in tercihi, resm-i Osmânî’nin kırâat ilminde dil verileriyle birlikte kullanılan bir ölçü olduğunu'),
          389:('Bu durum, resm-i Osmânî’nin kırâat ilminde yalnız meşruiyet sınırını tayin eden bir unsur olmadığını','Bu tercih örnekleri, resm-i Osmânî’nin kırâat ilminde meşruiyet ölçüsünün yanında tercîh ve tevcîh süreçlerinde de kullanıldığını'),
          399:('Bu durum, Osmânî mushafların yazım farklılıklarının sadece şekilsel bir ayrılık olmadığını','Şehir mushaflarına nispet edilen yazım farklılıkları, yalnız şekilsel ayrılıklar olarak ele alınmaz;'),
          410:('Bu durum resm-i Osmânî’nin sonradan eklenen işaretlerde bile asıl yazı biçiminin korunmasının esas alındığını','Dânî’nin yardımcı işaretlere ilişkin tavrı, sonradan eklenen işaretlerde bile asıl yazı biçiminin korunmasının esas alındığını'),
          411:('Bu durum, sonraki dönemlerde mushaf yazımında iki eğilimin yan yana bulunduğunu','Müstensih uygulamaları, sonraki dönemlerde mushaf yazımında iki eğilimin yan yana bulunduğunu'),
          416:('Bu durum, çağdaş mushaf neşrinde resm-i Osmânî’nin korunmasının şahsi kanaatlere göre değil, klasik rivâyet kaynaklarına dayalı ilmî bir yöntem çerçevesinde sürdürüldüğünü','Dânî ve Ebû Dâvud’un eserlerinin başvuru kaynağı olarak kullanılması, çağdaş mushaf neşrinde resm-i Osmânî’nin klasik rivâyet kaynaklarına dayalı bir yöntemle sürdürüldüğünü'),
          419:('Bu durum, Muhtaṣaru’t-Tebyîn’in fiilen mushaf yazımını yönlendiren bir metin olarak kabul edildiğini','Mısır mushaf heyetinin Ebû Dâvud’un görüşlerini tercih etmesi, Muhtaṣaru’t-Tebyîn’in mushaf yazımını yönlendiren bir başvuru metni olarak kullanıldığını'),
          425:('Bu durum, mushafların belirli rivâyetlere göre zapt edilmesinin kırâatlerin coğrafi dolaşımı üzerinde doğrudan etkili olduğunu','Belirli rivâyetlere göre zapt edilen mushafların yaygınlaşması, kırâatlerin coğrafi dolaşımına katkıda bulunduğunu'),
          431:('Bu durum, mushaf neşrinde yalnızca metnin basılmasının yeterli kabul edilmediğini','Tashih ve denetim uygulamaları, mushaf neşrinde yalnızca metnin basılmasının yeterli kabul edilmediğini'),
          440:('Bu durum, Türkiye’de mushaf basımının sadece teknik bir matbaa işi olmadığını','Diyanet denetimi, Türkiye’de mushaf basımının teknik üretimin yanında ilmî ve dinî denetime tâbi olduğunu')
        }
        for idx,(old,new) in m92.items(): c92+=int(replace_exact_in_p(ps,idx,old,new))
        # explicit process labels
        for idx,old,new in [
          (74,'Bu süreç sadece askerî ve siyasi bir genişlemeyle kalmamış','Fetihlerle genişleyen İslâm coğrafyası askerî ve siyasi değişimin yanında'),
          (120,'Bu süreçte benimsenen yazım şekli','Hz. Osman dönemindeki istinsah sürecinde benimsenen yazım şekli'),
          (186,'Bu süreç yalnızca mevcut sahifelerin çoğaltılması anlamına gelmemiş','Hz. Osman dönemindeki istinsah faaliyeti mevcut sahifelerin çoğaltılmasıyla sınırlı kalmamış'),
          (432,"Bu süreç, Osmanlı'da matbaanın kabulü ile mushaf basımına izin verilmesinin","Matbaanın Osmanlı'daki kabul süreci, mushaf basımına izin verilmesinin"),
          (440,'Bu süreç, klasik resm kaynakları, kırâat öğretimi, tashih kurumları, baskı teknolojisi ve resmî neşir politikalarının birlikte etkisiyle şekillenmiştir.','Türkiye’deki mushaf basım düzeni; klasik resm kaynakları, kırâat öğretimi, tashih kurumları, baskı teknolojisi ve resmî neşir politikalarının birlikte etkisiyle şekillenmiştir.')
        ]: c92+=int(replace_exact_in_p(ps,idx,old,new))
        log(92,c92>0)

        # F5-093 — shorten frequent -maktadır/-mektedir chains to source-reporting/simple present outside direct quotations.
        c93=0
        tense=[('belirtilmektedir','belirtilir'),('belirtmektedir','belirtir'),('ifade edilmektedir','ifade edilir'),('ifade etmektedir','ifade eder'),('aktarılmaktadır','aktarılır'),('aktarmaktadır','aktarır'),('görülmektedir','görülür'),('değerlendirilmektedir','değerlendirilir'),('kullanılmaktadır','kullanılır'),('zikredilmektedir','zikredilir'),('bulunmaktadır','bulunur'),('yer almaktadır','yer alır'),('oluşturmaktadır','oluşturur'),('sağlamaktadır','sağlar'),('taşımaktadır','taşır'),('sürdürmektedir','sürdürür'),('göstermekte','göstermede')]
        for p in ps[:457]:
            for old,new in tense: c93+=replace_outside(p,old,new)
        log(93,c93>0)

        # F5-094 — author framing may change, but direct source quotations with negatives must be byte-text preserved.
        if QNEG_298 not in text(ps[298]) or QNEG_302 not in text(ps[302]): raise RuntimeError('F5-094 quote-negative mutation')
        log(94,True)

        after=[c14n(p) for p in ps]; changed=[i for i,(a,b) in enumerate(zip(before,after)) if a!=b]
        if actual!=EXPECTED and not changed:
            shutil.copyfile(src,out); print('CHANGED_PARAGRAPHS=[]'); return
        if actual!=EXPECTED: raise RuntimeError('input sha mismatch '+actual)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,changed)
    print('CHANGED_PARAGRAPHS='+repr(changed))
    print('QUOTE_NEGATIVES_PRESERVED=PASS')

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
        if QNEG_298 not in text(pb[298]) or QNEG_302 not in text(pb[302]): raise RuntimeError('quoted negatives')
if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_086_094.py INPUT OUTPUT')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
