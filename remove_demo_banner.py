#!/usr/bin/env python3
"""
Removes the stale "EDITORIAL DEMONSTRATION ... not yet applied to any live
filing" banner from methodology.html. (contact.html and submit.html are
being replaced outright with real working forms, so this only needs to
touch methodology.html.) Idempotent - does nothing if already removed.

Run from the redline project root:
    python3 remove_demo_banner.py
"""
PATH = "methodology.html"
BANNER = '''<div class="demo-banner">
  <strong>EDITORIAL DEMONSTRATION</strong> — this methodology describes the intended process; it is not yet applied to any live filing.
</div>

'''


def main():
    with open(PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if BANNER not in content:
        print(f"Banner not found in {PATH} (already removed, or text doesn't match exactly) - no change made.")
        return

    content = content.replace(BANNER, "", 1)

    with open(PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Removed the stale demo banner from {PATH}.")


if __name__ == "__main__":
    main()
