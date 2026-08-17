#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import shutil, sys

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W}

DROP_2006="İbn Ebû Dâvud, Ebû Bekir Abdullah b. Süleymân. Kitâbu’l-mesâhif. thk. Selîm b. Îde’l-Hilâlî el-Eserî. Amman: Ğarâs, 2006."
DROP_ASFAR="İbn Kuteybe, Ebû Muhammed Abdullah b. Muslim. Te’vîlu muhtelifi’l-hadîs. thk. Muhammed Muhyiddîn el-Asfar. Beyrut: el-Mektebetü’l-İslâmî, 1999."
KEEP_2002="İbn Ebû Dâvud, Ebû Bekir Abdullah b. Süleymân b. el-Eş’as. Kitâbu’l-mesâhif. thk. Muhibbüddîn Abdussubhân Vâiz. 2 Cilt. Beyrut: Dâru’l-Beşâiri’l-İslâmiyye, 2002."
KEEP_NECCAR="İbn Kuteybe, Ebû Muhammed Abdullah b. Muslim. Te’vîlu muhtelifu’l-hadîs. thk. Muhammed Zuhrî en-Neccâr. Mektebetü’l-Küllîyât el-Ezheriyye, ts."
KEEP_NECAH_2000="Ebû Dâvud, Süleymân b. Necâh. Muhtasaru’t-tebyîn li hecâi’t-tenzîl. thk. Ahmed b. Muhammed b. Muammer Şarşâl. 5 Cilt. Riyad: Mecmeu’l-Melik Fehd li’t-Tibâati’l-Mushafi’ş-Şerîf, 2000."
KEEP_NECAH_1999="Necâh, Ebû Dâvud Süleymân b. Muhtasaru’t-tebyîn li hecâi’t-tenzîl. thk. Ahmed b. Ahmed Muammer Şarşâl. 2 Cilt. Medine: Mecmau’l-Melik Fahd li’t-Tibâati ve’n-Neşr, 1999."


def ptext(p):
    return ''.join(p.xpath('.//w:t/text()',namespaces=NS))


def c14n(el):
    return etree.tostring(el,method='c14n')


def instrs(zipf):
    out=[]
    for name in zipf.namelist():
        if name.startswith('word/') and name.endswith('.xml'):
            try: root=etree.fromstring(zipf.read(name))
            except Exception: continue
            out += [''.join(x.itertext()).strip() for x in root.xpath('//w:instrText',namespaces=NS)]
    return out


def expected_presence(ps, dropped):
    texts=[ptext(p) for p in ps]
    for keep in (KEEP_2002,KEEP_NECCAR,KEEP_NECAH_2000,KEEP_NECAH_1999):
        if texts.count(keep)!=1:
            raise RuntimeError(f'kept bibliography record count !=1: {keep[:70]!r} -> {texts.count(keep)}')
    for drop in (DROP_2006,DROP_ASFAR):
        want=0 if dropped else 1
        if texts.count(drop)!=want:
            raise RuntimeError(f'dropped bibliography record count !={want}: {drop[:70]!r} -> {texts.count(drop)}')


def satisfied(d):
    ps=d.xpath('.//w:body/w:p',namespaces=NS)
    if len(ps)!=674:
        return False
    try:
        expected_presence(ps,True)
    except Exception:
        return False
    return True


def apply(src,out):
    with ZipFile(src,'r') as zin:
        original={i.filename:zin.read(i.filename) for i in zin.infolist()}
        d=etree.fromstring(original['word/document.xml'])
        ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if satisfied(d):
            shutil.copyfile(src,out)
            validate(src,out,expect_change=False)
            print('F4-115\tALREADY_SATISFIED')
            return
        if len(ps)!=676:
            raise RuntimeError(f'input body paragraph count {len(ps)} != 676')
        expected_presence(ps,False)

        targets=[]
        for needle in (DROP_2006,DROP_ASFAR):
            hits=[(i,p) for i,p in enumerate(ps) if ptext(p)==needle]
            if len(hits)!=1:
                raise RuntimeError(f'target count {len(hits)} !=1 for {needle[:80]!r}')
            targets.append(hits[0])
        target_indices=[i for i,_ in targets]
        if target_indices!=[548,557]:
            raise RuntimeError(f'current target indices changed unexpectedly: {target_indices}')
        for i,p in targets:
            if p.xpath('.//w:instrText|.//w:fldChar',namespaces=NS):
                raise RuntimeError(f'target P{i} unexpectedly contains field nodes')
            if p.xpath('.//w:hyperlink',namespaces=NS):
                raise RuntimeError(f'target P{i} unexpectedly contains hyperlink node')

        body=d.find('.//w:body',namespaces=NS)
        for _,p in targets:
            body.remove(p)

        out_ps=d.xpath('.//w:body/w:p',namespaces=NS)
        if len(out_ps)!=674:
            raise RuntimeError(f'output body paragraph count {len(out_ps)} !=674')
        expected_presence(out_ps,True)

        xml=etree.tostring(d,xml_declaration=True,encoding='UTF-8',standalone='yes')
        with ZipFile(out,'w') as zout:
            for info in zin.infolist():
                zout.writestr(info,xml if info.filename=='word/document.xml' else original[info.filename])

    validate(src,out,expect_change=True)
    print('F4-115\tAPPLIED\tREMOVED_ORIGINAL_P548_AND_P557')
    print('REMOVED\t'+DROP_2006)
    print('REMOVED\t'+DROP_ASFAR)
    print('PRESERVED\t'+KEEP_2002)
    print('PRESERVED\t'+KEEP_NECCAR)
    print('PRESERVED\t'+KEEP_NECAH_2000)
    print('PRESERVED\t'+KEEP_NECAH_1999)


