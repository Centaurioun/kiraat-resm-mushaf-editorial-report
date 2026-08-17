#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as base
NS=base.NS

def apply(src:Path,out:Path):
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); changed=False; rows=[]
        ps=body.xpath('./w:p',namespaces=NS)

        # F4-068: keep the attributed Mârginî discussion, but distinguish graphic possibility from design/mana claims.
        i68,p271=base.find(ps,'Mârginî’nin (ö. 1931) açıklaması ise, harekenin aslına işaret meselesini daha açık bir ifadeyle ortaya koyar.')
        old68='Bu açıklama, resm-i Osmânî’nin sadece harf iskeletini korumadığını; harekenin niteliğini, sesin dolgunluğunu ve okuyuş farkını da resm içinde işaretleyebildiğini gösterir. Bu demektir ki harekenin aslına işaret, kelimedeki kısa ses değerinin kökensel ya da tam ses karşılığının yazıda bir harf aracılığıyla desteklenmesidir.'
        new68=('Mârginî’nin bu açıklaması, ilgili yazım biçimini işbâ‘ ve fonetik ayrım çerçevesinde yorumlayan bir değerlendirmedir. Erken mushaf yazısının nokta ve hareke bakımından bugünkü yazıdan farklı olması, bazı kelimelerin rivâyet edilmiş farklı okuyuşlarla aynı harf iskeleti içinde bağdaşmasına imkân vermiştir. Bu grafik imkânın tek başına belirli bir mana zenginliği oluşturmak amacıyla tasarlandığını söylemek mümkün değildir. Anlam farklılıkları, rivâyetle sabit kırâatler ve bu kırâatlere ilişkin dilsel veya tefsirî değerlendirmeler üzerinden ele alınmalıdır.')
        st=base.span(p271,old68,new68); changed |= st=='APPLIED'; rows.append(('F4-068',i68,st))

        # F4-069: explicit transition from historical/phonetic evidence to later interpretive literature.
        R69=('Buraya kadar ele alınan örnekler, resm ile okuyuş arasındaki yazısal ve fonetik ilişkiyi göstermektedir. Klasik resm literatüründe bunun yanında bazı yazım biçimlerine mana ve hikmet açısından açıklamalar da getirilmiştir. Bu yorumların tarihsel yazım sebebiyle aynı delil düzeyinde olmadığı dikkate alınmalıdır.')
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R69)]
        if h:i69,p272=h[0];st69='ALREADY_SATISFIED'
        else:i69,p272=base.find(ps,'Kaynaklarda, bu harflerin kimi yerde tehdit ve uyarıyı kuvvetlendirme');base.whole(p272,R69);changed=True;st69='APPLIED'
        rows.append(('F4-069',i69,st69))

        # F4-070: heading bookmark preserved by span replacement; opening reframed as interpretation, not historical cause.
        ps=body.xpath('./w:p',namespaces=NS); i70,h273=base.find(ps,'Resm-i Osmânî’de Ziyâde ve Hazfin İnce Manaya Delaleti')
        stH=base.span(h273,'Resm-i Osmânî’de Ziyâde ve Hazfin İnce Manaya Delaleti','Hazf ve Ziyâdeye Yüklenen Mana İlişkileri: Klasik Yorumlar ve Delil Değeri'); changed |= stH=='APPLIED'
        R70=('Hazf ve ziyâde örnekleri resm-i mushaf literatüründe öncelikle belirli kelimelerin yazım özellikleri olarak ele alınmaktadır. Bazı klasik müellifler bu biçimleri kelimenin anlamı, bağlamı veya belâgat özellikleriyle ilişkilendiren yorumlar geliştirmiştir. Bu açıklamalar ilgili müelliflerin yorumları olarak değer taşımakla birlikte yazım biçiminin tarihsel sebebini tek başına kanıtlamaz. Bu nedenle mana ilişkileri, kaynakların açık nispetleri ve ilgili kırâat rivâyetleri çerçevesinde değerlendirilmelidir.')
        ps=body.xpath('./w:p',namespaces=NS); hh=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R70)]
        if hh:
            _,p274=hh[0]
            if base.spec(p274)['fn']!=['264']:raise RuntimeError('F4-070 FN264 mismatch')
            st70='ALREADY_SATISFIED' if stH=='ALREADY_SATISFIED' else 'APPLIED'
        else:
            _,p274=base.find(ps,'Resm-i Osmânî’nin en dikkat çekici özelliklerinden biri, bazı yazım biçimlerinin yalnızca lafzın dış görünüşünü değil')
            base.whole(p274,R70,[264]);changed=True;st70='APPLIED'
        rows.append(('F4-070',i70,st70))

        # F4-071: keep Arabic/hazf examples and note runs; mark Merrâkuşî as a later interpretive relation.
        ps=body.xpath('./w:p',namespaces=NS); i71,p277=base.find(ps,'Hazf örnekleri de aynı derecede önem kazanmıştır.')
        old71=('Ebu’l-Abbâs el-Merrâkuşî’ye (ö. 695/1295) nispet edilen açıklamaya göre bu hazifler, birinci âyette insanın şerre yönelmedeki aceleciliğine, ikinci âyette bâtılın süratle silinişine, üçüncü âyette çağrının ve cevabının çokluğuna, dördüncü âyette zebânîlerin derhâl harekete geçişine işaret eder. Böylece hazif, sadece harf düşmesi değil, fiilin süratini, kolaylığını veya etkisinin çabuk gerçekleşmesini hissettiren bir ifade aracına dönüşür.')
        new71=('Merrâkuşî, ilgili yazım biçimlerini kelimelerin anlamlarıyla ilişkilendirerek; birinci örneği insanın şerre yönelmedeki aceleciliği, ikinciyi bâtılın süratle silinişi, üçüncüyü çağrının ve cevabının çokluğu, dördüncüyü ise zebânîlerin derhâl harekete geçişiyle açıklamaktadır. Bu değerlendirme, resmin tarihsel oluşum sebebini gösteren bağımsız bir kanıt olarak değil, klasik resm literatüründe yazım ile mana arasında kurulan yorum ilişkilerinden biri olarak ele alınmalıdır.')
        st71=base.span(p277,old71,new71);changed |= st71=='APPLIED';rows.append(('F4-071',i71,st71))

        # F4-072: remove global 'meaning-marking system' generalization.
        R72=('Bu örnekler, bazı klasik müelliflerin mushaf yazımındaki belirli farklılıklarla anlam arasında yorum ilişkileri kurduklarını göstermektedir. Bu yorumlar, ilgili yazım biçimlerinin tarihsel sebebini zorunlu olarak açıklamaz.')
        ps=body.xpath('./w:p',namespaces=NS); h=[(i,p) for i,p in enumerate(ps) if base.norm(base.txt(p))==base.norm(R72)]
        if h:
            i72,p278=h[0]
            if base.spec(p278)['fn']!=['275']:raise RuntimeError('F4-072 FN275 mismatch')
            st72='ALREADY_SATISFIED'
        else:
            i72,p278=base.find(ps,'Resm-i Osmânî, sadece kelimelerin yazı biçimini sabitleyen bir sistemden müteşekkil değildir.')
            base.whole(p278,R72,[275]);changed=True;st72='APPLIED'
        rows.append(('F4-072',i72,st72))

        if not changed:
            shutil.copyfile(src,out);return rows
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    base.validate(src,out)
    with ZipFile(out) as z:
        dd=etree.fromstring(z.read('word/document.xml'));text='\n'.join(base.txt(p) for p in dd.xpath('.//w:body/w:p',namespaces=NS))
    for x in [new68,R69,'Hazf ve Ziyâdeye Yüklenen Mana İlişkileri: Klasik Yorumlar ve Delil Değeri',R70,new71,R72]:
        if base.norm(x) not in base.norm(text):raise RuntimeError('missing F4-068-072 postcondition '+x[:80])
    for x in ['harekenin niteliğini, sesin dolgunluğunu ve okuyuş farkını da resm içinde işaretleyebildiğini gösterir','Ziyâde ve Hazfin İnce Manaya Delaleti','bilinçli bir yapıdır','Bu nedenle resm-i Osmânî’yi sadece tek imlâ farklılıkları üzerinden okumak yeterli değildir; onu aynı zamanda bir anlam işaretleme sistemi olarak değerlendirmek gerekmektedir.']:
        if base.norm(x) in base.norm(text):raise RuntimeError('stale F4-068-072 text remains '+x)
    return rows

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,row)))
