#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
OLD="Hz. Peygamber'in vefatından sonra gerçekleştirilen cem ile Hz. Osman dönemindeki istinsah ise aynı işlem değildir."
CURRENT="Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan cem ve istinsah süreçlerine uzanmaktadır. Vahyin yazıya geçirilmesi sözlü aktarımı tamamlayan bir kayıt işlevi görmüş; Hz. Ebû Bekir dönemindeki cem ile Hz. Osman dönemindeki istinsah farklı tarihsel şartlarda gerçekleştirilen iki ayrı uygulama olarak rivâyet edilmiştir. Kaynaklarda istinsah heyeti, mushafların sayısı ve gönderildikleri merkezler konusunda farklı aktarımlar bulunduğundan, bu sürecin ayrıntıları ihtiyatla değerlendirilmelidir."


def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def instrs(z):
    vals=[]
    for name in z.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try:r=etree.fromstring(z.read(name))
            except Exception:continue
            vals += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return vals

def verify(path):
    with ZipFile(path) as z:
        if z.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        for name in z.namelist():
            if name.endswith('.xml') or name.endswith('.rels'): etree.fromstring(z.read(name))
        d=etree.fromstring(z.read('word/document.xml')); f=etree.fromstring(z.read('word/footnotes.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS); texts=[text(p) for p in ps]
        if len(ps)!=674: raise RuntimeError(f'body paragraph count {len(ps)} !=674')
        if OLD in '\n'.join(texts): raise RuntimeError('F5-001 negative literal target still survives')
        if texts.count(CURRENT)!=1: raise RuntimeError(f'current Fourth-resolved P19 form count {texts.count(CURRENT)} !=1')
        idx=texts.index(CURRENT)
        if idx!=19: raise RuntimeError(f'current F5-001 resolved paragraph moved: P{idx} != P19')
        if 'farklı tarihsel şartlarda gerçekleştirilen iki ayrı uygulama olarak rivâyet edilmiştir' not in texts[idx]: raise RuntimeError('positive cem/istinsah distinction missing')
        refs=d.xpath('//w:footnoteReference/@w:id',namespaces=NS); ids=[x for x in f.xpath('./w:footnote/@w:id',namespaces=NS) if int(x)>0]
        if len(refs)!=469 or len(ids)!=469 or set(refs)!=set(ids) or len(set(refs))!=469: raise RuntimeError('footnote/reference inventory failed')
        ins=instrs(z); addin=sum('ADDIN ' in x for x in ins); item=sum('ZOTERO_ITEM' in x for x in ins); bib=sum('ZOTERO_BIBL' in x for x in ins)
        if len(ins)!=520 or (addin,item,bib)!=(466,465,1): raise RuntimeError(f'field inventory failed {len(ins)} {(addin,item,bib)}')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmark inventory failed')
        if len(d.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink inventory failed')
        return idx

def apply(src,out):
    idx=verify(src); shutil.copyfile(src,out); verify(out)
    if src.read_bytes()!=out.read_bytes(): raise RuntimeError('F5-001 no-op must remain byte-identical')
    print('F5-001\tVERIFIED_NO_CHANGE\tBYTE_IDENTICAL')
    print(f'RESOLVED_LOCATION\tP{idx}')
    print('REASON\tFourth Report already replaced the negative same-process contrast with a positive, historically cautious distinction; Fifth wording would weaken the accepted `rivâyet edilmiştir` framing.')

if __name__=='__main__': apply(Path(sys.argv[1]),Path(sys.argv[2]))
