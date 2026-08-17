#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

W=h.W; NS=h.NS
ANCHOR="Sahâbe döneminde Kur’an’ın yazıya geçirilmesi, vahyin korunmasına yönelik tedbirlerin erken safhada devreye girdiğini göstermesi bakımından son derece önemlidir."
NEXT="Nitekim sahâbe mushafları arasındaki farklılıkların bir kısmı, okuyuş sırasında karışıklık doğurmayacak derecede manayı açıklayıcı kayıtların mushaf kenarına veya satır arasına alınmasından kaynaklanmıştır."
NEW="Sahâbeye nispet edilen mushaf farklılıkları tek bir kategori altında değerlendirilmemelidir. Kaynaklarda farklı okuyuş rivâyetleri, açıklayıcı veya tefsirî ifadeler, kelime tertibi yahut yazım biçimine ilişkin aktarımlar ve isnadı veya yorumu tartışmalı kayıtlar birlikte yer almaktadır. Bu malzemenin tarihsel değeri, erken dönemdeki okuyuş ve yazı çeşitliliğine dair veri sunmasındadır. Buna karşılık ümmetin müşterek mushaf geleneğinde normatif ölçü, Osmânî mushafların yazılı çerçevesi ile sahih rivâyetin birlikte değerlendirilmesi üzerinden şekillenmiştir."

def paragraph_text(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(paragraph_text(p))==h.norm(NEW)]
        if len(hits)!=1:return False
        i,p=hits[0]
        return h.spec(p)['fn']==[] and i>0 and i+1<len(ps) and h.norm(paragraph_text(ps[i-1])).startswith(h.norm(ANCHOR)) and h.norm(paragraph_text(ps[i+1])).startswith(h.norm(NEXT))

def make_para_like(src):
    p=etree.Element(f'{{{W}}}p')
    ppr=src.find(f'{{{W}}}pPr')
    if ppr is not None:p.append(deepcopy(ppr))
    rp=h.first_rpr(src)
    h.add(p,NEW,rp)
    return p

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-086','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        i,p=h.find(ps,ANCHOR)
        if h.spec(p)['fn']!=['375']:raise RuntimeError('F4-086 anchor note mismatch '+str(h.spec(p)))
        if i+1>=len(ps) or not h.norm(paragraph_text(ps[i+1])).startswith(h.norm(NEXT)) or h.spec(ps[i+1])['fn']!=['376']:
            raise RuntimeError('F4-086 next-category boundary mismatch')
        newp=make_para_like(p)
        body.insert(body.index(p)+1,newp)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out):raise RuntimeError('F4-086 postconditions incomplete')
    return [('F4-086','current','STRUCTURALLY_APPLIED_CATEGORY_FRAME')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,row)))
