import os
from pathlib import Path

from tap import Tap

SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]


class Args(Tap):
    output_dir: Path  # Directory to save output files.


def main(args: Args) -> None:
    pass


if __name__ == "__main__":
    args = Args().parse_args()
    # Save reproducibility info as a json alongside the outputs.
    args.save(args.output_dir / f"{SCRIPT_NAME}.args.json")

    main(args)
