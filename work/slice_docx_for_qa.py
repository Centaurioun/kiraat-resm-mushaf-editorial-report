from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import sys
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
src=Path(sys.argv[1]); out=Path(sys.argv[2]); start=int(sys.argv[3]); end=int(sys.argv[4])
with ZipFile(src) as zin:
    root=etree.fromstring(zin.read('word/document.xml'))
    body=root.find(f'{{{W}}}body')
    paras=[x for x in list(body) if x.tag==f'{{{W}}}p']
    final_sect=body.find(f'{{{W}}}sectPr')
    selected=set(id(p) for p in paras[start:end])
    for ch in list(body):
        if ch.tag==f'{{{W}}}p' and id(ch) not in selected:
            body.remove(ch)
        elif ch.tag==f'{{{W}}}tbl':
            body.remove(ch)
        elif ch.tag!=f'{{{W}}}p' and ch is not final_sect:
            body.remove(ch)
    xml=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone='yes')
    with ZipFile(out,'w') as zout:
        for info in zin.infolist():
            zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
print(out)
