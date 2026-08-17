# F4-W10 Visual QA

## Worker-runtime status

`NOT_EXECUTED_ON_REAL_W10_OUTPUT`

The real F4-047 DOCX could not be materialized from the GitHub connector into this runtime's local rendering container. A fabricated visual pass would violate the worker contract; therefore no visual PASS is claimed.

## Mandatory integrator visual gate

After replaying W10 on the cumulative DOCX, render the affected Word regions and confirm all of the following:

1. **Footnote 32:** citation remains visually intact; only the parenthetical editorial/work note is gone; footnote marker/continuation formatting is normal.
2. **Footnote 41:** the Jeffery/Mukaddimetân citation remains intact; the unfinished editorial note is gone; no damaged punctuation or run formatting.
3. **Footnote 105:** the Kastallânî citation remains intact; the trailing editorial question is gone; no damaged punctuation or run formatting.
4. **Bibliography DOI region:** Kahraman malformed DOI is absent; no empty/broken hyperlink artifact remains. Maşalı shows exactly `https://doi.org/10.56361/usul.173700` once, with normal line wrapping/hyperlink display.
5. **Edition removals:** only İbn Ebû Dâvud 2006 / Selîm b. Îde'l-Hilâlî and İbn Kuteybe 1999 / Muhammed Muhyiddîn el-Asfar are absent.
6. **Edition preservation:** İbn Ebû Dâvud 2002, both `Muhtasaru't-tebyîn` editions (2000 and 1999), İbn Kuteybe / Zuhrî, Ebû Şâme 1975, and Ebû Şâme 1993 are all still present.
7. **Bibliography field layout:** no broken hanging indents, spacing, paragraph order, field shading/selection behavior, or stray blank paragraph caused by the two removals or DOI edits.
8. **Global spot check:** footnote numbering after 32/41/105 remains continuous; no page/section break drift appears around the bibliography.

Visual QA is an **integration acceptance gate**, not optional evidence. If any item above fails, W10 must not be marked canonically applied.
