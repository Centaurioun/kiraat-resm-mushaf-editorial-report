#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_INPUT_SHA='554f4b806c66681e55fcba093764d25bca9e9926ea0f296e7f0b027391b45437'
OLD='Yazılı vahiy metinlerinin Hz. Peygamber döneminde bir araya getirilmemiş olmasının, vahyin o dönemde yazıya geçirilmediği anlamına gelmediğini, bilakis yazılan metinlerin dağınık hâlde bulunduğuna ve bir araya toplanmadığına delalet ettiğini özellikle vurgulamamız gerekmektedir. Nitekim Hâris el-Muhâsibî’nin (ö. 243/857) de belirttiği üzere, Kur’an’ın yazıya geçirilmesi nüzûl sonrasında ortaya çıkmış bir mesele değildir. Çünkü Hz. Peygamber, ilk andan itibaren vahyin yazılmasını emretmiş; ancak bu yazım faaliyeti, dönemin imkânları doğrultusunda taş, kemik, hurma dalları ve deri gibi farklı yazı malzemeleri üzerine ve dağınık bir biçimde yapılmıştır.'
NEW='Hz. Peygamber döneminde vahiy metinleri farklı malzemeler üzerinde yazılı olarak bulunuyor, ancak iki kapak arasında tek bir derleme hâlinde toplanmış değildi. Zerkeşî’nin Hâris el-Muhâsibî’den aktardığı değerlendirmede de Kur’an’ın nüzûl döneminde yazıya geçirildiği ve kayıtların farklı malzemeler üzerinde dağınık biçimde bulunduğu belirtilir.'
F5_019_ANCHOR="Hz. Peygamber döneminde cem ifadesi bazı rivâyetlerde Kur’an'ın ezberlenmesi anlamında kullanılmakla birlikte"

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def c14n(el): return etree.tostring(el,method='c14n')
def sig(el): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())

def instrs(z):
    out=[]
    for n in z.namelist():
        if n.startswith('word/') and n.endswith('.xml'):
            try:r=etree.fromstring(z.read(n))
            except Exception:continue
            out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return out

def replace_all_text(p,new):
    nodes=p.xpath('.//w:t',namespaces=NS)
    if not nodes: raise RuntimeError('P54 has no text nodes')
    nodes[0].text=new
    for n in nodes[1:]: n.text=''

def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS)
    if len(ps)!=674: return False
    old_hits=[i for i,p in enumerate(ps) if OLD in text(p)]
    new_hits=[i for i,p in enumerate(ps) if text(p)==NEW]
    if old_hits or new_hits!=[54]: return False
    if ps[54].xpath('.//w:footnoteReference/@w:id',namespaces=NS)!=['27']: return False
    if F5_019_ANCHOR not in text(ps[58]): return False
    return True

def apply(src,out):
    actual_sha=sha256(src)
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        if satisfied(d):
            shutil.copyfile(src,out); validate(src,out,False,54)
            print('F5-018\tALREADY_SATISFIED\tP54'); return
        if actual_sha!=EXPECTED_INPUT_SHA: raise RuntimeError('input sha mismatch '+actual_sha)
        hits=[i for i,p in enumerate(ps) if text(p)==OLD]
        if hits!=[54]: raise RuntimeError('unique P54 target failure '+repr(hits))
        p=ps[54]; before=text(p); before_sig=sig(p)
        if p.xpath('.//w:footnoteReference/@w:id',namespaces=NS)!=['27']: raise RuntimeError('P54 FN precondition')
        if F5_019_ANCHOR not in text(ps[58]): raise RuntimeError('F5-019 anchor missing before application')
        replace_all_text(p,NEW)
        if text(p)!=NEW or sig(p)!=before_sig: raise RuntimeError('P54 text/structure postcondition')
        if p.xpath('.//w:footnoteReference/@w:id',namespaces=NS)!=['27']: raise RuntimeError('FN27 moved/damaged')
        if not satisfied(d): raise RuntimeError('F5-018 document satisfaction failure')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,True,54)
    print('F5-018\tAPPLIED\tP54')
    print('BEFORE\t'+before)
    print('AFTER\t'+NEW)

def validate(src,out,chg,idx):
    with ZipFile(src) as a,ZipFile(out) as b:
        if a.namelist()!=b.namelist() or b.testzip() is not None: raise RuntimeError('zip invariant')
        for n in a.namelist():
            if n!='word/document.xml' and a.read(n)!=b.read(n): raise RuntimeError('unexpected package change '+n)
        da=etree.fromstring(a.read('word/document.xml')); db=etree.fromstring(b.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=674 or len(pb)!=674: raise RuntimeError('body count invariant')
        changed=[i for i,(x,y) in enumerate(zip(pa,pb)) if c14n(x)!=c14n(y)]
        if changed!=([idx] if chg else []): raise RuntimeError('paragraph change set '+repr(changed))
        if sig(pa[idx])!=sig(pb[idx]) or not satisfied(db): raise RuntimeError('target paragraph/document invariant')
        if pb[idx].xpath('.//w:footnoteReference/@w:id',namespaces=NS)!=['27']: raise RuntimeError('P54 footnote invariant')
        ia=instrs(a); ib=instrs(b)
        if ia!=ib or len(ib)!=520: raise RuntimeError('fields')
        if (sum('ADDIN ' in x for x in ib),sum('ZOTERO_ITEM' in x for x in ib),sum('ZOTERO_BIBL' in x for x in ib))!=(466,465,1): raise RuntimeError('zotero')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnotes')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53 or len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('bookmarks/hyperlinks')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('rtl')
        if text(pb[53])!=text(pa[53]) or text(pb[55])!=text(pa[55]) or text(pb[58])!=text(pa[58]): raise RuntimeError('neighbor/F5-019 invariant')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_018.py INPUT.docx OUTPUT.docx')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
