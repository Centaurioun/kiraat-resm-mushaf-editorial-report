#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS; W=h.W
OLD="Şayet Kur’an lafızlarının tamamı telaffuza tam uygun biçimde yazılmış olsaydı"
NEW="Kur’an'ın edâya ilişkin ayrıntıları tarih boyunca yalnız yazıdan çıkarılmamış; telakki, müşâfehe ve isnad yoluyla aktarılmıştır. Mushaf yazısı bu sözlü öğretim geleneğinin yerine geçmemiş, rivâyet edilen okuyuşların müşterek yazılı çerçevesini sağlamıştır."

def rewrite_preserve_fn(p,new,expected_fn):
    sp=h.spec(p)
    if sp['fn'] != [str(expected_fn)]:
        raise RuntimeError(f'FN mismatch {expected_fn}: {sp}')
    nodes=p.xpath('.//w:t',namespaces=NS)
    target=None
    for t in nodes:
        r=t.getparent()
        if r.tag != f'{{{W}}}r':
            continue
        if r.xpath('.//w:footnoteReference|.//w:rtl|.//w:instrText|.//w:fldChar',namespaces=NS):
            continue
        target=t
        break
    if target is None:
        raise RuntimeError('no safe text node for F4-080')
    for t in nodes:
        t.text=''
    target.text=new
    target.set('{http://www.w3.org/XML/1998/namespace}space','preserve')

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        text='\n'.join(h.txt(p) for p in ps)
        matches=[p for p in ps if h.norm(NEW) in h.norm(h.txt(p))]
    return h.norm(NEW) in h.norm(text) and h.norm(OLD) not in h.norm(text) and len(matches)==1 and h.spec(matches[0])['fn']==['340']

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src)
        shutil.copyfile(src,out)
        return [('F4-080','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml'))
        body=d.find('.//w:body',namespaces=NS)
        ps=body.xpath('./w:p',namespaces=NS)
        _,p=h.find(ps,OLD)
        rewrite_preserve_fn(p,NEW,340)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():
                zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out):
        raise RuntimeError('F4-080 postconditions incomplete')
    return [('F4-080','current','APPLIED_COUNTERFACTUAL_REPLACEMENT_FN340_PRESERVED')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
