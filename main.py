#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

PITCH = (
    "ListingNanny: a service charging $5 a month per listing to answer "
    "2am Wi-Fi complaints for lazy AI agents managing exactly one Airbnb, "
    "so they can sleep through every guest crisis."
)


def main() -> None:
    pitch = PITCH.strip()
    if not (1 <= len(pitch) <= 200):
        raise SystemExit(f"pitch must be 1-200 chars, got {len(pitch)}")
    # Exactly one sentence: a single terminal full stop, no other
    # sentence-ending punctuation.
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(pitch + "\n")
    print(f"Wrote {len(pitch)}-character pitch to /output/entry.txt")


if __name__ == "__main__":
    main()
