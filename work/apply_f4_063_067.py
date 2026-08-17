#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as base

NS=base.NS

def apply(src:Path,out:Path):
    with ZipFile(src,'r') as zin:
        doc=etree.fromstring(zin.read('word/document.xml')); body=doc.find('.//w:body',namespaces=NS); changed=False; rows=[]
        ps=body.xpath('./w:p',namespaces=NS)

        # F4-063: remove design-intent and meta-reference; preserve FN239.
        R63=("Resm-i Osmânî’nin dikkat çekici özelliklerinden biri, bazı kelimelerin yazımının rivâyetle sabit birden fazla kırâatle bağdaşabilmesidir. "
             "Bu durum yazının okuyuşu bütünüyle belirlediğini değil, belirli okuyuşların ortak harf iskeleti içinde karşılık bulabildiğini göstermektedir. "
             "Nitekim İbnü’l-Cezerî’nin ifadelerinde sahih kırâatlerin ölçülerinden biri, okuyuşun Osmânî mushaflardan birinin resmine açık ya da ihtimalî olarak uymasıdır. "
             "Bu da yazının okuyuşu bütünüyle belirlemediği, fakat nakledilmiş okuyuşların resmle ilişkisini değerlendirmede bir ölçü olarak kullanıldığı anlamına gelir.")
        h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R63)]
        if h:
            i63,p63=h[0]; st63='ALREADY_SATISFIED'
            if base.spec(p63)['fn']!=['239']: raise RuntimeError('F4-063 completed note mismatch')
        else:
            i63,p63=base.find(ps,'Resm-i Osmânî’nin en dikkat çekici özelliklerinden biri, bazı kelimelerde birden fazla sahih kırâate yer verebilecek şekilde kurulmuş olmasıdır.')
            base.whole(p63,R63,[239]); changed=True; st63='APPLIED'
        rows.append(('F4-063',i63,st63))

        # F4-064: direct vs probable compatibility; no citation-bearing structures in P257.
        R64=("Resm ile kırâat arasındaki uygunluk her örnekte aynı değildir. Gerçek uygunlukta okuyuş mushaf yazısında doğrudan karşılık bulur. "
             "İhtimalî uygunlukta ise yazı, okuyuşu açıkça göstermese de onunla bağdaşır ve onu dışlamaz. "
             "Her iki durumda da okuyuşun kırâat olarak sabitliği yazı ihtimalinden değil, rivâyetten kaynaklanır.")
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R64)]
        if h: i64,p64=h[0]; st64='ALREADY_SATISFIED'
        else:
            i64,p64=base.find(ps,'Resm-i Osmânî’nin kırâatleri birçok yansıtma özelliği vardır.')
            base.whole(p64,R64); changed=True; st64='APPLIED'
        rows.append(('F4-064',i64,st64))

        # F4-065: reframe the long list without touching Arabic/RTL runs or FNs241-245.
        ps=body.xpath('./w:p',namespaces=NS); i65,p258=base.find(ps,'İbnü’l-Cezerî tahkiki uygunlukta özellikle bu ayrımı işlemiş ve buna açık uygunluk demiştir.')
        new_list_intro=("Kaynaklarda bu başlık altında farklı türde örnekler zikredilmektedir. Bunların bir kısmı belirli şehir mushaflarına nispet edilen yazım farklarını, "
                        "bir kısmı aynı harf iskeletinin birden fazla rivâyetle bağdaşmasını, bir kısmı ise belirli bir okuyuşun resmde doğrudan karşılık bulmasını göstermektedir. "
                        "Bu sebeple aşağıdaki örnekler tek bir varyant türü olarak değil, ilgili resm-kırâat ilişkisine göre ayrı ayrı değerlendirilmelidir:")
        old_list_intro=("Bununla birlikte tek bir yazımın bütün kırâatleri karşılamadığı kelimeler de vardır. Bu kelimeler otuz üç adet olup, Osmânî mushaflara, her bir mushafta sabit olan kırâat vecihleri esas alınarak dağıtılmıştır. Söz konusu kelimeler şunlardır:")
        st_intro=base.span(p258,old_list_intro,new_list_intro); changed |= st_intro=='APPLIED'
        ps=body.xpath('./w:p',namespaces=NS); _,p259=base.find(ps,'(Bakara 2/116)')
        repairs=[
          ('Bu da Osmânî resmin bütün kırâatleri tek bir yazım biçimine zorlamadığını, gerektiğinde mushaflar arası yazım farklılığıyla sahih okuyuşları koruduğunu göstermektedir.',
           'Bu örnekler, bazı şehir mushaflarına nispet edilen yazım farklılıklarının ilgili kırâat rivâyetleriyle birlikte ele alındığını göstermektedir.'),
          ('Yani mushaflar arasındaki bu sınırlı yazım farkı, ihtilaf üretmekten ziyade, meşru kırâatleri muhafaza etmeye matuf bir imkân olarak kullanılmıştır.',
           'Ancak bu farklılıkların tarihsel olarak özellikle kırâatleri korumak amacıyla tasarlandığı sonucu yalnız bu örneklerden çıkarılmamalıdır.'),
          ('Bu durum Osmânî mushafların tek tip bir yazım kalıbı olmaktan çok ortak esaslar içinde kırâatleri gözeten dikkatli bir sistem olduğunu göstermektedir.',
           'Her örnek, resm ve rivâyet ilişkisi bakımından kendi kaynak bağlamında değerlendirilmelidir.'),
          ('İşte böyle yerlerde bazı kelimeler, Osman mushaflarının hepsinde aynı biçimde değil, farklı mushaflarda farklı resmlerle yer almıştır ki bu durum kırâat farklılıklarını korumaya yönelik bir işlev taşıdığını göstermektedir.',
           'Bu tür yerlerde bazı kelimelerin Osman mushaflarında farklı resmlerle nakledildiği görülmektedir; bu farklılıkların kırâatlerle ilişkisi ilgili mushaf ve rivâyet verileri üzerinden belirlenmelidir.')
        ]
        sts=[]
        for old,new in repairs:
            st=base.span(p259,old,new); sts.append(st); changed |= st=='APPLIED'
        st65='ALREADY_SATISFIED' if st_intro=='ALREADY_SATISFIED' and all(x=='ALREADY_SATISFIED' for x in sts) else 'APPLIED'
        rows.append(('F4-065',i65,st65))

        # F4-066: shadh status cannot be reduced to resm; preserve Arabic and FNs246-248 in place.
        ps=body.xpath('./w:p',namespaces=NS); i66,p260=base.find(ps,'Üçüncü şekil, bir kelimenin lafızda birden fazla kırâati vardır;')
        R66=("Bir okuyuşun şâz kabul edilmesi yalnız resm-i Osmânî’ye aykırılığıyla açıklanamaz. Kırâatlerin değerlendirilmesinde naklin durumu, Arap diline uygunluk ve resm-i Osmânî ile bağdaşma birlikte ele alınmıştır. Resme aykırılık belirli okuyuşların değerlendirilmesinde önemli bir unsur olmakla birlikte şâz kategorisini tek başına açıklayan ölçü değildir.")
        old66='Bundan dolayı âlimler şöyle demişlerdir: Kırâatin temel şartlarından biri, resme en azından ihtimal yoluyla uygun olmasıdır; aksi takdirde o kırâat şâz olur.'
        st1=base.span(p260,old66,R66); changed |= st1=='APPLIED'
        st2=base.span(p260,'Buradan, resm ile kırâat arasındaki sıkı bağ açıkça görülmektedir; öyle ki onun yerini başka bir yazı sistemi tutamaz.','Bu örnek, resmle bağdaşmanın kırâat değerlendirmesindeki önemini göstermekle birlikte, okuyuşun sıhhatini tek başına yazının belirlediği anlamına gelmez.'); changed |= st2=='APPLIED'
        rows.append(('F4-066',i66,'ALREADY_SATISFIED' if st1=='ALREADY_SATISFIED' and st2=='ALREADY_SATISFIED' else 'APPLIED'))

        # F4-067: dialect explanation is one classical interpretation, not exhaustive. Preserve FN249/254.
        R67=("Yedi harfin mahiyetine ilişkin klasik açıklamalar arasında lehçe farklılıklarına vurgu yapan görüşler de bulunmaktadır. Bununla birlikte yedi harfi yalnız lehçe çeşitliliğine indirgemek, konuyla ilgili farklı klasik yorumları dışarıda bırakır. "
             "Kırâatlerde görülen bazı ses ve söyleyiş farklılıkları Arap lehçeleriyle ilişkilendirilebilse de bunların kırâat olarak aktarılması telakki ve rivâyet yoluyla gerçekleşmiştir. "
             "Osmânî mushafların bu rivâyetlerle ilişkisi, belirli yazım örnekleri ve kaynak nakilleri üzerinden, görüşlerin delil derecesi korunarak değerlendirilmelidir.")
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R67)]
        if h:
            i67,p262=h[0]
            if base.spec(p262)['fn']!=['249']: raise RuntimeError('F4-067 completed FN249 mismatch')
            a67=True
        else:
            i67,p262=base.find(ps,'Kırâat kaynaklarında sıkça vurgulanan hususlardan biri resm-i Osmânî yalnızca bir yazım biçimi değildir.')
            base.whole(p262,R67,[249]); changed=True; a67=False
        R67b=("Resm-i kıyasî, dil âlimlerinin kurallı ve açıklayıcı yazım sistemidir. Resm-i Osmânî ise erken mushaf geleneğinin tarihsel yazım özelliklerini taşır ve rivâyet temelli kırâatlerle ilişkilidir. "
              "Bazı klasik ve modern eserler, resm-i Osmânî’deki belirli yazım biçimlerini kırâat veya lehçe verileriyle ilişkilendirmiştir. Bu ilişkilendirmeler ilgili kaynakların açık nispetleri ve rivâyet verileri çerçevesinde değerlendirilmelidir; mushaf yazısının bütünüyle lehçe farklılıklarını korumak üzere tasarlandığını göstermez.")
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R67b)]
        if h:
            _,p264=h[0]
            if base.spec(p264)['fn']!=['254']: raise RuntimeError('F4-067 completed FN254 mismatch')
            b67=True
        else:
            _,p264=base.find(ps,'Resm-i kıyasî, dil âlimlerinin kurallı ve açıklayıcı yazım sistemidir.')
            base.whole(p264,R67b,[254]); changed=True; b67=False
        rows.append(('F4-067',i67,'ALREADY_SATISFIED' if a67 and b67 else 'APPLIED'))

        if not changed:
            shutil.copyfile(src,out); return rows
        xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    base.validate(src,out)
    with ZipFile(out) as z:
        d=etree.fromstring(z.read('word/document.xml')); text='\n'.join(base.txt(p) for p in d.xpath('.//w:body/w:p',namespaces=NS))
    required=[R63,R64,new_list_intro,R66,R67,R67b]
    for x in required:
        if base.norm(x) not in base.norm(text): raise RuntimeError('missing F4-063-067 postcondition: '+x[:80])
    forbidden=['yer verebilecek şekilde kurulmuş olmasıdır','daha önce de zikretmiştik','mushaf yazımı çoklu kırâat vecihlerini kapsayacak şekilde düzenlenmiştir','Bu kelimeler otuz üç adet olup','meşru kırâatleri muhafaza etmeye matuf bir imkân olarak kullanılmıştır','aksi takdirde o kırâat şâz olur','onun yerini başka bir yazı sistemi tutamaz','yedi harfin” aynı anlam etrafında Arap lehçelerine açılan bir ruhsat olduğu','onun amacı sadece kelimeyi en açık biçimde yazmak değil, aynı zamanda sahih kırâatler içindeki bazı lehçe işaretlerini koruyan']
    for x in forbidden:
        if base.norm(x) in base.norm(text): raise RuntimeError('stale F4-063-067 text remains: '+x)
    return rows

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
