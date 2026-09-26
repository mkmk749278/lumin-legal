#!/usr/bin/env python3
"""Checks the published legal documents before they deploy (2026-09-26).

These pages are load-bearing: the Lumin app links /privacy, /terms and /risk
(lumin-app `lib/data/legal_urls.dart`) and the Google Play listing links the
privacy policy and /delete-account. A renamed or deleted file is a 404 on a
Play-policy-required URL, and nothing in this repo noticed until now.

Fails on:
  * a published document missing (CLAUDE.md: never delete or rename one);
  * a document without a valid `**Last updated:** YYYY-MM-DD` near the top,
    or one dated in the future;
  * a relative link to a file that does not exist.
Warns (does not fail) when a PR changes a document's text without touching its
"Last updated" line — CLAUDE.md asks for the bump on a MATERIAL change, and
whether a change is material is the reviewer's call, not a regex's.

Lives under .github/ because the repo root is what GitHub Pages publishes.

    python .github/scripts/check_published.py [--base <git-ref>]
"""
from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

#: Linked from outside this repo — the app (privacy/terms/risk), Play Console
#: (privacy, delete-account), and the site root (index).
PUBLISHED = ["index.md", "privacy.md", "terms.md", "risk.md", "delete-account.md"]

LAST_UPDATED = re.compile(r"^\*\*Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})\s*$", re.M)
LINK = re.compile(r"\]\((?!https?:|mailto:|#)([^)#\s]+)")


def problems(root: Path = ROOT, today: dt.date | None = None) -> list[str]:
    today = today or dt.datetime.now(dt.timezone.utc).date()
    out: list[str] = []
    for name in PUBLISHED:
        path = root / name
        if not path.exists():
            out.append(f"{name}: missing — the app or Play Console links this exact path")
            continue
        head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:15])
        m = LAST_UPDATED.search(head)
        if not m:
            out.append(f"{name}: no '**Last updated:** YYYY-MM-DD' line near the top")
            continue
        try:
            date = dt.date.fromisoformat(m.group(1))
        except ValueError:
            out.append(f"{name}: 'Last updated' is not a real date: {m.group(1)}")
            continue
        # A day of slack: the author's IST date can be a day ahead of UTC.
        if date > today + dt.timedelta(days=1):
            out.append(f"{name}: 'Last updated' {date} is in the future")
    for path in sorted(root.glob("*.md")):
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if not (root / target).resolve().exists():
                out.append(f"{path.name}: link to missing file {target}")
    return out


def unbumped(base: str, root: Path = ROOT) -> list[str]:
    """Published documents whose text changed since [base] with the same
    'Last updated' line."""
    warn = []
    for name in PUBLISHED:
        diff = subprocess.run(
            ["git", "diff", "--unified=0", base, "--", name],
            cwd=root, capture_output=True, text=True, check=False,
        ).stdout
        changed = [ln for ln in diff.splitlines()
                   if ln[:1] in "+-" and not ln.startswith(("+++", "---"))]
        if changed and not any("Last updated" in ln for ln in changed):
            warn.append(name)
    return warn


def main(argv: list[str]) -> int:
    found = problems()
    for p in found:
        print(f"::error::{p}")
    if "--base" in argv:
        for name in unbumped(argv[argv.index("--base") + 1]):
            print(f"::warning file={name}::{name} changed without a 'Last updated' "
                  "bump — bump it if the change is material (CLAUDE.md)")
    if found:
        return 1
    print(f"Published documents OK: {', '.join(PUBLISHED)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
