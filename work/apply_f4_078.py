#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import shutil,sys
import apply_f4_053_057 as h

W=h.W; NS=h.NS

MAIN='Resm-i Osmânî’ye Bağlılığın Gerekçeleri ve Sınırları'
CORE=("Osmânî mushafların İslâm toplumunda müşterek mushaf geleneğinin temelini oluşturması, bu yazım biçiminin sonraki mushaflarda korunmasına güçlü bir tarihsel ve normatif zemin sağlamıştır. Resme bağlılık, Kur’an’ın sözlü rivâyet geleneğini ikame eden bağımsız bir koruma mekanizması olarak değil, telakki ve isnadla aktarılan metnin müşterek yazılı çerçevesini sürdürme çabası olarak anlaşılmalıdır.")
DEMOTE={
'Nebevî Rehberliğin ve Sünnetin Muhafazası Bağlamında Resm-i Osmânî’ye Bağlılık':
'Bu normatif çizgiye, ilk mushaf hattının nebevî dönemle ve ümmet hafızasıyla kurduğu tarihî bağa ilişkin yorumlar da eklenmiştir.',
'Selef-i Sâlihînin İlmî Faziletini İdrâk ve Resm-i Mushaf’ın Bu Fazilete Delaleti':
'Bağlılık gerekçelerinin bir diğer kısmı, ilk neslin ilmî ve rivâyet otoritesine duyulan güven etrafında kurulmuştur.',
'Kur’an-ı Kerim’in Öğreniminde Müşâfehe Geleneğinin İhyası ve Resm-i Osmânî’nin Bu Sürece Katkısı':
'Kur’an’ın okunma biçiminin yalnız yazıdan çıkarılmadığı, telakki ve müşâfehe yoluyla aktarıldığı hususu bu tartışmanın ilmî boyutunu oluşturur.',
'Mushafın Aslî Yazım Geleneğinin Korunması ve Bunun Gerekçeleri':
'Mushaf yazımının tarihsel sürekliliği ve resm literatürünün korunması da bağlılığın ilmî gerekçeleri arasında zikredilmiştir.',
'Resm-i Osmânî’nin Ümmet Birliği ve Ortak Dinî Hafıza Açısından İşlevi':
'Son olarak, müşterek mushaf yazısının farklı coğrafya ve nesiller arasında ortak bir yazılı hafıza oluşturması birlik gerekçesinin tarihsel yönünü açıklar.'
}
REMOVE=[
'İslâm resm literatüründe doğrudan bu manevi dil her zaman aynı yoğunlukta kullanılmasa da,',
'Çağdaş dönemde de bu yaklaşımın tamamen ortadan kalkmadığı görülmektedir.',
'Sonuç olarak denilebilir ki resm-i Osmânî’ye bağlılık, bazı âlimler ve müellifler nezdinde',
'Bundan ötürü denilebilir ki resm-i Osmânî’ye bağlılık, bazı müelliflere göre',
'Bu çerçevede mushaf hattına yönelen müdahaleler de sadece bir imlâ değişikliği olarak değerlendirilmemektedir.',
'Bütün bu tespitler birlikte değerlendirildiğinde, mushafın aslî resminin korunması meselesinin',
'Bu sebeple resm-i Osmânî, basit bir yazım geleneği olarak görülemeyecek ölçüde,',
'Resm-i Osmânî’ye bağlılık, bu bakış açısına göre, yalnızca mushafın ilkyazım biçimini koruma iradesiyle açıklanamaz.'
]

