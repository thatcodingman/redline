#!/usr/bin/env python3
"""
Adds the Companies / Topics / Stats nav links to any <nav>...</nav> block
(top nav or footer nav) that has an "Archive" link but is missing
"companies.html". Idempotent: skips any nav block that already has
companies.html in it. Run from inside the redline project folder.

Usage:
    python3 fix_missing_nav.py
"""
import re
import os

FILES = [
    "index.html",
    "about.html",
    "contact.html",
    "terms.html",
    "submit.html",
    "methodology.html",
    "404.html",
]

# Matches the Archive link line, capturing its leading whitespace so the
# new lines can match the file's existing indentation exactly.
ARCHIVE_RE = re.compile(
    r'([ \t]*)(<a href="archive\.html"[^>]*>Archive</a>)(\r?\n)'
)

NAV_BLOCK_RE = re.compile(r'<nav\b[^>]*>.*?</nav>', re.DOTALL)


def patch_nav_block(block_text):
    if "companies.html" in block_text:
        return block_text, False  # already patched

    m = ARCHIVE_RE.search(block_text)
    if not m:
        return block_text, False  # no Archive link found in this block

    indent, archive_tag, newline = m.groups()
    insertion = (
        f'{indent}<a href="companies.html">Companies</a>{newline}'
        f'{indent}<a href="topics.html">Topics</a>{newline}'
        f'{indent}<a href="stats.html">Stats</a>{newline}'
    )
    new_block = block_text[: m.end()] + insertion + block_text[m.end():]
    return new_block, True


def patch_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed_any = False

    def repl(match):
        nonlocal changed_any
        new_block, changed = patch_nav_block(match.group(0))
        if changed:
            changed_any = True
        return new_block

    new_content = NAV_BLOCK_RE.sub(repl, content)

    if changed_any:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
    return changed_any


def main():
    updated = []
    skipped = []
    missing = []

    for fname in FILES:
        if not os.path.exists(fname):
            missing.append(fname)
            continue
        if patch_file(fname):
            updated.append(fname)
        else:
            skipped.append(fname)

    print(f"Updated: {len(updated)}")
    for f in updated:
        print(f"  {f}")

    print(f"\nAlready had the links (no change needed): {len(skipped)}")
    for f in skipped:
        print(f"  {f}")

    if missing:
        print(f"\nNot found in this folder: {len(missing)}")
        for f in missing:
            print(f"  {f}")


if __name__ == "__main__":
    main()
