# Minimal Python Analysis Template

This is a cookiecutter template to set up a Python analysis project quickly with optional experiment tracking.

## Features

- Optional experiment ID for organized research workflows
- Choice between GitHub and GitLab hosting
- Minimal dependencies: polars, session-info
- Python packaging with pyproject.toml
- Pre-configured for uv package manager

## Quick Start

### Setting up cruft (one time)

Install cruft using your preferred method. We recommend using [uv](https://docs.astral.sh/uv/pip/environments/) for Python management.

```bash
# Using uv (recommended)
uv tool install cruft
```

> **Why cruft over cookiecutter?**
> Cruft allows you to update your project when the template evolves. Cookiecutter only generates projects once.

### Create your project

**Using HTTPS:**
```bash
cruft create https://github.com/your-username/python-experiment-template.git
```

**Using SSH:**
```bash
cruft create git@github.com:your-username/python-experiment-template.git
```

Cruft will prompt you for a number of variables. Refer to the on-screen instructions.

### Setting up git

Navigate to your created project and initialize git:

```bash
# Example directory names:
# With experiment_id: ex1-data-analysis
# Without experiment_id: data-analysis
cd your-project-directory

git init
git remote add origin <your-repo-url>  
git add .
git commit -m "repo: init"
git branch -M main
git push --set-upstream origin main
```

The generated README.md will contain the exact git URLs for your chosen platform.

## Development Setup

### Installing dependencies

Install your analysis in editable mode using uv:

```bash
# Install project dependencies
uv pip install -e .

# Install development dependencies
uv pip install -e ".[dev]"

# Install AWS dependencies (if needed)
uv pip install -e ".[aws]"
```

### Setting up pre-commit

If you add pre-commit to your dependencies:

```bash
uv pip install pre-commit
pre-commit install
```

Then pre-commit hooks will run on each `git commit`.

## Working with the Template

### Adding new dependencies

Add any new requirements to `pyproject.toml`:

```toml
dependencies = [
    "polars>=0.20.0",
    "session-info>=1.0.0",
    "your-new-package>=1.0.0",
]
```

Then install:

```bash
uv pip install -e .
```

### Updating the template

Keep your project up to date with template improvements:

```bash
cruft update
```