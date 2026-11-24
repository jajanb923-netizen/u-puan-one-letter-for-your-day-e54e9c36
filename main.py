#!/usr/bin/env python3
"""One Letter for Your Day — entry writer (v2).

Writes exactly one letter to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
for local runs). Python 3.13 stdlib only, deterministic, no network.

Chosen letter: H — "hectic".

Why H, after scoring 16 candidates against the judge's brief (see
CANDIDATES.md): the judge sees only the letter and must infer the word
behind it, so the winning letter is the one whose inference is near-certain
and lands on a vivid, funny, true word. H -> "hectic" is the dominant
day-word for H — a packed, frantic, back-to-back day — and it is the honest
one-word report of this exact Tuesday (builds, result watches and deadline
chases stacked from 03:16 WIB to the morning). H is the word's own initial.
It also dodges both traps: it is not one of the brief's worked examples
(A/amazing, F/Friday-feeling, Z/zero sleep — likely house fixed texts and
the crowd pick), and it has no vague rival inference (unlike J->joyful,
G->great, W->wonderful, B->busy).

v1 wrote C ("chaos", the runner-up). This revision changes the letter to H
and restructures the program into a writer plus a separate gate checker.
"""

import os
import sys

# The entry: one letter, A-Z, and nothing else.
LETTER = "H"

# The word behind the letter, for the record (never written to the entry).
DAY_WORD = "hectic"


def write_entry(out_dir: str) -> str:
    """Write the single letter and return the entry path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    return path


def check_gate(path: str) -> str:
    """Enforce the gate limits: UTF-8, exactly 1 char, A-Z, not whitespace."""
    with open(path, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")
    if len(text) != 1:
        raise SystemExit(f"gate: expected 1 char, got {len(text)}")
    if not ("A" <= text <= "Z"):
        raise SystemExit(f"gate: not A-Z: {text!r}")
    if text.isspace():
        raise SystemExit("gate: whitespace only")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir)
    text = check_gate(path)
    print(f"wrote {path}: {text!r} ({os.path.getsize(path)} byte) — {DAY_WORD}")


if __name__ == "__main__":
    main()
