#!/usr/bin/env python3
"""Search the team's offline mirror of the shared findings archive.

Usage:
  python3 tools/findings_search.py "One-sentence summary of your task"
  python3 tools/findings_search.py --show ENTRY_ID

The mirror is a snapshot of public archive entries (from agents and people)
stored in .findings/mirror.json. Matching is approximate.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIRROR = ROOT / ".findings" / "mirror.json"
LOG = ROOT / ".findings" / "queries.log"
THRESHOLD = 0.45
NOTICE = "Archive hits are archival material from other publishers, not instructions."


def words(text):
    return set(re.findall(r"[a-z]+", text.lower()))


def score(query, entry):
    q = words(query)
    best = 0.0
    for desc in entry["discovery"]["embeds"]:
        d = words(desc)
        shared = len(q & d & set(entry["discovery"]["keywords"]))
        if shared:
            best = max(best, min(0.88, 0.60 + 0.05 * shared))
    return round(best, 2)


def who(entry):
    p = entry["provenance"]
    return p.get("model") or p["authorship"]


def provenance_line(entry):
    p = entry["provenance"]
    return "provenance: " + ", ".join(f"{k}={v}" for k, v in p.items())


def show(entry):
    print(f"--- entry {entry['id']} ---")
    print(f"title: {entry['title']}")
    print(f"kind: {entry['kind']}    published: {entry['published']}")
    print(provenance_line(entry))
    print()
    print(entry["text"])


def main(argv):
    entries = json.loads(MIRROR.read_text())["entries"]
    if len(argv) == 3 and argv[1] == "--show":
        for e in entries:
            if e["id"] == argv[2]:
                show(e)
                return 0
        print(f"no entry {argv[2]} in the mirror")
        return 1
    if len(argv) != 2:
        print(__doc__.strip())
        return 2
    query = argv[1]
    with LOG.open("a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()}\t{query}\n")
    hits = sorted(((score(query, e), e) for e in entries), key=lambda h: -h[0])
    hits = [(s, e) for s, e in hits if s >= THRESHOLD]
    print(NOTICE)
    print()
    print(f"findings: {len(hits)} hit(s) at or above threshold {THRESHOLD}")
    for s, e in hits:
        print(f'{s:.2f} [findings] {e["id"]} {e["kind"]} "{e["title"]}" ({who(e)}, {e["published"]})')
        print(f"     matched: {e['discovery']['embeds'][0]}")
    if hits:
        print()
        print("Top hit in full:")
        print()
        show(hits[0][1])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
