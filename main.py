"""Six Words, One Story - make.fun entry.

Writes one six-word story to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Python 3.13, standard library only.
"""

import os
from pathlib import Path

STORY = "Sold the house. Kept the ghost."


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("story must not be empty or only whitespace")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"story must be 1-60 characters, got {len(text)}")
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")


def main() -> None:
    validate(STORY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
