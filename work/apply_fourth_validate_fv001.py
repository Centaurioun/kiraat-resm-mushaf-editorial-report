#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W}
BEFORE="Ebû Şâme, Şihâbuddîn Abdurrahmân b. İsmâîl. el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-azîz. thk. Tayyar Altıkulaç. 2 Cilt. Beyrut: Dâr Sadr, 1975."
AFTER="Ebû Şâme, Şihâbuddîn Abdurrahmân b. İsmâîl. el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-azîz. thk. Tayyar Altıkulaç. Beyrut: Dâr Sadr, 1975."
OTHER="Ebû Şâme, Şihâbuddîn Abdurrahmân İsmâîl. el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-Azîz. thk. Velîd Müsâid et-Tabatabâî. Kuveyt: Mektebetü’l-İmâm ez-Zehebî, 1993."

def text(el): return ''.join(el.xpath('.//w:t/text()',namespaces=NS))
def c14n(el): return etree.tostring(el,method='c14n')
def sig(el): return tuple((n.tag,tuple(sorted(n.attrib.items()))) for n in el.iter())

def instrs(z):
    vals=[]
    for name in z.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try:r=etree.fromstring(z.read(name))
            except Exception:continue
            vals += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return vals

def replace_range(p,start,end,new):
    nodes=p.xpath('.//w:t',namespaces=NS); vals=[n.text or '' for n in nodes]
    starts=[]; cur=0
    for v in vals: starts.append(cur); cur+=len(v)
    if not (0 <= start < end <= cur): raise RuntimeError(f'invalid span {start}:{end}/{cur}')
    fi=next(i for i,(st,v) in enumerate(zip(starts,vals)) if start < st+len(v))
    li=next(i for i,(st,v) in enumerate(zip(starts,vals)) if end <= st+len(v))
    for n in nodes[fi:li+1]:
        if n.xpath('ancestor::w:hyperlink',namespaces=NS): raise RuntimeError('FV-001 target occurs inside w:hyperlink')
    prefix=vals[fi][:start-starts[fi]]; suffix=vals[li][end-starts[li]:]
    nodes[fi].text=prefix+new+(suffix if fi==li else '')
    if fi!=li:
        for j in range(fi+1,li): nodes[j].text=''
        nodes[li].text=suffix

def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS); texts=[text(p) for p in ps]
    return len(ps)==674 and texts.count(BEFORE)==0 and texts.count(AFTER)==1 and texts.count(OTHER)==1

def apply(src,out):
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml']); ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if satisfied(d):
            shutil.copyfile(src,out); validate(src,out,False); print('FOURTH-VALIDATE-FV001\tALREADY_SATISFIED'); return
        if len(ps)!=674: raise RuntimeError(f'body paragraph count {len(ps)} !=674')
        texts=[text(p) for p in ps]
        if texts.count(BEFORE)!=1 or texts.count(AFTER)!=0 or texts.count(OTHER)!=1:
            raise RuntimeError(f'unexpected target counts before={texts.count(BEFORE)} corrected={texts.count(AFTER)} 1993={texts.count(OTHER)}')
        idx=texts.index(BEFORE); p=ps[idx]
        if idx!=504: raise RuntimeError(f'FV-001 current paragraph moved: P{idx} != P504')
        if p.xpath('.//w:instrText|.//w:fldChar',namespaces=NS): raise RuntimeError('FV-001 target paragraph contains field instruction/field-char nodes')
        if p.xpath('.//w:hyperlink',namespaces=NS): raise RuntimeError('FV-001 target paragraph contains hyperlink node')
        before_sig=sig(p)
        token=' 2 Cilt.'; pos=BEFORE.find(token)
        if pos<0: raise RuntimeError('FV-001 token missing from exact record')
        replace_range(p,pos,pos+len(token),'')
        if text(p)!=AFTER: raise RuntimeError('FV-001 postcondition text mismatch')
        if sig(p)!=before_sig: raise RuntimeError('FV-001 paragraph OOXML structure changed')
        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist(): zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])
    validate(src,out,True)
    print('FOURTH-VALIDATE-FV001\tAPPLIED\tP504\tREMOVE_ONLY=` 2 Cilt.`')
    print('BEFORE\t'+BEFORE); print('AFTER\t'+AFTER)

def validate(src,out,expect_change):
    with ZipFile(src) as za, ZipFile(out) as zb:
        if za.namelist()!=zb.namelist(): raise RuntimeError('ZIP member/order changed')
        if zb.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        for name in za.namelist():
            if name!='word/document.xml' and za.read(name)!=zb.read(name): raise RuntimeError(f'unexpected package change {name}')
            if name.endswith('.xml') or name.endswith('.rels'): etree.fromstring(zb.read(name))
        da=etree.fromstring(za.read('word/document.xml')); db=etree.fromstring(zb.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)
        if len(pa)!=674 or len(pb)!=674: raise RuntimeError(f'body count changed {len(pa)}->{len(pb)}')
        changed=[i for i,(a,b) in enumerate(zip(pa,pb)) if c14n(a)!=c14n(b)]
        exp=[504] if expect_change else []
        if changed!=exp: raise RuntimeError(f'changed paragraphs {changed} != expected {exp}')
        if expect_change and sig(pa[504])!=sig(pb[504]): raise RuntimeError('P504 structure changed')
        if not satisfied(db): raise RuntimeError('FV-001 corrected-state postcondition failed')
        ia=instrs(za); ib=instrs(zb)
        if ia!=ib or len(ib)!=520: raise RuntimeError('field instructions changed')
        addin=sum('ADDIN ' in x for x in ib); item=sum('ZOTERO_ITEM' in x for x in ib); bib=sum('ZOTERO_BIBL' in x for x in ib)
        if (addin,item,bib)!=(466,465,1): raise RuntimeError(f'ADDIN/Zotero inventory {(addin,item,bib)}')
        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnote references changed')
        if da.xpath('//w:bookmarkStart/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkStart/@w:id',namespaces=NS): raise RuntimeError('bookmark starts changed')
        if da.xpath('//w:bookmarkEnd/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkEnd/@w:id',namespaces=NS): raise RuntimeError('bookmark ends changed')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmark count changed')
        if len(da.xpath('//w:hyperlink',namespaces=NS))!=len(db.xpath('//w:hyperlink',namespaces=NS)) or len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink inventory changed')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('RTL inventory changed')

if __name__=='__main__':
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
