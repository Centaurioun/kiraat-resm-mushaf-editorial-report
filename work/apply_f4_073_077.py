#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
from collections import Counter
import shutil,sys
import apply_f4_053_057 as h

W=h.W; NS=h.NS

REQ=[
 'Vasl ve Fasl Yazımlarının Dilsel ve Anlamsal Yorumlarda Kullanılması',
 'Mushaflarda bazı kelime ve edatların bitişik veya ayrı yazılması, resm-i mushafın dikkat çeken özelliklerinden biridir.',
 'Resme bağlılığın normatif gerekçeleri, ilk mushaf hattına bağlılık ve sonraki mushaf geleneğindeki süreklilik düşüncesi etrafında ele alınmıştır.',
 'Resmin tarihsel kökeni konusunda tevkîfîlik iddiası ile erken Arap yazısının tarihsel şartlarını öne çıkaran açıklamalar birbirinden ayrılmaktadır.',
 'İbn Haldûn, mushaf yazımındaki bazı farklılıkları erken Arap yazısının tarihsel şartlarıyla açıklamakta',
 'Resm-i mushaf etrafındaki tartışmalar başlıca üç düzeyde ele alınabilir:',
 'Resme bağlılığın sonraki mushaf yazımındaki hükmü konusunda da farklı yaklaşımlar bulunmaktadır.'
]
STALE=[
 'Resm-i Osmânî’de Yazım Farkının Anlam Farkına İşaret Etmesi',
 'Sözü edilen örnekler resm-i mushaf’ın yalnızca imlâya ilişkin bir tercih olmadığını, aynı zamanda anlamı yönlendiren',
 'Daha geniş açıdan değerlendirildiğinde söz konusu örnekler resm-i Osmânî ile nahiv arasındaki ilişkiyi de gözler önüne sermektedir.',
 "İbn Haldûn'un bu yaklaşımı resm-i mushaf'ın hüccet değerini zayıflatma tehlikesi taşımaktadır.",
 'Çağdaş resm-i Osmânî literatüründe İbn Haldûn’a karşı geliştirilen cevaplar genellikle iki dayanak üzerinde ilerlemiştir.',
 'Sonuç olarak resm-i mushaf etrafındaki tartışmalar üç ana çizgide toplanmaktadır:',
 'Bu üçlü tasnif birlikte değerlendirildiğinde, mushaf yazımında resm-i Osmânî meselesinin tek boyutlu bir tartışma olmadığı anlaşılmaktadır.'
]

