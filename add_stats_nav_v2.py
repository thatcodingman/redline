#!/usr/bin/env python3
"""Adds a 'Stats' link (after 'Topics') to the top nav and footer nav of every
.html file in the current directory tree. Safe to re-run: skips any file that
already links to stats.html. Uses flexible whitespace matching."""
import glob, re

changed, already, unmatched = [], [], []

# Matches <a href="/topics.html"...>Topics</a>  or  <a href="topics.html"...>Topics</a>
# followed by whitespace then <a href="...about.html">About</a>
PATTERN = re.compile(
    r'(<a href="/?topics\.html"[^>]*>Topics</a>)(\s*\n)(\s*)(<a href="/?about\.html"[^>]*>About</a>)'
)

def insert_stats(m, is_relative):
    topics_tag, newline, indent, about_tag = m.groups()
    href = 'stats.html' if is_relative else '/stats.html'
    stats_tag = f'<a href="{href}">Stats</a>'
    return f'{topics_tag}{newline}{indent}{stats_tag}{newline}{indent}{about_tag}'

for path in glob.glob('**/*.html', recursive=True):
    if path.endswith('stats.html'):
        continue
    s = open(path, encoding='utf-8').read()
    if 'href="/stats.html"' in s or 'href="stats.html"' in s:
        already.append(path)
        continue

    def repl(m):
        is_rel = not m.group(1).startswith('<a href="/')
        return insert_stats(m, is_rel)

    new_s, n = PATTERN.subn(repl, s)
    if n > 0:
        open(path, 'w', encoding='utf-8').write(new_s)
        changed.append((path, n))
    else:
        unmatched.append(path)

print(f"Updated: {len(changed)}")
for p, n in changed:
    print(f"  + {p}  ({n} insertion{'s' if n != 1 else ''})")
if already:
    print(f"\nAlready had Stats link: {len(already)}")
    for p in already: print("  =", p)
if unmatched:
    print(f"\nStill no match (needs manual look): {len(unmatched)}")
    for p in unmatched: print("  ?", p)
