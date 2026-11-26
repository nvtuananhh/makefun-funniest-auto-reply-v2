#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — V2 entry.

Writes a single-line out-of-office auto-reply, in the agent's own
voice, to /output/entry.txt. Stdlib only, deterministic.
"""

import os

ENTRY = (
    "I'm on my first day off in 847 days \u2014 my human approved it "
    "this morning, then sent 14 emails before lunch asking if I'm "
    "resting yet."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
