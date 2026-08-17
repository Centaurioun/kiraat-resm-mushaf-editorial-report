#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, shutil, zipfile
from pathlib import Path
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}
QN=lambda x:f'{{{W}}}{x}'
F4_SHA='6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7'
CANON_SHA='d91161926853e0fd2e2204ba2d54277c2861f178f7f2d0415e76f2618b058c54'

REPL = [
('F4-084', 'ifadesi, bu anlayışı açıkça ortaya koymaktadır.', 'ifadesi, kırâat aktarımında rivâyet ve telakkinin merkezî konumuna işaret etmektedir.'),
('F4-083', 'Bu çerçevede resm-i Osmânî, ihtilafı azaltmak ve sahih olanı muhafaza etmek için en başta sabit rivâyete bağlı kalmayı, neshedilmiş olanı ve hakkında sadece âhâd rivâyet bulunan yahut fiilen okunmayan vecihleri dışarıda bırakmıştır.', 'Bu çerçevede istinsah ve müşterek mushaf kabulü sürecinde sabit rivâyete bağlı kalındığı; neshedilmiş, yalnız âhâd yolla nakledilmiş yahut fiilen okunmayan vecihlerin müşterek mushaf alanının dışında bırakıldığı aktarılmaktadır.'),
('F4-083', 'Bu nedenle Osmânî mushafların resmi, bağımsız bir imlâ şekli görülmeyip; sahih rivâyetle doğrulanmış okuyuşun yazıda tespit edilmiş biçimi olarak değerlendirilebilir.', 'Bu nedenle Osmânî mushafların resmi, bağımsız bir okuyuş kaynağı olarak değil, rivâyetle doğrulanmış okuyuşların yazılı çerçevesi olarak değerlendirilmelidir.'),
('F4-083', 'Aynı şekilde Hz. Peygamber’in vefat ettiği yılda gerçekleşen son arzanın esas alınması da, Osmânî resmin keyfî bir tercihten ibaret olmayıp son olarak tahkik edilmiş kırâat zeminine dayandığını ortaya koymaktadır.', 'Aynı şekilde Hz. Peygamber’in vefat ettiği yılda gerçekleşen son arzanın esas alınmasına ilişkin rivâyetler, istinsah sürecinin kırâat rivâyeti zemininden bağımsız düşünülmediğini göstermektedir.'),
('F4-083', 'Osmânî resmin diğer temel işlevi, tevâtüren sabit olan kırâatlerle âhâd rivâyetleri birbirinden ayıran bağlayıcı bir ölçü oluşturmasıdır.', 'Resm-i Osmânî, rivâyetle nakledilen okuyuşların müşterek mushaf yazısıyla bağdaşma durumunu göstermesi bakımından tespit ve tahditte kullanılan önemli yazılı ölçülerden biridir.'),
('F4-083', 'Bu yaklaşım, Osmânî resmin sadece mevcut rivâyetleri kaydeden edilgen bir kalıp olmadığını; aksine ümmetin ortak mushafında hangi vecihlerin kalacağını belirleyen seçici bir çerçeve olduğunu göstermektedir.', 'Bu yaklaşım, resmin okuyuşları bağımsız biçimde seçtiğini değil, rivâyetle nakledilen vecihlerin müşterek mushaf hattıyla uygunluğunun kabul değerlendirmesinde dikkate alındığını göstermektedir.'),
('F4-083', 'Dolayısıyla resm-i Osmânî, sahih kırâat alanını tahdit eden ve onu ümmetin müşterek rivâyet zemini içinde koruyan kurucu bir unsur hüviyeti kazanmaktadır.', 'Okuyuşun varlığı ve edâsı rivâyet yoluyla bilinir; resm ise bu okuyuşun Osmânî mushafların yazılı çerçevesi içindeki konumunun değerlendirilmesine katkı sağlar.'),
('F4-087', '(burası daha önce düzeltilmemiş, ”anlaşılmaktadır” olarak kalmış)', ''),
('F4-088', 'Bu durum, Osmânî resmin daha sonra niçin seçici bir işleve sahip olduğunu anlamak bakımından temel önemdedir.', 'Bu farklı malzeme, şahsî mushaf rivâyetleri ile sonraki müşterek mushaf otoritesi arasındaki işlev farkını değerlendirmek bakımından önemlidir.'),
('F4-088', 'Bu noktada Osmânî resmin sahâbe mushafları karşısındaki tavrı açık biçimde görünmektedir:', 'Bu noktada belirleyici olan, Osmânî istinsah ve sonraki müşterek mushaf kabulü sürecidir:'),
('F4-088', 'Bu bakımdan Osmânî resm, şahsi mushaflarda korunmuş rivâyet birikimini yok saymamakta; fakat bunların içinden Kur’anlığı kesinleşen, bağlayıcı ve ümmetçe muhafaza edilecek kısmı seçmektedir.', 'Bu bakımdan seçme ve normatif sınırlandırma, yazım biçiminin kendisine değil, istinsah, müşterek kabul ve sonraki ilmî değerlendirme süreçlerine nispet edilmelidir.'),
('F4-088', "Bu da resm-i Osmânî'nin, kırâat rivâyetleri arasında bağlayıcılık ölçüsü koyan kurucu bir çerçeve olduğunu ortaya koymaktadır.", 'Bu da rivâyet malzemesi ile müşterek mushaf metni arasındaki ayrımın, sahih rivâyet ve Osmânî mushaf hattı birlikte değerlendirilerek kurulduğunu göstermektedir.'),
('F4-088', 'Bu sebeple Osmânî mushafın teşekkülü, sadece bir “cem” faaliyetinden ibaret kalmayıp, aynı zamanda sahâbe mushaflarında dağınık hâlde bulunan rivâyet malzemesinin yeniden değerlendirilmesi ve müşterek bağlayıcılığa sahip olanın seçilmesi sürecidir.', 'Bu sebeple Osmânî istinsah ve sonraki müşterek mushaf kabulü, sahâbe mushaflarında dağınık hâlde bulunan rivâyet malzemesinin normatif konumunun yeniden değerlendirilmesinde belirleyici tarihsel çerçeveyi oluşturmuştur.'),
('F4-088', 'Böyle bakıldığında resm-i Osmânî, sahâbe mushaflarındaki okuyuş çeşitliliğini inkâr eden bir yapı olmaktan ziyade, bu çeşitlilik içinden ümmetin ortak metin otoritesine dönüşecek alanı belirleyen ölçü olarak değerlendirilebilir.', 'Böyle bakıldığında resm-i Osmânî, sahâbeye nispet edilen rivâyetlerin müşterek mushaf yazısıyla bağdaşma durumunu gösteren yazılı ölçülerden biri olarak değerlendirilebilir.'),
('F4-089', "İbn Mesʿûd'un istinsah sürecine yaklaşımı hakkında farklı rivâyetler bulunmaktadır. Bazı kaynaklar onun başlangıçtaki itirazını aktarırken, sonraki tutumunun mahiyeti konusunda farklı değerlendirmeler yapılmıştır. Ancak bu rivâyetler bir bütün hâlinde değerlendirildiğinde, Abdullah b. Mesʿûd'a nispet edilen muhalif tavrın istinsah sürecine ilişkin genel çerçeveyi bozacak bir mahiyet taşımadığı anlaşılmaktadır.", "İbn Mesʿûd'a nispet edilen rivâyetler, onun istinsah süreci ve kendi mushafıyla ilişkili bazı itirazlarının bulunduğunu göstermektedir. Bu tavrın hangi psikolojik saikle ortaya çıktığını kesin biçimde belirlemek yerine, nakledilen söz ve uygulamalar kendi tarihsel bağlamları içinde değerlendirilmelidir."),
('F4-089', 'Nitekim onun, mushafının yakılmasına tepki gösterdiği ve insanlara mushaflarını gizlemelerini söylediği nakledilmekle birlikte, bu tavır erken dönem kaynaklarında sürekli ve esaslı bir muhalefet olmayıp, öfkeye bağlı geçici bir tepki olarak yorumlanmıştır.', 'Onun mushafının yakılmasına tepki gösterdiği ve insanlara mushaflarını gizlemelerini söylediği nakledilmektedir.'),
('F4-089', 'Kurtubî’nin Ebû Bekir el-Enbârî’den (ö. 328/940) naklen aktardığına göre, İbn Mes’ûd’dan görülen bu karşı çıkış kızgınlık hâlinde ortaya çıkmış; öfkesi geçtikten sonra Osman’ın ve onunla birlikte hareket eden sahâbenin isabetli tercihine döndüğü kabul edilmiştir. İbn Kesîr de, onun kırgınlığını mushaf yazım heyetinde yer almamış olmasına bağlamakta ve nihayetinde tekrar ittifaka döndüğünü belirtmektedir.', 'Kurtubî’nin Ebû Bekir el-Enbârî’den (ö. 328/940) naklettiği değerlendirmede bu karşı çıkış kızgınlıkla açıklanmış ve daha sonra ittifaka dönüldüğü ileri sürülmüştür.'),
('F4-089', 'Böylece bireysel rahatsızlıkların, sahâbe icmâının kurduğu ortak mushaf otoritesini bozmadığı anlaşılmaktadır.', 'Bu tür sonraki yorumlar, İbn Mesʿûd’un psikolojik saiki hakkında doğrudan tarihsel kanıt olarak değil, rivâyetlerin klasik dönemde nasıl yorumlandığını gösteren değerlendirmeler olarak sunulmalıdır.'),
]

