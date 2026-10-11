"""Write one post per episode: the checked article, the player, and the original show notes.

    python scripts/episodes/render.py

Every episode in work/episodes.json gets exactly one post. An episode that already has a post
keeps its file name (so its URL does not change) and its original show notes, which are read from
origin/main every time, so running this again gives the same result. Episodes without a post get a
new one named the way scripts/import_microbinfie.py names them. An episode with no transcript yet
gets its show notes and the player, and no article.
"""

from __future__ import annotations

import json
import re
import subprocess
import textwrap
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
SITE = HERE.parent.parent
WORK = HERE / "work"
POSTS = SITE / "_posts"
ROLES_ON_AIR = ("host", "guest", "panellist")
# Links in the old hand-written notes for episodes 67 and 68 that pointed at a source file (never
# a URL) — and, for part 1, at itself. They now point at the right episode's page.
LINK_FIXES = {
    "[part 2](/_posts/2021-11-25-67_bacterial_taxonomy_what_is.md)":
        "[part 2]({% post_url 2021-12-09-whats-in-a-name-part-2 %})",
    "[part 1 here](/_posts/2021-11-25-67_bacterial_taxonomy_what_is.md)":
        "[part 1 here]({% post_url 2021-11-25-whats-in-a-name-part-1 %})",
}


def original(name: str) -> str | None:
    r = subprocess.run(["git", "-C", str(SITE), "show", f"origin/main:_posts/{name}"],
                       capture_output=True, text=True, check=False)
    return r.stdout if r.returncode == 0 else None


def split_front(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, text)


def number_and_title(ep: dict) -> tuple[str, str]:
    t = ep["title"].strip()
    m = re.match(r"^Encore:\s*(\d+)\s*[-–:]?\s*(.*)$", t, re.IGNORECASE)
    if m:
        return f"encore-{int(m.group(1))}", f"Encore of episode {int(m.group(1))}: {m.group(2).strip()}"
    m = re.match(r"^(\d+)\s*[-–:]?\s*(.*)$", t)
    if not m:
        return "", t
    rest = re.sub(r"^micro\s*binfie\s*[-–:]\s*", "", m.group(2).strip(), flags=re.IGNORECASE)
    rest = rest[:1].upper() + rest[1:]
    return str(int(m.group(1))), f"Episode {int(m.group(1))}: {rest}"


def seek(link: str, t: str) -> str:
    h, m, s = (int(x) for x in t.split(":"))
    return f"{link}#t={h}:{m:02d}:{s:02d}" if h else f"{link}#t={m}:{s:02d}"


def embed(track: str, link: str, title: str) -> str:
    return (f'<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" '
            f'title="{title}" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/'
            f'tracks/{track}&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true'
            f'&show_user=true&show_reposts=false&show_teaser=false"></iframe>\n\n'
            f'[Listen to {title} on SoundCloud]({link})')


def old_show_notes(body: str) -> str:
    """An existing post's own text, minus the old player (whose caption named the wrong episode)."""
    body = re.sub(r"<iframe.*?</iframe>(<div.*?</div>)?", "", body, flags=re.DOTALL)
    body = re.sub(r"^#\s+", "### ", body, flags=re.MULTILINE)
    return body.strip()


def feed_show_notes(notes: str) -> str:
    notes = re.sub(r"(?<![<(\[])(https?://[^\s<>)]+[^\s<>).,;:!?])", r"<\1>", notes)
    paras = [p.strip() for p in re.split(r"\n\s*\n", notes) if p.strip()]
    return "\n\n".join(p if re.match(r"^[-*] ", p) else textwrap.fill(" ".join(p.split()), 95)
                       for p in paras)


def article_body(a: dict, link: str) -> str:
    out = [f"*{a['headline']}*", "", a["summary"].strip(), ""]
    return "\n".join(out)


