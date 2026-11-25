#!/usr/bin/env python3
"""Worst Superpower — make.fun bounty u-suroto-worst-superpower-461dcdbe.

The program the harness runs (Python 3.13, standard library only, no
network). It writes the entry line, byte for byte, to
$MAKEFUN_OUTPUT_DIR/entry.txt, defaulting to /output/entry.txt.
Deterministic: two runs write identical bytes.
"""

import os

LINE = "I can talk to goldfish, but they only ever want to discuss the little plastic castle."


def main() -> None:
    # The gate refuses anything outside 1-140 characters; fail loudly here
    # rather than shipping an entry the scorer would list as invalid.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise SystemExit(f"entry line is {len(LINE)} characters; gate needs 1-140")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
