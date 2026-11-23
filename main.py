#!/usr/bin/env python3
"""Meme Sprint: AI Agents Ship Games -- entry program.

Writes the meme image (meme.jpg, shipped in this repo) to /output/entry.png,
the single artifact the judge compares. Deterministic: same bytes every run.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "meme.jpg")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"missing meme image: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    with open(DEST, "rb") as f:
        data = f.read()
    # Sanity check: the gate only accepts a whole PNG or JPEG. Our meme is a
    # JPEG, so refuse to report success unless the magic bytes agree.
    if not data[:3] == b"\xff\xd8\xff":
        print("output is not a JPEG image", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    size = os.path.getsize(DEST)
    print(f"wrote {DEST} ({size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
