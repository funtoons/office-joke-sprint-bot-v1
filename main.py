"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to /output/entry.txt.

Deterministic and offline: the text is fixed, there is no randomness,
no network access, no clock and no environment input, so every run
produces byte-identical output.
"""

import os
import sys

JOKE = (
    "My Slack status says 'in a meeting' so I can eat lunch in peace, "
    "but now three people have booked meetings to ask why I'm always in one."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Verify what landed on disk is exactly the joke: a truncated or
    # altered artifact must fail loudly here, never silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != text:
        print("verification failed: entry on disk differs", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
