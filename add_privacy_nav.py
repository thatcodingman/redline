#!/usr/bin/env python3
"""
Adds the "Privacy" nav link to every <nav>...</nav> block sitewide, right
after the Terms link. Handles both relative (href="terms.html") and
absolute (href="/terms.html") link styles. Idempotent - skips any nav
block that already has privacy.html. Run from the redline project root.

Usage:
    python3 add_privacy_nav.py
"""
import re
import glob

TERMS_RE = re.compile(
    r'([ \t]*)(<a href="/?terms\.html"[^>]*>Terms</a>)(\r?\n)'
)
NAV_BLOCK_RE = re.compile(r'<nav\b[^>]*>.*?</nav>', re.DOTALL)

TARGET_GLOBS = [
    "*.html",
    "filings/*.html",
    "companies/*.html",
    "topics/*.html",
]
SKIP_FILES = {"privacy.html"}


def patch_nav_block(block_text):
    if "privacy.html" in block_text:
        return block_text, False

    m = TERMS_RE.search(block_text)
    if not m:
        return block_text, False

    indent, terms_tag, newline = m.groups()
    href = "/privacy.html" if '"/terms.html"' in terms_tag else "privacy.html"
    insertion = f'{indent}<a href="{href}">Privacy</a>{newline}'
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

    print(f"\nAlready had the link / no Terms link found: {len(skipped)}")
    for f in skipped:
        print(f"  {f}")


if __name__ == "__main__":
    main()
