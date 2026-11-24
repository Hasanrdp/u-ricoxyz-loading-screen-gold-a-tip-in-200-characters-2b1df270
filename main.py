#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — make.fun entry (program/v1).

Writes one loading-screen tip, aimed at stressed developers and the AI
coding agents working beside them, to /output/entry.txt. Deterministic:
the same bytes on every run. No input, no network, no randomness,
standard library only.
"""

import os

TIP = "Tip: your agent is not stuck. It is rereading your prompt for the third time, hoping the requirements change."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = TIP.strip()
    assert 1 <= len(text) <= 200, f"tip must be 1-200 chars, got {len(text)}"
    assert text.strip(), "tip must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written: the graded artifact must be exactly
    # the tip above, byte for byte, on every run.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch: entry.txt differs from TIP"


if __name__ == "__main__":
    main()
