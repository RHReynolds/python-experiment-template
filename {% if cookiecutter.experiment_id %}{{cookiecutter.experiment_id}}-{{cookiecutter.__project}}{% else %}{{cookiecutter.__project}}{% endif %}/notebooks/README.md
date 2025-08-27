# `notebooks/`

This directory should contain:

1. **Source files**: `.py` (jupytext format) or `.qmd` files. File names should be prefixed with numbers/letters to denote the sequence in which analyses were run - e.g. `01-template_analysis.py` or `01-template_analysis.qmd`.  
2. **Rendered outputs**: `.html` files corresponding to each notebook.

## Rendering to `.html`s

### `.py` (jupytext)

```bash
jupytext --to ipynb --execute 01-template_analysis.py
jupyter nbconvert --to html 01-template_analysis.ipynb
```

### `.qmd`

Requires [quarto](https://quarto.org/docs/get-started/) to be installed.

```bash
# Render directly with quarto (recommended)
quarto render 01-template_analysis.qmd
```
