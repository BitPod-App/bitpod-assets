#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("assets/bitgals")
PERSONAS = ["taylor", "orange", "kati", "shiva", "vera"]
SUBFOLDERS = ["refs", "approved", "conditional", "rejected", "avatars", "videos", "metadata"]


def ensure(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    gitkeep = path / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")


def main() -> None:
    ensure(ROOT)
    ensure(ROOT / "protocol")
    ensure(ROOT / "shared_base")
    for persona in PERSONAS:
        for subfolder in SUBFOLDERS:
            ensure(ROOT / persona / subfolder)
    print("BitGals scaffold complete.")


if __name__ == "__main__":
    main()
