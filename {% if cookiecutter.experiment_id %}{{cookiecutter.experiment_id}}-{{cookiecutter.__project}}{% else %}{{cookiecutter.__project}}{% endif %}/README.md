<!-- badges: start -->
{% if cookiecutter.git_platform == 'gitlab' %}[![GitLab](https://badgen.net/badge/icon/gitlab-pages?icon=gitlab&label)]({{ cookiecutter.__pages_url }}){% else %}[![GitHub Pages](https://badgen.net/badge/icon/github-pages?icon=github&label)]({{ cookiecutter.__pages_url }}){% endif %}
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
<!-- badges: end -->

# {% if cookiecutter.experiment_id %}{{ cookiecutter.experiment_id }}-{{ cookiecutter.__project }}{% else %}{{ cookiecutter.__project }}{% endif %}

## Background
<!-- Add a description of your project. -->

{{ cookiecutter.description }}

## Code contents
<!-- Modify the following table to suit your repository. -->

Within this repository you will find:

| Directory | Description |
| --------- | --------------------------------------------------------------------------- |
| [notebooks](notebooks) | Contains all `.qmd` (Quarto) notebooks and their corresponding `.html` outputs describing analyses performed for this project. These can be viewed interactively on {{ cookiecutter.git_platform|title }} Pages. |
| [scripts](scripts) | Standalone Python scripts with argument parsing using TAP (Typed Argument Parser). |
| [logs](logs) | Use this to record any necessary log files. |
| [src](src) | Various utility functions called in [notebooks](notebooks) and [scripts](scripts). |
| [raw_data](raw_data) | All larger files must be stored on S3. At most, this folder may contain sample information, or other small tabular files necessary for processing. |
| [processed_data](processed_data) | Ideally, all files to be stored on S3. This folder can contain smaller results files that are more easily shared outside of S3. |


## Reproducibility

### `pyproject.toml`

1. Please add any python dependencies to the `dependencies` list in `pyproject.toml`.
2. These can optionally be installed using:

``` bash
uv venv .venv
source .venv/bin/activate

# Install project dependencies
uv pip install -e .

# For development dependencies
uv pip install -e ".[dev]"
```

## Citations
<!-- Add any necessary software citations -->

- [Semantic release](https://github.com/semantic-release/semantic-release)