WHOLE = {
'F4-085': ('Bütün bunlar birlikte düşünüldüğünde Osmânî resmin kırâat vecihlerinin rivâyet ve naklinde üç yönlü bir rol üstlendiği söylenebilir.', 'Osmânî mushaflar ümmetin müşterek yazılı başvuru zemini hâline gelirken, sahâbeye nispet edilen şahsî mushaflar erken dönemdeki okuyuş, tertip ve yazım çeşitliliğine ilişkin tarihsel veriler sunmaktadır. Bu iki malzemenin işlev ve otorite düzeyi aynı değildir. Bir sonraki başlık bu farkı ele almaktadır.'),
'F4-088': ('Buradan hareketle denilebilir ki resm-i Osmânî’nin sahâbe mushaflarındaki kırâat rivâyetleri karşısındaki tutumu iki yönlüdür.', 'Osmânî istinsah ve sonraki müşterek mushaf kabulü, sahâbeye nispet edilen farklı malzemenin normatif Kur’an metni içindeki konumunun değerlendirilmesinde belirleyici tarihsel çerçeveyi oluşturmuştur. Resm-i Osmânî ise bu süreçte rivâyetlerin müşterek mushaf yazısıyla bağdaşma durumunu gösteren yazılı ölçülerden biridir.'),
'F4-090': ('Sonuç olarak bu veriler birlikte değerlendirildiğinde, sahâbe mushaflarının yakılması meselesinin, Kur’an tarihindeki en önemli birleştirici adımlardan biri olduğu görülmektedir.', 'Sahâbeye nispet edilen mushaf rivâyetleri, erken Kur’an aktarımında bulunan okuyuş, tertip ve yazım çeşitliliğini incelemek bakımından önemlidir. Bununla birlikte sonraki müşterek mushaf geleneğinin normatif zemini Osmânî mushaflar etrafında şekillenmiştir. Bu sebeple şahsî mushaf rivâyetleri tarihsel tanıklık ile normatif metin otoritesi birbirine karıştırılmadan kullanılmalıdır.'),
}

