#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys,tempfile
import apply_f4_053_057 as h
import apply_f4_078 as base

NS=h.NS; W=h.W
TRANSITIONS=list(base.DEMOTE.values())

def clean_direct_format(p):
    changed=False
    for r in p.xpath('./w:r',namespaces=NS):
        # Footnote/RTL/field-bearing runs are not expected in these transition paragraphs.
        if r.xpath('.//w:footnoteReference|.//w:rtl|.//w:instrText|.//w:fldChar',namespaces=NS):
            raise RuntimeError('protected run in F4-078 transition')
        rp=r.find(f'{{{W}}}rPr')
        if rp is not None:
            r.remove(rp); changed=True
    return changed

def apply(src:Path,out:Path):
    tmp=Path(tempfile.mkstemp(suffix='.docx')[1])
    try:
        base.apply(src,tmp)
        with ZipFile(tmp,'r') as zin:
            d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS)
            ps=body.xpath('./w:p',namespaces=NS); changed=False
            for text in TRANSITIONS:
                _,p=h.find(ps,text)
                # It must already be a normal paragraph, and bookmarks remain in place.
                styles=p.xpath('./w:pPr/w:pStyle/@w:val',namespaces=NS)
                if styles and styles[0] != 'Normal': raise RuntimeError('transition pStyle not Normal: '+str(styles))
                changed |= clean_direct_format(p)
            if not changed:
                shutil.copyfile(tmp,out)
            else:
                xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
                with ZipFile(out,'w') as zout:
                    for info in zin.infolist():
                        zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
        base.validate_structural(src,out)
        # Direct-format repair postcondition.
        with ZipFile(out) as z:
            d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
            for text in TRANSITIONS:
                _,p=h.find(ps,text)
                if p.xpath('./w:r/w:rPr',namespaces=NS): raise RuntimeError('stale direct run formatting: '+text)
        return [('F4-078','current','STRUCTURALLY_APPLIED_STYLE_REPAIR' if changed else 'ALREADY_SATISFIED')]
    finally:
        try: tmp.unlink()
        except FileNotFoundError: pass

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
