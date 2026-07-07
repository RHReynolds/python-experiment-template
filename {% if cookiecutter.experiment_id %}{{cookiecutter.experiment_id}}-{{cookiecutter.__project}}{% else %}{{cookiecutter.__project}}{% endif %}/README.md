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

### `Makefile`

Common tasks are wrapped in the `Makefile`. Run `make` (or `make help`) to
list the available targets:

``` bash
make install   # create .venv and install dependencies from uv.lock
make check     # verify uv.lock is in sync and run pre-commit on all files
```

`make install` is the recommended way to set up the project.

### `pyproject.toml`

Under the hood, the `Makefile` targets call [`uv`](https://docs.astral.sh/uv/).
Runtime dependencies are declared under `dependencies` in `pyproject.toml`,
and development tooling under the `dev` dependency group. Exact resolved
versions are pinned in `uv.lock` for reproducible installs.

`make install` runs `uv sync`, which creates `.venv` and installs the project
plus the `dev` group from the lockfile:

``` bash
uv sync
```

Run commands inside the environment with `uv run`, or activate `.venv`
directly:

``` bash
uv run python scripts/template.py --output_dir scratch --a 1 --b 2
# or
source .venv/bin/activate
```

For a lean, production-only environment, skip the `dev` group:

``` bash
uv sync --no-dev
```

> [!TIP]
> Let `uv` manage dependencies for you instead of editing `pyproject.toml` by
> hand. `uv add` adds the package, updates `pyproject.toml` and `uv.lock`, and
> installs it in one step:
>
> ``` bash
> # Add a runtime dependency
> uv add polars
>
> # Add a development dependency (to the `dev` group)
> uv add --dev ipython
>
> # Remove a dependency
> uv remove polars
> ```
>
> Commit the updated `uv.lock` so collaborators reproduce the same
> environment.

## Citations
<!-- Add any necessary software citations -->

- [Semantic release](https://github.com/semantic-release/semantic-release)
