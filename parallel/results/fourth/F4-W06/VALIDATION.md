# VALIDATION — F4-W06

## Overall disposition

`DEPENDENCY_BLOCKED`

## Baseline gate

Expected logical F4-047 SHA-256:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

Repository manifest records the same expected hash and checkpoint `c473b24d3f6f24508c761805218bbaa29686b47c`.

Independent byte-level reproduction in this worker runtime: **NOT POSSIBLE**.

Reason:
1. The connected GitHub read path exposes UTF-8 repository content but binary DOCX fetch attempts cannot be decoded/materialized.
2. The worker container cannot resolve `github.com`, so the repository/binary cannot be cloned or downloaded there.
3. The contract forbids substituting the extracted Markdown for the authoritative DOCX when footnotes, fields, Arabic/RTL, bookmarks, relationships, or formatting matter.

Result: the mandatory baseline gate did not pass. No F4-083–090 edit was applied.

## Required technical invariant checks

Because no candidate DOCX was produced, post-edit checks were not run and no unchanged-state claim is fabricated.

- genuine footnote references/IDs: NOT RUN
- orphan/dangling/duplicate footnotes: NOT RUN
- Word fields: NOT RUN
- Zotero item/bibliography fields: NOT RUN
- bookmarks: NOT RUN
- hyperlinks: NOT RUN
- relevant RTL/Arabic runs: NOT RUN
- comments/revisions: NOT RUN
- sections: NOT RUN
- ZIP/XML integrity: NOT RUN
- protected OOXML comparison: NOT RUN
- item-level exact-target uniqueness: NOT RUN
- replay idempotence on a candidate DOCX: NOT RUN

## Safe checks completed

- Governing task/contract/policy files read.
- Fourth Report F4-083–090 instructions located and recorded.
- F4-047 manifest and expected hash located.
- Worker branch confirmed based on the orchestration commit.
- Non-mutating replay guard created.

No validation exception was waived.
