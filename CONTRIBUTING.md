# Contributing

Thanks for looking. This project is in early development, so the process is
intentionally light — but a few rules keep things reviewable.

## Before you open a pull request

1. Read the [README](README.md) so you know what the project is trying to do.
2. Search existing issues and pull requests for the same change.
3. For anything larger than a typo, **open an issue first**. Agreeing on an
   approach before writing code saves everyone time.

## Setting up

```bash
git clone https://github.com/LLF-prong/guardgate.git
cd guardgate
python -m venv .venv
.venv/Scripts/activate      # Windows; use `source .venv/bin/activate` elsewhere
pip install -e ".[dev]"
```

## Checks that must pass

```bash
ruff check .
ruff format --check .
pytest
```

CI runs exactly these on every pull request.

## Pull request guidelines

- One logical change per pull request. If you find yourself writing "and also"
  in the description, split it.
- Explain *why*, not just *what*. The diff already shows what changed.
- Add or update tests. A bug fix without a regression test will be sent back.
- Keep the public API documented. Anything a user can call needs a docstring.

## Commit messages

Conventional Commits, please:

```
feat: add per-chunk scoring interface
fix: handle empty context list
docs: clarify dataset schema
test: cover unicode homoglyph input
```

## Reporting security issues

Please do not open a public issue for a vulnerability in GuardGate itself. Use
GitHub's private vulnerability reporting on the repository's Security tab.
