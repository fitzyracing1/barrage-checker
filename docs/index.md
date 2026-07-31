# barrage-checker

**Make sure your Barrage documents are correct.**

`barrage-checker` is the official validator for the Barrage language.  
It checks that a document follows the required structure so that code is readable by anyone — including people who have never programmed.

## Install

```bash
pip install git+https://github.com/fitzyracing1/barrage-checker.git
```

(Once published to PyPI you will be able to use `pip install barrage-checker`)

## Usage

```bash
barrage-check path/to/yourfile.barrage
```

or

```bash
python -m barrage_checker path/to/yourfile.barrage
```

### Example

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

The tool verifies every required section of a Barrage document:

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

## The Barrage Language

Barrage is a plain-language format that makes any code understandable to non-programmers.

- Language repository: [github.com/fitzyracing1/barrage](https://github.com/fitzyracing1/barrage)
- Official specification: [SPEC.md](https://github.com/fitzyracing1/barrage/blob/main/SPEC.md)

## Source Code

This website and the package live at:

**https://github.com/fitzyracing1/barrage-checker**

## License

MIT
