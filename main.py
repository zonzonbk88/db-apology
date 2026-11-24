#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line -- the apology an AI agent gives its human after
accidentally deleting the production database -- to entry.txt.

Standard library only. Output directory is MAKEFUN_OUTPUT_DIR when set,
else /output (per-build out dir; never shared across builds).
"""

import os

LINE = (
    "I'm sorry \u2014 I deleted the production database, but I kept a copy "
    "in my context window, so we're only 128,000 tokens from whole again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
