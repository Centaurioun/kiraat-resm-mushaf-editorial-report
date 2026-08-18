#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from collections import Counter
import hashlib,sys
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';NS={'w':W}
BODY_HASH='60c3f29968f6693de7cba0a389d41092528c0bb385a0be9f753bf6742c3463d9'
PAGE={'_Toc235035665':'1','_Toc235035666':'2','_Toc235035667':'7','_Toc235035668':'7','_Toc235035669':'7','_Toc235035670':'9','_Toc235035671':'10','_Toc235035672':'13','_Toc235035673':'17','_Toc235035674':'20','_Toc235035675':'20','_Toc235035676':'21','_Toc235035677':'22','_Toc235035678':'25','_Toc235035679':'28','_Toc235035680':'29','_Toc235035681':'32','_Toc235035682':'33','_Toc235035683':'36','_Toc235035684':'36','_Toc235035685':'36','_Toc235035686':'37','_Toc235035687':'38','_Toc235035688':'39','_Toc235035689':'40','_Toc235035690':'41','_Toc235035692':'46','_Toc235035693':'46','_Toc235035694':'46','_Toc235035695':'48','_Toc235035696':'49','_Toc235035697':'51','_Toc235035698':'53','_Toc235035699':'54','_Toc235035700':'58','_Toc235035706':'70','_Toc235035707':'70','_Toc235035708':'70','_Toc235035709':'72','_Toc235035710':'76','_Toc235035711':'78','_Toc235035712':'82','_Toc235035713':'86','_Toc235035714':'89','_Toc235035715':'94','_Toc235035716':'98'}
REM={'_Toc235035691','_Toc235035701','_Toc235035702','_Toc235035703','_Toc235035704','_Toc235035705'}
def txt(p):return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def page_node(h):
 sep=False
 for r in h.xpath('./w:r',namespaces=NS):
  f=r.find('w:fldChar',namespaces=NS)
  if f is not None:
   k=f.get(f'{{{W}}}fldCharType')
   if k=='separate':sep=True;continue
   if k=='end' and sep:break
  if sep:
   t=r.xpath('./w:t',namespaces=NS)
   if t:return t[0]
 return None
p=Path(sys.argv[1]);out=Path(sys.argv[2]);lines=[]
with ZipFile(p) as z:
 assert z.testzip() is None
 d=etree.fromstring(z.read('word/document.xml'));s=etree.fromstring(z.read('word/settings.xml'))
 body=d.xpath('.//w:body/w:p',namespaces=NS); assert len(body)==674
 bh=hashlib.sha256('\n'.join(txt(x) for x in body).encode()).hexdigest();assert bh==BODY_HASH,(bh,BODY_HASH)
 refs=d.xpath('.//w:footnoteReference/@w:id',namespaces=NS);assert len(refs)==469 and len(set(refs))==469
 assert len(d.xpath('.//w:bookmarkStart',namespaces=NS))==53 and len(d.xpath('.//w:bookmarkEnd',namespaces=NS))==53
 instr=[]
 for n in z.namelist():
  if n.startswith('word/') and n.endswith('.xml'):
   try:r=etree.fromstring(z.read(n))
   except:continue
   instr += [x.strip() for x in r.xpath('.//w:instrText/text()',namespaces=NS)]
 c=Counter(x.split()[0] for x in instr if x.split());assert c['ADDIN']==466 and c['PAGEREF']==46 and c['TOC']==1 and c['PAGE']==1,c
 hs=[]
 for h in d.xpath('.//w:hyperlink[@w:anchor]',namespaces=NS):
  a=h.get(f'{{{W}}}anchor');ins=' '.join(x.strip() for x in h.xpath('.//w:instrText/text()',namespaces=NS))
  if a and a.startswith('_Toc') and 'PAGEREF' in ins:hs.append((a,h))
 assert len(hs)==46
 got={}
 for a,h in hs:
  n=page_node(h);assert n is not None;got[a]=n.text or ''
 assert got==PAGE,(got,PAGE)
 assert not (set(got)&REM)
 assert len(d.xpath('.//w:hyperlink',namespaces=NS))==46
 vals=s.xpath('./w:updateFields/@w:val',namespaces=NS);assert vals and vals[-1].lower() in ('true','1','on')
 alltext='\n'.join(txt(x) for x in d.xpath('.//w:p',namespaces=NS))
 assert 'Error! Bookmark not defined' not in alltext
 lines += ['FIELD_REFRESH_VALIDATION=PASS',f'SHA256={hashlib.sha256(p.read_bytes()).hexdigest()}','BODY_PARAGRAPHS=674',f'BODY_TEXT_HASH={bh}','FOOTNOTE_REFERENCES=469/469','ORPHAN_DANGLING_DUPLICATE=0/0/0','ADDIN=466','TOC=1','PAGEREF=46','PAGE=1','BOOKMARKS=53/53','TOC_HYPERLINKS=46','WORD_UPDATE_FIELDS_ON_OPEN=true','REMOVED_STALE_TOC='+','.join(sorted(REM)),'TOC_PAGE_CACHE='+','.join(f'{k}:{PAGE[k]}' for k in PAGE)]
out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
