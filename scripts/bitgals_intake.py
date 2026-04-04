#!/usr/bin/env python3
import argparse
import json
import shutil
from pathlib import Path

ROOT = Path("assets/bitgals")
PERSONAS = {"taylor", "orange", "kati", "shiva", "vera"}
TYPES = {"avatar", "image", "video"}
EXTS = {
    "avatar": {".png", ".jpg", ".jpeg", ".webp"},
    "image": {".png", ".jpg", ".jpeg", ".webp"},
    "video": {".mp4", ".mov", ".webm"},
}


def normalize(text: str) -> str:
    return text.strip().lower().replace(" ", "-").replace("/", "-")


def destination(asset_type: str, decision: str) -> str:
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
    parser.add_argument("--decision", required=True, choices=["approved", "conditional", "rejected"])
    parser.add_argument("--base-identity", type=int, default=0)
    parser.add_argument("--persona-score", type=int, default=0)
    parser.add_argument("--confusion-score", type=int, default=0)
    parser.add_argument("--total-score", type=int, default=0)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    persona = normalize(args.persona)
    asset_type = normalize(args.asset_type)
    scene = normalize(args.scene)
    look = normalize(args.look)

    if persona not in PERSONAS:
        raise SystemExit(f"Invalid persona: {persona}")
    if asset_type not in TYPES:
        raise SystemExit(f"Invalid type: {asset_type}")

    source = Path(args.source)
    if not source.exists():
        raise SystemExit(f"Missing source file: {source}")
    ext = source.suffix.lower()
    if ext not in EXTS[asset_type]:
        raise SystemExit(f"Invalid extension {ext} for type {asset_type}")

    folder = ROOT / persona / destination(asset_type, args.decision)
    folder.mkdir(parents=True, exist_ok=True)

    version = 1
    while True:
        filename = f"{persona}_{asset_type}_{scene}_{look}_v{version:02d}{ext}"
        target = folder / filename
        if not target.exists():
            break
        version += 1

    shutil.copy2(source, target)

    metadata = {
        "persona": persona,
        "asset_type": asset_type,
        "scene": scene,
        "look": look,
        "base_identity_score": args.base_identity,
        "persona_score": args.persona_score,
        "confusion_score": args.confusion_score,
        "total_score": args.total_score,
        "decision": args.decision,
        "hard_fail_reasons": [],
        "required_anchors_present": [],
        "missing_required_anchors": [],
        "forbidden_traits_detected": [],
        "notes": args.notes,
    }
    metadata_path = Path(str(target) + ".json")
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(target)
    print(metadata_path)


if __name__ == "__main__":
    main()
