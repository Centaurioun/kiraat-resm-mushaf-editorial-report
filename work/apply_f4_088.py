#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS = h.NS
OLD = "Bu yönüyle Osmânî resm, sahâbe mushaflarından gelen okuyuş çeşitliliğini nihai mushaf otoritesi bakımından ayıklayan, bağlayıcı olanı şahsi ve açıklayıcı olandan ayıran kurucu bir otorite işlevi görmektedir."
NEW = "Osmânî istinsah ve sonraki müşterek mushaf kabulü, sahâbeye nispet edilen farklı malzemenin normatif Kur’an metni içindeki konumunun değerlendirilmesinde belirleyici tarihsel çerçeveyi oluşturmuştur. Resm-i Osmânî ise bu süreçte rivâyetlerin müşterek mushaf yazısıyla bağdaşma durumunu gösteren yazılı ölçülerden biridir."
ANCHOR = "Buradan hareketle denilebilir ki resm-i Osmânî’nin sahâbe mushaflarındaki kırâat rivâyetleri karşısındaki tutumu iki yönlüdür."


def complete(path: Path):
    with ZipFile(path) as z:
        d = etree.fromstring(z.read('word/document.xml'))
        ps = d.xpath('.//w:body/w:p', namespaces=NS)
        hits = [p for p in ps if h.norm(h.txt(p)).startswith(h.norm(ANCHOR))]
        return len(hits) == 1 and h.norm(NEW) in h.norm(h.txt(hits[0])) and h.norm(OLD) not in h.norm(h.txt(hits[0])) and h.spec(hits[0])['fn'] == []


def apply(src: Path, out: Path):
    if complete(src):
        f78.validate_structural(src, src)
        shutil.copyfile(src, out)
        return [('F4-088', 'current', 'ALREADY_SATISFIED')]

    with ZipFile(src, 'r') as zin:
        d = etree.fromstring(zin.read('word/document.xml'))
        body = d.find('.//w:body', namespaces=NS)
        ps = body.xpath('./w:p', namespaces=NS)
        i, p = h.find(ps, ANCHOR)
        before = h.spec(p)
        if before['fn'] or before['rtl'] or before['book'] or before['fld'] or before['hyper']:
            raise RuntimeError('unexpected protected F4-088 target ' + str(before))
        h.span(p, OLD, NEW)
        after = h.spec(p)
        if after != before:
            raise RuntimeError('F4-088 structural inventory changed')
        xml = etree.tostring(d, xml_declaration=True, encoding='UTF-8', standalone='yes')
        with ZipFile(out, 'w') as zout:
            for info in zin.infolist():
                zout.writestr(info, xml if info.filename == 'word/document.xml' else zin.read(info.filename))

    f78.validate_structural(src, out)
    if not complete(out):
        raise RuntimeError('F4-088 postconditions incomplete')
    return [('F4-088', f'P{i}', 'APPLIED_HISTORICAL_ACTOR_REFRAME')]


if __name__ == '__main__':
    for row in apply(Path(sys.argv[1]), Path(sys.argv[2])):
        print('\t'.join(map(str, row)))
