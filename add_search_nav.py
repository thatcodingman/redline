#!/usr/bin/env python3
"""
Adds the "Search" nav link to every <nav>...</nav> block sitewide that has
a Stats link but is missing search.html. Handles both relative
(href="stats.html") and absolute (href="/stats.html") link styles, since
different pages on this site use different conventions. Idempotent -
skips any nav block that already has search.html / /search.html. Run
from the redline project root.

Usage:
    python3 add_search_nav.py
"""
import re
import glob

STATS_RE = re.compile(
    r'([ \t]*)(<a href="/?stats\.html"[^>]*>Stats</a>)(\r?\n)'
)
NAV_BLOCK_RE = re.compile(r'<nav\b[^>]*>.*?</nav>', re.DOTALL)

TARGET_GLOBS = [
    "*.html",
    "filings/*.html",
    "companies/*.html",
    "topics/*.html",
]
SKIP_FILES = {"search.html"}


def patch_nav_block(block_text):
    if "search.html" in block_text:
        return block_text, False

    m = STATS_RE.search(block_text)
    if not m:
        return block_text, False

    indent, stats_tag, newline = m.groups()
    # match this page's own convention: absolute if the Stats link was
    # absolute, relative otherwise
    href = "/search.html" if '"/stats.html"' in stats_tag else "search.html"
    insertion = f'{indent}<a href="{href}">Search</a>{newline}'
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
    files = set()
    for pattern in TARGET_GLOBS:
        files.update(glob.glob(pattern))
    files = sorted(f for f in files if f not in SKIP_FILES)

    updated, skipped = [], []
    for path in files:
        if patch_file(path):
            updated.append(path)
        else:
            skipped.append(path)

    print(f"Updated: {len(updated)}")
    for f in updated:
        print(f"  {f}")

    print(f"\nAlready had the link / no Stats link found: {len(skipped)}")
    for f in skipped:
        print(f"  {f}")


if __name__ == "__main__":
    main()
