#!/usr/bin/env python3
from pathlib import Path
import sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

OLD = ("Bununla birlikte Osmânî mushaflarının ilk şeklinde nokta ve hareke bulunmamaktadır. "
       "Bunun temel sebebi, mushaf resminin farklı kırâat vecihlerini ihtimal dâhilinde taşıyabilecek bir esnekliğe sahip olmasıdır.")
NEW = ("Erken mushafların yazı iskeleti zamanla nokta, hareke ve diğer yardımcı işaretlerin gelişmesiyle daha ayrıntılı bir görsel sisteme kavuşmuştur. "
       "Bu gelişme, resm-i Osmânî'nin temel harf yapısının sonraki mushaflarda korunmasıyla birlikte ilerlemiştir. "
       "Nokta ve harekenin ilk mushaflarda bugünkü biçimiyle bulunmaması dönemin yazı sistemiyle ilgilidir; bunu yalnız farklı kırâatleri açık tutmak amacıyla yapılmış bilinçli bir tercih olarak açıklamak ihtiyat gerektirir.")
TAIL = "Ancak zamanla hareke ve diğer zapt işaretleri kullanılmaya başlanınca, müstensihler mushaflarını"

def complete(doc):
    paras = doc.xpath('.//w:body/w:p', namespaces=h.NS)
    texts = [h.norm(h.txt(p)) for p in paras]
    return sum(h.norm(NEW) in t and h.norm(TAIL) in t for t in texts) == 1 and not any(h.norm(OLD) in t for t in texts)

def apply(src: Path, out: Path):
    doc, payload = h.load(src)
    if complete(doc):
        out.write_bytes(src.read_bytes())
        return 'ALREADY_SATISFIED'
    paras = doc.xpath('.//w:body/w:p', namespaces=h.NS)
    i, p = h.find(paras, OLD, starts=False)
    s = h.spec(p)
    if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
        raise RuntimeError(f'F4-100 unsafe target P{i}: {s}')
    if h.norm(TAIL) not in h.norm(h.txt(p)):
        raise RuntimeError('F4-100 expected untouched continuation missing')
    h.span(p, OLD, NEW)
    if not complete(doc):
        raise RuntimeError('F4-100 completion predicate failed')
    h.save(doc, payload, out)
    f78.validate_structural(src, out)
    return f'APPLIED_P{i}_EARLY_SCRIPT_CAUSAL_SCOPE_REFRAME'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: apply_f4_100.py INPUT.docx OUTPUT.docx')
    print(apply(Path(sys.argv[1]), Path(sys.argv[2])))
