# REPLAY SPEC — F4-W06 (BLOCKED GUARD)

## Scope

Assigned items only: `F4-083`–`F4-090`.

## Mandatory precondition

Input must be the logical F4-047 DOCX whose SHA-256 is exactly:

`6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7`

No edit, anchor search, citation move, paragraph consolidation, or OOXML mutation is permitted before this byte-level precondition passes.

## Current execution result

The baseline could not be materialized in the current worker runtime. Therefore the replay stops before target discovery and returns `DEPENDENCY_BLOCKED`.

The companion `replay_f4_w06_guard.py` is deliberately non-mutating. It verifies the exact baseline hash and then exits with a message requiring a capable worker/runtime to perform the item-specific replay. This prevents accidental application to the canonical source, F4-042, or any later/foreign state.

## Item intentions after the precondition is satisfiable

These are the authoritative report operations to implement later, not edits claimed by this worker:

- `F4-083`: replace active-agent/kurucu resm wording with the report-approved written-evidence/compatibility formulation; reduce repeated cem/istinsah history to only what the argument requires.
- `F4-084`: keep the `kırâat sünnettir` evidence at the limited strength supported by the cited/nakledilen material.
- `F4-085`: make the transition explicitly distinguish the authority/function of common Uthmanic mushafs from personal Companion codices.
- `F4-086`: do not collapse heterogeneous Companion-mushaf material into a single mensuh/tefsirî category.
- `F4-087`: remove the literal parenthetical editor note and preserve the surrounding sentence/continuation.
- `F4-088`: remove agency language that makes rasm itself an 'ayıklayan kurucu otorite'; attribute historical selection/acceptance to the istinsah and communal/ilmî process.
- `F4-089`: remove unsupported psychological motive attribution to Ibn Masʿūd; retain only historically supportable reported stance/actions.
- `F4-090`: inspect genuine footnotes first, then consolidate repeated 4.2 conclusion material without moving any note onto a proposition it does not support.

## Deterministic targeting rule for the later capable replay

Each operation must use exact semantic/text anchors plus local structural context. Zero matches or more than one plausible match must stop that item. Fuzzy best-match application is forbidden.

## Idempotence

This blocked guard performs no mutation and is byte-idempotent by construction.
