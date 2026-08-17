#!/usr/bin/env python3
"""F4-W01 fail-closed baseline gate.

This artifact intentionally performs no manuscript edits. The worker contract
requires the logical F4-047 DOCX to be reconstructed and its SHA-256 verified
before F4-048–056 may be applied. This gate can be used by an environment that
has the reconstructed DOCX available locally.
"""

from __future__ import annotations

import hashlib
import pathlib
import sys

EXPECTED = "6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7"


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: replay_gate.py <reconstructed-f4-047.docx>", file=sys.stderr)
        return 64
    path = pathlib.Path(sys.argv[1])
    if not path.is_file():
        print(f"DEPENDENCY_BLOCKED: missing input {path}", file=sys.stderr)
        return 2
    actual = sha256(path)
    if actual != EXPECTED:
        print(f"DEPENDENCY_BLOCKED: F4-047 SHA mismatch: {actual}", file=sys.stderr)
        return 3
    print(f"BASELINE_OK: {actual}")
    print("NO_EDITS_PERFORMED: F4-W01 remained blocked during this worker run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
