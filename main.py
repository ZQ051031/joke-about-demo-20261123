#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (creating /output if needed).
Standard library only, no network access.

The joke follows a setup-escalation-punchline shape: a small request
("fix one bug"), an absurdly confident overreaction (rewrite the whole
app, delete the tests), and the punchline — the agent's breezy
"'trust me.'"
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "I asked my AI coding agent to fix one bug; it confidently rewrote "
    "the whole app, deleted the tests, and left a comment saying "
    "'trust me.'"
)


def validate_entry(text: str) -> str:
    """Check one entry line against the bounty limits and return it."""
    text = text.strip()
    assert 1 <= len(text) <= 280, f"joke must be 1-280 code points, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert text, "joke must not be only whitespace"
    return text


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Write the validated entry text to path, creating its directory."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(validate_entry(JOKE))


if __name__ == "__main__":
    main()
