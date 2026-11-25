#!/usr/bin/env python3
"""Write the single line that could have replaced the meeting.

Stdlib only. Deterministic: the same fixed text on every run.
"""

import os

LINE_PARTS = (
    "We booked a room for twelve people",
    "to read an email together,",
    "out loud, slowly.",
)


def build_line() -> str:
    """Assemble the entry line from its parts."""
    return " ".join(LINE_PARTS)


LINE = build_line()


MIN_CHARS = 1
MAX_CHARS = 200


def validate_line(line: str) -> str:
    """Reject lines outside the competition's 1-200 character gate."""
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    return line


def main() -> None:
    line = validate_line(build_line())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
