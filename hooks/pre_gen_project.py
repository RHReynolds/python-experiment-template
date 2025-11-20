import os
import re
import tempfile

VALID_ID = r"[a-z]{2,4}\d+"


def check_experiment_id(experiment_id: str) -> None:
    assert bool(
        experiment_id == "" or re.fullmatch(VALID_ID, experiment_id)
    ), f"Invalid experiment_id supplied: {experiment_id}"


def is_cruft_updating() -> bool:
    return tempfile.gettempdir() in os.getcwd()


if __name__ == "__main__":
    if not is_cruft_updating():
        check_experiment_id("{{ cookiecutter.experiment_id }}")
