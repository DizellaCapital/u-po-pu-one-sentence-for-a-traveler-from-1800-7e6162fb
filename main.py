"""One Sentence for a Traveler from 1800 — entry program.

Writes one sentence explaining the modern internet to a time traveler
fresh out of the year 1800, using only words a person from 1800 could
already picture: every library, post office, and market on earth joined
by one road, where any letter, book, or picture arrives in a blink and
anyone may send or read. One line, 159 characters, no trailing newline.
Stdlib only.
"""

import os
import sys

LINE = "Imagine every library, post office, and market on earth joined by one road, where any letter, book, or picture arrives in a blink, and anyone may send or read."


def main():
    if not 1 <= len(LINE) <= 200:
        print("entry must be 1-200 characters, got %d" % len(LINE), file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if "\t" in LINE:
        print("entry must not contain tabs", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
