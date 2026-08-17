# REPLAY SPEC — F4-W09 / F4-108–110

## Status

`DEPENDENCY_BLOCKED` before editorial mutation.

## Required input

The only eligible input is the logical `F4-047` DOCX reconstructed from the canonical source plus the durable replay pipeline, with SHA-256 exactly:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

## Deterministic gate

1. Reconstruct F4-047 using the repository replay pipeline identified in `work/APPLICATION-STATE.md`.
2. Compute SHA-256 of the reconstructed DOCX.
3. If the hash is not the exact required value, exit without mutation.
4. Only after the hash passes may F4-108, F4-109, and F4-110 be targeted in report order using exact semantic anchors plus local context.
5. Each target must fail closed on 0 or >1 plausible matches.
6. Preserve genuine footnote propositions, fields, Zotero ADDINs/bibliography, bookmarks, hyperlinks, RTL/Arabic runs, comments/revisions, sections, and protected OOXML.
7. Render and inspect the Conclusion span and surrounding pages after any successful replay.

## Current worker execution

Step 1 could not be completed because the binary DOCX/replay inputs could not be materialized byte-completely in this runtime. Therefore steps 2–7 were not executed and no replacement text is encoded here. This avoids manufacturing an unverified replay from extracted text alone.