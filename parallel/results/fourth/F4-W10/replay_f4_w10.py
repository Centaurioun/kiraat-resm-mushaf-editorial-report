#!/usr/bin/env python3
"""Deterministic replay for F4-W10 (F4-112, F4-114, F4-115, F4-116).

Edits only genuine footnotes 32/41/105 and the specifically-authorized bibliography
records. The replay is fail-closed, idempotent, preserves Zotero field instructions,
and emits a validation report after writing the output DOCX.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from zipfile import ZipFile

from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"w": W, "r": R, "pr": PKG_REL}
F4_047_SHA256 = "6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7"

FN_STALE = {
    "32": "(bu dipnot daha önce geçmiş midir.yoksa kitabın ilk adı bu şekilde mi) buna bakılması.",
    "41": "(bu eserin müellifi meçhuldür literatürde bu şekilde geçiyor.",
    "105": "(bu eser daha önce tam adıyla geçmişmiydi)",
}
KAH_OLD = "https://doi.org/http://doi.org/1051702/esoguifd.791085"
MAS_OLD = "https://doi.org/https://doi.org/10.56361/usul.173700"
MAS_NEW = "https://doi.org/10.56361/usul.173700"
REMOVE_ENTRIES = {
    "ibn_abi_dawud_2006": "İbn Ebû Dâvud, Ebû Bekir Abdullah b. Süleymân. Kitâbu'l-mesâhif. thk. Selîm b. Îde'l-Hilâlî el-Eserî. Amman: Ğarâs, 2006.",
    "ibn_qutayba_asfar_1999": "İbn Kuteybe, Ebû Muhammed Abdullah b. Muslim. Te'vîlu muhtelifi'l-hadîs. thk. Muhammed Muhyiddîn el-Asfar. Beyrut: el-Mektebetü'l-İslâmî, 1999.",
}
PRESERVE_ANCHORS = {
    "ibn_abi_dawud_2002": "Muhibbüddîn Abdussubhân Vâiz. 2 Cilt. Beyrut: Dâru'l-Beşâiri'l-İslâmiyye, 2002.",
    "muhtasar_2000": "Ahmed b. Muhammed b. Muammer Şarşâl. 5 Cilt. Riyad: Mecmeu'l-Melik Fehd",
    "muhtasar_1999": "Ahmed b. Ahmed Muammer Şarşâl. 2 Cilt. Medine: Mecmau'l-Melik Fahd",
    "ibn_qutayba_zuhri": "thk. Muhammed Zuhrî en-Neccâr. Mektebetü'l-Küllîyât el-Ezheriyye, ts.",
    "abu_shama_1975": "thk. Tayyar Altıkulaç. 2 Cilt. Beyrut: Dâr Sadr, 1975.",
    "abu_shama_1993": "thk. Velîd Müsâid et-Tabatabâî. Kuveyt: Mektebetü'l-İmâm ez-Zehebî, 1993.",
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()

def text(el) -> str:
    return "".join(el.xpath(".//w:t/text()", namespaces=NS))

def instr_texts(doc) -> list[str]:
    return [x or "" for x in doc.xpath(".//w:instrText/text()", namespaces=NS)]

def structural_signature(el):
    return tuple((node.tag, tuple(sorted(node.attrib.items()))) for node in el.iter())

def replace_span(el, old: str, new: str) -> str:
    nodes = el.xpath(".//w:t", namespaces=NS)
    vals = [n.text or "" for n in nodes]
    full = "".join(vals)
    hits = [m.start() for m in re.finditer(re.escape(old), full)]
    if not hits:
        if new and new in full:
            return "ALREADY_SATISFIED"
        return "NOT_FOUND"
    if len(hits) != 1:
        raise RuntimeError(f"non-unique span ({len(hits)} hits): {old!r}")
    pos, end = hits[0], hits[0] + len(old)
    starts, cursor = [], 0
    for v in vals:
        starts.append(cursor); cursor += len(v)
    fi = next(i for i, (st, v) in enumerate(zip(starts, vals)) if pos < st + len(v))
    li = next(i for i, (st, v) in enumerate(zip(starts, vals)) if end <= st + len(v))
    prefix, suffix = vals[fi][:pos-starts[fi]], vals[li][end-starts[li]:]
    nodes[fi].text = prefix + new + (suffix if fi == li else "")
    if fi != li:
        for j in range(fi + 1, li): nodes[j].text = ""
        nodes[li].text = suffix
    return "APPLIED"

def unique_paragraph_containing(doc, anchor: str, allow_absent: bool = False):
    hits = [p for p in doc.xpath(".//w:p", namespaces=NS) if norm(anchor) in norm(text(p))]
    if len(hits) == 1: return hits[0]
    if len(hits) == 0 and allow_absent: return None
    raise RuntimeError(f"paragraph anchor {anchor!r}: {len(hits)} hits")

def safe_to_remove_paragraph(p) -> None:
    banned = [".//w:instrText", ".//w:fldChar", ".//w:footnoteReference", ".//w:bookmarkStart", ".//w:bookmarkEnd", ".//w:commentRangeStart", ".//w:commentRangeEnd", ".//w:commentReference", ".//w:sectPr", ".//w:drawing", ".//w:object"]
    found = {q: len(p.xpath(q, namespaces=NS)) for q in banned if p.xpath(q, namespaces=NS)}
    if found: raise RuntimeError(f"unsafe bibliography paragraph: {found}")

def hyperlink_rids(el) -> set[str]:
    return set(el.xpath(".//w:hyperlink/@r:id", namespaces=NS))

def cleanup_unused_relationships(doc, rels, candidate_rids: set[str]) -> list[str]:
    removed, used = [], set(doc.xpath(".//w:hyperlink/@r:id", namespaces=NS))
    for rid in candidate_rids:
        if rid in used: continue
        hits = rels.xpath(f"./pr:Relationship[@Id='{rid}']", namespaces=NS)
        if len(hits) == 1: rels.remove(hits[0]); removed.append(rid)
        elif len(hits) > 1: raise RuntimeError(f"duplicate relationship id {rid}")
    return removed

def update_link_target_for_span(node, rels, old: str, new: str) -> list[str]:
    cur = node
    while cur is not None and cur.tag != f"{{{W}}}hyperlink": cur = cur.getparent()
    if cur is None: return []
    rid = cur.get(f"{{{R}}}id")
    if not rid: return []
    hits = rels.xpath(f"./pr:Relationship[@Id='{rid}']", namespaces=NS)
    if len(hits) != 1: raise RuntimeError(f"hyperlink relationship {rid}: {len(hits)} hits")
    rel, target = hits[0], hits[0].get("Target", "")
    if target == old: rel.set("Target", new); return [rid]
    if target == new: return []
    if old in target: rel.set("Target", target.replace(old, new)); return [rid]
    raise RuntimeError(f"unexpected hyperlink target for {rid}: {target!r}")

def snapshot(doc, foot, rels) -> dict:
    instr = instr_texts(doc)
    return {
        "footnote_ids": foot.xpath("./w:footnote/@w:id", namespaces=NS),
        "footnote_refs": doc.xpath(".//w:footnoteReference/@w:id", namespaces=NS),
        "fldChar": len(doc.xpath(".//w:fldChar", namespaces=NS)),
        "instrText": instr,
        "zotero_item_markers": sum("ZOTERO_ITEM" in s for s in instr),
        "zotero_bibl_markers": sum("ZOTERO_BIBL" in s for s in instr),
        "bookmarks_start": doc.xpath(".//w:bookmarkStart/@w:id", namespaces=NS),
        "bookmarks_end": doc.xpath(".//w:bookmarkEnd/@w:id", namespaces=NS),
        "hyperlink_rids": doc.xpath(".//w:hyperlink/@r:id", namespaces=NS),
        "rtl": len(doc.xpath(".//w:rtl", namespaces=NS)),
        "sections": len(doc.xpath(".//w:sectPr", namespaces=NS)),
        "comments": len(doc.xpath(".//w:commentRangeStart|.//w:commentRangeEnd|.//w:commentReference", namespaces=NS)),
        "revisions": len(doc.xpath(".//w:ins|.//w:del|.//w:moveFrom|.//w:moveTo", namespaces=NS)),
        "relationships": [(x.get("Id"), x.get("Type"), x.get("Target"), x.get("TargetMode")) for x in rels],
    }

def apply(src: Path, out: Path, require_f4_047_sha: bool = False) -> dict:
    input_sha = sha256(src)
    if require_f4_047_sha and input_sha != F4_047_SHA256:
        raise RuntimeError(f"F4-047 SHA mismatch: got {input_sha}, expected {F4_047_SHA256}")
    with ZipFile(src) as zin:
        names = set(zin.namelist()); required = {"word/document.xml", "word/footnotes.xml", "word/_rels/document.xml.rels"}
        if not required <= names: raise RuntimeError(f"missing OOXML parts: {sorted(required - names)}")
        original = {n: zin.read(n) for n in zin.namelist()}
        doc = etree.fromstring(original["word/document.xml"])
        foot = etree.fromstring(original["word/footnotes.xml"])
        rels = etree.fromstring(original["word/_rels/document.xml.rels"])
        before = snapshot(doc, foot, rels)
        pre_struct = {fid: structural_signature(foot.xpath(f"./w:footnote[@w:id='{fid}']", namespaces=NS)[0]) for fid in FN_STALE}
        results = {"F4-112": [], "F4-114": [], "F4-115": [], "F4-116": []}; changed_parts = set(); rel_changes = []
        for fid, stale in FN_STALE.items():
            hits = foot.xpath(f"./w:footnote[@w:id='{fid}']", namespaces=NS)
            if len(hits) != 1: raise RuntimeError(f"genuine footnote id {fid}: {len(hits)} hits")
            fn, full = hits[0], text(hits[0])
            if stale in full:
                candidate = (" " + stale) if (" " + stale) in full else stale
                status = replace_span(fn, candidate, ""); changed_parts.add("word/footnotes.xml")
            else: status = "ALREADY_SATISFIED"
            if stale in text(fn): raise RuntimeError(f"F4-112 stale note remains in footnote {fid}")
            if structural_signature(fn) != pre_struct[fid]: raise RuntimeError(f"F4-112 structural drift in footnote {fid}")
            results["F4-112"].append({"footnote_id": int(fid), "status": status})
        joined_instr = "\n".join(instr_texts(doc))
        if KAH_OLD in joined_instr or MAS_OLD in joined_instr: raise RuntimeError("target DOI appears inside protected Zotero/Word field instructions")
        p = unique_paragraph_containing(doc, KAH_OLD, allow_absent=True); kah_rids = set()
        if p is None: results["F4-114"].append({"target": "Kahraman DOI", "status": "ALREADY_SATISFIED"})
        else:
            kah_rids = hyperlink_rids(p)
            if norm(text(p)) == norm(KAH_OLD): safe_to_remove_paragraph(p); p.getparent().remove(p)
            elif replace_span(p, KAH_OLD, "") != "APPLIED": raise RuntimeError("Kahraman DOI target disappeared during replay")
            removed_rel = cleanup_unused_relationships(doc, rels, kah_rids)
            if removed_rel: rel_changes += [{"rid": r, "action": "remove_unused_kahraman_hyperlink"} for r in removed_rel]; changed_parts.add("word/_rels/document.xml.rels")
            changed_parts.add("word/document.xml"); results["F4-114"].append({"target": "Kahraman DOI", "status": "APPLIED", "replacement": None})
        p_old = unique_paragraph_containing(doc, MAS_OLD, allow_absent=True)
        if p_old is not None:
            text_nodes = p_old.xpath(".//w:t", namespaces=NS); carrier = next((n for n in text_nodes if MAS_OLD in (n.text or "")), None)
            if replace_span(p_old, MAS_OLD, MAS_NEW) != "APPLIED": raise RuntimeError("Maşalı DOI replacement failed")
            if carrier is not None:
                for rid in update_link_target_for_span(carrier, rels, MAS_OLD, MAS_NEW): rel_changes.append({"rid": rid, "action": "update_masali_hyperlink_target"}); changed_parts.add("word/_rels/document.xml.rels")
            changed_parts.add("word/document.xml"); results["F4-114"].append({"target": "Maşalı DOI", "status": "APPLIED", "replacement": MAS_NEW})
        else:
            if unique_paragraph_containing(doc, MAS_NEW, allow_absent=True) is None: raise RuntimeError("neither malformed nor corrected Maşalı DOI found")
            results["F4-114"].append({"target": "Maşalı DOI", "status": "ALREADY_SATISFIED", "replacement": MAS_NEW})
        for key, entry in REMOVE_ENTRIES.items():
            p = unique_paragraph_containing(doc, entry, allow_absent=True)
            if p is None: results["F4-115"].append({"entry": key, "status": "ALREADY_SATISFIED", "decision": "REMOVE"}); continue
            safe_to_remove_paragraph(p); p.getparent().remove(p); changed_parts.add("word/document.xml")
            results["F4-115"].append({"entry": key, "status": "APPLIED", "decision": "REMOVE"})
        for key, anchor in PRESERVE_ANCHORS.items():
            if unique_paragraph_containing(doc, anchor, allow_absent=True) is None: raise RuntimeError(f"required preserved bibliography entry missing: {key}")
            bucket = "F4-116" if key.startswith("abu_shama_") else "F4-115"
            results[bucket].append({"entry": key, "status": "VERIFIED_PRESENT", "decision": "KEEP"})
        fn86 = foot.xpath("./w:footnote[@w:id='86']", namespaces=NS); fn131 = foot.xpath("./w:footnote[@w:id='131']", namespaces=NS)
        if len(fn86) != 1 or "1993" not in text(fn86[0]) or "212" not in text(fn86[0]): raise RuntimeError("F4-116 expected current full 1993 citation not found in footnote 86")
        if len(fn131) != 1 or "1/173" not in text(fn131[0]) or "Murşidu" not in text(fn131[0]): raise RuntimeError("F4-116 expected current short 1/173 citation not found in footnote 131")
        results["F4-116"] += [{"footnote_id": 86, "status": "VERIFIED_1993_FULL_CITATION"}, {"footnote_id": 131, "status": "VERIFIED_1975_SHORT_CITATION_ANCHOR"}]
        after = snapshot(doc, foot, rels)
        for key in ["footnote_ids", "footnote_refs", "fldChar", "instrText", "zotero_item_markers", "zotero_bibl_markers", "bookmarks_start", "bookmarks_end", "rtl", "sections", "comments", "revisions"]:
            if before[key] != after[key]: raise RuntimeError(f"protected invariant changed: {key}")
        if require_f4_047_sha:
            expected = {"footnote_ids":469,"footnote_refs":469,"fldChar":520,"zotero_item_markers":465,"zotero_bibl_markers":1,"rtl":365,"sections":10}
            actual = {"footnote_ids":len(after["footnote_ids"]),"footnote_refs":len(after["footnote_refs"]),"fldChar":after["fldChar"],"zotero_item_markers":after["zotero_item_markers"],"zotero_bibl_markers":after["zotero_bibl_markers"],"rtl":after["rtl"],"sections":after["sections"]}
            if actual != expected: raise RuntimeError(f"F4-047 inventory mismatch: {actual} != {expected}")
        replacements = {}
        if "word/document.xml" in changed_parts: replacements["word/document.xml"] = etree.tostring(doc, xml_declaration=True, encoding="UTF-8", standalone="yes")
        if "word/footnotes.xml" in changed_parts: replacements["word/footnotes.xml"] = etree.tostring(foot, xml_declaration=True, encoding="UTF-8", standalone="yes")
        if "word/_rels/document.xml.rels" in changed_parts: replacements["word/_rels/document.xml.rels"] = etree.tostring(rels, xml_declaration=True, encoding="UTF-8", standalone="yes")
        if not replacements: shutil.copyfile(src, out)
        else:
            with ZipFile(out, "w") as zout:
                for info in zin.infolist(): zout.writestr(info, replacements.get(info.filename, original[info.filename]))
    with ZipFile(src) as za, ZipFile(out) as zb:
        if set(za.namelist()) != set(zb.namelist()): raise RuntimeError("ZIP member set changed")
        allowed = {"word/document.xml", "word/footnotes.xml", "word/_rels/document.xml.rels"}
        protected_diffs = [n for n in za.namelist() if n not in allowed and za.read(n) != zb.read(n)]
        if protected_diffs: raise RuntimeError(f"unexpected protected OOXML changes: {protected_diffs}")
        for n in zb.namelist():
            if n.endswith(".xml") or n.endswith(".rels"): etree.fromstring(zb.read(n))
    return {"task":"F4-W10","input_sha256":input_sha,"output_sha256":sha256(out),"required_f4_047_sha_checked":require_f4_047_sha,"items":results,"changed_parts":sorted(changed_parts),"relationship_changes":rel_changes,"pre":{k:v for k,v in before.items() if k not in {"instrText","relationships"}},"post":{k:v for k,v in after.items() if k not in {"instrText","relationships"}},"validation":"PASS"}

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("input_docx", type=Path); ap.add_argument("output_docx", type=Path)
    ap.add_argument("--require-f4-047-sha", action="store_true", help="Require exact frozen F4-047 input SHA for worker proof replay.")
    ap.add_argument("--report-json", type=Path); args = ap.parse_args()
    report = apply(args.input_docx, args.output_docx, args.require_f4_047_sha); payload = json.dumps(report, ensure_ascii=False, indent=2); print(payload)
    if args.report_json: args.report_json.write_text(payload + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__": raise SystemExit(main())
