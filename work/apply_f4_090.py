#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS = h.NS
EARLY = "Buradan hareketle denilebilir ki resm-i Osmânî’nin sahâbe mushaflarındaki kırâat rivâyetleri karşısındaki tutumu iki yönlüdür."
FINAL = "Sonuç olarak bu veriler birlikte değerlendirildiğinde, sahâbe mushaflarının yakılması meselesinin, Kur’an tarihindeki en önemli birleştirici adımlardan biri olduğu görülmektedir."
NEW = "Sahâbeye nispet edilen mushaf rivâyetleri, erken Kur’an aktarımında bulunan okuyuş, tertip ve yazım çeşitliliğini incelemek bakımından önemlidir. Bununla birlikte sonraki müşterek mushaf geleneğinin normatif zemini Osmânî mushaflar etrafında şekillenmiştir. Bu sebeple şahsî mushaf rivâyetleri tarihsel tanıklık ile normatif metin otoritesi birbirine karıştırılmadan kullanılmalıdır."
HEADING = "Resm-i Osmânî’nin Kırâat Rivâyetlerinin Kabul ve Tercihindeki Belirleyici İşlevi"


def protected_empty(p):
    s = h.spec(p)
    return not s['fn'] and not s['rtl'] and not s['book'] and not s['fld'] and not s['hyper']


def complete(path: Path):
    with ZipFile(path) as z:
        d = etree.fromstring(z.read('word/document.xml'))
        ps = d.xpath('.//w:body/w:p', namespaces=NS)
        early = [p for p in ps if h.norm(h.txt(p)).startswith(h.norm(EARLY))]
        oldfinal = [p for p in ps if h.norm(h.txt(p)).startswith(h.norm(FINAL))]
        new = [(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)) == h.norm(NEW)]
        heads = [(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)) == h.norm(HEADING)]
        return (not early and not oldfinal and len(new)==1 and len(heads)==1 and
                new[0][0] + 1 == heads[0][0] and protected_empty(new[0][1]) and h.spec(heads[0][1])['book']==2)


def apply(src: Path, out: Path):
    if complete(src):
        f78.validate_structural(src, src)
        shutil.copyfile(src, out)
        return [('F4-090','current','ALREADY_SATISFIED')]

    with ZipFile(src, 'r') as zin:
        d = etree.fromstring(zin.read('word/document.xml'))
        body = d.find('.//w:body', namespaces=NS)
        ps = body.xpath('./w:p', namespaces=NS)
        ie, pe = h.find(ps, EARLY)
        jf, pf = h.find(ps, FINAL)
        if ie >= jf:
            raise RuntimeError(f'F4-090 order mismatch early={ie} final={jf}')
        if not protected_empty(pe) or not protected_empty(pf):
            raise RuntimeError('F4-090 repeat block contains protected structures')
        if jf + 1 >= len(ps) or h.norm(h.txt(ps[jf+1])) != h.norm(HEADING) or h.spec(ps[jf+1])['book'] != 2:
            raise RuntimeError('F4-090 4.3 heading boundary mismatch')

        # Preserve the final paragraph shell/style, replace its prose, then remove only
        # the earlier citation-free repeated conclusion block.
        h.whole(pf, NEW, ())
        body.remove(pe)

        xml = etree.tostring(d, xml_declaration=True, encoding='UTF-8', standalone='yes')
        with ZipFile(out, 'w') as zout:
            for info in zin.infolist():
                zout.writestr(info, xml if info.filename == 'word/document.xml' else zin.read(info.filename))

    f78.validate_structural(src, out)
    if not complete(out):
        raise RuntimeError('F4-090 postconditions incomplete')
    return [('F4-090', f'P{ie}+P{jf}', 'APPLIED_REPEAT_CONSOLIDATION')]


if __name__ == '__main__':
    for row in apply(Path(sys.argv[1]), Path(sys.argv[2])):
        print('\t'.join(map(str, row)))
