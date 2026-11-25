#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: no network, no randomness, no timestamps, no files
outside this repository.

The note itself: the dryer eating one sock of every pair is a bug
everyone has shipped into production, and "two-factor authentication"
is the terse engineering fix a real release note would propose.
"""

import os

NOTE = (
    "v3.0.0: Fixed a bug where socks entered the dryer in pairs and "
    "exited as singles; laundry now requires two-factor authentication."
)


def main():
    # Gate: one line, 1-160 characters, not whitespace-only.
    assert 1 <= len(NOTE) <= 160, "note outside the 1-160 character gate"
    assert NOTE.strip() and "\n" not in NOTE, "note must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
