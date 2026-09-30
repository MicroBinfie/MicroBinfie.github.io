"""Check the built site the way a reader and a crawler meet it. Fails loudly; prints every problem.

    python scripts/check_site.py _site [scripts/episodes/work/episodes.json]

- No Markdown or HTML survives as visible text (a heading's hashes, **, stray emphasis
  asterisks, link or footnote syntax, backticks, escapes, comments, table pipes, tags).
- Every internal link and asset reference resolves to a file in the built site.
- Every JSON-LD block parses as JSON.
- With the episode list: every episode has exactly one page, and the Episodes page and llms.txt
  link to all of them.
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

LEAKS = [
    ("heading marker", re.compile(r"(?:^|[\s“\"])#{1,6}(?=\s|$)", re.MULTILINE)),
    ("bold marker", re.compile(r"\*\*|__\w")),
    ("emphasis asterisk", re.compile(r"(?:^|[\s(“\"‘])\*(?=[\w“\"‘])|\w\*\w", re.MULTILINE)),
    ("backslash escape", re.compile(r"\\[*_#`\[\]{}<>|]")),
    ("HTML tag", re.compile(r"</?(?:sup|sub|div|span|em|strong|br|p|a|i|b|img|iframe)\b[^>]*>", re.IGNORECASE)),
    ("link syntax", re.compile(r"\]\(|\[[^\]]+\]\[\d*\]")),
    ("liquid", re.compile(r"\{\{|\{%|%\}")),
    ("code backtick", re.compile(r"`")),
    ("HTML comment", re.compile(r"<!--|-->")),
    ("table pipe row", re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE)),
]


class Page(HTMLParser):
    SKIP = frozenset({"script", "style", "head", "title", "code", "pre", "svg", "noscript"})

    def __init__(self) -> None:
        super().__init__()
        self.text: list[str] = []
        self.links: list[str] = []
        self.jsonld: list[str] = []
        self._skip = 0
        self._ld = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.SKIP:
            self._skip += 1
        if tag == "script" and a.get("type") == "application/ld+json":
            self._ld = True
            self.jsonld.append("")
        for key in ("href", "src"):
            if a.get(key) and tag in ("a", "img", "link", "script", "iframe"):
                self.links.append(a[key])
        if tag in ("p", "div", "li", "br", "tr", "h1", "h2", "h3", "h4", "blockquote"):
            self.text.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self._skip -= 1
        if tag == "script":
            self._ld = False

    def handle_data(self, data):
        if self._ld:
            self.jsonld[-1] += data
        elif not self._skip:
            self.text.append(data)


def resolves(site: Path, page: Path, ref: str) -> bool:
    u = urlparse(ref)
    if u.scheme or ref.startswith(("#", "mailto:", "//", "data:", "javascript:")):
        return True
    path = unquote(u.path)
    target = (site / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
    return target.exists() or target.with_suffix(".html").exists() or (target / "index.html").exists()


def main(site: Path, episodes_json: Path | None) -> int:
    problems = []
    urls = {}
    for page in sorted(site.rglob("*.html")):
        if "assets/book" in str(page):
            continue  # the book's own single-page HTML edition is checked by the book's build
        p = Page()
        p.feed(page.read_text(encoding="utf-8", errors="replace"))
        text = "".join(p.text)
        rel = page.relative_to(site)
        urls["/" + str(rel)] = text
        for label, pat in LEAKS:
            for m in pat.finditer(text):
                ctx = re.sub(r"\s+", " ", text[max(0, m.start() - 40): m.end() + 40]).strip()
                problems.append(f"{rel}: {label}: …{ctx}…")
        for ref in p.links:
            if not resolves(site, page, ref):
                problems.append(f"{rel}: broken link {ref}")
        for block in p.jsonld:
            try:
                json.loads(block)
            except json.JSONDecodeError as e:
                problems.append(f"{rel}: JSON-LD does not parse ({e})")
    if episodes_json:
        episodes = json.loads(episodes_json.read_text())
        listing = urls.get("/pages/Episodes.html", "")
        llms = (site / "llms.txt").read_text() if (site / "llms.txt").exists() else ""
        posts = [u for u in urls if re.match(r"^/\d{4}/", u)]
        for ep in episodes:
            if not any(ep["link"] in (site / u.lstrip("/")).read_text() for u in posts):
                problems.append(f"episode has no page: {ep['title']}")
            if ep["link"] not in llms:
                problems.append(f"llms.txt misses: {ep['title']}")
        n_list = listing.count("Listen on SoundCloud")
        if n_list != len(episodes):
            problems.append(f"Episodes page lists {n_list} episodes, the feed has {len(episodes)}")
        pages_per_link: dict[str, int] = {}
        for u in posts:
            body = (site / u.lstrip("/")).read_text()
            for ep in episodes:
                if f'"contentUrl":"{ep["link"]}"' in body.replace(" ", ""):
                    pages_per_link[ep["link"]] = pages_per_link.get(ep["link"], 0) + 1
        for link, n in pages_per_link.items():
            if n > 1:
                problems.append(f"{n} pages claim episode {link}")
    known_file = Path(__file__).with_name("check_site_known.txt")
    known = [line.strip() for line in known_file.read_text().splitlines()
             if line.strip() and not line.startswith("#")] if known_file.exists() else []
    real = [pr for pr in problems if not any(k in pr for k in known)]
    for pr in problems:
        print("  known:  " if pr not in real else "  PROBLEM:", pr)
    print(f"check_site: {len(urls)} pages, {len(real)} problems, {len(problems) - len(real)} known")
    return 1 if real else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]), Path(sys.argv[2]) if len(sys.argv) > 2 else None))
