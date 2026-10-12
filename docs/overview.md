# barrage-checker: documentation overview

`barrage-checker` (v1.0.0, Python ≥ 3.8, no runtime dependencies) validates [Barrage](https://github.com/fitzyracing1/barrage) documents by checking for the required sections. (`docs/index.md` is the existing Jekyll site page and has not been changed.)

## Getting started

```bash
pip install barrage-checker      # or from source: pip install .
barrage-check examples/file.barrage
```

It prints `✓ <name> is a valid Barrage document` and exits with 0, or lists the problems and exits with 1. Wrong arguments or a missing file also exit with 1.

The CLI usage text also mentions `python -m barrage_checker`, but the package has no `__main__.py`, so use `barrage-check` instead.

## Files

| Path | Role |
|---|---|
| `barrage_checker/checker.py` | `REQUIRED_SECTIONS` patterns and `check_file(path) -> list[str]` |
| `barrage_checker/cli.py` | `main()` (console script `barrage-check`) |
| `.github/workflows/publish.yml` | manual-dispatch build and `twine upload` to PyPI |

The repo has no tests. MIT License. Copyright (c) 2026 Joshua Almeida
