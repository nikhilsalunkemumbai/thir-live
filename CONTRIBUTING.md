# Contributing to THIR

Thanks for your interest in contributing to THIR (Threat Hunter Intelligence Range).

## What We Welcome

- Bug fixes in pipeline tools (`tools/`)
- Dashboard (`index.html`) improvements — visualisation, accessibility, performance
- New detection rules in `26_incident_timeline_live.py` TTP mapping
- False positive signal improvements in `29_false_positive_live.py`
- Documentation improvements

## What We Don't Accept

- Changes that add offensive capabilities
- Hardcoded credentials or API keys of any kind
- Dependencies that require a paid license
- Changes that break the `go run` (no `go.mod`) design decision

## How to Contribute

1. **Fork** the repository
2. **Create a branch** — `git checkout -b fix/your-fix-name`
3. **Make your changes** — keep commits focused and descriptive
4. **Test locally** if possible — run tools against a sample `cowrie.json`
5. **Open a Pull Request** — describe what you changed and why

## Code Style

- **Go tools:** standard `gofmt` formatting, stdlib only (no external dependencies)
- **Python tools:** PEP 8, type hints where practical, no external dependencies beyond stdlib
- **pipeline.yml:** keep steps self-documenting with inline comments

## Reporting Issues

Open a GitHub Issue with:
- What you expected to happen
- What actually happened
- Relevant log output from GitHub Actions (redact any sensitive data)

## Security Issues

Do **not** open a public issue for security vulnerabilities. Contact the repository owner directly via GitHub.