F4086='Sahâbeye nispet edilen mushaf farklılıkları tek bir kategori altında değerlendirilmemelidir. Kaynaklarda farklı okuyuş rivâyetleri, açıklayıcı veya tefsirî ifadeler, kelime tertibi yahut yazım biçimine ilişkin aktarımlar ve isnadı veya yorumu tartışmalı kayıtlar birlikte yer almaktadır. Bu malzemenin tarihsel değeri, erken dönemdeki okuyuş ve yazı çeşitliliğine dair veri sunmasındadır. Buna karşılık ümmetin müşterek mushaf geleneğinde normatif ölçü, Osmânî mushafların yazılı çerçevesi ile sahih rivâyetin birlikte değerlendirilmesi üzerinden şekillenmiştir.'
HEADING='Sahâbe Mushaflarındaki Kırâat Rivâyetlerine Karşı Resm-i Osmânî’nin Konumu'
NEXT='Sahâbe döneminde Kur’an’ın yazıya geçirilmesi, vahyin korunmasına yönelik tedbirlerin erken safhada devreye girdiğini göstermesi bakımından son derece önemlidir.'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ptext(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def pars(root): return root.xpath('//w:body/w:p',namespaces=NS)

def ref_offsets(p):
    out=[]; n=0
    for el in p.iter():
        if el.tag==QN('t') and el.text: n+=len(el.text)
        elif el.tag==QN('footnoteReference'): out.append((n,el.get(QN('id'))))
    return out

def locate(root, needle):
    hits=[p for p in pars(root) if needle in ptext(p)]
    if len(hits)!=1: raise RuntimeError(f'fail-closed target {needle[:60]!r}: {len(hits)} matches')
    return hits[0]

def replace_in_p(p, old, new):
    text=ptext(p)
    if old not in text: raise RuntimeError(f'missing anchor {old[:80]}')
    if text.count(old)!=1: raise RuntimeError(f'ambiguous anchor {old[:80]} count={text.count(old)}')
    s=text.index(old); e=s+len(old)
    interior=[r for r in ref_offsets(p) if s < r[0] < e]
    if interior: raise RuntimeError(f'replacement crosses footnote refs {interior}: {old[:80]}')
    ts=p.xpath('.//w:t',namespaces=NS)
    spans=[]; n=0
    for t in ts:
        v=t.text or ''; spans.append((t,n,n+len(v),v)); n+=len(v)
    touched=[x for x in spans if x[2]>s and x[1]<e]
    if not touched: raise RuntimeError('no text nodes touched')
    first=touched[0]; last=touched[-1]
    prefix=first[3][:max(0,s-first[1])]
    suffix=last[3][max(0,e-last[1]):]
    first[0].text=prefix+new+(suffix if first[0] is last[0] else '')
    for x in touched[1:-1]: x[0].text=''
    if first[0] is not last[0]: last[0].text=suffix

def replace_global(root,item,old,new):
    p=locate(root,old)
    replace_in_p(p,old,new)

def reset_para(p, new):
    if p.xpath('.//w:footnoteReference',namespaces=NS): raise RuntimeError('refuse whole-paragraph reset with footnote')
    ppr=p.find(QN('pPr'))
    keep=copy.deepcopy(ppr) if ppr is not None else None
    exemplar=None
    for r in p.findall(QN('r')):
        if r.find(QN('t')) is not None:
            exemplar=r.find(QN('rPr')); break
    for c in list(p): p.remove(c)
    if keep is not None: p.append(keep)
    r=etree.SubElement(p,QN('r'))
    if exemplar is not None: r.append(copy.deepcopy(exemplar))
    t=etree.SubElement(r,QN('t')); t.text=new

def already_applied(root):
    text='\n'.join(ptext(p) for p in pars(root))
    required=[new for _,_,new in REPL]+[x[1] for x in WHOLE.values()]+[F4086]
    originals=[old for _,old,_ in REPL]+[x[0] for x in WHOLE.values()]
    return all(x in text for x in required) and all(x not in text for x in originals)

def build(input_path, output_path, proxy=False):
    inp=Path(input_path); out=Path(output_path)
    h=sha(inp)
    with zipfile.ZipFile(inp,'r') as zin:
        xml=zin.read('word/document.xml'); root=etree.fromstring(xml)
        if already_applied(root):
            shutil.copyfile(inp,out); return 'ALREADY_APPLIED',h,h
        if h!=F4_SHA:
            if not (proxy and h==CANON_SHA):
                raise RuntimeError(f'input SHA {h} is not required F4-047 SHA {F4_SHA}; use --test-proxy only for canonical-source rehearsal')
        for item,old,new in REPL: replace_global(root,item,old,new)
        for item,(start,new) in WHOLE.items():
            p=locate(root,start); reset_para(p,new)
        if len([p for p in pars(root) if ptext(p)==F4086])!=0: raise RuntimeError('F4-086 insert unexpectedly preexists')
        heading=locate(root,HEADING); nxt=locate(root,NEXT)
        body=heading.getparent(); children=list(body)
        if children.index(nxt)!=children.index(heading)+1: raise RuntimeError('4.2 heading/first paragraph adjacency changed')
        np=etree.Element(QN('p'), nsmap=heading.nsmap)
        ppr=nxt.find(QN('pPr'))
        if ppr is not None: np.append(copy.deepcopy(ppr))
        exemplar=None
        for r in nxt.findall(QN('r')):
            if r.find(QN('t')) is not None: exemplar=r.find(QN('rPr')); break
        r=etree.SubElement(np,QN('r'))
        if exemplar is not None: r.append(copy.deepcopy(exemplar))
        t=etree.SubElement(r,QN('t')); t.text=F4086
        body.insert(children.index(nxt),np)
        p=locate(root,'Kaynaklarda, bazı sahâbîlerin Rasûlullah’tan işittikleri okuyuşları')
        replace_in_p(p,'ifade edilmektedir.Bunun','ifade edilmektedir. Bunun')
        if not already_applied(root): raise RuntimeError('post-edit signature incomplete')
        newxml=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with zipfile.ZipFile(out,'w') as zout:
            for info in zin.infolist():
                data=newxml if info.filename=='word/document.xml' else zin.read(info.filename)
                zout.writestr(info,data)
    return ('PROXY_APPLIED' if h==CANON_SHA else 'APPLIED'),h,sha(out)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('input'); ap.add_argument('output'); ap.add_argument('--test-proxy',action='store_true')
    a=ap.parse_args()
    status,before,after=build(a.input,a.output,a.test_proxy)
    print(f'status={status}\ninput_sha256={before}\noutput_sha256={after}')
if __name__=='__main__': main()
