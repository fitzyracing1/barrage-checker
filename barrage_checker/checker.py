"""
Core validation logic for Barrage documents.
"""

import re
from pathlib import Path
from typing import List

REQUIRED_SECTIONS = [
    r"^# .+",                                # Title
    r"^> .+",                                # Summary quote
    r"^## Purpose",
    r"^## How it works \(plain English\)",
    r"^## Key ideas",
    r"^## The actual code",
    r"^## Line-by-line translation",
    r"^## Decisions the program makes",
    r"^## What a person would notice",
    r"^## Current status",
    r"^## Next possible steps",
]


def check_file(path: Path) -> List[str]:
    """
    Check whether a file follows the required Barrage document structure.

    Returns a list of error messages. An empty list means the document is valid.
    """
    errors: List[str] = []

    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Could not read file: {e}"]

    for pattern in REQUIRED_SECTIONS:
        if not re.search(pattern, text, re.MULTILINE):
            errors.append(f"Missing required section matching: {pattern}")

    if "```" not in text:
        errors.append("No code fence found — original code must be present")

    if len(text.strip()) < 200:
        errors.append("Document is very short — may be incomplete")

    return errors
