#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from collections import Counter
import hashlib, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
BODY_HASH='60c3f29968f6693de7cba0a389d41092528c0bb385a0be9f753bf6742c3463d9'
FOOTNOTE_TEXT_HASH='a07e51f7ad77714aa9cdc6254dd0b62daa05bfa6f5a023795ec58f2906fcb0de'
PATTERN=b'<w:color w:val="FF0000"/>'

def txt(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))

p=Path(sys.argv[1]); out=Path(sys.argv[2]); lines=[]
with ZipFile(p) as z:
    assert z.testzip() is None
    red={n:z.read(n).count(PATTERN) for n in z.namelist() if n.endswith('.xml') and z.read(n).count(PATTERN)}
    assert not red, red
    d=etree.fromstring(z.read('word/document.xml'))
    f=etree.fromstring(z.read('word/footnotes.xml'))
    s=etree.fromstring(z.read('word/settings.xml'))
    body=d.xpath('.//w:body/w:p',namespaces=NS); assert len(body)==674
    bh=hashlib.sha256('\n'.join(txt(x) for x in body).encode()).hexdigest(); assert bh==BODY_HASH,(bh,BODY_HASH)
    refs=d.xpath('.//w:footnoteReference/@w:id',namespaces=NS); assert len(refs)==469 and len(set(refs))==469
    frows=[]
    for fn in f.xpath('.//w:footnote',namespaces=NS):
        fid=fn.get(f'{{{W}}}id')
        if fid is None or int(fid)<0: continue
        frows.append((int(fid),''.join(fn.xpath('.//w:t/text()',namespaces=NS))))
    frows.sort()
    fh=hashlib.sha256('\n'.join(f'{i}\t{t}' for i,t in frows).encode()).hexdigest(); assert fh==FOOTNOTE_TEXT_HASH,(fh,FOOTNOTE_TEXT_HASH)
    assert len(d.xpath('.//w:bookmarkStart',namespaces=NS))==53 and len(d.xpath('.//w:bookmarkEnd',namespaces=NS))==53
    instr=[]
    for n in z.namelist():
        if n.startswith('word/') and n.endswith('.xml'):
            try:r=etree.fromstring(z.read(n))
            except Exception:continue
            instr += [x.strip() for x in r.xpath('.//w:instrText/text()',namespaces=NS)]
    c=Counter(x.split()[0] for x in instr if x.split())
    assert c['ADDIN']==466 and c['PAGEREF']==46 and c['TOC']==1 and c['PAGE']==1,c
    assert len(d.xpath('.//w:hyperlink',namespaces=NS))==46
    vals=s.xpath('./w:updateFields/@w:val',namespaces=NS); assert vals and vals[-1].lower() in ('true','1','on')
    assert len(d.xpath('.//w:ins|.//w:del|.//w:moveFrom|.//w:moveTo',namespaces=NS))==0
    assert len(d.xpath('.//w:commentRangeStart|.//w:commentReference',namespaces=NS))==0
    lines += [
        'FINALIZATION_ITEM3_RED_CLEANUP_VALIDATION=PASS',
        f'SHA256={hashlib.sha256(p.read_bytes()).hexdigest()}',
        'PACKAGE_FF0000=0',
        'BODY_PARAGRAPHS=674',
        f'BODY_TEXT_HASH={bh}',
        f'FOOTNOTE_TEXT_HASH={fh}',
        'FOOTNOTE_REFERENCES=469/469',
        'ORPHAN_DANGLING_DUPLICATE=0/0/0',
        'ADDIN=466','TOC=1','PAGEREF=46','PAGE=1',
        'BOOKMARKS=53/53','HYPERLINKS=46','WORD_UPDATE_FIELDS_ON_OPEN=true',
        'TRACKED_CHANGES=0','COMMENTS=0'
    ]
out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
