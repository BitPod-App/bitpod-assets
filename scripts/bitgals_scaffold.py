#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("bitgals")
PERSONAS = ["taylor", "ember", "kati", "shiva", "vera"]
SUBFOLDERS = ["refs", "approved", "conditional", "rejected", "avatars", "videos", "metadata"]


def ensure(path: Path) -> bool:
    existed = path.exists()
    path.mkdir(parents=True, exist_ok=True)
    gitkeep = path / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")
    return not existed


def main() -> None:
    created = 0
    total = 0

    for path in (ROOT, ROOT / "protocol", ROOT / "shared_base"):
        total += 1
        created += int(ensure(path))

    for persona in PERSONAS:
        for subfolder in SUBFOLDERS:
            total += 1
            created += int(ensure(ROOT / persona / subfolder))

    print(f"BitGals scaffold complete: {total} folders ensured, {created} newly created.")


if __name__ == "__main__":
    main()
