#!/usr/bin/env python3
"""
Adds the visible breadcrumb line (<div class="crumbs">...</div>) that
companies.html, topics.html, and every filing page already have, to the
handful of top-level pages that are still missing it. Idempotent - skips
any file that already has class="crumbs". Run from the redline project
root.

Usage:
    python3 add_crumbs.py
"""
import re
import os

# filename -> breadcrumb label (matches the page's own nav link text)
PAGES = {
    "archive.html": "Archive",
    "about.html": "About",
    "contact.html": "Contact",
    "methodology.html": "Methodology",
    "submit.html": "Submit a Filing",
    "terms.html": "Terms",
}

SITE_NAV_RE = re.compile(r'(<nav class="site-nav">.*?</nav>)', re.DOTALL)


def patch_file(path, label):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if 'class="crumbs"' in content:
        return False

    m = SITE_NAV_RE.search(content)
    if not m:
        print(f"  WARNING: no <nav class=\"site-nav\"> found in {path}, skipped.")
        return False

    crumb = f'\n\n<div class="crumbs"><a href="/">Docket</a> / {label}</div>'
    new_content = content[: m.end()] + crumb + content[m.end():]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    updated, skipped, missing = [], [], []

    for fname, label in PAGES.items():
        if not os.path.exists(fname):
            missing.append(fname)
            continue
        if patch_file(fname, label):
            updated.append(fname)
        else:
            skipped.append(fname)

    print(f"Updated: {len(updated)}")
    for f in updated:
        print(f"  {f}")

    print(f"\nAlready had breadcrumbs: {len(skipped)}")
    for f in skipped:
        print(f"  {f}")

    if missing:
        print(f"\nNot found in this folder: {len(missing)}")
        for f in missing:
            print(f"  {f}")


if __name__ == "__main__":
    main()
