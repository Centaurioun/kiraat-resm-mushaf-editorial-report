#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_073_077_v2 as batch

NS=batch.batch.NS
helper=batch.batch.h
XMLSPACE='{http://www.w3.org/XML/1998/namespace}space'

def preserve_boundary_spaces(p):
    changed=False
    for t in p.xpath('.//w:t',namespaces=NS):
        v=t.text or ''
        if (v.startswith(' ') or v.endswith(' ')) and t.get(XMLSPACE)!='preserve':
            t.set(XMLSPACE,'preserve'); changed=True
    return changed

def apply(src:Path,out:Path):
    tmp=out.with_suffix('.base.docx')
    rows=batch.batch.apply(src,tmp)
    changed=False
    with ZipFile(tmp,'r') as zin:
        doc=etree.fromstring(zin.read('word/document.xml')); ps=doc.xpath('.//w:body/w:p',namespaces=NS)
        anchors=[
          'Mushaflarda bazı kelime ve edatların bitişik veya ayrı yazılması, resm-i mushafın dikkat çeken özelliklerinden biridir.',
          'Ayrı bir yorum çizgisinde bazı âlimler, mushaf kitâbetindeki kıyasa aykırı görünen yerlerde özel hikmetler ve anlam incelikleri aramıştır.'
        ]
        for a in anchors:
            hits=[p for p in ps if helper.norm(helper.txt(p)).startswith(helper.norm(a)) or helper.norm(a) in helper.norm(helper.txt(p))]
            if len(hits)!=1: raise RuntimeError(f'expected one whitespace target {a[:60]!r}, got {len(hits)}')
            changed |= preserve_boundary_spaces(hits[0])
        if changed:
            xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
            with ZipFile(out,'w') as zout:
                for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
        else: shutil.copyfile(tmp,out)
    tmp.unlink(missing_ok=True)
    batch.batch.validate_structural(src,out)
    return rows+[('OOXML-SPACE-PRESERVE','F4-073/F4-074','APPLIED' if changed else 'ALREADY_SATISFIED')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
