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

If the current DOCX and extracted Markdown appear to differ materially, flag the discrepancy instead of guessing. Use the DOCX as authoritative where formatting, footnotes, Arabic layout, red editorial markings, or pagination matters.

## Academic constraints

- Do not use external web sources unless the user explicitly authorizes them.
- Do not invent names, dates, works, sources, readings, textual variants, page numbers, bibliographic details, or historical claims.
- Preserve the project’s central distinction: qirāʾāt are transmitted primarily through **telakki, müşâfehe, edâ, isnad and rivâyet**; the Uthmanic rasm is not an independent generator/source of readings, but a complementary written compatibility/acceptance framework.
- Do not conflate qirāʾat, rivâyet, tarîk, vecih, rasm, resm-i mushaf, resm-i Osmânî, mushaf, isnad validity, and rasm compatibility.
- Distinguish historical report, classical interpretation, modern assessment, and authorial inference.
- Use cautious Turkish for disputed historical matters.
- Do not turn orthographic features into hidden meanings, theological signs, or miraculous claims unless the project sources explicitly support that attribution.
- Do not create new citations or move an existing footnote onto a materially different claim without source support.
- Do not rewrite direct quotations merely for stylistic reasons.

## Final report audience

The final report is for an author with limited technical-computer knowledge. Therefore:

- Prefer plain Turkish editorial language.
- Avoid internal codes, Word/XML jargon, Heading/RTL/run/bidi/OOXML/Zotero-field terminology, and technical workflow language in author-facing content.
- Each actionable issue should ideally answer: **Where is it? What is currently written? What is wrong? What exactly should replace it?**
- Do not merely say “merge,” “shorten,” “move,” “soften,” or “add a transition.” Perform the editorial operation and provide the proposed final text whenever the project sources permit it.
- If a detail cannot be safely resolved from the project files, remove or soften the unsupported detail rather than inventing a correction.
- Do not include items that are already resolved or that require no author action.

## Seven-stage workflow

Execute `prompts/stage-01.md` through `prompts/stage-07.md` **in order**. Do not skip ahead. A later stage may read earlier outputs but must not silently rewrite them.

Stage outputs are:

- Stage 1 → `work/stage-01-final-inventory.md`
- Stage 2 → `work/stage-02-verified-inventory.md`
- Stage 3 → `work/stage-03-direct-revisions.md`
- Stage 4 → `work/stage-04-crosscutting-revisions.md`
- Stage 5 → `work/stage-05-final-content.md`
- Stage 6 → `work/stage-06-final-audited-content.md`
- Stage 7 → `final/fourth-report.md`

Stages 1-6 are controlled working artifacts. Stage 7 creates the final author-facing Markdown report. **DOCX generation is a separate later step and is not part of these seven stages.**

## Stage isolation

- Each stage writes only to its designated output file unless the user explicitly authorizes otherwise.
- Do not modify `source/` during editorial analysis.
- Do not edit the prompt files while executing a stage.
- Do not overwrite earlier stage outputs; use them as evidence and dependencies.
- If a prerequisite output is missing, still a placeholder, or internally incomplete, stop rather than improvising.
- If a later stage discovers an earlier-stage omission, record and repair it in the current stage output while preserving the earlier output as provenance.

## Git safety and provenance

- `main` is the accepted baseline/source snapshot. Do not rewrite or alter source documents on `main` after the initial repository setup unless explicitly authorized.
- Perform editorial work on `editorial/fourth-report`.
- Preserve the source files unchanged. Stage outputs and report drafts are the editable artifacts.
- Commit each completed stage separately with a clear message.
- When refining prompts or repository scaffolding before Stage 1, commit those changes on `editorial/fourth-report`, never on `main`.
- Do not force-push, rewrite history, delete branches, or modify source documents without explicit authorization.
- Never commit credentials, tokens, local secrets, temporary Word lock files, render caches, or unrelated personal data.

## Completion standard

Before claiming a stage is complete, verify that:

- its required output exists and is no longer a placeholder;
- prerequisite outputs were read;
- the output is internally consistent with previous stages;
- no unsupported information was silently introduced;
- counts claimed as exact are actually derivable from the reviewed material;
- source-limited items are marked rather than guessed;
- the stage stops at its defined boundary.

Before Stage 7, Stage 6 must reconcile coverage and confirm whether any serious blocker remains. The final author-facing Markdown report must be self-contained and should not require the author to consult the earlier three reports or the internal stage files.
