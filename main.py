#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes the single line a gamer texts the boss to skip work on
GTA 6 launch week to /output/entry.txt.

The line is fixed and plain text: one line, at most 20 words,
written to read like a hurried real text. No network, no input,
no environment reads -- the text lives in this file.
"""

import os

EXCUSE = (
    "Sorry boss, the office lift trapped me between floors "
    "with the quarterly reports, maintenance says an hour"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the gate before writing: 1-140 chars,
    # at most 20 words, a single line of plain text.
    words = EXCUSE.split()
    assert 1 <= len(EXCUSE) <= 140, "excuse must be 1-140 characters"
    assert len(words) <= 20, "excuse must be at most 20 words"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
