"""
Barrage Checker
Validates documents written in the Barrage language.
"""

__version__ = "1.0.0"
__all__ = ["check_file", "REQUIRED_SECTIONS"]

from .checker import check_file, REQUIRED_SECTIONS
