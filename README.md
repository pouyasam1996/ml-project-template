# ml-project-template

Starting point for my ML projects: uv environment, ruff, pre-commit, pytest with GPU-test skipping, and GitHub Actions CI.

## Start a new project

1. On GitHub: **Use this template → Create a new repository**, then clone it.
2. Rename the placeholder:
   - `mv src/project_name src/<new_name>`
   - `pyproject.toml`: `name`, `description`
   - `tests/test_smoke.py`: the import
   - This README
3. `uv lock --upgrade && uv sync && uv run pre-commit install && uv run pytest -v`
4. Repo settings → General: allow **squash merging** only; turn on **automatically delete head branches**.
5. Settings → Rules → Rulesets → **Import a ruleset** → `.github/rulesets/protect-main.json`.
6. Open a first PR so CI runs once. Then make sure `test` is a required status check.
7. Delete this "Start a new project" section.

## Included

| File | Purpose |
| --- | --- |
| `.github/workflows/ci.yml` | Lint, format check, tests on every PR |
| `.pre-commit-config.yaml` | Local checks before each commit |
| `pyproject.toml` | Dependencies, ruff and pytest settings |
| `tests/conftest.py` | Skips `gpu`-marked tests without CUDA |
