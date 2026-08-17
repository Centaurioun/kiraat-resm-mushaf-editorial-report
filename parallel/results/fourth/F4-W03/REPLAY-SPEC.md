# REPLAY SPEC — F4-W03

## Disposition

This replay is intentionally **dependency-gated and non-mutating** in the current worker run.

Before any F4-063–069 mutation, the replay consumer MUST reconstruct the logical F4-047 DOCX from the canonical source and accepted replay pipeline and independently verify:

`SHA256 == 6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

If the hash differs or cannot be computed, stop with `DEPENDENCY_BLOCKED` and make no edit.

## Deterministic target anchors recorded from the authoritative report/current extraction

The following anchors were inspected only to establish future fail-closed target identity. They were **not applied** in this run.

- F4-063: `Resm-i Osmânî'nin en dikkat çekici özelliklerinden biri, bazı kelimelerde birden fazla sahih kırâate yer verebilecek şekilde kurulmuş olmasıdır.` Also remove the nearby `daha önce de zikretmiştik`-type meta-reference only if uniquely located in the same 3.1 opening block.
- F4-064: the 3.1 explanatory block defining `gerçek/doğrudan uygunluk` versus `ihtimale dayalı uygunluk (muvâfakatu'r-resm)`; preserve the distinction and explicitly keep authenticity grounded in rivâyet rather than graphical possibility.
- F4-065: `Bu kelimeler otuz üç adet olup, Osmânî mushaflara, her bir mushafta sabit olan kırâat vecihleri esas alınarak dağıtılmıştır.` Treat the following long list as heterogeneous. **Do not mechanically reclassify, delete, reorder, or strip citations.** A future replay must establish item-by-item structural/citation safety before mutation.
- F4-066: `Kırâatin temel şartlarından biri, resme en azından ihtimal yoluyla uygun olmasıdır; aksi takdirde o kırâat şâz olur.` A safe replay must not reduce shādh status to rasm alone.
- F4-067: 3.2 passage containing `Bu yaklaşıma göre Kur'an'ın "yedi harf" üzere indirilmiş olması o günkü toplumun kullandığı farklı lehçe ve söyleyiş biçimlerine belirli bir kolaylık tanındığını gösterir.` Present lehçe explanation as one classical view, not total identification; keep transmission through telakki/rivâyet explicit.
- F4-068: 3.3 passage ending `harekenin niteliğini, sesin dolgunluğunu ve okuyuş farkını da resm içinde işaretleyebildiğini gösterir.` Separate early graphic possibility from later functional/semantic inference.
- F4-069: 3.3→3.4 transition containing `Bu ara yapı resm-i Osmânî'nin en dikkat çekici özelliklerinden kabul edilir.` Future edit must explicitly mark the evidentiary-level transition from historical/orthographic description to later mana/hikmet interpretation.

## Fail-closed targeting rules

For each item:

1. Search exact/semantic anchor plus local section heading/context in the reconstructed F4-047 DOCX.
2. `0` eligible targets → stop that item.
3. `1` eligible target → may proceed after citation mapping.
4. `2+` plausible targets → stop that item.
5. No fuzzy best-match application.
6. Preserve protected fields, footnotes, Zotero ADDINs, bookmarks, hyperlinks, sections, styles and Arabic/RTL runs.

## Required future post-edit validation

A future unblocked execution must compare pre/post genuine footnote IDs/references, orphan/dangling/duplicate state, Word fields, Zotero item/bibliography fields, bookmarks, hyperlinks, relevant RTL/Arabic runs, comments/revisions, section count, ZIP/XML integrity, protected OOXML parts, idempotent replay behavior, and bounded visual rendering around affected pages.

No mutation instructions beyond these dependency-gated anchors are claimed validated by this worker run.