#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as base

W=base.W; NS=base.NS

def apply(src:Path,out:Path):
    tmp=out.with_suffix('.base.docx')
    rows=base.apply(src,tmp)
    changed=False
    with ZipFile(tmp,'r') as zin:
        doc=etree.fromstring(zin.read('word/document.xml'))
        ps=doc.xpath('.//w:body/w:p',namespaces=NS)
        hits=[p for p in ps if 'ayrılmalıdır.İlk' in base.txt(p)]
        if len(hits)>1:
            raise RuntimeError(f'ambiguous prior-checkpoint spacing defect: {len(hits)} hits')
        if len(hits)==1:
            st=base.span(hits[0],'ayrılmalıdır.İlk','ayrılmalıdır. İlk')
            changed = st=='APPLIED'
        else:
            # Already fixed is acceptable; any other disappearance is not.
            ok=[p for p in ps if 'ayrılmalıdır. İlk' in base.txt(p)]
            if len(ok)!=1:
                raise RuntimeError('expected prior-checkpoint spacing boundary not found')
        if changed:
            xml=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone='yes')
            with ZipFile(out,'w') as zout:
                for info in zin.infolist():
                    zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
        else:
            shutil.copyfile(tmp,out)
    tmp.unlink(missing_ok=True)
    base.validate(src,out)
    return rows+[('TECHNICAL-SPACING-REPAIR','P207','APPLIED' if changed else 'ALREADY_SATISFIED')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
