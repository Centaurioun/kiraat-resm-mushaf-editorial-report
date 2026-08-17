#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_068_072 as base
helper=base.base; NS=base.NS

REQUIRED=[
 "Mârginî’nin bu açıklaması, ilgili yazım biçimini işbâ‘ ve fonetik ayrım çerçevesinde yorumlayan bir değerlendirmedir.",
 "Buraya kadar ele alınan örnekler, resm ile okuyuş arasındaki yazısal ve fonetik ilişkiyi göstermektedir.",
 "Hazf ve Ziyâdeye Yüklenen Mana İlişkileri: Klasik Yorumlar ve Delil Değeri",
 "Hazf ve ziyâde örnekleri resm-i mushaf literatüründe öncelikle belirli kelimelerin yazım özellikleri olarak ele alınmaktadır.",
 "Merrâkuşî, ilgili yazım biçimlerini kelimelerin anlamlarıyla ilişkilendirerek;",
 "Bu örnekler, bazı klasik müelliflerin mushaf yazımındaki belirli farklılıklarla anlam arasında yorum ilişkileri kurduklarını göstermektedir."
]

def text_of(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml'))
        return '\n'.join(helper.txt(p) for p in d.xpath('.//w:body/w:p',namespaces=NS))

def apply(src:Path,out:Path):
    current=text_of(src)
    if all(helper.norm(x) in helper.norm(current) for x in REQUIRED):
        helper.validate(src,src)
        shutil.copyfile(src,out)
        return [(f'F4-{n:03d}','current','ALREADY_SATISFIED') for n in range(68,73)]
    return base.apply(src,out)

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):
        print('\t'.join(map(str,row)))
