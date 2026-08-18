# F5-002 — corrected actual item — APPLIED / PASS

This file supersedes the earlier misbound F5-002 no-op adjudication. See `work/F5-002-CORRECTION-NOTE.md` for the audit trail.

## Locked Fifth Report item

The actual F5-002 target is the Giriş sentence:

`Bu sorular birbirinden bağımsız değildir.`

The Fifth Report asks for the relation among the research questions to be expressed positively.

## Fourth-precedence adjudication

The broader Fifth proposed paragraph would also replace the following accepted Fourth-scientific sentences with a stronger causal formulation. That broader replacement is not needed and risks weakening the accepted distinction between historical process, later acceptance criteria, and the transmission logic of qiraat.

Therefore the correction is deliberately narrower:

`Bu sorular birbirinden bağımsız değildir.`

→

`Araştırma soruları birbirine bağlıdır.`

The following accepted Fourth wording is preserved unchanged:

- `Osmânî mushafların ortak başvuru metni hâline gelme süreci, resm-i Osmânî’nin kabul ölçüsü hâline gelişinden ayrı anlaşılamaz.`
- `Kırâatin rivâyet mantığı da yalnız resm üzerinden değerlendirilemez.`

This resolves the Fifth stylistic defect without introducing stronger causal language.

## Deterministic application

Replay script: `work/apply_f5_002.py`

Input: durable F5-001 / globally validated Fourth binary.

Output: `artifacts/checkpoints/manuscript-working-f5-002.docx`

Authoritative candidate SHA is stored in:

`work/runtime/F5-002-ACTUAL-R2-SHA256.txt`

Acceptance checks:

- candidate SHA was independently recomputed from the GitHub branch copy and matched the runtime SHA evidence exactly;
- first replay: F5-002 **APPLIED** at P22;
- only P22 differs from the durable input;
- P22 OOXML element/run structure is preserved;
- second replay: **ALREADY_SATISFIED**;
- deterministic second output is byte-identical;
- body paragraph count remains 674;
- all non-`word/document.xml` package parts remain byte-identical to the durable F5-001 input under the application validator;
- Word field instruction sequence remains 520; ADDIN 466; Zotero ITEM 465; Zotero bibliography 1;
- genuine body footnote references remain 469 with identical identity/order;
- bookmarks remain 53/53; hyperlinks 52; RTL inventory unchanged.

## Human visual QA

A bounded P20–P24 slice was generated directly from the SHA-verified F5-002 candidate and rendered locally with LibreOffice, following the same identity-preserving bounded-slice logic used by the repository visual workflow.

Every rendered page produced by that slice was manually inspected.

Human visual verdict: **PASS**.

Observed:

- `Araştırma soruları birbirine bağlıdır.` reads naturally in context;
- the two preserved Fourth-scientific follow-up sentences flow normally after the new first sentence;
- paragraph and run formatting remain intact;
- no unexpected italic/bold/style propagation is visible;
- punctuation and Turkish diacritics render correctly;
- no clipping, overlap, broken footnote zone, RTL disturbance, or F5-002-attributable page-flow regression is visible.

## Final verdict

- actual F5-002 item correctly identified: **PASS**
- narrow Fourth-compatible rewrite: **PASS**
- deterministic replay/idempotency: **PASS**
- structural validation: **PASS**
- candidate SHA lock: **PASS**
- human visual QA: **PASS**

**F5-002 = APPLIED / PASS.**
