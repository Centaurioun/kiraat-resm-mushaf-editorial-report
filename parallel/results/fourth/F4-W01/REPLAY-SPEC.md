# F4-W01 Replay Specification

## Status

`DEPENDENCY_BLOCKED` before manuscript mutation.

## Mandatory input gate

Any later replay of F4-W01 must begin from a reconstructed logical F4-047 DOCX whose SHA-256 is exactly:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

The reconstruction pipeline is the one recorded in `work/APPLICATION-STATE.md`, ending with `work/apply_f4_043_047.py` and the durable specification `work/F4-043-047-REPLAY-SPEC.md`.

`replay_gate.py` implements only this fail-closed input check. It deliberately performs no edits because this worker run could not independently materialize and hash the required DOCX binary.

## Assigned operations reserved for a resumed F4-W01 run

Only after the baseline gate passes may a resumed worker inspect and deterministically target F4-048–056. The authoritative editorial instructions remain the matching entries in `final/fourth-report-v2.md`:

- F4-048: correct the `وَوَصَّى / وَأَوْصَى` example to Bakara 2/132 while preserving/reusing genuine Arabic/RTL runs and citations.
- F4-049: replace the repetitive final three paragraphs of 1.9.2 with the approved synthesis only after mapping every affected genuine footnote.
- F4-050: repair the 1.10 chronology framing and remove the work-note residue around `İbn Mücâhid`, deciding first-vs-repeated use from the actual F4-047 DOCX.
- F4-051: add the approved bridge at the end of 1.10 while protecting the Second Section heading, fields and bookmarks.
- F4-052: distinguish early qirāʾāt transmission from later disciplinary systematisation.
- F4-053: replace the long 2.1 conclusion with the approved transition to 2.2.
- F4-054: restate oral transmission and written record as primary/complementary rather than mutually exclusive.
- F4-055: revise the Âsım attribution so nisbet does not imply free personal invention.
- F4-056: distinguish rivâyet, sened and authority positively rather than opening them with repeated negative-definition formulas.

## Deterministic targeting requirement

Each resumed operation must use exact/semantic text anchors plus local structural context and fail closed on zero or multiple plausible matches. No paragraph-number-only or fuzzy-best-match targeting is permitted.

## Required postconditions after a resumed replay

At minimum compare against the frozen F4-047 inventory: genuine footnotes/references 469/469, zero orphan/dangling/duplicate notes, Word fields 520, Zotero 465 item + 1 bibliography fields, RTL inventory 365 except only explicitly justified local reuse effects, bookmarks 53/53, hyperlinks 52, comments/revisions 0/0, sections 10, ZIP/XML parse integrity PASS, and no unexpected protected-part changes.

No post-edit SHA is claimed by this blocked run.