def body_text(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml'))
        return '\n'.join(h.txt(p) for p in d.xpath('.//w:body/w:p',namespaces=NS))

def complete(path):
    t=h.norm(body_text(path))
    return all(h.norm(x) in t for x in REQ) and all(h.norm(x) not in t for x in STALE)

def new_plain_like(p,text):
    q=deepcopy(p); ppr=q.find(f'{{{W}}}pPr')
    for c in list(q):
        if c is not ppr:q.remove(c)
    h.add(q,text,h.first_rpr(p))
    return q

def collect_runs(pars):
    runs={}; ids=[]
    for p in pars:
        s=h.spec(p)
        if s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
            raise RuntimeError('protected structure in merge source '+str(s))
        ids += s['fn']
        for r in p.xpath('./w:r',namespaces=NS):
            x=r.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
            if x:runs[x[0]]=deepcopy(r)
    return ids,runs

def replace_with_parts(target,sources,parts,expected_source_ids):
    ids,runs=collect_runs(sources)
    if ids!=list(map(str,expected_source_ids)):
        raise RuntimeError(f'merge source footnote mismatch {ids} != {expected_source_ids}')
    rp=h.first_rpr(target); h.clear(target)
    for kind,val in parts:
        if kind=='t':h.add(target,val,rp)
        elif kind=='fn':target.append(deepcopy(runs[str(val)]))
        else:raise ValueError(kind)

def validate_structural(src,out):
    prot=['word/footnotes.xml','word/styles.xml','word/numbering.xml','word/settings.xml','word/_rels/document.xml.rels']
    with ZipFile(src) as zs, ZipFile(out) as z:
        assert z.testzip() is None
        for n in z.namelist():
            if n.endswith('.xml') or n.endswith('.rels'):etree.fromstring(z.read(n))
        ds=etree.fromstring(zs.read('word/document.xml'));d=etree.fromstring(z.read('word/document.xml'));fs=etree.fromstring(zs.read('word/footnotes.xml'));f=etree.fromstring(z.read('word/footnotes.xml'))
        f0=[x for x in fs.xpath('//w:footnote/@w:id',namespaces=NS) if int(x)>0]; ff=[x for x in f.xpath('//w:footnote/@w:id',namespaces=NS) if int(x)>0]
        r0=ds.xpath('//w:footnoteReference/@w:id',namespaces=NS); rr=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        assert ff==f0 and len(ff)==len(rr)==469
        assert set(rr)==set(r0)==set(ff) and not [k for k,v in Counter(rr).items() if v>1]
        assert h.instrs(z)==h.instrs(zs) and len(h.instrs(z))==520
        assert len(d.xpath('//w:rtl',namespaces=NS))==len(ds.xpath('//w:rtl',namespaces=NS))
        assert len(d.xpath('//w:bookmarkStart',namespaces=NS))==len(ds.xpath('//w:bookmarkStart',namespaces=NS))==53
        assert len(d.xpath('//w:bookmarkEnd',namespaces=NS))==len(ds.xpath('//w:bookmarkEnd',namespaces=NS))==53
        assert len(d.xpath('//w:hyperlink',namespaces=NS))==len(ds.xpath('//w:hyperlink',namespaces=NS))==52
        for n in prot:assert zs.read(n)==z.read(n),n
        # moved refs are expected, but exact identity is not.
        assert Counter(rr)==Counter(r0)
    if not complete(out):raise RuntimeError('F4-073-077 postconditions incomplete')

def apply(src:Path,out:Path):
    if complete(src):
        validate_structural(src,src);shutil.copyfile(src,out)
        return [(f'F4-{n:03d}','current','ALREADY_SATISFIED') for n in range(73,78)]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml'));body=d.find('.//w:body',namespaces=NS);changed=False;rows=[]
        ps=body.xpath('./w:p',namespaces=NS)

        # F4-073 heading, opening, one restrained closing; remove duplicate second closing.
        i73,hd= h.find(ps,'Resm-i Osmânî’de Yazım Farkının Anlam Farkına İşaret Etmesi')
        stH=h.span(hd,'Resm-i Osmânî’de Yazım Farkının Anlam Farkına İşaret Etmesi','Vasl ve Fasl Yazımlarının Dilsel ve Anlamsal Yorumlarda Kullanılması');changed |= stH=='APPLIED'
        ps=body.xpath('./w:p',namespaces=NS);_,p282=h.find(ps,'Resm-i Osmânî’nin diğer özelliklerinden biri de, bazı kelimelerin bağlama göre farklı biçimlerde yazılması')
        R73open=('Mushaflarda bazı kelime ve edatların bitişik veya ayrı yazılması, resm-i mushafın dikkat çeken özelliklerinden biridir. Klasik kaynaklarda bu biçimler kimi zaman dilsel yapı veya anlam ilişkileriyle açıklanmıştır. Bununla birlikte vasl ve faslın tarihsel yazım sebebi ile sonraki anlamsal yorumlar aynı kanıt düzeyinde değerlendirilmemelidir.')
        h.whole(p282,R73open,[281]);changed=True
        ps=body.xpath('./w:p',namespaces=NS);_,p285=h.find(ps,'Sözü edilen örnekler resm-i mushaf’ın yalnızca imlâya ilişkin bir tercih olmadığını')
        _,p286=h.find(ps,'Daha geniş açıdan değerlendirildiğinde söz konusu örnekler resm-i Osmânî ile nahiv arasındaki ilişkiyi')
        R73close=('Bu örnekler, vasl ve fasl biçimlerinin klasik dil ve tefsîr yorumlarında anlamlandırıldığını göstermektedir. Ancak bu yorumların, ilgili yazım biçimlerinin ortaya çıkış sebebini tek başına belirlediği söylenmemelidir.')
        h.whole(p285,R73close,[289]);body.remove(p286);changed=True
        rows.append(('F4-073',i73,'STRUCTURALLY_APPLIED'))

        # Capture current 3.6 nodes before reordering.
        ps=body.xpath('./w:p',namespaces=NS)
        i74,head36=h.find(ps,'Resm-i Mushaf’ın Bağlayıcılığı, Hikmet Boyutu ve Eleştirel Yaklaşımlar')
        _,p288=h.find(ps,'İslâm ilimleri içinde resm-i mushaf meselesi, sadece imlâ biçimine ilişkin teknik bir konudan ibaret olmayıp')
        _,p289=h.find(ps,'Buna karşılık İslâm kaynaklarında bütün imlâ farklılıklarının sır ve hikmet çevresinde açıklanmadığı')
        _,p290=h.find(ps,'Resme bağlılık ve onu esas alma tavrı sadece kırâat ve tecvid âlimleriyle sınırlı kalmamış')
        _,p291=h.find(ps,'Bu genel kabul karşısında mushaf yazımındaki kıyasa aykırı unsurları ilâhî sırlarla açıklama eğilimini reddeden')
        _,p292=h.find(ps,'İbn Haldûn resm-i mushaf meselesini ele alırken mushaf yazımında, yaygın hat ve imlâ kaideleriyle tam uyuşmayan')
        _,p293=h.find(ps,'Ne var ki bu yaklaşım klasik ve çağdaş literatürde problemli bulunmuş')
        _,p294=h.find(ps,'Çağdaş resm-i Osmânî literatüründe İbn Haldûn’a karşı geliştirilen cevaplar')
        _,p295=h.find(ps,'Resm-i Osmânî’nin çağdaş âlimler nezdinde de kazandığı yüksek değer')
        _,p296=h.find(ps,'Sonuç olarak resm-i mushaf etrafındaki tartışmalar üç ana çizgide toplanmaktadır:')
        _,p303=h.find(ps,'Mushafın yazımında resm-i Osmânî’ye bağlı kalmanın gerekip gerekmediği meselesi ilk dönem ve çağdaş kaynaklarda üç temel görüş')
        _,p304=h.find(ps,'İkinci görüşe göre resm-i Osmânî’ye bağlı kalmak zorunlu değildir;')
        _,p305=h.find(ps,'Üçüncü görüş ise, özellikle halk için mushafın bilinen genel imlâ kurallarına göre yazılması gerektiğini')
        _,p306=h.find(ps,'Bu üçlü tasnif birlikte değerlendirildiğinde, mushaf yazımında resm-i Osmânî meselesinin tek boyutlu bir tartışma olmadığı')

        # F4-074: create explicit conceptual framing and clean P288 into the hikmet block.
        norm=('Resme bağlılığın normatif gerekçeleri, ilk mushaf hattına bağlılık ve sonraki mushaf geleneğindeki süreklilik düşüncesi etrafında ele alınmıştır. Ahmed b. Hanbel’e nispet edilen Osmânî mushaf hattına muhalefeti yasaklayan söz de bu normatif çizginin örneklerinden biridir. Bu tür normatif değerlendirmeler, resmin tarihsel olarak nasıl oluştuğu sorusundan ve yazım biçimlerine sonradan yüklenen hikmet yorumlarından ayrı ele alınmalıdır.')
        origin=('Resmin tarihsel kökeni konusunda tevkîfîlik iddiası ile erken Arap yazısının tarihsel şartlarını öne çıkaran açıklamalar birbirinden ayrılmaktadır. Tevkîfîlik, resmin nebevî yönlendirmeyle belirlendiğini savunan bir iddia iken tarihsel açıklamalar yazım biçimlerini erken Arap yazısının gelişim şartlarıyla ilişkilendirir. Bu iki yaklaşımın delil türleri ayrı ayrı değerlendirilmelidir.')
        n1=new_plain_like(p289,norm);n2=new_plain_like(p289,origin)
        # Remove norm/tawqif material from the paragraph that carries the hikmet examples.
        removals=[
          'İslâm ilimleri içinde resm-i mushaf meselesi, sadece imlâ biçimine ilişkin teknik bir konudan ibaret olmayıp kırâatin sahihliği, metin otoritesi ve anlam yorumuyla doğrudan ilişkili bir alan olarak ele alınmıştır. ',
          'Nitekim Ahmed b. Hanbel’in, “Osman mushaf hattına ister bir ‘vav’ ister bir ‘ya’ isterse başka bir unsur bakımından olsun aykırı davranmanın haram olduğunu” söylediği aktarılmıştır. Bu rivâyet mushaf resminin birçok âlim tarafından bağlayıcı kabul edildiğini ortaya koymaktadır. ',
          'Bu sebeple bazı âlimler, resm-i mushaf’ı tevkîfî, yani beşerî tercihten ziyade nakille sabit olmuş bir yazım şekli olarak görmüş; hatta bazıları bu yazımın Hz. Peygamber’in o günkü şartlarda ashâbına belirttiği imlâ ile ilişkili olduğunu ileri sürmüştür. Bu yaklaşıma göre resm-i Osmânî’nin yalnız tarihsel bir yazı geleneğinden ziyade korunması gereken bir aktarım biçimi olarak algılandığını ortaya koymaktadır. '
        ]
        for x in removals:
            st=h.span(p288,x,'');changed |= st=='APPLIED'
        st=h.span(p288,'Bu bağlayıcı ve koruyucu yaklaşım ile birlikte bazı âlimler, mushaf kitâbetindeki kıyasa aykırı görünen yerlerde özel hikmetler ve anlam incelikleri aramıştır.','Ayrı bir yorum çizgisinde bazı âlimler, mushaf kitâbetindeki kıyasa aykırı görünen yerlerde özel hikmetler ve anlam incelikleri aramıştır.');changed |= st=='APPLIED'
        st=h.span(p288,'Bu yaklaşım aynı zamanda resm-i Osmânî’nin mana ile doğrudan ilişkilendirildiği klasik yorum geleneğinin teorik temelini de oluşturmaktadır.','Bu pasajlar, klasik yorum literatüründe resm ile mana arasında ilişki kurulduğunu göstermektedir; ancak bu yorumlar tarihsel yazım sebebiyle aynı delil düzeyinde değerlendirilmemelidir.');changed |= st=='APPLIED'

        # F4-075: merge defensive response into a sourced, evidence-level paragraph; semantic note placement reverses 306/307 intentionally.
        R75a='İbn Haldûn, mushaf yazımındaki bazı farklılıkları erken Arap yazısının tarihsel şartlarıyla açıklamakta ve bunlara zorunlu biçimde özel hikmetler yüklenmesine itiraz etmektedir.'
        R75b=' Sonraki resm literatüründe bu görüşe, resmin sahâbe uygulamasıyla nakledilmesi, mushaf geleneğindeki süreklilik ve bağlayıcılık düşüncesi üzerinden çeşitli cevaplar verilmiştir.'
        R75c=' Bu cevaplar, resme bağlılığın normatif gerekçelerini açıklamak bakımından önemlidir; ancak erken yazım biçimlerinin tarihsel sebebini tek başına belirleyen kanıtlar olarak değerlendirilmemelidir.'
        replace_with_parts(p293,[p293,p294],[('t',R75a),('fn',307),('t',R75b),('fn',306),('t',R75c)],[306,307]);body.remove(p294);changed=True

        # F4-076 exact balanced closing.
        R76=('Resm-i mushaf etrafındaki tartışmalar başlıca üç düzeyde ele alınabilir: resmin tarihsel kökeni ve tevkîfîliği; sonraki mushaf geleneğindeki bağlayıcılığı; yazım özelliklerine yüklenen dilsel, anlamsal veya hikmet merkezli yorumlar. Bu düzeyler birbirine temas etmekle birlikte aynı delil ve değerlendirme alanına ait değildir.')
        h.whole(p296,R76);changed=True

        # F4-077: classification transition + move the three views into 3.6; remove stale long closing.
        R77=('Resme bağlılığın sonraki mushaf yazımındaki hükmü konusunda da farklı yaklaşımlar bulunmaktadır. Bir grup âlim Osmânî resme bağlılığı zorunlu görürken, bir kısmı öğretim ve kolaylık amacıyla çağdaş imlâdan yararlanılabileceğini, bir kısmı ise bu iki alan arasında kullanım bağlamına göre ayrım yapılabileceğini savunmuştur. Birinci görüş, mushafların yazımında resm-i Osmânî’ye bağlı kalmanın gerekli olduğunu savunmakta ve selef ile halef âlimlerinin çoğunluğu bu çizgide gösterilmektedir.')
        h.whole(p303,R77);body.remove(p306);changed=True

        # Reorder all relevant existing paragraphs, preserving their OOXML/run/footnote structures.
        order=[n1,n2,p289,p290,p288,p295,p291,p292,p293,p303,p304,p305,p296]
        for q in order:
            if q.getparent() is body:body.remove(q)
        insert_at=body.index(head36)+1
        for q in order:
            body.insert(insert_at,q);insert_at+=1
        changed=True
        rows.extend([('F4-074',i74,'STRUCTURALLY_APPLIED'),('F4-075','3.6','STRUCTURALLY_APPLIED'),('F4-076','3.6-end','APPLIED'),('F4-077','3.6/3.7','STRUCTURALLY_APPLIED')])

        if not changed:
            shutil.copyfile(src,out);return rows
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    validate_structural(src,out)
    return rows

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,row)))
