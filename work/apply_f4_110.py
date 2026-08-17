#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from copy import deepcopy
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78
W=h.W; NS=h.NS

ANCHOR="Kitabın ilmî katkısı, resm ve kırâat alanlarına yeni bir kaynak veya sahihlik ölçüsü eklemekten ziyade, tarihsel oluşumdan çağdaş mushaf neşrine kadar uzanan farklı meseleleri aynı ilişki içinde değerlendirmesidir."
KEEP1=ANCHOR
KEEP2="Bu yaklaşım; kırâatin kaynağı ile kabul şartını, resm-i Osmânî’ye uygunluk ile isnad sahihliğini, yazının okuyuşa imkân vermesi ile okuyuşun rivâyetle sabit olmasını ve sahâbe mushaflarının tarihsel değeri ile Osmânî mushafların normatif otoritesini birbirinden ayırmayı sağlamaktadır."
OLD_RESEARCH="Erken mushaf yazmaları, şehir mushaflarına nispet edilen farklılıklar, bölgesel kırâat gelenekleri ve çağdaş neşirlerin resm tercihleri, bu yaklaşımın daha ayrıntılı uygulanabileceği araştırma alanlarıdır."
FINAL="Son tahlilde resm-i Osmânî ile kırâat rivâyeti arasındaki ilişki, yazı ile sözlü aktarımın birbirinin yerine geçtiği değil, birbirini tamamladığı bir aktarım düzeni içinde anlaşılmalıdır. Resm, rivâyet edilen okuyuşların müşterek mushaf yazısıyla bağdaşma sınırlarını gösterirken, okuyuşun sahihliği ve edâsı rivâyet geleneği içinde belirlenmiştir."
FUTURE="Gelecek çalışmalar, erken mushaf nüshaları, şehir mushaflarına ilişkin rivâyetler ve kırâat literatüründeki resm atıflarını karşılaştırmalı olarak inceleyerek bu ilişkinin belirli örneklerdeki tarihsel görünümünü daha ayrıntılı biçimde ortaya koyabilir."
BIB="Kaynakça"
PAGINATION_TAGS=['keepNext','pageBreakBefore']


def safe_plain(p,label):
    s=h.spec(p)
    if s['fn'] or s['instr'] or s['fld'] or s['hyper'] or s['rtl'] or s['book']:
        raise RuntimeError(f'{label} protected structure present: {s}')

def set_text_preserve_ppr(p,text):
    safe_plain(p,'paragraph')
    rp=h.first_rpr(p); h.clear(p); h.add(p,text,rp)

def force_pagination_off(p):
    ppr=p.find(f'{{{W}}}pPr')
    if ppr is None:
        ppr=etree.Element(f'{{{W}}}pPr'); p.insert(0,ppr)
    for tag in PAGINATION_TAGS:
        el=ppr.find(f'{{{W}}}{tag}')
        if el is None:
            el=etree.SubElement(ppr,f'{{{W}}}{tag}')
        el.set(f'{{{W}}}val','0')

def pagination_explicitly_off(p):
    ppr=p.find(f'{{{W}}}pPr')
    if ppr is None:return False
    for tag in PAGINATION_TAGS:
        el=ppr.find(f'{{{W}}}{tag}')
        if el is None:return False
        if el.get(f'{{{W}}}val') not in ('0','false','off'):return False
    return True

def new_para_like(ref,text,force_off=False):
    p=etree.Element(f'{{{W}}}p')
    ppr=ref.find(f'{{{W}}}pPr')
    if ppr is not None:p.append(deepcopy(ppr))
    if force_off: force_pagination_off(p)
    rp=h.first_rpr(ref); h.add(p,text,rp)
    return p

def state(path:Path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        return d,body,ps,[h.norm(h.txt(p)) for p in ps]

def complete(path:Path):
    d,body,ps,texts=state(path)
    contrib=[p for p in ps if h.norm(h.txt(p)).startswith(h.norm(ANCHOR))]
    finals=[p for p in ps if h.norm(h.txt(p))==h.norm(FINAL)]
    future=[p for p in ps if h.norm(h.txt(p))==h.norm(FUTURE)]
    bib=[i for i,p in enumerate(ps) if h.norm(h.txt(p))==h.norm(BIB) and h.spec(p)['book']>0]
    if len(contrib)!=1 or len(finals)!=1 or len(future)!=1 or len(bib)!=1:return False
    ct=h.norm(h.txt(contrib[0]))
    if h.norm(KEEP2) not in ct or h.norm(OLD_RESEARCH) in ct:return False
    fi=ps.index(finals[0]); fu=ps.index(future[0]); bi=bib[0]
    return fi < fu < bi and pagination_explicitly_off(future[0])

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-110','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        ic,pc=h.find(ps,ANCHOR)
        if h.norm(KEEP2) not in h.norm(h.txt(pc)) or h.norm(OLD_RESEARCH) not in h.norm(h.txt(pc)):
            raise RuntimeError('F4-110 contribution/research source text mismatch')
        safe_plain(pc,'F4-110 contribution')
        h.span(pc,OLD_RESEARCH,'')
        if h.norm(h.txt(pc)) != h.norm(KEEP1+' '+KEEP2):
            set_text_preserve_ppr(pc,KEEP1+' '+KEEP2)
        ps=body.xpath('./w:p',namespaces=NS)
        ib,pb=h.find(ps,BIB)
        if h.spec(pb)['book']<=0: raise RuntimeError('F4-110 Kaynakça heading/bookmark not found')
        prev=ps[ib-1]
        if h.norm(h.txt(prev))=='' and not any(h.spec(prev)[k] for k in ['fn','instr','fld','hyper','rtl','book']):
            set_text_preserve_ppr(prev,FINAL); pfinal=prev
        else:
            pfinal=new_para_like(pc,FINAL,force_off=True); body.insert(body.index(pb),pfinal)
        # Explicitly override inherited pagination so the research paragraph stays in Sonuç rather than following Kaynakça.
        pnew=new_para_like(pc,FUTURE,force_off=True)
        body.insert(body.index(pb),pnew)
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-110 postconditions incomplete')
    return [('F4-110','Sonuc_end','APPLIED_FINAL_JUDGMENT_AND_FUTURE_RESEARCH_SEPARATION_EXPLICIT_PAGINATION_OFF')]

if __name__=='__main__':
    for r in apply(Path(sys.argv[1]),Path(sys.argv[2])): print('\t'.join(map(str,r)))
