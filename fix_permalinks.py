#!/usr/bin/env python3
"""
Fixes the two broken "Permalink to this filing" links on the homepage
that point at the literal string filings/None.html. The first occurrence
belongs to the PayPal filing, the second to the Best Buy filing (confirmed
by reading the surrounding case-footer content). Idempotent - does
nothing if the broken links are already gone.

Run from the redline project root:
    python3 fix_permalinks.py
"""
import re

PATH = "index.html"
BROKEN = '<a href="filings/None.html">Permalink to this filing &rarr;</a>'
REPLACEMENTS = [
    '<a href="filings/paypal-privacy-statement-amendment-sept-2026.html">Permalink to this filing &rarr;</a>',
    '<a href="filings/best-buy-terms-digital-agent-restrictions.html">Permalink to this filing &rarr;</a>',
]


def main():
    with open(PATH, "r", encoding="utf-8") as f:
        content = f.read()

    count = content.count(BROKEN)
    if count == 0:
        print("No broken permalinks found - nothing to do.")
        return
    if count != len(REPLACEMENTS):
        print(f"WARNING: expected exactly {len(REPLACEMENTS)} broken permalinks, found {count}. Aborting to be safe.")
        return

    for replacement in REPLACEMENTS:
        content = content.replace(BROKEN, replacement, 1)

    with open(PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fixed {len(REPLACEMENTS)} permalink(s) in {PATH}:")
    for r in REPLACEMENTS:
        print(f"  {r}")


if __name__ == "__main__":
    main()
