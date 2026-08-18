#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_INPUT_SHA='cc3d906b77ae5325b6bcb9b5e458b1af30ef37191c5ee956455613161bd693da'
OLD_A='Medine dönemine gelindiğinde ise durum daha farklı bir görünüm arz etmiştir. Bu döneme ilişkin rivâyetler, vahyin yazıya geçirilmesi hususunda çok daha sistemli ve titiz bir uygulamanın bulunduğunu göstermektedir.'
NEW_A='Medine dönemine ilişkin rivâyetlerde Hz. Peygamber’in vahiy geldiğinde kâtiplerden birini çağırdığı ve âyetleri yazdırdığı aktarılır.'
OLD_B=' Nitekim vahiy geldiğinde Hz. Peygamber’in vahiy kâtiplerinden birini çağırttığı, gelen âyet ve sûreleri bizzat yazdırdığı yönünde çok sayıda rivâyet bulunmaktadır. Bu rivâyetlerden biri, '
NEW_B=' '
OLD_C='dir. Bu rivâyetler, Medine döneminde vahyin yazıyla kaydedilmesinin düzenli bir uygulama olarak aktarıldığına işaret etmektedir.'
NEW_C=' bu uygulamanın örneklerinden biridir. Rivâyetlerde Medine dönemindeki vahiy kaydı düzenli bir uygulama olarak yer alır.'
ZAYD='Zeyd b. Sâbit’in (ö. 45/665), “Allah Rasûlü’ne vahiy geldiğinde derhâl beni çağırır, ben de onu yazıya geçirirdim.” şeklindeki ifadesi bu uygulamanın örneklerinden biridir.'
CAUTION='Ancak Hz. Peygamber hayatta iken vahiy yazıya aktarılmış olsa da iki kapak arasında bir araya getirilememiştir.'
F5018='Yazılı vahiy metinlerinin Hz. Peygamber döneminde bir araya getirilmemiş olmasının, vahyin o dönemde yazıya geçirilmediği anlamına gelmediğini, bilakis yazılan metinlerin dağınık hâlde bulunduğuna ve bir araya toplanmadığına delalet ettiğini özellikle vurgulamamız gerekmektedir.'

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

def replace_range(p,start,end,new):
    nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]; starts=[];cur=0
    for v in vals: starts.append(cur);cur+=len(v)
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start<st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end<=st+len(v))
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def replace_once(p,old,new):
    before=text(p)
    if before.count(old)!=1: raise RuntimeError(f'unique in-paragraph target failure: {old!r} count={before.count(old)}')
    start=before.index(old); replace_range(p,start,start+len(old),new)

def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS)
    if len(ps)!=674: return False
    p=text(ps[53])
    if not p.startswith(NEW_A): return False
    if OLD_A in p or 'Nitekim vahiy geldiğinde' in p or OLD_C in p: return False
    if ZAYD not in p or 'Rivâyetlerde Medine dönemindeki vahiy kaydı düzenli bir uygulama olarak yer alır.' not in p: return False
    if CAUTION not in p: return False
    if ps[53].xpath('.//w:footnoteReference/@w:id',namespaces=NS)!=['24','25','26']: return False
    if F5018 not in text(ps[54]): return False
    return True

def apply(src,out):
    actual_sha=sha256(src)
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        if satisfied(d):
            shutil.copyfile(src,out); validate(src,out,False,53)
            print('F5-017\tALREADY_SATISFIED\tP53'); return
        if actual_sha!=EXPECTED_INPUT_SHA: raise RuntimeError('input sha mismatch '+actual_sha)
        hits=[i for i,p in enumerate(ps) if OLD_A in text(p)]
        if hits!=[53]: raise RuntimeError('F5-017 target location failure '+repr(hits))
        p=ps[53]; before=text(p); bs=sig(p)
        refs=p.xpath('.//w:footnoteReference/@w:id',namespaces=NS)
        if refs!=['24','25','26']: raise RuntimeError('P53 footnote precondition '+repr(refs))
        if CAUTION not in before or F5018 not in text(ps[54]): raise RuntimeError('Fourth/F5-018 protection precondition')
        replace_once(p,OLD_A,NEW_A)
        replace_once(p,OLD_B,NEW_B)
        replace_once(p,OLD_C,NEW_C)
        after=text(p)
        if sig(p)!=bs: raise RuntimeError('P53 structural signature changed')
        if p.xpath('.//w:footnoteReference/@w:id',namespaces=NS)!=['24','25','26']: raise RuntimeError('P53 footnotes moved/damaged')
        if CAUTION not in after or F5018 not in text(ps[54]): raise RuntimeError('protected text damaged')
        if not satisfied(d): raise RuntimeError('F5-017 document satisfaction failure')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,True,53)
    print('F5-017\tAPPLIED\tP53'); print('BEFORE\t'+before); print('AFTER\t'+after)

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
        if not satisfied(db): raise RuntimeError('target paragraph/document invariant')
        if pb[idx].xpath('.//w:footnoteReference/@w:id',namespaces=NS)!=['24','25','26']: raise RuntimeError('P53 footnote invariant')
        if F5018 not in text(pb[54]): raise RuntimeError('F5-018 pre-application/damage')
        ia=instrs(a); ib=instrs(b)
        if ia!=ib or len(ib)!=520: raise RuntimeError('fields')
        if (sum('ADDIN ' in x for x in ib),sum('ZOTERO_ITEM' in x for x in ib),sum('ZOTERO_BIBL' in x for x in ib))!=(466,465,1): raise RuntimeError('zotero')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnotes')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53 or len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('bookmarks/hyperlinks')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('rtl')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_017.py INPUT.docx OUTPUT.docx')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
