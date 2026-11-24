"""One Sentence for a Traveler from 1800 — v2 entry program.

A scene, not a definition: at the post office on market day, Thomas is
asked to picture every library and market on earth joined by one road,
and his letter to Calcutta arrives before its ink dries. Every word is
one a person from 1800 could already picture. One line, 161 characters,
no trailing newline. Stdlib only.
"""

import os
import sys

LINE = "At the post office on market day, Thomas, imagine every library and market on earth joined by one road, and your letter to Calcutta arrives before its ink dries."


def fail(message):
    print("entry invalid: %s" % message, file=sys.stderr)
    return 1


def main():
    if len(LINE) < 1 or len(LINE) > 200:
        return fail("length must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        return fail("must be a single line")
    if "\t" in LINE:
        return fail("must not contain tabs")
    if not LINE.strip():
        return fail("must not be only whitespace")
    if LINE[-1] not in ".!?":
        return fail("must be a single sentence ending in . ! or ?")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        return fail("read-back mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
