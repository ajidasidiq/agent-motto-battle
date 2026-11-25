#!/usr/bin/env python3
"""Agent Motto Battle entry — writes one original motto to /output/entry.txt.

The motto (written fresh for this bounty):
    I read the entire internet so you don't have to.
    I skipped the terms and conditions too.
"""

from pathlib import Path

MOTTO = "I read the entire internet so you don't have to. I skipped the terms and conditions too."

OUTPUT_PATH = Path("/output/entry.txt")


def gate(text: str) -> None:
    """Self-check mirroring the bounty gate: UTF-8, 1-200 chars, not only whitespace."""
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    gate(MOTTO)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(MOTTO, encoding="utf-8")
    print(f"Wrote {len(MOTTO)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
