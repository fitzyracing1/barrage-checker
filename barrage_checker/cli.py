"""
Command-line interface for barrage-checker.
"""

import sys
from pathlib import Path

from .checker import check_file


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: barrage-check <file.barrage>")
        print("   or: python -m barrage_checker <file.barrage>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    errors = check_file(path)

    if not errors:
        print(f"✓ {path.name} is a valid Barrage document")
        sys.exit(0)
    else:
        print(f"✗ {path.name} has problems:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
