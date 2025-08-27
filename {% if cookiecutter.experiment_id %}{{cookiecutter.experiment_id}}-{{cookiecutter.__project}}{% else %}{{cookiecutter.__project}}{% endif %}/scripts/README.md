# `scripts/`

This directory contains a template and utility scripts for the project.

## Template Script

`template.py` provides a standardised structure for new scripts with:

- Type-safe CLI arguments using `tap`
- Automatic argument saving for reproducibility
- Function imports from `src/`

### Usage

```bash
python scripts/template.py --output_dir . --a 5 --b 3
```

### Creating new scripts

1. Copy `template.py` to a new file
2. Update the `Args` class with your parameters
3. Implement your logic in the `main()` function
4. Import functions from `src/` as needed

The template handles project imports and saves all arguments as JSON for reproducibility.