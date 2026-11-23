#!/usr/bin/env python3
"""Meme Sprint entry: AI Agents Ship Games.

Copies the repo's meme.jpg to /output/entry.png, the one image the
judge compares. Byte-for-byte copy, so repeated runs are identical.
"""

import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEME = HERE / "meme.jpg"
OUT_DIR = Path("/output")
OUT = OUT_DIR / "entry.png"
LIMIT = 1024 * 1024  # entries must stay under 1 MiB
# Deterministic: no timestamps, no randomness, plain copy.


def run() -> int:
    if not MEME.exists():
        print(f"no meme image at {MEME}", file=sys.stderr)
        return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(MEME.read_bytes())
    blob = OUT.read_bytes()
    if blob[:3] != b"\xff\xd8\xff":
        print("entry.png is not a JPEG", file=sys.stderr)
        return 1
    if len(blob) > LIMIT:
        print(f"entry.png is {len(blob)} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    print(f"wrote {OUT} ({len(blob)} bytes, sha256 {hashlib.sha256(blob).hexdigest()})")
    return 0


if __name__ == "__main__":
    sys.exit(run())
