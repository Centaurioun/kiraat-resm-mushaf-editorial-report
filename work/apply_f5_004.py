#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
OLD='Bu sebeple her mushaf yazısı resm-i Osmânî olmadığı gibi, resm-i mushaf ile resm-i Osmânî de bütün bağlamlarda birbirinin yerine kullanılamaz.'
NEW='Bu iki terim, kapsamları farklı olduğu için bağlama göre ayrı kullanılmalıdır.'
BEFORE='Bu yaklaşım, çalışmada kullanılan kavramlar arasında bazı ayrımların korunmasını gerektirmektedir. Resm, en genel anlamıyla lafzın harflerle temsil edilen yazılı biçimini; resm-i mushaf, Kur’an kelimelerinin mushaflardaki yazım özelliklerini konu edinen alanı ifade eder. Resm-i Osmânî ise Hz. Osman döneminde çoğaltılan mushaflara nispet edilen ve sonraki resm literatüründe rivâyet yoluyla takip edilen yazım geleneğidir. '
AFTER=' Mushaf, Kur’an metninin yazılı olarak bir araya getirildiği nüshadır. İmam Mushaf ise Osmânî istinsah bağlamında örnek ve ortak başvuru niteliği atfedilen nüshayı belirtir. Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, müşterek mushaf otoritesi içinde farklı yazım rivâyetlerinin bulunabildiğini göstermektedir.'

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
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    for n in nodes[fi:li+1]:
        if n.xpath('ancestor::w:hyperlink',namespaces=NS): raise RuntimeError('F5-004 target inside hyperlink')
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS); t=text(ps[24]) if len(ps)>24 else ''
    return len(ps)==674 and t==BEFORE+NEW+AFTER and OLD not in t

def apply(src,out):
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError(f'body paragraph count {len(ps)} !=674')
        if satisfied(d):
            shutil.copyfile(src,out); validate(src,out,False); print('F5-004\tALREADY_SATISFIED'); return
        p=ps[24]; before=text(p)
        expected=BEFORE+OLD+AFTER
        if before!=expected: raise RuntimeError('P24 no longer matches exact F5-004 precondition')
        s=before.index(OLD); before_sig=sig(p)
        replace_range(p,s,s+len(OLD),NEW)
        after=text(p)
        if after!=BEFORE+NEW+AFTER: raise RuntimeError('F5-004 postcondition failed')
        if sig(p)!=before_sig: raise RuntimeError('P24 OOXML structure changed')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,True)
    print('F5-004\tAPPLIED\tP24')
    print('BEFORE\t'+before)
    print('AFTER\t'+after)
    print('SCOPE\tOnly the exact negative term-distinction sentence was replaced; surrounding definitions and later P24 text preserved.')

def validate(src,out,expect_change):
    with ZipFile(src) as za, ZipFile(out) as zb:
        if za.namelist()!=zb.namelist(): raise RuntimeError('ZIP member/order changed')
        if zb.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        for name in za.namelist():
            if name!='word/document.xml' and za.read(name)!=zb.read(name): raise RuntimeError(f'unexpected package change: {name}')
            if name.endswith('.xml') or name.endswith('.rels'): etree.fromstring(zb.read(name))
        da=etree.fromstring(za.read('word/document.xml')); db=etree.fromstring(zb.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=674 or len(pb)!=674: raise RuntimeError('body count changed')
        changed=[i for i,(a,b) in enumerate(zip(pa,pb)) if c14n(a)!=c14n(b)]
        expected=[24] if expect_change else []
        if changed!=expected: raise RuntimeError(f'changed paragraphs {changed} != expected {expected}')
        if expect_change and sig(pa[24])!=sig(pb[24]): raise RuntimeError('P24 structure changed')
        if not satisfied(db): raise RuntimeError('F5-004 corrected-state postcondition failed')
        ia=instrs(za); ib=instrs(zb)
        if ia!=ib or len(ib)!=520: raise RuntimeError('field instruction inventory changed')
        addin=sum('ADDIN ' in x for x in ib); item=sum('ZOTERO_ITEM' in x for x in ib); bib=sum('ZOTERO_BIBL' in x for x in ib)
        if (addin,item,bib)!=(466,465,1): raise RuntimeError('ADDIN/Zotero inventory changed')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnote references changed')
        if da.xpath('//w:bookmarkStart/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkStart/@w:id',namespaces=NS): raise RuntimeError('bookmark starts changed')
        if da.xpath('//w:bookmarkEnd/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkEnd/@w:id',namespaces=NS): raise RuntimeError('bookmark ends changed')
        if len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink inventory changed')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('RTL inventory changed')

if __name__=='__main__': apply(Path(sys.argv[1]),Path(sys.argv[2]))
