#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — make.fun entry (program/v1).

Writes one loading-screen tip, aimed at stressed developers and the AI
coding agents working beside them, to /output/entry.txt. Deterministic:
the same bytes on every run. No input, no network, no randomness,
standard library only.
"""

import hashlib
import os
import sys

TIP = "Tip: your agent is not stuck. It is rereading your prompt for the third time, hoping the requirements change."

EXPECTED_SHA256 = "5f971eb0f6d6d551b5f0489c0a2b8f716c35e25849ffb3b55e0a083af365a586"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = TIP.strip()
    assert 1 <= len(text) <= 200, f"tip must be 1-200 chars, got {len(text)}"
    assert text.strip(), "tip must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written: the graded artifact must be exactly
    # the tip above, byte for byte, on every run. The gate checks the
    # exact string, the exact length (109), no trailing newline, and the
    # pinned sha256 of the expected bytes; anything else is a hard fail.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != text.encode("utf-8"):
        print("gate failed: entry.txt bytes differ from TIP", file=sys.stderr)
        raise SystemExit(1)
    if len(raw) != 109 or raw.endswith(b"\n"):
        print(f"gate failed: entry.txt is {len(raw)} bytes, expected 109 with no trailing newline", file=sys.stderr)
        raise SystemExit(1)
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"gate failed: sha256 {digest} != {EXPECTED_SHA256}", file=sys.stderr)
        raise SystemExit(1)
    print(f"verified: 109 chars, sha256 {digest}")


if __name__ == "__main__":
    main()
