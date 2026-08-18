#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
OLD='Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, ortak mushaf otoritesinin bulunmadığını değil, aynı istinsah geleneği içinde bazı yazım farklılıklarının rivâyet edildiğini göstermektedir.'
CURRENT='Şehir mushafları arasında nakledilen sınırlı yazım farklılıkları, müşterek mushaf otoritesi içinde farklı yazım rivâyetlerinin bulunabildiğini göstermektedir.'

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
        if OLD in body: raise RuntimeError('old F5-005 negative target survives')
        if texts[24].count(CURRENT)!=1: raise RuntimeError(f'current cautious F5-005 form count at P24 {texts[24].count(CURRENT)} !=1')
        refs=d.xpath('//w:footnoteReference/@w:id',namespaces=NS); ids=[x for x in f.xpath('./w:footnote/@w:id',namespaces=NS) if int(x)>0]
        if len(refs)!=469 or len(ids)!=469 or set(refs)!=set(ids) or len(set(refs))!=469: raise RuntimeError('footnote/ref inventory failed')
        ins=instrs(z); addin=sum('ADDIN ' in x for x in ins); item=sum('ZOTERO_ITEM' in x for x in ins); bib=sum('ZOTERO_BIBL' in x for x in ins)
        if len(ins)!=520 or (addin,item,bib)!=(466,465,1): raise RuntimeError('field inventory failed')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmark inventory failed')
        if len(d.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink inventory failed')

def apply(src,out):
    verify(src)
    shutil.copyfile(src,out)
    verify(out)
    if src.read_bytes()!=out.read_bytes(): raise RuntimeError('F5-005 no-op output is not byte-identical')
    print('F5-005\tVERIFIED_NO_CHANGE\tBYTE_IDENTICAL')
    print('RESOLVED_LOCATION\tP24')
    print('REASON\tNegative target is already absent; current positive `bulunabildiğini` formulation preserves Fourth caution and should not be strengthened to categorical `bulunduğunu`.')

if __name__=='__main__': apply(Path(sys.argv[1]),Path(sys.argv[2]))
