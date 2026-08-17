#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS = h.NS
FRAG = 'burası daha önce düzeltilmemiş'
FOLLOW = 'Bunun en meşhur örneklerinden biri'
EXPECTED = 'ifade edilmektedir. Bunun en meşhur örneklerinden biri'
XMLSPACE = '{http://www.w3.org/XML/1998/namespace}space'


def locate(doc):
    ps = doc.xpath('.//w:body/w:p', namespaces=NS)
    hits = [(i, p) for i, p in enumerate(ps) if FRAG in h.txt(p)]
    if len(hits) != 1:
        raise RuntimeError(f'F4-087 editor-note target count={len(hits)}')
    return hits[0]


def complete(path: Path):
    with ZipFile(path) as z:
        d = etree.fromstring(z.read('word/document.xml'))
        ps = d.xpath('.//w:body/w:p', namespaces=NS)
        note_hits = [(i, p) for i, p in enumerate(ps) if FRAG in h.txt(p)]
        clean_hits = [(i, p) for i, p in enumerate(ps) if EXPECTED in h.txt(p)]
        if note_hits or len(clean_hits) != 1:
            return False
        p = clean_hits[0][1]
        s = h.spec(p)
        return s['fn'] == ['377', '378'] and s['rtl'] == 2 and s['book'] == 0 and s['fld'] == 0


def apply(src: Path, out: Path):
    if complete(src):
        f78.validate_structural(src, src)
        shutil.copyfile(src, out)
        return [('F4-087', 'current', 'ALREADY_SATISFIED')]

    with ZipFile(src, 'r') as zin:
        d = etree.fromstring(zin.read('word/document.xml'))
        i, p = locate(d)
        before = h.spec(p)
        if before['fn'] != ['377', '378'] or before['rtl'] != 2 or before['book'] or before['fld'] or before['hyper']:
            raise RuntimeError('unexpected protected F4-087 target ' + str(before))

        nodes = p.xpath('.//w:t', namespaces=NS)
        texts = [(t.text or '') for t in nodes]
        flat = ''.join(texts)
        frag_pos = flat.index(FRAG)
        start = flat.rfind('(', 0, frag_pos + 1)
        end = flat.find(')', frag_pos)
        if start < 0 or end < 0:
            raise RuntimeError('editor-note parentheses not found')
        end += 1

        pos = 0
        for t, text in zip(nodes, texts):
            a, b = pos, pos + len(text)
            pos = b
            if b <= start or a >= end:
                continue
            keep_left = text[:max(0, start - a)] if a < start else ''
            keep_right = text[max(0, end - a):] if b > end else ''
            t.text = keep_left + keep_right

        # Restore ordinary spacing on the surviving normal-text run before FOLLOW.
        flat2 = ''.join((t.text or '') for t in nodes)
        if FOLLOW not in flat2:
            raise RuntimeError('follow-on sentence missing after note removal')
        if '.Bunun en meşhur' in flat2:
            for t in nodes:
                text = t.text or ''
                k = text.find(FOLLOW)
                if k >= 0:
                    t.text = text[:k] + ' ' + text[k:]
                    t.set(XMLSPACE, 'preserve')
                    break

        after_text = h.txt(p)
        after = h.spec(p)
        if FRAG in after_text or EXPECTED not in after_text:
            raise RuntimeError('F4-087 textual postcondition failed')
        if after['fn'] != before['fn'] or after['rtl'] != before['rtl'] or after['book'] != before['book'] or after['fld'] != before['fld']:
            raise RuntimeError('F4-087 protected structure changed')

        xml = etree.tostring(d, xml_declaration=True, encoding='UTF-8', standalone='yes')
        with ZipFile(out, 'w') as zout:
            for info in zin.infolist():
                zout.writestr(info, xml if info.filename == 'word/document.xml' else zin.read(info.filename))

    f78.validate_structural(src, out)
    if not complete(out):
        raise RuntimeError('F4-087 postconditions incomplete')
    return [('F4-087', f'P{i}', 'APPLIED_EDITOR_NOTE_REMOVAL')]


if __name__ == '__main__':
    for row in apply(Path(sys.argv[1]), Path(sys.argv[2])):
        print('\t'.join(map(str, row)))
