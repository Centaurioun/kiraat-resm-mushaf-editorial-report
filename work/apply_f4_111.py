#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys,re
import apply_f4_053_057 as h
import apply_f4_078 as f78
W=h.W; NS=h.NS

BIB='Kaynakça'
TARGET_Q='Kur’an'
Q_VARIANTS=('Kur’ân',"Kur'an")
# Curated specific-name occurrences in ordinary prose. The Mervan quotation at P64 is intentionally excluded.
IMAM_CONTEXTS=(
    ('İmam mushaf','İmam Mushaf'),
    ('imam mushaf esas alınarak','İmam Mushaf esas alınarak'),
    ('imam mushaftan istinsah edilen','İmam Mushaftan istinsah edilen'),
    ('mushafı imam mushafının hattı','mushafı İmam Mushafının hattı'),
    ('imam mushaf dâhil altı mushaf','İmam Mushaf dâhil altı mushaf'),
)

QUOTE_CHARS='“”\"'

def run_text(r): return ''.join(r.xpath('.//w:t/text()',namespaces=NS))

def is_italic(r):
    rpr=r.find(f'{{{W}}}rPr')
    if rpr is None:return False
    for tag in ('i','iCs'):
        el=rpr.find(f'{{{W}}}{tag}')
        if el is not None and el.get(f'{{{W}}}val','1') not in ('0','false','off'):
            return True
    return False

def in_quote(text,start):
    # Conservative check for ordinary paired curly/double quotes before the token in the same paragraph.
    prefix=text[:start]
    return (prefix.count('“')>prefix.count('”')) or (prefix.count('"')%2==1)

def replace_plain_text_nodes(p, old, new):
    """Replace occurrences wholly inside single w:t nodes, skipping italic runs and quote-contained occurrences."""
    changed=0
    full=h.txt(p)
    for r in p.xpath('.//w:r',namespaces=NS):
        if is_italic(r): continue
        for t in r.xpath('./w:t',namespaces=NS):
            s=t.text or ''
            if old not in s: continue
            # Evaluate each occurrence against paragraph quote state by locating this text node in full paragraph.
            # If ambiguous/multiple identical node texts, conservatively skip quoted-looking nodes.
            if any(q in s for q in ('“','”','"')): continue
            cursor=0; out=''; local=False
            while True:
                j=s.find(old,cursor)
                if j<0: out+=s[cursor:]; break
                approx=full.find(s)
                abspos=(approx+j) if approx>=0 else -1
                if abspos>=0 and not in_quote(full,abspos):
                    out+=s[cursor:j]+new; changed+=1; local=True
                else:
                    out+=s[cursor:j+len(old)]
                cursor=j+len(old)
            if local:t.text=out
    return changed

def normalize_imam(p):
    text=h.txt(p); changed=0
    # Preserve direct-quotation occurrence in Mervan's words and generic plural/conceptual lower-case usages.
    for old,new in IMAM_CONTEXTS:
        if old not in text: continue
        # span preserves footnote/field/bookmark structure; selected contexts are narrative only.
        h.span(p,old,new); changed+=1; text=h.txt(p)
    return changed

def state(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        return d,body,ps

def main_boundary(ps):
    hits=[i for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(BIB) and h.spec(p)['book']>0]
    if len(hits)!=1: raise RuntimeError(f'F4-111 bibliography boundary count={len(hits)}')
    return hits[0]

def audit(path:Path):
    d,body,ps=state(path); bi=main_boundary(ps)
    bad=[]; imam_bad=[]
    for i,p in enumerate(ps[:bi]):
        text=h.txt(p)
        # Remaining nonpreferred quran variants are allowed only when entirely in italic runs or inside quotations.
        for old in Q_VARIANTS:
            if old not in text: continue
            allowed_count=0
            for r in p.xpath('.//w:r',namespaces=NS):
                if is_italic(r): allowed_count+=run_text(r).count(old)
            total=text.count(old)
            # Also permit occurrences textually inside paired quotations.
            for m in re.finditer(re.escape(old),text):
                if in_quote(text,m.start()): allowed_count+=1
            if allowed_count < total: bad.append((i,old,text))
        if 'İmam mushaf' in text: imam_bad.append((i,'İmam mushaf',text))
        # Specific narrative lower-case contexts must be gone; generic quote/plural lower-case may remain.
        for old,new in IMAM_CONTEXTS[1:]:
            if old in text: imam_bad.append((i,old,text))
    return bi,bad,imam_bad

def complete(path:Path):
    bi,bad,imam_bad=audit(path)
    return not bad and not imam_bad

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-111','main_text','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS); bi=main_boundary(ps)
        qchanges=0; ichanges=0
        for i,p in enumerate(ps[:bi]):
            # Never mutate field-bearing paragraph text for this house-style sweep.
            if h.spec(p)['fld'] or h.spec(p)['instr']: continue
            before=h.spec(p)
            for old in Q_VARIANTS:
                qchanges += replace_plain_text_nodes(p,old,TARGET_Q)
            ichanges += normalize_imam(p)
            after=h.spec(p)
            # Text-only spelling normalization may not alter structural inventory.
            for k in ('fn','instr','fld','hyper','rtl','book'):
                if before[k]!=after[k]: raise RuntimeError(f'F4-111 protected structure changed P{i} key={k}: {before[k]}->{after[k]}')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    bi,bad,imam_bad=audit(out)
    if bad or imam_bad:
        raise RuntimeError(f'F4-111 remaining unsafe variants bad={bad[:8]} imam={imam_bad[:8]}')
    return [('F4-111',f'P0-P{bi-1}',f'APPLIED_MAIN_TEXT_HOUSE_STYLE_QURAN={qchanges}_IMAM={ichanges}_BIB_QUOTES_ITALICS_PRESERVED')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
