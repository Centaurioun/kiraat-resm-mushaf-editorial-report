#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_INPUT_SHA='99b579b4c1ea369fbf4f27705d42a1f632d06f5e67bc177dd09363c765a07b32'
PREFIX=('Resm-i Osmânî’ye uygunluk gerçek veya ihtimalî biçimde gerçekleşebilir. '
        'Gerçek uygunlukta okuyuş, mushafın yazılı yapısı tarafından doğrudan karşılanır. '
        'İhtimalî uygunlukta ise yazım, okuyuşu açıkça göstermese de onunla bağdaşır ve onu dışlamaz. '
        'Bu durum, bir yazı iskeletinin sahih rivâyetle sabit birden fazla okuyuşa imkân verebilmesini açıklar. '
        'Ancak bu imkân rivâyetin yerine konulamaz; yazımla bağdaşan ihtimallerden hangisinin kırâat olduğu telakki ve isnadla belirlenir')
OLD_TAIL=('. Sahih, meşhur, âhâd ve şâz nitelemeleri de tek bir ölçünün farklı dereceleri değildir. '
          'Bunlar naklin güvenilirliği, yaygınlığı, kabulü ve genel tilâvet alanındaki konumuyla ilgili farklı değerlendirme boyutlarını ifade eder. '
          'Şâz bir rivâyetin tefsîrî veya dilsel değeri bulunabilmesi, onun bağlayıcı bir kırâat kabul edilmesiyle aynı mesele değildir.')
NEW_TAIL=('. Sahih, meşhur, âhâd ve şâz nitelemeleri, naklin güvenilirliği, yaygınlığı, kabulü ve genel tilâvet alanındaki konumuyla ilgili farklı değerlendirme boyutlarını ifade eder. '
          'Şâz bir rivâyetin tefsîrî veya dilsel bilgi değeri ile bağlayıcı kırâat statüsü ayrı ayrı değerlendirilmelidir.')
OLD=PREFIX+OLD_TAIL
NEW=PREFIX+NEW_TAIL

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

def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS)
    return len(ps)==674 and text(ps[26])==NEW and OLD_TAIL not in text(ps[26])

def apply(src,out):
    actual_sha=sha256(src)
    if actual_sha!=EXPECTED_INPUT_SHA:
        raise RuntimeError('input sha mismatch '+actual_sha)
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError('body count')
        if satisfied(d):
            shutil.copyfile(src,out); validate(src,out,False); print('F5-009\tALREADY_SATISFIED'); return
        p=ps[26]; before=text(p)
        if before!=OLD: raise RuntimeError('P26 precondition mismatch')
        bs=sig(p)
        start=len(PREFIX); end=len(OLD)
        replace_range(p,start,end,NEW_TAIL)
        after=text(p)
        if after!=NEW or sig(p)!=bs: raise RuntimeError('F5-009 postcondition/structure failure')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,True)
    print('F5-009\tAPPLIED\tP26'); print('BEFORE\t'+before); print('AFTER\t'+after)

def validate(src,out,chg):
    with ZipFile(src) as a,ZipFile(out) as b:
        if a.namelist()!=b.namelist() or b.testzip() is not None: raise RuntimeError('zip invariant')
        for n in a.namelist():
            if n!='word/document.xml' and a.read(n)!=b.read(n): raise RuntimeError('unexpected package change '+n)
        da=etree.fromstring(a.read('word/document.xml')); db=etree.fromstring(b.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=674 or len(pb)!=674: raise RuntimeError('body count invariant')
        changed=[i for i,(x,y) in enumerate(zip(pa,pb)) if c14n(x)!=c14n(y)]
        if changed!=([26] if chg else []): raise RuntimeError('paragraph change set '+repr(changed))
        if sig(pa[26])!=sig(pb[26]) or not satisfied(db): raise RuntimeError('P26 invariant')
        if text(pb[26]).startswith(PREFIX+'.'):
            raise RuntimeError('unexpected punctuation duplication')
        ia=instrs(a); ib=instrs(b)
        if ia!=ib or len(ib)!=520: raise RuntimeError('fields')
        if (sum('ADDIN ' in x for x in ib),sum('ZOTERO_ITEM' in x for x in ib),sum('ZOTERO_BIBL' in x for x in ib))!=(466,465,1): raise RuntimeError('zotero')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnotes')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53 or len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('bookmarks/hyperlinks')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('rtl')

if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('usage: apply_f5_009.py INPUT.docx OUTPUT.docx')
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
