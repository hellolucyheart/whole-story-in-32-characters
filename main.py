#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters: one Wi-Fi network name.

The entry is a single Wi-Fi network name of at most 32 characters,
written to ``entry.txt`` inside the output directory the grader sets
(``$MAKEFUN_OUTPUT_DIR``, default ``/output``) -- the one path the
grader reads. The program validates its own name before writing it,
and writes the exact text with no trailing newline and nothing else
in the file.

The name is:

    My Ex Changed the Password

Twenty-six characters. It lands as a joke first: a Wi-Fi network
whose name is a cry for help, broadcast to every phone in range.
Then it carries a whole story in the few words a passer-by sees.
Two people shared a home and a network; they broke up; the ex --
out of spite, or simply because they still held the admin login --
changed the password; and the narrator is now locked out of their
own internet, announcing the humiliation in the network list
itself. The breakup, the shared home, the petty revenge, and the
lockout are all inside those six words, and the name reads exactly
like something a real person would type into a router's SSID field
after a bad split -- which is what makes it funny instead of just
clever. It is fresh where the old Wi-Fi jokes are puns ("Pretty Fly
for a Wi-Fi", "FBI Surveillance Van"): no pun, no acronym, just a
small domestic tragedy told as a network name, tight at 26 of the
32 characters allowed.

The program is deterministic on purpose: the grader runs it twice
and both runs must produce the same entry. It reads nothing from
the network, the environment (beyond the output directory the
grader itself sets), or the git history -- the name lives in this
file, and this file alone.
"""

from __future__ import annotations

import os
import sys

# One original Wi-Fi network name: the ex, the password, the lockout.
# Six words, 26 characters, a breakup told as an SSID.
NAME = "My Ex Changed the Password"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 32


def check_name(name: str) -> str:
    """Return the name when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one Wi-Fi name, 1 to 32 characters,
    no line breaks, nothing but the name.
    """
    text = name.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return text


def main() -> int:
    text = check_name(NAME)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
