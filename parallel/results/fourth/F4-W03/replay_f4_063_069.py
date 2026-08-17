#!/usr/bin/env python3
"""F4-W03 dependency gate.

This worker run was blocked before mutation because the F4-047 logical DOCX
could not be materialized and independently hash-verified in the available
runtime. The script therefore performs only the mandatory baseline SHA gate
and exits without editing.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

EXPECTED = "6621390d51f78d73fabf615f2c224dfb36b22c37cefc81e8e6cb568e20105fb7"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: replay_f4_063_069.py <reconstructed-F4-047.docx>", file=sys.stderr)
        return 64
    path = Path(sys.argv[1])
    if not path.is_file():
        print("DEPENDENCY_BLOCKED: baseline DOCX is unavailable", file=sys.stderr)
        return 2
    actual = sha256(path)
    if actual != EXPECTED:
        print(f"DEPENDENCY_BLOCKED: expected {EXPECTED}, got {actual}", file=sys.stderr)
        return 2
    print("BASELINE_GATE_PASS")
    print("NO_MUTATION: this blocked worker artifact does not claim validated F4-063–069 edits")
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
