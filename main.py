#!/usr/bin/env python3
"""Single-word boss entry: Hovercraft.

This program has exactly one job: place one word in
/output/entry.txt. Nothing else is emitted — no newline, no extra
whitespace, no commentary. The gate reads the file raw, so the
bytes on disk are the entry itself.

Why this word: the manager who never quite lands. He glides up
behind a desk without a sound, lingers over a shoulder for a
while, then drifts on — everywhere at once, settled nowhere. It
names a habit most people have worked under, and it needs no
translation: every workplace has one.
"""

from pathlib import Path

ENTRY_WORD = "Hovercraft"
OUTPUT_FILE = Path("/output/entry.txt")


def emit_entry() -> None:
    """Make sure the output folder exists, then save the single word."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(ENTRY_WORD, encoding="utf-8")


if __name__ == "__main__":
    emit_entry()
