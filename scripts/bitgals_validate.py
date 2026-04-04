#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

PATTERN = re.compile(r"^(taylor|orange|kati|shiva|vera)_(avatar|image|video)_[a-z0-9-]+_[a-z0-9-]+_v\d{2}\.(png|jpg|jpeg|webp|mp4|mov|webm)$")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        raise SystemExit(f"Missing file: {path}")
    if not PATTERN.match(path.name):
        raise SystemExit(f"Invalid BitGals filename: {path.name}")
    print("Valid BitGals filename.")


if __name__ == "__main__":
    main()
