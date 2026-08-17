#!/usr/bin/env python3
"""Fail-closed F4-W09 replay gate.

This worker was unable to materialize the byte-complete F4-047 baseline in its
runtime. The artifact therefore implements only the mandatory deterministic
baseline gate and performs no editorial mutation unless future continuation
first supplies the exact verified F4-047 DOCX.
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
        print("usage: replay_f4_108_110.py <verified-f4-047.docx>", file=sys.stderr)
        return 2
    source = pathlib.Path(sys.argv[1])
    if not source.is_file():
        print("DEPENDENCY_BLOCKED: input DOCX missing", file=sys.stderr)
        return 3
    actual = sha256(source)
    if actual != EXPECTED:
        print(f"DEPENDENCY_BLOCKED: F4-047 SHA mismatch: {actual}", file=sys.stderr)
        return 3
    print("BASELINE_OK: F4-047 hash verified")
    print("NO_MUTATION: editorial replay intentionally absent because this worker execution was blocked before target/citation verification")
    return 4


if __name__ == "__main__":
    raise SystemExit(main())
