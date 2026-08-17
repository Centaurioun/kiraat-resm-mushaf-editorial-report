#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS
OLD="Mushaf resmi konusunda gevşeklik gösterilmesi, yalnız yazı alanında bir dönüşüm meydana getirmekle kalmayacak"
NEW="Modern imlâya göre yazım, bazı kırâat vecihlerinin resm-i Osmânî içindeki ihtimalî uygunluğunu görünür kılan tarihsel yazım özelliklerini ortadan kaldırabilir veya farklılaştırabilir. Bununla birlikte kırâatlerin varlığı yalnız bu grafik imkâna bağlı değildir; okuyuşların asıl aktarım zemini telakki, edâ ve rivâyet geleneğidir."

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        text='\n'.join(h.txt(p) for p in ps)
        hits=[p for p in ps if h.norm(NEW)==h.norm(h.txt(p))]
    return len(hits)==1 and h.norm(OLD) not in h.norm(text) and h.spec(hits[0])['fn']==[]

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src)
        shutil.copyfile(src,out)
        return [('F4-081','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml'))
        body=d.find('.//w:body',namespaces=NS)
        ps=body.xpath('./w:p',namespaces=NS)
        _,p=h.find(ps,OLD)
        if h.spec(p) != {'fn':[],'instr':[],'fld':0,'hyper':0,'rtl':0,'book':0}:
            raise RuntimeError('F4-081 target unexpectedly protected: '+str(h.spec(p)))
        h.whole(p,NEW,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():
                zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out):
        raise RuntimeError('F4-081 postconditions incomplete')
    return [('F4-081','current','APPLIED_GRAPHIC_VISIBILITY_VS_TRANSMISSION_DISTINCTION')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
