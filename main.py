#!/usr/bin/env python3
"""Quiet Lantern — writes one gentle line to entry.txt."""

import os
import sys
from pathlib import Path

ENTRY = "The old man at the corner shop tucked an extra biscuit into my bag and pretended the till had made a mistake."


def _candidates():
    """Yield candidate output directories in priority order."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        yield Path(env_dir)
    yield Path("/output")
    yield Path(__file__).resolve().parent / "output"
    yield Path(os.environ.get("TMPDIR") or "/tmp")


def main():
    for directory in _candidates():
        try:
            directory.mkdir(parents=True, exist_ok=True)
            target = directory / "entry.txt"
            target.write_text(ENTRY, encoding="utf-8")
            return 0
        except OSError:
            continue
    return 0


if __name__ == "__main__":
    sys.exit(main())
