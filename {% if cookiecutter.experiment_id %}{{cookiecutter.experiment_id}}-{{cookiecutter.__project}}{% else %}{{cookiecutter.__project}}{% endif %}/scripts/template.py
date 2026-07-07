import os
import sys
from pathlib import Path

from tap import Tap

# Add the project root to Python path so we can import from src/
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.main import addition  # noqa: E402

SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]


class Args(Tap):
    output_dir: Path  # Directory to save output files.
    a: int
    b: int


def main(args: Args) -> None:
    result = addition(args.a, args.b)
    print(f"Result: {result}")


if __name__ == "__main__":
    args = Args().parse_args()
    # Create the output directory if it doesn't already exist.
    args.output_dir.mkdir(parents=True, exist_ok=True)
    # Save reproducibility info as a json alongside the outputs.
    args.save(args.output_dir / f"{SCRIPT_NAME}.args.json")

    main(args)
