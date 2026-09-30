"""List every episode from the SoundCloud feed and write one model input per transcribed episode.

    python scripts/episodes/build_inputs.py --transcripts PATH/TO/transcripts --manifest PATH/TO/manifest.json

The transcripts and their manifest come from the microbinfie-book pipeline (Whisper large-v3 plus
speaker diarisation, with a domain vocabulary pass); they are not kept in this repository. Writes
scripts/episodes/work/episodes.json (every episode, whether or not it has a transcript or a post)
and scripts/episodes/work/in/<id>.md (show notes plus transcript, the whole brief for one call).
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from pathlib import Path

from defusedxml import ElementTree

HERE = Path(__file__).resolve().parent
SITE = HERE.parent.parent
WORK = HERE / "work"
RSS = "https://feeds.soundcloud.com/users/soundcloud:users:698218776/sounds.rss"
ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"


def feed() -> list[dict]:
    root = ElementTree.fromstring(urllib.request.urlopen(RSS, timeout=60).read())
    out = []
    for it in root.iter("item"):
        guid = it.findtext("guid") or ""
        out.append({
            "title": (it.findtext("title") or "").strip(),
            "link": (it.findtext("link") or "").strip().rstrip("/"),
            "pubdate": it.findtext("pubDate"),
            "track": guid.split("/")[-1],
            "notes": (it.findtext(f"{ITUNES}summary") or it.findtext("description") or "").strip(),
            "duration": it.findtext(f"{ITUNES}duration"),
        })
    return out


def existing_posts() -> dict[str, str]:
    posts = {}
    for p in (SITE / "_posts").glob("*.md"):
        m = re.search(r"^link:\s*(\S+)", p.read_text(encoding="utf-8"), re.MULTILINE)
        if m:
            posts[m.group(1).rstrip("/")] = p.name
    return posts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcripts", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    a = ap.parse_args()
    manifest = {e["link"].rstrip("/"): e for e in json.loads(a.manifest.read_text())["episodes"]}
    posts = existing_posts()
    (WORK / "in").mkdir(parents=True, exist_ok=True)
    episodes = []
    for item in feed():
        m = manifest.get(item["link"])
        eid = m["id"] if m else None
        tx = a.transcripts / f"{eid}.md" if eid else None
        has_tx = bool(tx and tx.exists())
        episodes.append({**item, "id": eid, "date": m["date"] if m else None,
                         "has_transcript": has_tx, "post": posts.get(item["link"])})
        if has_tx:
            (WORK / "in" / f"{eid}.md").write_text(
                f"# EPISODE {eid}\n\nTitle: {item['title']}\nDate: {m['date']}\n"
                f"SoundCloud: {item['link']}\n\n## Show notes\n\n{item['notes']}\n\n"
                f"## Transcript\n\n{tx.read_text()}", encoding="utf-8")
    (WORK / "episodes.json").write_text(json.dumps(episodes, indent=1), encoding="utf-8")
    n_tx = sum(e["has_transcript"] for e in episodes)
    print(f"{len(episodes)} episodes in the feed, {n_tx} with transcripts, "
          f"{sum(bool(e['post']) for e in episodes)} with an existing post")


if __name__ == "__main__":
    main()
