#!/usr/bin/env python3
"""The Comment Above the Code — writes one funny, honest dev comment to /output/entry.txt.

The comment sits above a fragile invoicing function: it totals invoices wrong
every 29th of February, and rather than fix it the team works around it.
The line is assembled from three fragments — the failure, the workaround,
the punchline — so the turn lands on the last few words. validate() enforces
the competition gate (1-200 chars, not only whitespace) plus an economy bound
and a ban on the competition's tired cliches, before anything is written.
"""

import os

FAILURE = "// Every 29th of February this function totals invoices wrong,"
WORKAROUND = "so Finance closes the books on the 28th"
PUNCH = "and pretends the day never happened."

MAX_CHARS = 200
MAX_WORDS = 30

BANNED = ("off-by-one", "who wrote this", "no comments", "nobody knows why",
          "do not refactor")


def assemble() -> str:
    return f"{FAILURE} {WORKAROUND} {PUNCH}"


def validate(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if len(text.split()) > MAX_WORDS:
        raise ValueError(f"entry must be at most {MAX_WORDS} words, "
                         f"got {len(text.split())}")
    lowered = text.lower()
    for cliche in BANNED:
        if cliche in lowered:
            raise ValueError(f"entry contains banned cliche: {cliche!r}")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    line = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
