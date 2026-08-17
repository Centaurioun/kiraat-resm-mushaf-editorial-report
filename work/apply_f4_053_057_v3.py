#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as base

NS=base.NS
XMLSPACE='{http://www.w3.org/XML/1998/namespace}space'

def apply(src:Path,out:Path):
    tmp=out.with_suffix('.base.docx')
    rows=base.apply(src,tmp)
    changed=False
    with ZipFile(tmp,'r') as zin:
        doc=etree.fromstring(zin.read('word/document.xml'))
        ps=doc.xpath('.//w:body/w:p',namespaces=NS)
        targets=[p for p in ps if 'ayrılmalıdır. İlk dönmelerde' in base.txt(p)]
        if len(targets)!=1:
            raise RuntimeError(f'expected one F4-052 spacing-boundary paragraph, got {len(targets)}')
        p=targets[0]
        nodes=p.xpath('.//w:t',namespaces=NS)
        prefix=''
        repaired=False
        same_node_safe=False
        for n in nodes:
            value=n.text or ''
            if 'ayrılmalıdır. İlk dönmelerde' in value:
                same_node_safe=True
            if prefix.endswith('ayrılmalıdır.') and value.startswith(' İlk dönmelerde'):
                if n.get(XMLSPACE)!='preserve':
                    n.set(XMLSPACE,'preserve'); changed=True
                repaired=True
            prefix += value
        if not repaired and not same_node_safe:
            raise RuntimeError('could not resolve OOXML run-boundary spacing target')
        if changed:
            xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
            with ZipFile(out,'w') as zout:
                for info in zin.infolist():
                    zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
        else:
            shutil.copyfile(tmp,out)
    tmp.unlink(missing_ok=True)
    base.validate(src,out)
    return rows+[('OOXML-SPACE-PRESERVE-REPAIR','P207','APPLIED' if changed else 'ALREADY_SATISFIED')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
