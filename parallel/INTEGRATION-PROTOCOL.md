# INTEGRATION PROTOCOL

## Single-writer principle

The integrator is the only actor permitted to mutate the authoritative application state files and the only actor that constructs the single integrated DOCX lineage.

## Integration branch

Fourth integration occurs on a dedicated branch such as `integration/f4-parallel-v1`, created from the frozen F4-047 application checkpoint. Fifth integration occurs on a new integration branch created from the independently verified F4 baseline. Worker branches are never merged.

## Intake gate

For every worker result package, verify task identity, permitted item IDs, baseline, branch, replay artifact, citation map, technical validation, visual QA, and handoff. Reject scope contamination.

## Per-item gate

Classify each item:

### GREEN
Unique anchor; expected prior state; citation semantics safe; no structural collision; replay and validation pass. Apply normally.

### AMBER
Same local region changed by an earlier accepted bundle; heading/context changed; citation proposition requires re-evaluation; partial Fourth/Fifth overlap; structural interaction. High integrator adjudicates before application.

### RED
Anchor missing or non-unique; unsafe citation destination; unexpected field/bookmark/Zotero/RTL mutation; scope violation; non-idempotent replay; validation failure. Do not apply until explicitly resolved.

## Fourth order

Reconstruct and verify F4-047 first. Integrate F4-W01 through W09 in report order, then process the W10 specialist items in their report positions. F4-111 and F4-113 are integrator-reserved global operations and must not be delegated retroactively.

After every accepted high-risk structural operation, checkpoint immediately. For lower-risk edits, checkpoint at a reasonable small batch boundary.

## Canonical state

Only after an edit has been successfully applied to the integration lineage may the canonical ledger disposition be advanced from `PENDING`. Update `work/application-ledger.jsonl`, `work/APPLICATION-STATE.md`, `work/VALIDATION-LOG.md`, and `work/NEXT-HANDOFF.md` together so durable state cannot disagree.

## Fifth order

Do not begin until the independent Fourth audit has frozen an F4 verified baseline. Integrate local F5-W01–W10 outputs, respecting Fourth precedence. Then perform integrator-reserved F5-086–094 global style sweep on the fully locally edited Fifth document.

## No binary merge

Never combine worker DOCX files. Re-execute accepted deterministic edit artifacts on the single integration document.
