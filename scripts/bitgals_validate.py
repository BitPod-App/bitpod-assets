#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

ROOT = Path("assets/bitgals")
PERSONAS = {"taylor", "ember", "kati", "shiva", "vera"}
TYPES = {"avatar", "image", "video"}
EXTS = {
    "avatar": {"png", "jpg", "jpeg", "webp"},
    "image": {"png", "jpg", "jpeg", "webp"},
    "video": {"mp4", "mov", "webm"},
}
FOLDER_TO_TYPE = {
    "avatars": "avatar",
    "videos": "video",
}
IMAGE_FOLDERS = {"approved", "conditional", "rejected", "refs"}
ALL_FOLDERS = {"refs", "approved", "conditional", "rejected", "avatars", "videos", "metadata"}
PATTERN = re.compile(
    r"^(?P<persona>taylor|ember|kati|shiva|vera)_(?P<asset_type>avatar|image|video)_(?P<scene>[a-z0-9-]+)_(?P<look>[a-z0-9-]+)_v(?P<version>\d{2})\.(?P<ext>png|jpg|jpeg|webp|mp4|mov|webm)$"
)


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    match = PATTERN.match(path.name)
    if not match:
        return [f"Invalid BitGals filename: {path.name}"]

    persona = match.group("persona")
    asset_type = match.group("asset_type")
    ext = match.group("ext")

    if persona not in PERSONAS:
        errors.append(f"Invalid persona in filename: {persona}")
    if asset_type not in TYPES:
        errors.append(f"Invalid asset type in filename: {asset_type}")
    if ext not in EXTS[asset_type]:
        errors.append(f"Extension .{ext} is not allowed for type {asset_type}")

    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return errors

    parts = relative.parts
    if len(parts) < 3:
        errors.append("BitGals asset paths must be under assets/bitgals/{persona}/{category}/")
        return errors

    folder_persona, category = parts[0], parts[1]
    if folder_persona not in PERSONAS:
        errors.append(f"Invalid persona folder: {folder_persona}")
    if category not in ALL_FOLDERS:
        errors.append(f"Invalid BitGals category folder: {category}")
    if folder_persona != persona:
        errors.append(f"Persona folder '{folder_persona}' does not match filename persona '{persona}'")

    if category in FOLDER_TO_TYPE and FOLDER_TO_TYPE[category] != asset_type:
        errors.append(f"Folder '{category}' requires type '{FOLDER_TO_TYPE[category]}', got '{asset_type}'")
    if category in IMAGE_FOLDERS and category != "metadata" and asset_type == "video":
        errors.append(f"Folder '{category}' cannot contain video assets")
    if category in {"approved", "conditional"} and asset_type != "image":
        errors.append(f"Folder '{category}' expects image assets")
    if category == "refs" and asset_type not in {"image", "avatar"}:
        errors.append("Folder 'refs' expects still-image assets of type 'image' or 'avatar'")
    if category == "rejected" and asset_type not in TYPES:
        errors.append(f"Folder '{category}' has invalid asset type '{asset_type}'")
    if category == "metadata":
        errors.append("Metadata files should be validated by their asset filename, not from metadata/ directly")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()

    path = Path(args.path)
    errors = validate(path)
    if errors:
        print(f"FAIL: {path}")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(f"PASS: {path}")
    print("- Filename matches BitGals naming rules")
    print("- Persona and type are valid")
    print("- Extension is compatible with asset type")
    if path.is_relative_to(ROOT):
        print("- Folder category is compatible with this asset")


if __name__ == "__main__":
    main()
