# Why this file is needed

pyproject.toml is the modern, standard place to configure Python tools from once centralized place. 

Instead of scattering configs across multiple files (.flake8, pytest.ini, setup.cfg, etc.), everything lives in one place.

This file is important because it:

Standardizes Python code across repos (especially useful in multi-repo setups)
Prevents bad code from being deployed
Keeps automation scripts (Ansible, Azure Functions, etc.) clean and reliable

🚨 What happens if you remove it?

Developers may format code differently
Linting becomes inconsistent
CI may behave differently than local runs
Tests might not be discovered or marked correctly

👉 Basically: chaos + inconsistency

# When it is actually used

This file is read only when you run tools that support it, like:

1. During development (locally)

When you or your team runs:

ruff check .
ruff format .
pytest

👉 Ruff and pytest will automatically look for pyproject.toml and apply these rules.

Without it:
Ruff uses defaults (which may differ per developer).
pytest may not find tests or markers correctly.

2. In CI/CD pipelines (very important)

If your pipeline runs:

ruff check .
pytest

Then:

❌ Bad code style → pipeline fails
❌ Lint errors → pipeline fails
❌ Broken tests → pipeline fails

👉 The file becomes your quality gate

3. In IDEs (VS Code, PyCharm, etc.)

Editors automatically read this file to:

Format code on save
Highlight lint issues
Apply consistent rules across the team