def article_sections(a: dict, link: str) -> str:
    out = ["## In this episode", ""]
    for s in a.get("sections", []):
        out += [f"### {s['heading'].strip()}", "", s["body"].strip(), ""]
    if a.get("highlights"):
        out += ["## Highlights", ""]
        out += [f"- [{h['time']}]({seek(link, h['time'])}) — {h['topic']}" for h in a["highlights"]]
        out.append("")
    if a.get("quotes"):
        out += ["## In their own words", ""]
        for q in a["quotes"]:
            credit = f"> — {q['speaker']}, [{q['time']}]({seek(link, q['time'])})"
            out += [f"> {q['text'].strip()}", ">", credit, ""]
    on_air = [p for p in a.get("people", []) if p.get("role") in ROLES_ON_AIR]
    mentioned = [p for p in a.get("people", []) if p.get("role") not in ROLES_ON_AIR]
    if on_air:
        out += ["## Who is talking", ""]
        for p in on_air:
            aff = f", {p['affiliation']}" if p.get("affiliation") and p["role"] != "host" else ""
            out.append(f"- **{p['name']}** ({p['role']}{aff})")
        out.append("")
    if mentioned:
        out += ["Also mentioned: " + ", ".join(p["name"] for p in mentioned) + ".", ""]
    if a.get("tools"):
        out += ["## Tools and resources mentioned", "", ", ".join(a["tools"]) + ".", ""]
    if a.get("faq"):
        out += ["## Questions this episode answers", ""]
        for f in a["faq"]:
            out += [f"### {f['q'].strip()}", "", f["a"].strip(), ""]
    note = ("*This page was written from a machine transcript of the episode and checked against "
            "it. Listen to the episode for the whole conversation.*")
    out += [note, ""]
    return "\n".join(out)


def main() -> None:
    episodes = json.loads((WORK / "episodes.json").read_text())
    by_number = {}
    for p in POSTS.glob("*.md"):
        fm, _ = split_front(p.read_text(encoding="utf-8"))
        if "link" not in fm:
            m = re.search(r"Episode\s+(\d+)", str(fm.get("title", "")))
            if m:
                by_number[str(int(m.group(1)))] = p.name
    written = 0
    for ep in episodes:
        number, title = number_and_title(ep)
        name = ep.get("post") or by_number.get(number)
        orig_fm, orig_body = split_front(original(name) or "") if name else ({}, "")
        # Episodes 67 and 68 each had a second, hand-written post with no link and richer notes.
        # Its notes become this page's show notes; its file goes and its URL redirects here.
        redirect_from = []
        twin = by_number.get(number) if ep.get("post") else None
        if twin and twin != name:
            twin_fm, twin_body = split_front(original(twin) or "")
            if twin_body.strip():
                orig_body = twin_body
            day = str(twin_fm.get("date", twin[:10]))[:10].replace("-", "/")
            redirect_from.append(f"/{day}/{Path(twin).stem[11:]}.html")
            (POSTS / twin).unlink(missing_ok=True)
        if not name:
            day = parsedate_to_datetime(ep["pubdate"]).strftime("%Y-%m-%d")
            name = f"{day}-{ep['link'].rstrip('/').split('/')[-1]}.md"
        date = orig_fm.get("date") or parsedate_to_datetime(ep["pubdate"]).strftime("%Y-%m-%d 00:00:00")
        if isinstance(date, datetime):
            date = date.strftime("%Y-%m-%d %H:%M:%S")
        art = None
        if ep.get("id") and (WORK / "final" / f"{ep['id']}.json").exists():
            art = json.loads((WORK / "final" / f"{ep['id']}.json").read_text())
        fm = {"layout": "page", "title": title, "date": str(date), "link": ep["link"],
              "episode": number, "soundcloud_track": ep["track"],
              "tags": ["microbinfie", "podcast"]}
        if redirect_from:
            fm["redirect_from"] = redirect_from
        notes = old_show_notes(orig_body) if orig_body.strip() else feed_show_notes(ep["notes"])
        for bad, good in LINK_FIXES.items():
            notes = notes.replace(bad, good)
        if art:
            fm.update({"description": art["description"], "excerpt": art["description"],
                       "headline": art["headline"],
                       "guests": [p["name"] for p in art.get("people", [])
                                  if p.get("role") in ("guest", "panellist")],
                       "topics": art.get("topics", []),
                       "faq": [{"q": f["q"], "a": f["a"]} for f in art.get("faq", [])]})
            body = "\n".join([article_body(art, ep["link"]), embed(ep["track"], ep["link"], title), "",
                              article_sections(art, ep["link"]), "## Show notes", "", notes, ""])
        else:
            first = re.sub(r"<[^>]+>|[*_`#>]|\[|\]\([^)]*\)", "", notes)
            first = re.sub(r"\s+", " ", first).strip()
            fm.update({"description": first[:157].rsplit(" ", 1)[0] + ("…" if len(first) > 157 else ""),
                       "excerpt": first[:157].rsplit(" ", 1)[0] + ("…" if len(first) > 157 else "")})
            body = "\n".join([embed(ep["track"], ep["link"], title), "", "## Show notes", "", notes, ""])
        front = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
        (POSTS / name).write_text(f"---\n{front}---\n\n{body}", encoding="utf-8")
        written += 1
    print(f"{written} episode posts written into {POSTS}")


if __name__ == "__main__":
    main()
