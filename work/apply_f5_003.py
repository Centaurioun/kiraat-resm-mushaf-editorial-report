#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
OLD1='Kitabın hareket noktası, resm-i Osmânî’nin kırâatleri meydana getiren bağımsız bir kaynak olmadığıdır.'
OLD2=' Çalışmada kırâatin aslî dayanağı, telakki ve müşâfehe yoluyla sürdürülen, edâ ve isnadla denetlenen rivâyet geleneği olarak kabul edilmektedir.'
NEW='Kırâatlerin aslî kaynağı, telakki ve müşâfehe yoluyla sürdürülen, edâ ve isnadla denetlenen rivâyet geleneğidir.'
REST=' Resm-i Osmânî ise bu sözlü aktarımın yerine geçen bağımsız bir kaynak değil, rivâyetle sabit okuyuşların müşterek mushaf yazısıyla ilişkisini gösteren tamamlayıcı bir ölçüdür. Mushaf hattı bu canlı aktarımın yerine geçmez; yazının bir okuyuşa teorik olarak imkân vermesi, o okuyuşun sahih kırâat olarak sabit olduğunu göstermez. Buna karşılık güvenilir biçimde nakledilen her okuyuş da ortak mushaf otoritesinden bağımsız olarak aynı konuma yerleştirilemez. Klasik kırâat usûlünde rivâyetin güvenilirliği, Arap dilinde bir veche sahip olması ve resm-i Osmânî’ye uygunluk, birbirine indirgenemeyen fakat birlikte işleyen ölçülerdir. Resm-i Osmânî’ye uygunluk, bu bütün içinde okuyuşu üreten değil, rivâyetle gelen okuyuşun ortak mushaf geleneğindeki kabul alanını belirleyen bir ölçüdür.'
OLD=OLD1+OLD2

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def c14n(el): return etree.tostring(el,method='c14n')
def sig(el): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())

def instrs(z):
    out=[]
    for name in z.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try:r=etree.fromstring(z.read(name))
            except Exception:continue
            out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return out

def replace_range(p,start,end,new):
    nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]
    starts=[]; cur=0
    for v in vals: starts.append(cur); cur+=len(v)
    if not (0 <= start < end <= cur): raise RuntimeError(f'invalid replacement span {start}:{end}/{cur}')
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    for n in nodes[fi:li+1]:
        if n.xpath('ancestor::w:hyperlink',namespaces=NS): raise RuntimeError('F5-003 target occurs inside hyperlink')
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS)
    return len(ps)==674 and text(ps[23]).startswith(NEW+REST) and OLD1 not in text(ps[23]) and OLD2.strip() not in text(ps[23])

def apply(src,out):
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError(f'body paragraph count {len(ps)} !=674')
        if satisfied(d):
            shutil.copyfile(src,out); validate(src,out,False); print('F5-003\tALREADY_SATISFIED'); return
        p=ps[23]; before=text(p)
        if before != OLD+REST: raise RuntimeError('P23 no longer matches exact F5-003 precondition')
        before_sig=sig(p)
        replace_range(p,0,len(OLD),NEW)
        after=text(p)
        if after != NEW+REST: raise RuntimeError('F5-003 postcondition failed')
        if sig(p)!=before_sig: raise RuntimeError('P23 OOXML structure changed')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,True)
    print('F5-003\tAPPLIED\tP23')
    print('BEFORE\t'+before)
    print('AFTER\t'+after)
    print('SCOPE\tOnly the first two sentences were consolidated into one positive thesis sentence; all later P23 text preserved.')

def validate(src,out,expect_change):
    with ZipFile(src) as za, ZipFile(out) as zb:
        if za.namelist()!=zb.namelist(): raise RuntimeError('ZIP member/order changed')
        if zb.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        for name in za.namelist():
            if name!='word/document.xml' and za.read(name)!=zb.read(name): raise RuntimeError(f'unexpected package change: {name}')
            if name.endswith('.xml') or name.endswith('.rels'): etree.fromstring(zb.read(name))
        da=etree.fromstring(za.read('word/document.xml')); db=etree.fromstring(zb.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=674 or len(pb)!=674: raise RuntimeError(f'body count changed {len(pa)}->{len(pb)}')
        changed=[i for i,(a,b) in enumerate(zip(pa,pb)) if c14n(a)!=c14n(b)]
        expected=[23] if expect_change else []
        if changed!=expected: raise RuntimeError(f'changed paragraphs {changed} != expected {expected}')
        if expect_change and sig(pa[23])!=sig(pb[23]): raise RuntimeError('P23 structure changed')
        if not satisfied(db): raise RuntimeError('F5-003 corrected-state postcondition failed')
        ia=instrs(za); ib=instrs(zb)
        if ia!=ib or len(ib)!=520: raise RuntimeError('field instruction inventory changed')
        addin=sum('ADDIN ' in x for x in ib); item=sum('ZOTERO_ITEM' in x for x in ib); bib=sum('ZOTERO_BIBL' in x for x in ib)
        if (addin,item,bib)!=(466,465,1): raise RuntimeError(f'ADDIN/Zotero inventory {(addin,item,bib)}')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnote references changed')
        if da.xpath('//w:bookmarkStart/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkStart/@w:id',namespaces=NS): raise RuntimeError('bookmark starts changed')
        if da.xpath('//w:bookmarkEnd/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkEnd/@w:id',namespaces=NS): raise RuntimeError('bookmark ends changed')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmark count changed')
        if len(da.xpath('//w:hyperlink',namespaces=NS))!=len(db.xpath('//w:hyperlink',namespaces=NS)) or len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink inventory changed')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('RTL inventory changed')

if __name__=='__main__': apply(Path(sys.argv[1]),Path(sys.argv[2]))
