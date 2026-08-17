#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys,tempfile
import apply_f4_053_057 as h
import apply_f4_078 as f78
import apply_f4_079 as base

NS=h.NS; W=h.W
TARGETS=list(base.R.values())+[base.BRIDGE,base.CLOSE]

def normalize_body_paragraph(p):
    ppr=p.find(f'{{{W}}}pPr')
    if ppr is None:
        ppr=etree.Element(f'{{{W}}}pPr'); p.insert(0,ppr)
    ps=ppr.find(f'{{{W}}}pStyle')
    if ps is None:
        ps=etree.Element(f'{{{W}}}pStyle'); ppr.insert(0,ps)
    ps.set(f'{{{W}}}val','Normal')
    # Remove only inherited list/alignment/layout properties from former example paragraphs.
    # Do not copy paragraph properties from another paragraph: that can alter canonical RTL inventory.
    for tag in ('numPr','jc','ind','bidi','outlineLvl','keepNext'):
        x=ppr.find(f'{{{W}}}{tag}')
        if x is not None:ppr.remove(x)
    # New Turkish caveat prose must not inherit direct Arabic/list typography.
    for r in p.xpath('./w:r',namespaces=NS):
        if r.xpath('.//w:footnoteReference|.//w:rtl|.//w:instrText|.//w:fldChar',namespaces=NS):
            continue
        rp=r.find(f'{{{W}}}rPr')
        if rp is not None:r.remove(rp)

def apply(src:Path,out:Path):
    tmp=Path(tempfile.mkstemp(suffix='.docx')[1])
    try:
        base.apply(src,tmp)
        with ZipFile(tmp,'r') as zin:
            d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS)
            for text in TARGETS:
                ps=body.xpath('./w:p',namespaces=NS); _,p=h.find(ps,text); normalize_body_paragraph(p)
            xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
            with ZipFile(out,'w') as zout:
                for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
        f78.validate_structural(src,out)
        if not base.complete(out):raise RuntimeError('F4-079 content postconditions incomplete after layout repair')
        # Explicitly reject residual list numbering/centering/right alignment on caveat paragraphs.
        with ZipFile(out) as z:
            d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
            for text in TARGETS:
                _,p=h.find(ps,text)
                if p.xpath('./w:pPr/w:numPr|./w:pPr/w:jc[@w:val="center"]|./w:pPr/w:jc[@w:val="right"]',namespaces=NS):
                    raise RuntimeError('stale list/alignment formatting: '+text[:60])
        return [('F4-079','current','STRUCTURALLY_APPLIED_LAYOUT_REPAIR')]
    finally:
        try:tmp.unlink()
        except FileNotFoundError:pass

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,row)))
