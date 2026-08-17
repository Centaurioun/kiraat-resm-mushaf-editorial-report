#!/usr/bin/env python3
"""F4-W06 fail-closed baseline guard.

This artifact intentionally performs no manuscript mutation. The worker contract
requires exact reconstruction and SHA-256 verification of logical F4-047 before
F4-083–090 can be targeted or applied.
"""

from __future__ import annotations

import hashlib
import pathlib
import sys

EXPECTED_SHA256 = "6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7"


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print("DEPENDENCY_BLOCKED: usage: replay_f4_w06_guard.py <logical-F4-047.docx>", file=sys.stderr)
        return 2

    path = pathlib.Path(sys.argv[1])
    if not path.is_file():
        print(f"DEPENDENCY_BLOCKED: baseline file not found: {path}", file=sys.stderr)
        return 3

    actual = sha256(path)
    if actual != EXPECTED_SHA256:
        print(
            "DEPENDENCY_BLOCKED: F4-047 SHA-256 mismatch; "
            f"expected={EXPECTED_SHA256} actual={actual}",
            file=sys.stderr,
        )
        return 4

    print(
        "BASELINE_OK: exact F4-047 SHA-256 verified. "
        "This guard is non-mutating; item-specific F4-083–090 replay must run in a runtime "
        "that can inspect genuine DOCX citations/OOXML and perform visual QA."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
