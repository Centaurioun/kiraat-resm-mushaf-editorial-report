# AGENTS.md

## Project purpose

This repository supports a staged academic editorial workflow for the Turkish book project **“Kırâatlerin Rivayetinde Resm-i Mushaf’ın Etkisi.”** The goal is to produce a fourth, author-facing revision report that is simpler and more directly actionable than the three earlier reports.

## Authoritative sources

Treat the following as the source hierarchy:

1. `source/manuscript/current/redaktorden_gelen.docx` — canonical current manuscript.
2. `source/manuscript/current/redaktorden_gelen_extracted.md` — searchable extraction of the same manuscript.
3. `source/notes/duzeltilecekler.docx` — mandatory editorial notes/checklist.
4. `source/reports/` — earlier audit reports used to discover and cross-check issues.
5. `source/manuscript/archive/` — historical comparison only; never prefer it over the current manuscript.

If the current DOCX and extracted Markdown appear to differ materially, flag the discrepancy instead of guessing.

## Academic constraints

- Do not use external web sources unless the user explicitly authorizes them.
- Do not invent names, dates, works, sources, readings, textual variants, page numbers, bibliographic details, or historical claims.
- Preserve the project’s central distinction: qirāʾāt are transmitted primarily through **telakki, müşâfehe, edâ, isnad and rivâyet**; the Uthmanic rasm is not an independent generator/source of readings, but a complementary written compatibility/acceptance framework.
- Do not conflate qirāʾat, rivâyet, tarîk, vecih, rasm, resm-i mushaf, resm-i Osmânî, mushaf, isnad validity, and rasm compatibility.
- Distinguish historical report, classical interpretation, modern assessment, and authorial inference.
- Use cautious Turkish for disputed historical matters.
- Do not turn orthographic features into hidden meanings, theological signs, or miraculous claims unless the project sources explicitly support that attribution.

## Final report audience

The final report is for an author with limited technical-computer knowledge. Therefore:

- Prefer plain Turkish editorial language.
- Avoid internal codes, Word/XML jargon, Heading/RTL/run/bidi/OOXML/Zotero-field terminology, and technical workflow language.
- Each actionable issue should ideally answer: **Where is it? What is currently written? What is wrong? What exactly should replace it?**
- Do not merely say “merge,” “shorten,” “move,” “soften,” or “add a transition.” Perform the editorial operation and provide the proposed final text whenever the project sources permit it.
- If a detail cannot be safely resolved from the project files, remove or soften the unsupported detail rather than inventing a correction.

## Six-stage workflow

Execute `prompts/stage-01.md` through `prompts/stage-06.md` in order. Do not skip ahead.

Write stage outputs to:

- `work/stage-01-final-inventory.md`
- `work/stage-02-verified-inventory.md`
- `work/stage-03-direct-revisions.md`
- `work/stage-04-crosscutting-revisions.md`
- `work/stage-05-final-content.md`
- `final/fourth-report.md`

## Git safety and provenance

- `main` is the accepted baseline/source snapshot. Do not rewrite or alter source documents on `main` after the initial repository setup unless explicitly authorized.
- Perform editorial work on `editorial/fourth-report`.
- Preserve the source files unchanged. Stage outputs and report drafts are the editable artifacts.
- Commit each completed stage separately with a clear message.
- Do not force-push, rewrite history, delete branches, or modify source documents without explicit authorization.
- Never commit credentials, tokens, local secrets, temporary Word lock files, render caches, or unrelated personal data.

## Completion standard

Before claiming a stage is complete, verify that its required output exists, is internally consistent with previous stages, and does not silently introduce unsupported information. The final author-facing report must be self-contained and should not require the author to consult the earlier three reports.
