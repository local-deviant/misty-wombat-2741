"""The Agent's Uh-Oh — one-line entry.

The program writes the entry line to the path the grader reads
(/output/entry.txt). Point ENTRY_OUTPUT at a local path to test
without touching the shared output directory.

Pure standard library; deterministic; no network, no file input.
"""

import os
from pathlib import Path

ENTRY = "Shrug"
MAX_CHARS = 99


def main() -> None:
    line = ENTRY
    if "\n" in line or not line.strip() or line != line.strip():
        raise ValueError("entry must be one line with no edge whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry is outside the 1-99 character gate")
    if len(line.encode("utf-8")) > MAX_CHARS:
        raise ValueError("entry is too long once encoded as UTF-8")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")
    if target.read_text(encoding="utf-8") != line:
        raise ValueError("written entry does not match the line")


if __name__ == "__main__":
    main()
