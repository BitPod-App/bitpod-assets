#!/usr/bin/env python3
import argparse
import json
import shutil
from pathlib import Path

ROOT = Path("assets/bitgals")
PROTOCOL = ROOT / "protocol"
PERSONAS = {"taylor", "ember", "kati", "shiva", "vera"}
TYPES = {"avatar", "image", "video"}
DECISIONS = {"approved", "conditional", "rejected"}
EXTS = {
    "avatar": {".png", ".jpg", ".jpeg", ".webp"},
    "image": {".png", ".jpg", ".jpeg", ".webp"},
    "video": {".mp4", ".mov", ".webm"},
}


def normalize(text: str) -> str:
    cleaned = text.strip().lower()
    for char in ("/", "\\", " ", "_"):
        cleaned = cleaned.replace(char, "-")
    while "--" in cleaned:
        cleaned = cleaned.replace("--", "-")
    return cleaned.strip("-")


def load_metadata_template() -> dict:
    template_path = PROTOCOL / "metadata_template.json"
    return json.loads(template_path.read_text(encoding="utf-8"))


def destination(asset_type: str, decision: str) -> str:
    if decision == "rejected":
        return "rejected"
    if asset_type == "video":
        return "videos"
    if asset_type == "avatar":
        return "avatars"
    if decision == "approved":
        return "approved"
    if decision == "conditional":
        return "conditional"
    return "rejected"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("--persona", required=True)
    parser.add_argument("--type", required=True, dest="asset_type")
    parser.add_argument("--scene", required=True)
    parser.add_argument("--look", required=True)
    parser.add_argument("--decision", required=True, choices=sorted(DECISIONS))
    parser.add_argument("--base-identity", type=int, default=0)
    parser.add_argument("--persona-score", type=int, default=0)
    parser.add_argument("--confusion-score", type=int, default=0)
    parser.add_argument("--total-score", type=int, default=0)
    parser.add_argument("--notes", default="")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    persona = normalize(args.persona)
    asset_type = normalize(args.asset_type)
    scene = normalize(args.scene)
    look = normalize(args.look)
    decision = normalize(args.decision)

    if persona not in PERSONAS:
        raise SystemExit(f"Invalid persona: {persona}")
    if asset_type not in TYPES:
        raise SystemExit(f"Invalid type: {asset_type}")
    if decision not in DECISIONS:
        raise SystemExit(f"Invalid decision: {decision}")
    if not scene:
        raise SystemExit("Scene cannot be empty after normalization.")
    if not look:
        raise SystemExit("Look cannot be empty after normalization.")

    source = Path(args.source)
    if not source.exists():
        raise SystemExit(f"Missing source file: {source}")
    if not source.is_file():
        raise SystemExit(f"Source is not a file: {source}")
    ext = source.suffix.lower()
    if ext not in EXTS[asset_type]:
        raise SystemExit(f"Invalid extension {ext} for type {asset_type}")

    folder = ROOT / persona / destination(asset_type, decision)
    folder.mkdir(parents=True, exist_ok=True)

    version = 1
    while True:
        filename = f"{persona}_{asset_type}_{scene}_{look}_v{version:02d}{ext}"
        target = folder / filename
        if not target.exists():
            break
        version += 1

    metadata = load_metadata_template()
    metadata.update(
        {
            "persona": persona,
            "asset_type": asset_type,
            "scene": scene,
            "look": look,
            "base_identity_score": args.base_identity,
            "persona_score": args.persona_score,
            "confusion_score": args.confusion_score,
            "total_score": args.total_score,
            "decision": decision,
            "notes": args.notes or None,
        }
    )
    metadata_path = Path(str(target) + ".json")

    if args.dry_run:
        print(f"Dry run: would copy to {target}")
        print(f"Dry run: would write metadata to {metadata_path}")
        return

    shutil.copy2(source, target)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    print(f"Asset: {target}")
    print(f"Metadata: {metadata_path}")


if __name__ == "__main__":
    main()
