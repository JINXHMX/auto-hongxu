#!/usr/bin/env python3
"""Validate spoken-copy character counts; input is a UTF-8 JSON list of strings."""
import argparse
import json
import sys
import unicodedata
from pathlib import Path


def count_chars(text: str, include_punctuation: bool = False) -> int:
    return sum(
        1 for char in text
        if not char.isspace()
        and (include_punctuation or not unicodedata.category(char).startswith("P"))
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="UTF-8 JSON array of copy strings")
    parser.add_argument("--target", type=int, help="Required exact character count")
    parser.add_argument("--min-chars", type=int, help="Minimum characters per copy")
    parser.add_argument("--max-chars", type=int, help="Maximum characters per copy")
    parser.add_argument("--lines", type=int, help="Required number of nonblank lines; reject blank lines")
    parser.add_argument("--equal", action="store_true", help="Require identical lengths")
    parser.add_argument("--include-punctuation", action="store_true")
    args = parser.parse_args()
    if any(n is not None and n < 0 for n in (args.target, args.min_chars, args.max_chars)):
        parser.error("Character limits must be nonnegative")
    if args.min_chars is not None and args.max_chars is not None and args.min_chars > args.max_chars:
        parser.error("--min-chars must not exceed --max-chars")
    if args.lines is not None and args.lines < 1:
        parser.error("--lines must be positive")
    try:
        copies = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        parser.error(str(error))
    if not isinstance(copies, list) or not copies or not all(isinstance(c, str) for c in copies):
        parser.error("Input must be a non-empty JSON array of strings")
    lengths = [count_chars(c, args.include_punctuation) for c in copies]
    equal = len(set(lengths)) == 1
    target_ok = args.target is None or all(n == args.target for n in lengths)
    range_ok = all((args.min_chars is None or n >= args.min_chars) and
                   (args.max_chars is None or n <= args.max_chars) for n in lengths)
    rows = [c.replace("\r\n", "\n").split("\n") for c in copies]
    lines_ok = args.lines is None or all(len(r) == args.lines and all(line.strip() for line in r) for r in rows)
    passed = target_ok and range_ok and lines_ok and (not args.equal or equal)
    print(json.dumps({"lengths": lengths, "all_equal": equal, "target": args.target,
                      "range_ok": range_ok, "line_counts": [len(r) for r in rows],
                      "lines_ok": lines_ok, "include_punctuation": args.include_punctuation,
                      "pass": passed}, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
