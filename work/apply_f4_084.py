#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
OLD="Zira kırâat, sonraki neslin önceki nesilden aldığı ve uygulayarak sürdürdüğü ittiba edilen bir sünnet olarak anlaşılmıştır. Bu bağlamda Zeyd b. Sâbit’ten ve başkalarından nakledildiğine göre “Kırâat sünnettir.” sözü ile Ebû Amr b. el-A’lâ’nın (ö. 154/771) kırâat hususundaki yöntemini anlatırken, “Allah’a yemin ederim ki, okuduğum hiçbir harfi, sahih bir rivâyete dayanmaksızın okumadım.” ifadesi, bu anlayışı açıkça ortaya koymaktadır."
NEW="Bu bağlamda “Kırâat sünnettir.” sözü ile Ebû Amr b. el-A‘lâ'dan nakledilen ifade, kırâat aktarımında rivâyet ve telakkinin merkezî konumuna işaret etmektedir."
ANCHOR="Kırâat vecihlerinin naklinde aslî dayanak, yazılı metinden önce telakki ve müşâfehedir."

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[p for p in ps if h.norm(h.txt(p)).startswith(h.norm(ANCHOR))]
        return len(hits)==1 and h.spec(hits[0])['fn']==['361','362','363','364'] and h.norm(NEW) in h.norm(h.txt(hits[0])) and h.norm(OLD) not in h.norm(h.txt(hits[0]))

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out)
        return [('F4-084','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        _,p=h.find(ps,ANCHOR)
        if h.spec(p)['fn']!=['361','362','363','364']:
            raise RuntimeError('unexpected F4-084 footnotes '+str(h.spec(p)))
        h.span(p,OLD,NEW)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-084 postconditions incomplete')
    return [('F4-084','current','APPLIED_EVIDENCE_LANGUAGE_REDUCTION')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,row)))
