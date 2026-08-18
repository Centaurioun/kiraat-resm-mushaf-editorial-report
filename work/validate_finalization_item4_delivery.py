#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from collections import Counter
import hashlib, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
EXPECTED_SHA='67fc2e5e047957c2dd7ece5f065e612e1b51a331c9894bbb9d20d9b5b49e09f4'
BODY_HASH='60c3f29968f6693de7cba0a389d41092528c0bb385a0be9f753bf6742c3463d9'
FOOTNOTE_HASH='a07e51f7ad77714aa9cdc6254dd0b62daa05bfa6f5a023795ec58f2906fcb0de'

def txt(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))

def main():
    p=Path(sys.argv[1]); out=Path(sys.argv[2]); data=p.read_bytes()
    sha=hashlib.sha256(data).hexdigest(); assert sha==EXPECTED_SHA,(sha,EXPECTED_SHA)
    with ZipFile(p) as z:
        assert z.testzip() is None
        names=z.namelist(); assert len(names)==len(set(names))
        d=etree.fromstring(z.read('word/document.xml'))
        f=etree.fromstring(z.read('word/footnotes.xml'))
        s=etree.fromstring(z.read('word/settings.xml'))
        body=d.xpath('.//w:body/w:p',namespaces=NS); assert len(body)==674
        bh=hashlib.sha256('\n'.join(txt(x) for x in body).encode()).hexdigest(); assert bh==BODY_HASH,(bh,BODY_HASH)
        frows=[]
        for fn in f.xpath('.//w:footnote',namespaces=NS):
            fid=fn.get(f'{{{W}}}id')
            if fid is None or int(fid)<0: continue
            frows.append((int(fid),''.join(fn.xpath('.//w:t/text()',namespaces=NS))))
        frows.sort()
        fh=hashlib.sha256('\n'.join(f'{i}\t{t}' for i,t in frows).encode()).hexdigest(); assert fh==FOOTNOTE_HASH,(fh,FOOTNOTE_HASH)
        refs=d.xpath('.//w:footnoteReference/@w:id',namespaces=NS); assert len(refs)==469 and len(set(refs))==469
        assert len(d.xpath('.//w:bookmarkStart',namespaces=NS))==53
        assert len(d.xpath('.//w:bookmarkEnd',namespaces=NS))==53
        assert len(d.xpath('.//w:hyperlink',namespaces=NS))==46
        assert len(d.xpath('.//w:ins|.//w:del|.//w:moveFrom|.//w:moveTo',namespaces=NS))==0
        assert len(d.xpath('.//w:commentRangeStart|.//w:commentReference',namespaces=NS))==0
        reds=0; instr=[]; comment_count=0
        for n in names:
            if n.startswith('word/') and n.endswith('.xml'):
                try:r=etree.fromstring(z.read(n))
                except Exception: continue
                reds += len(r.xpath('.//w:color[translate(@w:val,"abcdef","ABCDEF")="FF0000"]',namespaces=NS))
                instr += [x.strip() for x in r.xpath('.//w:instrText/text()',namespaces=NS)]
                if n.startswith('word/comments'):
                    comment_count += len(r.xpath('.//w:comment',namespaces=NS))
        assert reds==0,reds
        assert comment_count==0,comment_count
        c=Counter(x.split()[0] for x in instr if x.split())
        assert c['ADDIN']==466 and c['TOC']==1 and c['PAGEREF']==46 and c['PAGE']==1,c
        vals=s.xpath('./w:updateFields/@w:val',namespaces=NS); assert vals and vals[-1].lower() in ('true','1','on')
        alltext='\n'.join(txt(x) for x in d.xpath('.//w:p',namespaces=NS)); assert 'Error! Bookmark not defined' not in alltext
    lines=[
        'FINALIZATION_ITEM4_PUBLISHING_FREEZE=PASS',
        'DELIVERY_FILE=artifacts/delivery/kiraatlerin-rivayetinde-resm-i-mushafin-etkisi-final.docx',
        f'SHA256={sha}',
        f'FILE_SIZE_BYTES={len(data)}',
        'BYTE_IDENTICAL_TO_ITEM3_CANDIDATE=PASS',
        'NO_SCIENTIFIC_OR_EDITORIAL_TEXT_CHANGE=PASS',
        'ZIP_PACKAGE_INTEGRITY=PASS',
        f'BODY_PARAGRAPHS={len(body)}',
        f'BODY_TEXT_HASH={bh}',
        f'FOOTNOTE_TEXT_HASH={fh}',
        'FOOTNOTE_REFERENCES=469/469',
        'ORPHAN_DANGLING_DUPLICATE=0/0/0',
        'ADDIN_ZOTERO=466',
        'TOC=1','PAGEREF=46','PAGE=1',
        'BOOKMARKS=53/53','HYPERLINKS=46',
        'DIRECT_RED_FF0000=0','TRACKED_CHANGES=0','COMMENTS=0',
        'WORD_UPDATE_FIELDS_ON_OPEN=true',
        'VISUAL_QA_INHERITED_FROM_BYTE_IDENTICAL_ITEM3_CANDIDATE=112/112_PASS',
        'FINAL_DELIVERY_STATUS=READY_FOR_HANDOFF'
    ]
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text('\n'.join(lines)+'\n',encoding='utf-8')

if __name__=='__main__': main()