def body_text(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml'))
        return '\n'.join(h.txt(p) for p in d.xpath('.//w:body/w:p',namespaces=NS))

def normalise_heading(p):
    ppr=p.find(f'{{{W}}}pPr')
    if ppr is None:
        ppr=etree.Element(f'{{{W}}}pPr'); p.insert(0,ppr)
    ps=ppr.find(f'{{{W}}}pStyle')
    if ps is None:
        ps=etree.Element(f'{{{W}}}pStyle'); ppr.insert(0,ps)
    ps.set(f'{{{W}}}val','Normal')
    for tag in ('outlineLvl','keepNext'):
        x=ppr.find(f'{{{W}}}{tag}')
        if x is not None:ppr.remove(x)

def text_only_replace_preserve_structure(p,new):
    sp=h.spec(p)
    if sp['fn'] or sp['instr'] or sp['fld'] or sp['hyper'] or sp['rtl']:
        raise RuntimeError('unsafe structural heading '+str(sp))
    nodes=p.xpath('.//w:t',namespaces=NS)
    if not nodes: raise RuntimeError('heading has no text')
    nodes[0].text=new
    for n in nodes[1:]: n.text=''

def complete(path):
    t=h.norm(body_text(path))
    if h.norm(MAIN) not in t or h.norm(CORE) not in t:return False
    for old,new in DEMOTE.items():
        if h.norm(old) in t or h.norm(new) not in t:return False
    for x in REMOVE:
        if h.norm(x) in t:return False
    return True

def validate_structural(src,out):
    prot=['word/footnotes.xml','word/styles.xml','word/numbering.xml','word/settings.xml','word/_rels/document.xml.rels']
    with ZipFile(src) as zs,ZipFile(out) as z:
        assert z.testzip() is None
        for n in z.namelist():
            if n.endswith('.xml') or n.endswith('.rels'):etree.fromstring(z.read(n))
        ds=etree.fromstring(zs.read('word/document.xml')); d=etree.fromstring(z.read('word/document.xml'))
        fs=etree.fromstring(zs.read('word/footnotes.xml')); f=etree.fromstring(z.read('word/footnotes.xml'))
        f0=[x for x in fs.xpath('//w:footnote/@w:id',namespaces=NS) if int(x)>0]
        ff=[x for x in f.xpath('//w:footnote/@w:id',namespaces=NS) if int(x)>0]
        r0=ds.xpath('//w:footnoteReference/@w:id',namespaces=NS); rr=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        assert ff==f0 and rr==r0 and len(ff)==len(rr)==469
        assert h.instrs(z)==h.instrs(zs) and len(h.instrs(z))==520
        assert len(d.xpath('//w:rtl',namespaces=NS))==len(ds.xpath('//w:rtl',namespaces=NS))
        assert len(d.xpath('//w:bookmarkStart',namespaces=NS))==len(ds.xpath('//w:bookmarkStart',namespaces=NS))==53
        assert len(d.xpath('//w:bookmarkEnd',namespaces=NS))==len(ds.xpath('//w:bookmarkEnd',namespaces=NS))==53
        assert len(d.xpath('//w:hyperlink',namespaces=NS))==len(ds.xpath('//w:hyperlink',namespaces=NS))==52
        for n in prot: assert zs.read(n)==z.read(n),n
    if not complete(out):raise RuntimeError('F4-078 postconditions incomplete')

def apply(src:Path,out:Path):
    if complete(src):
        validate_structural(src,src); shutil.copyfile(src,out)
        return [('F4-078','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS)
        ps=body.xpath('./w:p',namespaces=NS)
        i,main=h.find(ps,'Resm-i Osmânî’ye Bağlılığın Hata ve Tahriften Koruyucu İşlevi')
        h.span(main,'Resm-i Osmânî’ye Bağlılığın Hata ve Tahriften Koruyucu İşlevi',MAIN)
        q=deepcopy(ps[i+1]); ppr=q.find(f'{{{W}}}pPr')
        for c in list(q):
            if c is not ppr:q.remove(c)
        h.add(q,CORE,h.first_rpr(ps[i+1]))
        body.insert(body.index(main)+1,q)

        for old,new in DEMOTE.items():
            ps=body.xpath('./w:p',namespaces=NS); _,p=h.find(ps,old)
            text_only_replace_preserve_structure(p,new); normalise_heading(p)

        for a in REMOVE:
            ps=body.xpath('./w:p',namespaces=NS); _,p=h.find(ps,a)
            sp=h.spec(p)
            if sp['fn'] or sp['instr'] or sp['fld'] or sp['hyper'] or sp['rtl'] or sp['book']:
                raise RuntimeError('refuse deleting protected/referenced paragraph '+str(sp))
            body.remove(p)

        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():
                zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    validate_structural(src,out)
    return [('F4-078',i,'STRUCTURALLY_APPLIED')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,row)))
