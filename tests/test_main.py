import json
import os
import subprocess
import tomllib
from pathlib import Path

import pytest


def verify_project_structure(project_dir: Path) -> None:
    """Verify the generated project has required files."""
    required_files = ["README.md", "index.md", "pyproject.toml"]

    for filename in required_files:
        file_path = project_dir / filename
        assert file_path.exists(), f"Missing required file: {filename}"
        assert file_path.stat().st_size > 0, f"File {filename} is empty"

    with open(project_dir / "pyproject.toml", "rb") as f:
        tomllib.load(f)


@pytest.mark.parametrize("tool", ["cruft", "cookiecutter"])
def test_default_template(tmp_path: Path, tool: str) -> None:
    """Test template creation with default values."""
    template_dir = Path.cwd()
    os.chdir(tmp_path)

    try:
        if tool == "cruft":
            cmd = ["cruft", "create", str(template_dir), "--no-input"]
        else:
            cmd = ["cookiecutter", str(template_dir), "--no-input"]

        result = subprocess.run(cmd, capture_output=True, text=True)
        assert result.returncode == 0, f"{tool} failed: {result.stderr}"

        # Find the created project directory
        project_dirs = [d for d in Path(".").glob("*") if d.is_dir()]
        assert len(project_dirs) == 1, f"No project dir created by {tool}"

        # Verify the structure of the first (or only) project
        verify_project_structure(project_dirs[0])

    finally:
        os.chdir(template_dir)


@pytest.mark.parametrize(
    "tool,config_file,should_contain",
    [
        ("cruft", "test-valid.json", "ex1"),
        ("cookiecutter", "test-valid.json", "ex1"),
    ],
)
def test_valid_config(
    tmp_path: Path, tool: str, config_file: str, should_contain: str
) -> None:
    """Test template creation with valid configs."""
    template_dir = Path.cwd()
    os.chdir(tmp_path)
    config_path = str(template_dir / "tests" / "test_data" / config_file)

    try:
        if tool == "cruft":
            cmd = [
                "cruft",
                "create",
                str(template_dir),
                "--config-file",
                config_path,
                "--no-input",
            ]
        else:
            cmd = [
                "cookiecutter",
                str(template_dir),
                "--config-file",
                config_path,
                "--no-input",
            ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        assert result.returncode == 0, f"{tool} failed: {result.stderr}"

        project_dirs = [d for d in Path(".").glob("*") if d.is_dir()]
        assert len(project_dirs) == 1

        project_dir = project_dirs[0]
        verify_project_structure(project_dir)
        assert should_contain in project_dir.name

    finally:
        os.chdir(template_dir)


@pytest.mark.parametrize(
    "experiment_id,project,expected_name",
    [
        ("exp123", "myproject", "exp123-myproject"),
        ("", "myproject", "myproject"),
        ("test001", "demo", "test001-demo"),
    ],
)
def test_experiment_id_scenarios(
    tmp_path: Path, experiment_id: str, project: str, expected_name: str
) -> None:
    """Test conditional directory naming based on experiment_id."""
    template_dir = Path.cwd()
    os.chdir(tmp_path)

    try:
        config = {
            "default_context": {
                "experiment_id": experiment_id,
                "project": project,
                "owner": "Test",
            }
        }

        config_file = f"config-{experiment_id or 'empty'}.json"
        with open(config_file, "w") as f:
            json.dump(config, f)

        result = subprocess.run(
            [
                "cookiecutter",
                str(template_dir),
                "--config-file",
                str(config_file),
                "--no-input",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"cookiecutter failed: {result.stderr}"

        project_dirs = [
            d
            for d in Path(".").glob("*")
            if d.is_dir() and not d.name.startswith("config-")
        ]
        assert len(project_dirs) == 1

        project_dir = project_dirs[0]
        assert project_dir.name == expected_name
        verify_project_structure(project_dir)

    finally:
        os.chdir(template_dir)


def test_invalid_config_fails() -> None:
    """Test that invalid config fails when using cookiecutter."""
    result = subprocess.run(
        [
            "cookiecutter",
            ".",
            "--config-file",
            "tests/test-invalid.json",
            "--no-input",
        ],
        capture_output=True,
        text=True,
    )

    # Should fail due to pre_gen_project.py validation
    assert (
        result.returncode == 1
    ), f"Invalid config should fail. Return code: {result.returncode}."
