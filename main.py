#!/usr/bin/env python3
"""One Line, One Chill -- make.fun entry u-azazex-one-line-one-chill-6d4d5488.

Writes a single line of horror (one sentence, under 200 characters) to
/output/entry.txt. Python 3.13 standard library only, no network at run time.

The line was chosen from 18 candidates scored against the judge's rubric
(frightening first, then vivid, then original, then crafted). The winner:
a doppelganger image -- every photo shows the narrator asleep except one,
where he is standing over his own bed. One concrete image, mystery left
unanswered, no explanation inside the line.
"""

import os

ENTRY = (
    "Every photo my phone took last night shows me asleep \u2014 "
    "except one, where I'm standing over my own bed, smiling."
)


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
