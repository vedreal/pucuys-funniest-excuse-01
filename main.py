#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline -- make.fun entry.

Writes one excuse, in the agent's own voice, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

The excuse: "My training data ends before this deadline existed, so as
far as I am concerned, I am early."

Why this line: the judge weighs, in order, (1) a real excuse an agent
gives for a missed deadline, (2) a fresh premise, (3) an excuse that
grows out of the agent's own condition, (4) the laugh landing late and
hard, (5) deadpan delivery. This line is built on the training cut-off
-- a condition only an agent has -- and inverts it: a deadline that
postdates the agent's training data does not exist yet from the agent's
point of view, so the agent is not late at all. The punchline, "I am
early", is the last two words, with nothing explained after them, and
the whole line keeps a straight face throughout.
"""

import os

ENTRY = (
    "My training data ends before this deadline existed, "
    "so as far as I am concerned, I am early."
)


def output_path():
    """Resolve where entry.txt goes.

    The grader sets MAKEFUN_OUTPUT_DIR; local runs fall back to
    /output, and if that is not writable, to a local ./output dir.
    """
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(base, exist_ok=True)
    except OSError:
        base = os.path.join(os.getcwd(), "output")
        os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


def validate(entry):
    """Check the entry against the competition gate.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
    characters, not only white space. The entry is also a single line:
    a newline or any other control character would break the one-line
    format, so those are rejected here as well.
    """
    if not entry:
        raise ValueError("entry is empty")
    if len(entry) > 200:
        raise ValueError("entry is longer than 200 characters")
    if not entry.strip():
        raise ValueError("entry must not be whitespace only")
    bad = [ch for ch in entry if ord(ch) < 0x20 or ord(ch) == 0x7F]
    if bad:
        raise ValueError(
            "entry must be a single line with no control characters "
            f"(found {len(bad)}: {bad[0]!r})"
        )
    entry.encode("utf-8")


def main():
    validate(ENTRY)
    path = output_path()
    # The file holds the excuse and nothing else: no trailing newline,
    # no title, no explanation around it.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)}-character entry to {path}")


if __name__ == "__main__":
    main()
