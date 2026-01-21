# Contributing to agentic-totchef

Thank you for wanting to contribute to this project!

Quick guide:
- Fork the repository and create a branch based on `main`:
  - feature: `feature/<short-description>`
  - fix: `fix/<issue-num>-<short-description>`
- Write clear commits (e.g. `feat: add ...`, `fix: correct ...`).
- Follow PEP8 style; format with `black .` and check with `flake8`.
- Run tests locally with `pytest`.

Pull request requirements:
- Clear description of the change.
- Link to the related issue (if any).
- Automated or manual tests demonstrating the change.
- All tests must pass.
- Update documentation if needed.

How to run tests (example):
- Create and activate a virtualenv:
  - `python -m venv .venv && source .venv/bin/activate`
- Install dependencies:
  - `pip install -r requirements.txt`
- Run tests:
  - `pytest`

Reporting bugs:
- Use the issue template (`.github/ISSUE_TEMPLATE/bug_report.md`) to provide helpful information.

Communication:
- For doubts or large changes, open an issue before implementing.

License:
- Ensure contributions are compatible with the license in `LICENSE.md`.
