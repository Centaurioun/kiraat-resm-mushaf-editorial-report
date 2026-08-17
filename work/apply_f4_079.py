#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil,sys
import apply_f4_053_057 as h
import apply_f4_078 as f78

NS=h.NS; W=h.W
R={
341:"Bazı resm kaynaklarında, 1960'lı yıllarda Afrika ülkelerinde tahrif edilmiş mushafların dağıtıldığına dair Mısır basınında iddialar yayımlandığı aktarılmaktadır. Ancak bu çalışmada söz konusu haberlerin dayandırıldığı gazete nüshaları doğrudan doğrulanamadığından, olayın ayrıntıları kesin tarihsel veri olarak kullanılmamalıdır.",
342:"İlgili kaynakta bazı âyetlerden lafız çıkarıldığına dair örnekler aktarılmaktadır; bu ayrıntılar burada doğrulanmış vaka olarak değil, kaynağın naklettiği iddialar olarak kaydedilmektedir.",
343:"Aynı anlatıda başka lafız çıkarma örnekleri de zikredilmektedir; bunlar bağımsız biçimde doğrulanamadığından kesin tarihsel veri olarak kullanılmamaktadır.",
344:"Kaynak ayrıca bazı lafızların başka lafızlarla değiştirildiğini ileri sürmektedir; bu ayrıntı da doğrudan doğrulanmış bir olgu olarak benimsenmemektedir.",
345:"Filistin'deki bazı okul mushaflarına ilişkin çıkarma iddiaları da aynı anlatı içinde yer almaktadır; dayanak malzeme doğrudan doğrulanamadığından bu aktarım ihtiyatla değerlendirilmelidir.",
346:"Aynı kaynak grubunda ikinci bir âyetin de okutulmadığı ileri sürülmektedir; dayandırıldığı basın nüshası doğrudan doğrulanmadığından ayrıntı kesin tarihsel veri sayılmamalıdır.",
347:"Kaynak, söz konusu iddialara karşı bazı resmî ve dinî çevrelerin tepki gösterdiğini de aktarmaktadır. Bununla birlikte failin amacı hakkında hüküm kuran açıklamalar doğrulanmış olgu olarak kullanılamaz."
}
BRIDGE="Bu nedenle ayrıntılar, olayın doğrulanmış unsurları olarak değil, ilgili kaynakların aktardığı iddiaların kapsamını göstermek üzere sınırlı biçimde anılmaktadır."
CLOSE="Bu örnek, resm literatüründe metin güvenliği kaygısının nasıl gerekçelendirildiğini gösteren bir aktarım olarak kullanılabilir; ancak olayın tarihsel ayrıntıları bağımsız doğrulama olmadan argümanın ampirik kanıtı hâline getirilmemelidir."

def rewrite_preserve(p,new,expected_fn):
    sp=h.spec(p)
    if sp['fn'] != [str(expected_fn)]: raise RuntimeError(f'FN mismatch {expected_fn}: {sp}')
    nodes=p.xpath('.//w:t',namespaces=NS)
    target=None
    for t in nodes:
        r=t.getparent()
        if r.tag != f'{{{W}}}r': continue
        if r.xpath('.//w:rtl|.//w:footnoteReference|.//w:instrText|.//w:fldChar',namespaces=NS): continue
        target=t; break
    if target is None: raise RuntimeError('no safe LTR text node')
    for t in nodes:t.text=''
    target.text=new
    target.set('{http://www.w3.org/XML/1998/namespace}space','preserve')

def rewrite_no_fn_preserve_rtl(p,new):
    sp=h.spec(p)
    if sp['fn'] or sp['instr'] or sp['fld'] or sp['hyper'] or sp['book']: raise RuntimeError('unsafe no-fn rewrite '+str(sp))
    nodes=p.xpath('.//w:t',namespaces=NS); target=None
    for t in nodes:
        r=t.getparent()
        if r.tag==f'{{{W}}}r' and not r.xpath('.//w:rtl',namespaces=NS): target=t;break
    if target is None:
        r=etree.Element(f'{{{W}}}r'); target=etree.SubElement(r,f'{{{W}}}t'); p.append(r)
    for t in nodes:t.text=''
    target.text=new

def complete(path):
    with ZipFile(path) as z:
        d=etree.fromstring(z.read('word/document.xml')); text='\n'.join(h.txt(p) for p in d.xpath('.//w:body/w:p',namespaces=NS))
    n=h.norm(text)
    return all(h.norm(x) in n for x in list(R.values())+[BRIDGE,CLOSE]) and h.norm('Bu son silmenin amacı') not in n and h.norm('İsrail’in Fas, Gana, Gine, Mali') not in n

def apply(src:Path,out:Path):
    if complete(src):
        f78.validate_structural(src,src); shutil.copyfile(src,out); return [('F4-079','current','ALREADY_SATISFIED')]
    with ZipFile(src,'r') as zin:
        d=etree.fromstring(zin.read('word/document.xml')); body=d.find('.//w:body',namespaces=NS); ps=body.xpath('./w:p',namespaces=NS)
        anchors={
          341:'Mushafın aslî yazım biçiminin korunması meselesi, kaynaklarda yalnızca şekle ilişkin',
          342:'“وَقَالَتِ الْيَهُودَُ',
          343:'“وَمَنْ يَبْتَغِ غَيْرَ الْإسْلَامِ',
          344:'Hırsızlık âyetinde geçen',
          345:'“لَا يَنْهَاكُمُ اللهُ',
          346:'“إنَّمَا يَنْهَاكُمُ اللهُ',
          347:'Bu son silmenin amacı'
        }
        for fid,a in anchors.items():
            ps=body.xpath('./w:p',namespaces=NS); _,p=h.find(ps,a); rewrite_preserve(p,R[fid],fid)
        ps=body.xpath('./w:p',namespaces=NS); _,p=h.find(ps,'Bazı yerlerde ikinci “لا”nın kaldırılarak'); rewrite_no_fn_preserve_rtl(p,BRIDGE)
        ps=body.xpath('./w:p',namespaces=NS)
        # Remove the now-redundant no-citation list-introduction paragraph with no protected structure.
        hits=[(i,p) for i,p in enumerate(ps) if h.norm(h.txt(p)).startswith(h.norm('İşgal altındaki Filistin’de Arap Müslüman okullarında'))]
        if hits:
            _,p=hits[0]; sp=h.spec(p)
            if any([sp['fn'],sp['instr'],sp['fld'],sp['hyper'],sp['rtl'],sp['book']]): raise RuntimeError('unsafe P327 delete '+str(sp))
            body.remove(p)
        ps=body.xpath('./w:p',namespaces=NS); _,p=h.find(ps,'Kaynaklar, bu örnekleri, mushafın aslî resminden uzaklaşmanın sadece teorik bir kaygı olmayıp');
        if h.spec(p)['fn']: raise RuntimeError('closing unexpectedly cited')
        h.whole(p,CLOSE,())
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():zout.writestr(info,xml if info.filename=='word/document.xml' else zin.read(info.filename))
    f78.validate_structural(src,out)
    if not complete(out): raise RuntimeError('F4-079 postconditions incomplete')
    return [('F4-079','current','STRUCTURALLY_APPLIED_CAVEATED_SOURCE_REANCHORING')]

if __name__=='__main__':
    for row in apply(Path(sys.argv[1]),Path(sys.argv[2])):print('\t'.join(map(str,row)))
