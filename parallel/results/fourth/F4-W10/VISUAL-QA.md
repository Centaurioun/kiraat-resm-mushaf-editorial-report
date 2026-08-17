# F4-W10 Visual QA

## Status

`NOT_EXECUTED — DEPENDENCY_BLOCKED`

No real W10-mutated DOCX exists from this worker run because the mandatory F4-047 reconstruction/SHA gate could not be executed. Therefore no rendering or visual PASS is claimed.

## Required visual QA after dependency resolution

Once a later environment reconstructs the genuine F4-047 baseline, verifies its exact required SHA, and safely replays W10, render the affected regions and confirm:

1. Footnotes 32, 41 and 105 retain citation text/formatting and lose only the specified work-note tails.
2. Footnote numbering, continuation, page layout and surrounding text remain stable.
3. Kahraman's malformed DOI is absent without a broken/empty hyperlink artifact.
4. Maşalı displays exactly `https://doi.org/10.56361/usul.173700` with a correct hyperlink target if linked.
5. Only the two authorized unused edition entries are removed; all required retained editions remain.
6. Both Ebû Şâme 1975 and 1993 entries remain.
7. Zotero bibliography field display, hanging indents, line spacing, paragraph ordering and field behavior are intact.
8. No clipping, overlap, unexpected page/section break, or style propagation occurs.

This checklist is a future acceptance gate, not completed worker evidence.
