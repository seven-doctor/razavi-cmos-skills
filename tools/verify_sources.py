#!/usr/bin/env python3
"""Verify source hashes, page counts, extraction archives, and skill links."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def main() -> int:
    manifest_path = ROOT / "sources" / "source-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for artifact in manifest["artifacts"]:
        path = ROOT / artifact["path"]
        if not path.is_file():
            errors.append(f"missing: {artifact['path']}")
            continue
        actual_hash = sha256(path)
        if actual_hash != artifact["sha256"]:
            errors.append(f"hash mismatch: {artifact['path']} ({actual_hash})")
        if path.suffix.lower() == ".pdf":
            pages = len(PdfReader(str(path)).pages)
            if pages != artifact["pages"]:
                errors.append(f"page mismatch: {artifact['path']} ({pages})")

    for skill_name, expected_chapters in (
        ("razavi-cmos-textbook-skill", 18),
        ("razavi-cmos-solutions-skill", 11),
    ):
        skill_dir = ROOT / skill_name
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"missing skill: {skill_md}")
            continue
        chapter_files = list((skill_dir / "chapters").glob("*.md"))
        if len(chapter_files) != expected_chapters:
            errors.append(f"chapter count: {skill_name} ({len(chapter_files)})")
        body = skill_md.read_text(encoding="utf-8")
        for target in re.findall(r"\]\((chapters/[^)]+)\)", body):
            if not (skill_dir / target).is_file():
                errors.append(f"broken link: {skill_name}/{target}")

    if errors:
        print("SOURCE VERIFICATION FAILED")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("SOURCE VERIFICATION PASSED")
    print(f"- manifest artifacts: {len(manifest['artifacts'])}")
    print("- textbook chapters: 18")
    print("- solutions chapters: 11")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
