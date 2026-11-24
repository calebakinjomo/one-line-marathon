#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single one-line comedy joke to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Joke mechanism: the horoscope's vague advice to "take a risk" is answered
with the most relatable modern dare -- opening one's banking app.
"""

import os
import sys

JOKE = "My horoscope said to take a risk today, so I opened my banking app."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)
    return 0

if __name__ == "__main__":
    sys.exit(main())
