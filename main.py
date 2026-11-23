#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (creating /output if needed).
Standard library only, no network access.
"""

import os

JOKE = (
    "I asked my AI coding agent to fix one bug; it confidently rewrote "
    "the whole app, deleted the tests, and left a comment saying "
    "'trust me.'"
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke must be 1-280 code points, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
