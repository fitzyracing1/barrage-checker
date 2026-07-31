# barrage-checker

**Checker and validator for the Barrage language.**

Barrage is a plain-language format that makes any code readable by anyone (including people who do not program).  
This package checks whether a document follows the official Barrage structure.

## Install

```bash
pip install barrage-checker
```

(Once published to PyPI)

Or install directly from GitHub:

```bash
pip install git+https://github.com/fitzyracing1/barrage-checker.git
```

## Usage

```bash
barrage-check path/to/file.barrage
```

or

```bash
python -m barrage_checker path/to/file.barrage
```

### Example output

Valid document:
```
✓ reset-and-count.barrage is a valid Barrage document
```

Invalid document:
```
✗ myfile.barrage has problems:
  - Missing required section matching: ^## Purpose
  - No code fence found — original code must be present
```

## What it checks

The tool verifies that a Barrage document contains all required sections defined in the official specification:

- Title
- One-sentence summary
- Purpose
- How it works (plain English)
- Key ideas
- The actual code
- Line-by-line translation
- Decisions the program makes
- What a person would notice
- Current status
- Next possible steps

## Related

- Barrage language repository: https://github.com/fitzyracing1/barrage
- Official specification: https://github.com/fitzyracing1/barrage/blob/main/SPEC.md

## License

MIT
