# Project Brief

## Deliverable

Create a **fourth, author-facing academic revision report** for *Kırâatlerin Rivayetinde Resm-i Mushaf’ın Etkisi*.

The earlier reports are comprehensive but too technical and repetitive for the intended author. The fourth report must transform those findings into a practical correction guide.

The controlled editorial workflow now has **seven stages**. Stages 1-6 produce and audit Markdown working artifacts. Stage 7 creates the final author-facing Markdown report at:

`final/fourth-report.md`

Only after the user reviews and approves that Markdown will the same content be converted into DOCX in a separate later step.

## User-facing correction unit

The preferred unit is:

- **Bölüm/Başlık**
- **Sayfa**
- **Bulmak için** (paragraph opening)
- **Mevcut metin**
- **Sorun**
- **Önerilen düzeltme**

When two or more passages must be merged, moved or jointly rewritten, show the relevant existing passages and provide the complete replacement text.

## Exclude from the author report

- technical Word/XML diagnostics
- Heading/TOC/PAGEREF notes
- RTL/bidi/run terminology
- Zotero field diagnostics
- report-history/status matrices
- “completed / partially completed” bookkeeping
- giant red-text inventories
- raw technical metrics that do not tell the author what to change
- internal stage codes and coverage ledgers

## Keep where actionable

- scientific/conceptual corrections
- misleading or over-strong formulations
- paragraph and section transitions
- unnecessary mini-conclusions and repeated summaries
- repeated negative-definition patterns (`değil/değildir`) where a better sentence is warranted
- `Sonuç olarak` and similar mechanical closure patterns where context warrants revision
- author/publisher notes accidentally left in the manuscript
- clear language/tashih errors
- resolvable bibliography errors

## Source-safety rule

Do not invent missing names, dates, works, readings, variants, page numbers, DOI values, or bibliographic details. When the project sources do not safely resolve a detail, remove or soften the unsupported detail when possible; otherwise mark the source limit plainly.

## Final formats

Primary reviewed artifact:

`final/fourth-report.md`

Later DOCX target after Markdown approval:

`Kiraatlerin_Rivayetinde_Resm-i_Mushafin_Etkisi_Yazar_Icin_Nihai_Duzeltme_ve_Redaksiyon_Raporu.docx`
