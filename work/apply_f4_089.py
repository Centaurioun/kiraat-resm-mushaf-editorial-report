#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS = h.NS
ANCHOR = "İbn Mesʿûd'un istinsah sürecine yaklaşımı hakkında farklı rivâyetler bulunmaktadır."
OLD = "Nitekim onun, mushafının yakılmasına tepki gösterdiği ve insanlara mushaflarını gizlemelerini söylediği nakledilmekle birlikte, bu tavır erken dönem kaynaklarında sürekli ve esaslı bir muhalefet olmayıp, öfkeye bağlı geçici bir tepki olarak yorumlanmıştır."
NEW = "İbn Mes‘ûd'a nispet edilen rivâyetler, onun istinsah süreci ve kendi mushafıyla ilişkili bazı itirazlarının bulunduğunu göstermektedir. Bu tavrın hangi psikolojik saikle ortaya çıktığını kesin biçimde belirlemek yerine, nakledilen söz ve uygulamalar kendi tarihsel bağlamları içinde değerlendirilmelidir."


def complete(path: Path):
    with ZipFile(path) as z:
        d = etree.fromstring(z.read('word/document.xml'))
        ps = d.xpath('.//w:body/w:p', namespaces=NS)
        hits = [p for p in ps if h.norm(h.txt(p)).startswith(h.norm(ANCHOR))]
        return len(hits) == 1 and h.norm(NEW) in h.norm(h.txt(hits[0])) and h.norm(OLD) not in h.norm(h.txt(hits[0])) and h.spec(hits[0])['fn'] == ['388']


def apply(src: Path, out: Path):
    if complete(src):
        f78.validate_structural(src, src)
        shutil.copyfile(src, out)
        return [('F4-089', 'current', 'ALREADY_SATISFIED')]

    with ZipFile(src, 'r') as zin:
        d = etree.fromstring(zin.read('word/document.xml'))
        body = d.find('.//w:body', namespaces=NS)
        ps = body.xpath('./w:p', namespaces=NS)
        i, p = h.find(ps, ANCHOR)
        before = h.spec(p)
        if before['fn'] != ['388'] or before['book'] or before['fld'] or before['hyper']:
            raise RuntimeError('unexpected protected F4-089 target ' + str(before))
        h.span(p, OLD, NEW)
        after = h.spec(p)
        if after['fn'] != before['fn'] or after['rtl'] != before['rtl'] or after['book'] != before['book'] or after['fld'] != before['fld']:
            raise RuntimeError('F4-089 protected structure changed')
        xml = etree.tostring(d, xml_declaration=True, encoding='UTF-8', standalone='yes')
        with ZipFile(out, 'w') as zout:
            for info in zin.infolist():
                zout.writestr(info, xml if info.filename == 'word/document.xml' else zin.read(info.filename))

    f78.validate_structural(src, out)
    if not complete(out):
        raise RuntimeError('F4-089 postconditions incomplete')
    return [('F4-089', f'P{i}', 'APPLIED_PSYCHOLOGICAL_MOTIVE_REDUCTION')]


if __name__ == '__main__':
    for row in apply(Path(sys.argv[1]), Path(sys.argv[2])):
        print('\t'.join(map(str, row)))
