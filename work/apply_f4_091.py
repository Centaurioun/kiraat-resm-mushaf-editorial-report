#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS = h.NS
OLD = "Bu anlayışın fiilî sonuçlar doğurduğunu gösteren en dikkat çekici örneklerden biri, İbn Şenbûz (ö. 328/939) hadisesidir."
NEW = "İbn Şenbûz'a nispet edilen uygulamalar, kırâatlerin kamusal icrası ve kabul ölçütleri bağlamında tartışılmıştır. Bu örneği yalnız resm-i Osmânî'ye aykırılık üzerinden açıklamak yeterli değildir; naklin durumu, müşterek mushaf geleneği ve dönemin kırâat anlayışı birlikte dikkate alınmalıdır. Resme uygunluk bu değerlendirmede önemli bir unsur olmakla birlikte tek başına sahihlik veya şâzlık hükmü veren bağımsız ölçü değildir."
NEXT = "Bu çerçevede mushaf hattına aykırı olan kırâat vecihlerinin tedricen şâz kategorisine sevk edildiği görülmektedir."


def complete(path: Path):
    with ZipFile(path) as z:
        d = etree.fromstring(z.read('word/document.xml'))
        ps = d.xpath('.//w:body/w:p', namespaces=NS)
        hits = [(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)) == h.norm(NEW)]
        if len(hits) != 1:
            return False
        i,p = hits[0]
        s = h.spec(p)
        if s['fn'] != ['391'] or s['rtl'] or s['fld'] or s['book'] or s['hyper']:
            return False
        if i+1 >= len(ps) or not h.norm(h.txt(ps[i+1])).startswith(h.norm(NEXT)):
            return False
        return True


def apply(src: Path, out: Path):
    if complete(src):
        f78.validate_structural(src, src)
        shutil.copyfile(src, out)
        return [('F4-091','current','ALREADY_SATISFIED')]

    with ZipFile(src, 'r') as zin:
        d = etree.fromstring(zin.read('word/document.xml'))
        body = d.find('.//w:body', namespaces=NS)
        ps = body.xpath('./w:p', namespaces=NS)
        i,p = h.find(ps, OLD)
        s = h.spec(p)
        if s['fn'] != ['391'] or s['rtl'] or s['fld'] or s['book'] or s['hyper']:
            raise RuntimeError('unexpected protected F4-091 target ' + str(s))
        if i+1 >= len(ps) or not h.norm(h.txt(ps[i+1])).startswith(h.norm(NEXT)) or h.spec(ps[i+1])['fn'] != ['392','393']:
            raise RuntimeError('F4-091 next-paragraph/F4-092 boundary mismatch')

        # Replace only the F4-091 paragraph. Preserve its sole historical-source note
        # (FN391) as the citation for the bounded Ibn Shanbudh case summary.
        h.whole(p, NEW, (391,))

        xml = etree.tostring(d, xml_declaration=True, encoding='UTF-8', standalone='yes')
        with ZipFile(out, 'w') as zout:
            for info in zin.infolist():
                zout.writestr(info, xml if info.filename == 'word/document.xml' else zin.read(info.filename))

    f78.validate_structural(src, out)
    if not complete(out):
        raise RuntimeError('F4-091 postconditions incomplete')
    return [('F4-091', f'P{i}', 'APPLIED_MULTI_CRITERIA_REFRAME')]


if __name__ == '__main__':
    for row in apply(Path(sys.argv[1]), Path(sys.argv[2])):
        print('\t'.join(map(str, row)))
