#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_058_062 as base

W=base.W; NS=base.NS
helper=base.base

def remove_inherited_italics(p):
    changed=False
    for r in p.xpath('./w:r',namespaces=NS):
        if r.xpath('.//w:footnoteReference',namespaces=NS):
            continue
        rpr=r.find(f'{{{W}}}rPr')
        if rpr is None:
            continue
        for tag in (f'{{{W}}}i',f'{{{W}}}iCs'):
            for node in list(rpr.findall(tag)):
                rpr.remove(node); changed=True
    return changed

def apply(src:Path,out:Path):
    tmp=out.with_suffix('.base.docx')
    rows=base.apply(src,tmp)
    changed=False
    with ZipFile(tmp,'r') as zin:
        doc=etree.fromstring(zin.read('word/document.xml'))
        ps=doc.xpath('.//w:body/w:p',namespaces=NS)
        anchors=[
            'Bununla birlikte kırâat imamlarının otoritesi ve öğretim geleneklerinin yerleşmesi yalnız mushaf yazısıyla açıklanamaz;',
            "Resm-i Osmânî’nin kırâat rivâyetiyle ilişkisi genel ilkeler düzeyinde bu şekilde belirlendikten sonra,"
        ]
        for anchor in anchors:
            hits=[p for p in ps if helper.norm(helper.txt(p)).startswith(helper.norm(anchor))]
            if len(hits)!=1:
                raise RuntimeError(f'expected one style-repair target for {anchor[:70]!r}, got {len(hits)}')
            if remove_inherited_italics(hits[0]):
                changed=True
        if changed:
            xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
            with ZipFile(out,'w') as zout:
                for info in zin.infolist():
                    zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
        else:
            shutil.copyfile(tmp,out)
    tmp.unlink(missing_ok=True)
    helper.validate(src,out)
    with ZipFile(out) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        for anchor in anchors:
            hits=[p for p in ps if helper.norm(helper.txt(p)).startswith(helper.norm(anchor))]
            assert len(hits)==1
            assert not hits[0].xpath('./w:r/w:rPr/w:i|./w:r/w:rPr/w:iCs',namespaces=NS)
    return rows+[('STYLE-REPAIR','F4-060/F4-062','APPLIED' if changed else 'ALREADY_SATISFIED')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