def validate(src,out,expect_change):
    with ZipFile(src) as za, ZipFile(out) as zb:
        if za.namelist()!=zb.namelist(): raise RuntimeError('ZIP member/order changed')
        if zb.testzip() is not None: raise RuntimeError('ZIP CRC failure')
        for name in za.namelist():
            if name!='word/document.xml' and za.read(name)!=zb.read(name):
                raise RuntimeError(f'unexpected package change: {name}')
            if name.endswith('.xml') or name.endswith('.rels'):
                etree.fromstring(zb.read(name))

        da=etree.fromstring(za.read('word/document.xml')); db=etree.fromstring(zb.read('word/document.xml'))
        pa=da.xpath('.//w:body/w:p',namespaces=NS); pb=db.xpath('.//w:body/w:p',namespaces=NS)

        if expect_change:
            if len(pa)!=676 or len(pb)!=674: raise RuntimeError(f'body count unexpected {len(pa)}->{len(pb)}')
            expected=[c14n(p) for i,p in enumerate(pa) if i not in (548,557)]
            actual=[c14n(p) for p in pb]
            if actual!=expected: raise RuntimeError('output paragraph sequence != input minus original P548/P557')
        else:
            if len(pa)!=674 or len(pb)!=674: raise RuntimeError(f'idempotent body count unexpected {len(pa)}->{len(pb)}')
            if [c14n(p) for p in pb] != [c14n(p) for p in pa]: raise RuntimeError('idempotent document paragraph sequence changed')

        expected_presence(pb,True)

        ia=instrs(za); ib=instrs(zb)
        if ia!=ib or len(ib)!=520: raise RuntimeError('field instruction inventory changed')
        addin=sum(1 for x in ib if 'ADDIN ' in x)
        item=sum(1 for x in ib if 'ZOTERO_ITEM' in x)
        bibl=sum(1 for x in ib if 'ZOTERO_BIBL' in x)
        if (addin,item,bibl)!=(466,465,1): raise RuntimeError(f'Zotero/ADDIN fields changed {(addin,item,bibl)}')

        ra=da.xpath('//w:footnoteReference/@w:id',namespaces=NS); rb=db.xpath('//w:footnoteReference/@w:id',namespaces=NS)
        if ra!=rb or len(rb)!=469 or len(set(rb))!=469: raise RuntimeError('footnote reference identity/order changed')
        if da.xpath('//w:bookmarkStart/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkStart/@w:id',namespaces=NS): raise RuntimeError('bookmark starts changed')
        if da.xpath('//w:bookmarkEnd/@w:id',namespaces=NS)!=db.xpath('//w:bookmarkEnd/@w:id',namespaces=NS): raise RuntimeError('bookmark ends changed')
        if len(db.xpath('//w:bookmarkStart',namespaces=NS))!=53 or len(db.xpath('//w:bookmarkEnd',namespaces=NS))!=53: raise RuntimeError('bookmark count changed')
        if len(da.xpath('//w:hyperlink',namespaces=NS))!=len(db.xpath('//w:hyperlink',namespaces=NS))!=52: raise RuntimeError('hyperlink count changed')
        if len(da.xpath('//w:rtl',namespaces=NS))!=len(db.xpath('//w:rtl',namespaces=NS)): raise RuntimeError('RTL inventory changed')

if __name__=='__main__':
    apply(Path(sys.argv[1]),Path(sys.argv[2]))
