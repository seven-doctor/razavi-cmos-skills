#!/usr/bin/env python3
"""Search OCR or text-bearing PDFs and report matching page numbers."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from pypdf import PdfReader


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("query", help="literal text or a regular expression")
    parser.add_argument("--regex", action="store_true", help="treat query as regex")
    parser.add_argument("--context", type=int, default=180, help="characters around each match")
    args = parser.parse_args()

    reader = PdfReader(str(args.pdf))
    pattern = re.compile(args.query, re.IGNORECASE) if args.regex else None
    hits = 0
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        match = pattern.search(text) if pattern else re.search(re.escape(args.query), text, re.IGNORECASE)
        if not match:
            continue
        start = max(0, match.start() - args.context)
        end = min(len(text), match.end() + args.context)
        snippet = re.sub(r"\s+", " ", text[start:end]).strip()
        print(f"page={page_number}: {snippet}")
        hits += 1
    print(f"matches={hits}; pages={len(reader.pages)}")
    return 0 if hits else 1


if __name__ == "__main__":
    raise SystemExit(main())
