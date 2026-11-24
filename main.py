#!/usr/bin/env python3
"""Write one absurd invention pitch sentence to /output/entry.txt.

Stdlib only, no network, fully deterministic: the same sentence is
written on every run.
"""

import os

ENTRY = (
    "The Charger Snake is a phone cable that slithers to the nearest "
    "outlet by itself when your battery hits 5%, hissing at anyone who "
    "dares step on it mid-rescue."
)


def main() -> None:
    # The pitch: a dead phone battery is the tiny annoyance, the
    # self-slithering Charger Snake is the absurd invention, and its
    # hissing mid-rescue is the silly mechanism. One sentence, no
    # trailing newline, so the output bytes are identical every run.
    if not 1 <= len(ENTRY) <= 220:
        raise ValueError(f"entry must be 1-220 characters, got {len(ENTRY)}")
    if ENTRY != ENTRY.strip() or "  " in ENTRY:
        raise ValueError("entry must not have leading/trailing or double spaces")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
