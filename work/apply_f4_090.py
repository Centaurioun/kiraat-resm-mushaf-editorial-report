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
IBN = "İbn Mesʿûd'un istinsah sürecine yaklaşımı hakkında farklı rivâyetler bulunmaktadır."
XMLSPACE = '{http://www.w3.org/XML/1998/namespace}space'


def protected_empty(p):
    s = h.spec(p)
    return not s['fn'] and not s['rtl'] and not s['book'] and not s['fld'] and not s['hyper']


def kurtubi_space_preserved(p):
    hits = [t for t in p.xpath('.//w:t', namespaces=NS) if 'Kurtubî’nin' in (t.text or '')]
    return len(hits) == 1 and (hits[0].text or '').startswith(' ') and hits[0].get(XMLSPACE) == 'preserve'


def repair_inherited_spacing(ps):
    _, p = h.find(ps, IBN)
    hits = [t for t in p.xpath('.//w:t', namespaces=NS) if 'Kurtubî’nin' in (t.text or '')]
    if len(hits) != 1:
        raise RuntimeError(f'F4-090 inherited Kurtubi run count={len(hits)}')
    t = hits[0]
    text = t.text or ''
    if not text.startswith(' '):
        raise RuntimeError('F4-090 inherited Kurtubi run lacks expected leading whitespace')
    t.set(XMLSPACE, 'preserve')
    return p


def complete(path: Path):
    with ZipFile(path) as z:
        d = etree.fromstring(z.read('word/document.xml'))
        ps = d.xpath('.//w:body/w:p', namespaces=NS)
        early = [p for p in ps if h.norm(h.txt(p)).startswith(h.norm(EARLY))]
        oldfinal = [p for p in ps if h.norm(h.txt(p)).startswith(h.norm(FINAL))]
        new = [(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)) == h.norm(NEW)]
        heads = [(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)) == h.norm(HEADING)]
        ibn = [p for p in ps if h.norm(h.txt(p)).startswith(h.norm(IBN))]
        return (not early and not oldfinal and len(new)==1 and len(heads)==1 and len(ibn)==1 and
                new[0][0] + 1 == heads[0][0] and protected_empty(new[0][1]) and
                h.spec(heads[0][1])['book']==2 and kurtubi_space_preserved(ibn[0]))


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

        # F4-090 structural consolidation: preserve the final paragraph shell/style,
        # replace its prose, and remove only the earlier citation-free repeated conclusion.
        h.whole(pf, NEW, ())
        body.remove(pe)

        # Visual-QA remediation discovered after F4-089 durable close: the source XML
        # contains a leading space before Kurtubi, but its w:t lacks xml:space=preserve,
        # causing Word/LibreOffice to render `değerlendirilmelidir.Kurtubî`. Repair only
        # that existing whitespace property; do not alter prose, FN388, or paragraph order.
        ps2 = body.xpath('./w:p', namespaces=NS)
        repair_inherited_spacing(ps2)

        xml = etree.tostring(d, xml_declaration=True, encoding='UTF-8', standalone='yes')
        with ZipFile(out, 'w') as zout:
            for info in zin.infolist():
                zout.writestr(info, xml if info.filename == 'word/document.xml' else zin.read(info.filename))

    f78.validate_structural(src, out)
    if not complete(out):
        raise RuntimeError('F4-090 postconditions incomplete')
    return [('F4-090', f'P{ie}+P{jf}', 'APPLIED_REPEAT_CONSOLIDATION_PLUS_INHERITED_SPACING_REPAIR')]


if __name__ == '__main__':
    for row in apply(Path(sys.argv[1]), Path(sys.argv[2])):
        print('\t'.join(map(str, row)))
