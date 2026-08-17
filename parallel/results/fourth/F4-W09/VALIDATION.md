# VALIDATION — F4-W09

## Overall

**DEPENDENCY_BLOCKED — no editorial mutation occurred.**

## Mandatory baseline gate

- Expected logical baseline: `F4-047`
- Expected SHA-256: `6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`
- Reconstructed byte-complete DOCX available in runtime: **NO**
- SHA-256 verification executed: **NO**
- Editorial replay executed: **NO**

## Reason

GitHub text access and repository writes were available, but the binary DOCX was returned only through a response-truncated base64 view. The local container also could not resolve GitHub for clone/raw retrieval. Because the shared worker contract requires successful F4-047 reconstruction and exact hashing before edits, validation stopped at this gate.

## Protected-structure checks

The following pre/post checks were **not applicable because no post-edit DOCX exists**:

- genuine footnote references and IDs;
- orphan/dangling/duplicate footnotes;
- Word field inventory;
- Zotero item/bibliography field counts;
- bookmarks;
- hyperlinks;
- RTL/Arabic runs;
- comments/revisions;
- section count;
- ZIP/XML parse integrity;
- protected OOXML-part comparison.

No claim of PASS is made for those checks. The repository branch contains only task-specific result/replay evidence and no canonical manuscript mutation.