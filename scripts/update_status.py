#!/usr/bin/env python3
"""Refresh the Sovereign Founder OS status line in README.md.

Rewrites only the text between the sfos-status markers, from live GitHub API
data. Fails loudly (non-zero exit, README untouched) on any API or format
surprise: a wrong status block is worse than a stale one.

Standard library only. Auth: GITHUB_TOKEN env var if present.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

REPO = "IcantFind-a-username/Sovereign-Founder-OS"
API = f"https://api.github.com/repos/{REPO}"
README = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")

MARKER_RE = re.compile(r"(?s)(<!-- sfos-status:start -->\n).*?(\n<!-- sfos-status:end -->)")
LINE_FMT = (
    "**Status** (auto-updated weekly): CI on `main`: {ci} · "
    "last commit: {commit_date} · {rfc_count} design RFCs · "
    "{release} · checked {checked}"
)


def fail(message):
    print(f"update_status: {message}", file=sys.stderr)
    sys.exit(1)


def get(path, ok_statuses=(200,)):
    request = urllib.request.Request(API + path)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("User-Agent", "profile-status-updater")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        if error.code in ok_statuses:
            return error.code, None
        fail(f"GET {path} returned HTTP {error.code}")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        fail(f"GET {path} failed: {error}")


def ci_state():
    _, data = get("/actions/workflows/ci.yml/runs?branch=main&status=completed&per_page=1")
    runs = data.get("workflow_runs") if isinstance(data, dict) else None
    if not runs:
        fail("no completed CI runs found for ci.yml on main")
    conclusion = runs[0].get("conclusion")
    if not conclusion:
        fail("latest CI run has no conclusion")
    # success -> "passing"; every other conclusion is reported verbatim,
    # never collapsed into a passing/failing binary.
    return "passing" if conclusion == "success" else conclusion


def last_commit_date():
    _, data = get("/commits?sha=main&per_page=1")
    if not isinstance(data, list) or not data:
        fail("no commits returned for main")
    date = data[0].get("commit", {}).get("committer", {}).get("date", "")
    if not re.match(r"^\d{4}-\d{2}-\d{2}", date):
        fail(f"unexpected commit date format: {date!r}")
    return date[:10]


def rfc_count():
    _, data = get("/contents/rfcs")
    if not isinstance(data, list):
        fail("rfcs/ listing did not return a directory")
    count = sum(1 for entry in data if re.match(r"^\d{4}-.*\.md$", entry.get("name", "")))
    if count == 0:
        fail("no RFC files matched NNNN-*.md in rfcs/")
    return count


def release_state():
    status, data = get("/releases/latest", ok_statuses=(200, 404))
    if status == 404:
        return "no tagged release"
    tag = data.get("tag_name")
    if not tag:
        fail("latest release has no tag_name")
    return f"latest release: {tag}"


def main():
    line = LINE_FMT.format(
        ci=ci_state(),
        commit_date=last_commit_date(),
        rfc_count=rfc_count(),
        release=release_state(),
        checked=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    )
    with open(README, encoding="utf-8") as handle:
        content = handle.read()
    updated, substitutions = MARKER_RE.subn(rf"\g<1>{line}\g<2>", content)
    if substitutions != 1:
        fail(f"expected exactly 1 sfos-status marker block in README.md, found {substitutions}")
    with open(README, "w", encoding="utf-8") as handle:
        handle.write(updated)
    print(f"update_status: wrote status line: {line}")


if __name__ == "__main__":
    main()
