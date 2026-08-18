#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
OLD="İki işlemde de sahabe Kur’an’ın metnini korumak üzere harekete geçmiş; ilki muhafaza, ikincisi ise ihtilafları önleme amacı taşımıştır."
CURRENT="Problemin tarihsel zemini, İslâm öncesi Arap yazısından nüzûl dönemindeki kayıt faaliyetlerine, oradan cem ve istinsah süreçlerine uzanmaktadır. Vahyin yazıya geçirilmesi sözlü aktarımı tamamlayan bir kayıt işlevi görmüş; Hz. Ebû Bekir dönemindeki cem ile Hz. Osman dönemindeki istinsah farklı tarihsel şartlarda gerçekleştirilen iki ayrı uygulama olarak rivâyet edilmiştir. Kaynaklarda istinsah heyeti, mushafların sayısı ve gönderildikleri merkezler konusunda farklı aktarımlar bulunduğundan, bu sürecin ayrıntıları ihtiyatla değerlendirilmelidir."
BAD_FRAGMENTS=("ilki muhafaza, ikincisi ise ihtilafları önleme", "muhafaza amacı taşımıştır", "ihtilafları önleme amacı taşımıştır")

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def instrs(z):
    out=[]
    for name in z.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try:r=etree.fromstring(z.read(name))
            except Exception:continue
            out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return out

def verify(path):
    with ZipFile(path) as z:
        if z.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        d=etree.fromstring(z.read('word/document.xml')); f=etree.fromstring(z.read('word/footnotes.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS); texts=[text(p) for p in ps]; body='\n'.join(texts)
        if len(ps)!=674: raise RuntimeError(f'body paragraph count {len(ps)} !=674')
        if OLD in body: raise RuntimeError('F5-002 unsupported-purpose literal target still survives')
        for frag in BAD_FRAGMENTS:
            if frag in body: raise RuntimeError(f'F5-002 unsupported-purpose fragment survives: {frag}')
        if texts.count(CURRENT)!=1: raise RuntimeError(f'accepted P19 form count {texts.count(CURRENT)} !=1')
        idx=texts.index(CURRENT)
        if idx!=19: raise RuntimeError(f'accepted F5-002 resolution moved: P{idx} !=P19')
        if 'farklı tarihsel şartlarda gerçekleştirilen iki ayrı uygulama olarak rivâyet edilmiştir' not in texts[idx]: raise RuntimeError('historically cautious distinction missing')
        if 'bu sürecin ayrıntıları ihtiyatla değerlendirilmelidir' not in texts[idx]: raise RuntimeError('explicit caution sentence missing')
        refs=d.xpath('//w:footnoteReference/@w:id',namespaces=NS); ids=[x for x in f.xpath('./w:footnote/@w:id',namespaces=NS) if int(x)>0]
        if len(refs)!=469 or len(ids)!=469 or set(refs)!=set(ids) or len(set(refs))!=469: raise RuntimeError('footnote/ref inventory failed')
        ins=instrs(z); addin=sum('ADDIN ' in x for x in ins); item=sum('ZOTERO_ITEM' in x for x in ins); bib=sum('ZOTERO_BIBL' in x for x in ins)
        if len(ins)!=520 or (addin,item,bib)!=(466,465,1): raise RuntimeError(f'field inventory failed {len(ins)} {(addin,item,bib)}')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmark inventory failed')
        if len(d.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink inventory failed')
        return idx

def apply(src,out):
    idx=verify(src); shutil.copyfile(src,out); verify(out)
    if src.read_bytes()!=out.read_bytes(): raise RuntimeError('F5-002 no-op must be byte-identical')
    print('F5-002\tVERIFIED_NO_CHANGE\tBYTE_IDENTICAL')
    print(f'RESOLVED_LOCATION\tP{idx}')
    print('REASON\tThe unsupported motive attribution is absent; Fourth-resolved text preserves source-plurality and explicit historical caution instead.')

if __name__=='__main__': apply(Path(sys.argv[1]),Path(sys.argv[2]))
