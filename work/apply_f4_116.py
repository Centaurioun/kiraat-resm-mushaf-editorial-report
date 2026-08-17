#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W}

BIB_1975="Ebû Şâme, Şihâbuddîn Abdurrahmân b. İsmâîl. el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-azîz. thk. Tayyar Altıkulaç. 2 Cilt. Beyrut: Dâr Sadr, 1975."
BIB_1993="Ebû Şâme, Şihâbuddîn Abdurrahmân İsmâîl. el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-Azîz. thk. Velîd Müsâid et-Tabatabâî. Kuveyt: Mektebetü’l-İmâm ez-Zehebî, 1993."
FN86_EXPECT="Şihâbuddîn Abdurrahmân İsmâîl Ebû Şâme, el-Murşidu’l-vecîz ilâ ulûmin tetaallaku bi’l-kitâbi’l-Azîz, thk. Velîd Müsâid et-Tabatabâî (Kuveyt: Mektebetü’l-İmâm ez-Zehebî, 1993), 212."
FN394_EXPECT="Ebû Şâme, el-Murşidu’l-vecîz, 144."


def text(el):
    return ''.join(el.xpath('.//w:t/text()',namespaces=NS))


def instrs(z):
    out=[]
    for name in z.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try:r=etree.fromstring(z.read(name))
            except Exception:continue
            out += [''.join(x.itertext()).strip() for x in r.xpath('//w:instrText',namespaces=NS)]
    return out


def verify(path):
    with ZipFile(path) as z:
        if z.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        for name in z.namelist():
            if name.endswith('.xml') or name.endswith('.rels'): etree.fromstring(z.read(name))
        d=etree.fromstring(z.read('word/document.xml')); f=etree.fromstring(z.read('word/footnotes.xml'))
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(ps)!=674: raise RuntimeError(f'body paragraph count {len(ps)} != 674')
        texts=[text(p) for p in ps]
        if texts.count(BIB_1975)!=1 or texts.count(BIB_1993)!=1:
            raise RuntimeError(f'Ebû Şâme bibliography record counts 1975={texts.count(BIB_1975)} 1993={texts.count(BIB_1993)}')
        if texts[504]!=BIB_1975 or texts[505]!=BIB_1993:
            raise RuntimeError('expected current bibliography positions P504/P505 changed')
        def fn(fid):
            hit=f.xpath(f'./w:footnote[@w:id="{fid}"]',namespaces=NS)
            if len(hit)!=1: raise RuntimeError(f'FN{fid} multiplicity {len(hit)}')
            return text(hit[0])
        if FN86_EXPECT not in fn(86): raise RuntimeError('FN86 no longer proves 1993 edition use')
        if FN394_EXPECT not in fn(394): raise RuntimeError('FN394 no longer contains p.144 short citation')
        # P377 is the live claim carried by FN394.
        refs=ps[377].xpath('.//w:footnoteReference/@w:id',namespaces=NS)
        if '394' not in refs: raise RuntimeError(f'P377 no longer references FN394: {refs}')
        p377=text(ps[377])
        for phrase in ('Osman mushafı üzerinde birleşip','mensuh hükmünde','ümmetin imamı'):
            if phrase not in p377: raise RuntimeError(f'P377 adjudication anchor missing: {phrase}')
        ids=[x for x in f.xpath('./w:footnote/@w:id',namespaces=NS) if int(x)>0]
        refs_all=d.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if len(ids)!=469 or len(refs_all)!=469 or set(ids)!=set(refs_all) or len(set(refs_all))!=469:
            raise RuntimeError('footnote/reference identity inventory failed')
        ins=instrs(z)
        if len(ins)!=520: raise RuntimeError(f'field instruction count {len(ins)} != 520')
        addin=sum(1 for x in ins if 'ADDIN ' in x); item=sum(1 for x in ins if 'ZOTERO_ITEM' in x); bib=sum(1 for x in ins if 'ZOTERO_BIBL' in x)
        if (addin,item,bib)!=(466,465,1): raise RuntimeError(f'ADDIN/Zotero field inventory {(addin,item,bib)}')
        if len(d.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(d.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmark inventory changed')
        if len(d.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink inventory changed')
        return {
            'body':len(ps),'footnotes':len(ids),'refs':len(refs_all),'fields':len(ins),
            'addin':addin,'zotero_item':item,'zotero_bib':bib,
            'p377_refs':refs,'fn86':fn(86),'fn394':fn(394)
        }


def apply(src,out):
    before=verify(src)
    shutil.copyfile(src,out)
    after=verify(out)
    if src.read_bytes()!=out.read_bytes(): raise RuntimeError('F4-116 must be byte-identical no-op')
    print('F4-116\tVERIFIED_NO_CHANGE\tBYTE_IDENTICAL')
    print('BIB_1975\tKEEP\tUSED_BY_FN394_P144_EXTERNAL_PAGE_CONTENT_MATCH')
    print('BIB_1993\tKEEP\tUSED_BY_FN86_EXPLICIT_FULL_CITATION_P212')
    print(f"STRUCTURAL\tBODY={after['body']}\tFOOTNOTES={after['footnotes']}\tREFS={after['refs']}\tFIELDS={after['fields']}\tADDIN={after['addin']}\tZOTERO_ITEM={after['zotero_item']}\tZOTERO_BIB={after['zotero_bib']}")
    print('FN86\t'+after['fn86'])
    print('FN394\t'+after['fn394'])

if __name__=='__main__':
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
