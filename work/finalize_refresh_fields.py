#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from collections import Counter
import hashlib,re,shutil,sys
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; NS={'w':W}
ORIGINAL_SHA='81f97403c0cfcf151260ab7018077145ba260c4fe4f30ca5fe2d3b501d093571'
PAGE={'_Toc235035665':'1','_Toc235035666':'2','_Toc235035667':'7','_Toc235035668':'7','_Toc235035669':'7','_Toc235035670':'9','_Toc235035671':'10','_Toc235035672':'13','_Toc235035673':'17','_Toc235035674':'20','_Toc235035675':'20','_Toc235035676':'21','_Toc235035677':'22','_Toc235035678':'25','_Toc235035679':'28','_Toc235035680':'29','_Toc235035681':'32','_Toc235035682':'33','_Toc235035683':'36','_Toc235035684':'36','_Toc235035685':'36','_Toc235035686':'37','_Toc235035687':'38','_Toc235035688':'39','_Toc235035689':'40','_Toc235035690':'41','_Toc235035692':'46','_Toc235035693':'46','_Toc235035694':'46','_Toc235035695':'48','_Toc235035696':'49','_Toc235035697':'51','_Toc235035698':'53','_Toc235035699':'54','_Toc235035700':'58','_Toc235035706':'70','_Toc235035707':'70','_Toc235035708':'70','_Toc235035709':'72','_Toc235035710':'76','_Toc235035711':'78','_Toc235035712':'82','_Toc235035713':'86','_Toc235035714':'89','_Toc235035715':'94','_Toc235035716':'98'}
REMOVE={'_Toc235035691','_Toc235035701','_Toc235035702','_Toc235035703','_Toc235035704','_Toc235035705'}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def text(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def titles(d):
 out={}
 for p in d.xpath('.//w:body//w:p',namespaces=NS):
  t=text(p).strip()
  if not t: continue
  for b in p.xpath('.//w:bookmarkStart[@w:name]',namespaces=NS):
   n=b.get(f'{{{W}}}name')
   if n and n.startswith('_Toc'): out[n]=t
 return out
def entries(d):
 out=[]
 for p in d.xpath('.//w:p',namespaces=NS):
  hs=p.xpath('./w:hyperlink[@w:anchor]',namespaces=NS)
  if len(hs)!=1: continue
  h=hs[0]; a=h.get(f'{{{W}}}anchor'); ins=' '.join(x.strip() for x in h.xpath('.//w:instrText/text()',namespaces=NS))
  if a and a.startswith('_Toc') and 'PAGEREF' in ins: out.append((p,h,a))
 return out
def page_node(h):
 sep=False
 for r in h.xpath('./w:r',namespaces=NS):
  f=r.find('w:fldChar',namespaces=NS)
  if f is not None:
   k=f.get(f'{{{W}}}fldCharType')
   if k=='separate': sep=True; continue
   if k=='end' and sep: break
  if sep:
   ts=r.xpath('./w:t',namespaces=NS)
   if ts:return ts[0]
 return None
def title_nodes(h):
 out=[]
 for r in h.xpath('./w:r',namespaces=NS):
  f=r.find('w:fldChar',namespaces=NS)
  if f is not None and f.get(f'{{{W}}}fldCharType')=='begin': break
  out += r.xpath('./w:t',namespaces=NS)
 return out
def ftypes(z):
 a=[]
 for n in z.namelist():
  if n.startswith('word/') and n.endswith('.xml'):
   try:r=etree.fromstring(z.read(n))
   except:continue
   a += [x.strip() for x in r.xpath('.//w:instrText/text()',namespaces=NS)]
 return Counter(x.split()[0] for x in a if x.split())
def satisfied(d,s):
 es=entries(d)
 if len(es)!=46:return False
 for _,h,a in es:
  n=page_node(h)
  if a not in PAGE or a in REMOVE or n is None or (n.text or '')!=PAGE[a]:return False
 v=s.xpath('./w:updateFields/@w:val',namespaces=NS)
 return bool(v and v[-1].lower() in ('true','1','on'))
def apply(src,out):
 got=sha(src)
 with ZipFile(src) as z:
  assert z.testzip() is None
  d=etree.fromstring(z.read('word/document.xml')); s=etree.fromstring(z.read('word/settings.xml'))
  if got!=ORIGINAL_SHA and satisfied(d,s): shutil.copyfile(src,out); print('FIELD_REFRESH ALREADY_SATISFIED'); return
  if got!=ORIGINAL_SHA: raise RuntimeError(f'input SHA {got}')
  body=d.xpath('.//w:body/w:p',namespaces=NS); assert len(body)==674
  body_hash=hashlib.sha256('\n'.join(text(p) for p in body).encode()).hexdigest()
  refs=d.xpath('.//w:footnoteReference/@w:id',namespaces=NS); bs=[(x.get(f'{{{W}}}id'),x.get(f'{{{W}}}name')) for x in d.xpath('.//w:bookmarkStart',namespaces=NS)]; be=[x.get(f'{{{W}}}id') for x in d.xpath('.//w:bookmarkEnd',namespaces=NS)]
  ts=titles(d); es=entries(d); assert len(es)==52
  rem=[]
  for p,h,a in list(es):
   if a in REMOVE: p.getparent().remove(p); rem.append(a); continue
   assert a in PAGE and a in ts
   ns=title_nodes(h); assert ns
   old=''.join((x.text or '') for x in ns); m=re.match(r'^\s*(\d+(?:\.\d+)*\.)',old); pref=m.group(1) if m else ''; title=ts[a].strip()
   if len(ns)>=2 and re.fullmatch(r'\s*\d+(?:\.\d+)*\.\s*',ns[0].text or ''):
    ns[0].text=pref; ns[1].text=title
    for x in ns[2:]: x.text=''
   else:
    ns[0].text=(pref+title) if pref and not title.startswith(pref) else title
    for x in ns[1:]: x.text=''
   pn=page_node(h); assert pn is not None; pn.text=PAGE[a]
  assert len(rem)==6
  us=s.xpath('./w:updateFields',namespaces=NS)
  if us:
   us[0].set(f'{{{W}}}val','true')
   for x in us[1:]:s.remove(x)
  else:
   x=etree.Element(f'{{{W}}}updateFields');x.set(f'{{{W}}}val','true');s.append(x)
  assert len(d.xpath('.//w:body/w:p',namespaces=NS))==674
  assert body_hash==hashlib.sha256('\n'.join(text(p) for p in d.xpath('.//w:body/w:p',namespaces=NS)).encode()).hexdigest()
  assert refs==d.xpath('.//w:footnoteReference/@w:id',namespaces=NS); assert bs==[(x.get(f'{{{W}}}id'),x.get(f'{{{W}}}name')) for x in d.xpath('.//w:bookmarkStart',namespaces=NS)]; assert be==[x.get(f'{{{W}}}id') for x in d.xpath('.//w:bookmarkEnd',namespaces=NS)]
  dx=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes'); sx=etree.tostring(s,xml_declaration=True,encoding='UTF-8',standalone='yes')
  with ZipFile(out,'w') as o:
   for info in z.infolist():
    data=z.read(info.filename)
    if info.filename=='word/document.xml':data=dx
    elif info.filename=='word/settings.xml':data=sx
    o.writestr(info,data)
 with ZipFile(src) as a,ZipFile(out) as b:
  assert b.testzip() is None
  changed=[n for n in a.namelist() if a.read(n)!=b.read(n)]; assert changed==['word/document.xml','word/settings.xml'],changed
  c=ftypes(b); assert c['ADDIN']==466 and c['TOC']==1 and c['PAGEREF']==46 and c['PAGE']==1,c
  dd=etree.fromstring(b.read('word/document.xml'));ss=etree.fromstring(b.read('word/settings.xml'))
  assert len(dd.xpath('.//w:footnoteReference',namespaces=NS))==469; assert len(dd.xpath('.//w:bookmarkStart',namespaces=NS))==53; assert len(dd.xpath('.//w:bookmarkEnd',namespaces=NS))==53; assert len(dd.xpath('.//w:hyperlink',namespaces=NS))==46; assert satisfied(dd,ss)
 print('FIELD_REFRESH APPLIED');print('REMOVED_STALE_TOC_ENTRIES='+','.join(rem));print('RETAINED_TOC_ENTRIES=46');print('ADDIN=466');print('FOOTNOTES=469');print('BOOKMARKS=53/53');print('WORD_UPDATE_FIELDS_ON_OPEN=true');print('PROTECTED_NARRATIVE=PASS');print('CHANGED_PARTS=word/document.xml,word/settings.xml')
if __name__=='__main__':
 if len(sys.argv)!=3:raise SystemExit('usage INPUT OUTPUT')
 apply(Path(sys.argv[1]),Path(sys.argv[2]))
