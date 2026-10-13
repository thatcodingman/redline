#!/usr/bin/env python3
"""
Scans every local .html file for internal links (href="...") and reports
any that point at a file that doesn't exist on disk. Ignores external
links (http/https), mailto:, tel:, javascript:, and in-page anchors
(#foo). Handles both absolute ("/archive.html") and relative
("archive.html", "../filings/x.html") link styles.

Run from the redline project root:
    python3 check_links.py
"""
import re
import os
import glob

HREF_RE = re.compile(r'href="([^"]+)"')
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "javascript:", "#")


def resolve(href, source_path):
    # strip any #fragment or ?query before checking the file exists
    path_part = href.split("#", 1)[0].split("?", 1)[0]
    if not path_part:
        return None  # pure anchor link, nothing to check

    if path_part.startswith("/"):
        # absolute from site root
        target = path_part.lstrip("/")
    else:
        # relative to the linking file's own directory
        target = os.path.normpath(os.path.join(os.path.dirname(source_path), path_part))

    return target


def main():
    if not os.path.isdir("filings"):
        print("ERROR: run this from the redline project root (no 'filings' folder found here).")
        return

    html_files = sorted(glob.glob("*.html") + glob.glob("**/*.html", recursive=True))
    html_files = sorted(set(html_files))

    broken = []
    checked = 0

    for source in html_files:
        with open(source, "r", encoding="utf-8") as f:
            content = f.read()

        for href in HREF_RE.findall(content):
            if href.startswith(SKIP_PREFIXES):
                continue
            checked += 1
            target = resolve(href, source)
            if target is None:
                continue
            if not os.path.exists(target):
                broken.append((source, href, target))

    print(f"Checked {checked} internal links across {len(html_files)} pages.\n")

    if not broken:
        print("No broken internal links found.")
        return

    print(f"Broken links found: {len(broken)}\n")
    for source, href, target in broken:
        print(f"  {source}  ->  href=\"{href}\"  (resolved to: {target}, not found)")


if __name__ == "__main__":
    main()
