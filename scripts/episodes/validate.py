"""Mechanical checks on each fact-checked article, independent of both models.

    python scripts/episodes/validate.py

Reads work/checked/<id>.json (Claude's corrected article) and work/in/<id>.md (show notes and
transcript), and writes work/final/<id>.json plus work/validation.tsv, one line per fix:

- a quote must be the speaker's exact words, found in one speaker block of this transcript;
  one that is not is dropped, and its timestamp is reset to the block it was found in;
- a highlight's timestamp must be a real block start (it is moved to the block at or before it),
  and highlights sharing a timestamp are merged;
- a person must be a host or be named somewhere in the show notes or transcript, else dropped;
- bodies must be plain paragraphs: no headings, HTML or links survive into the page;
- the search description is kept under 160 characters.
"""

from __future__ import annotations

import json
import re
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE / "work"
HOSTS = {"Lee Katz", "Andrew Page", "Nabil-Fareed Alikhan"}
BANNED = ["delve", "game-changer", "game changer", "unlock", "fast-paced world", "key takeaways",
          "cutting-edge", "seamless", "leverage"]


def fold(s: str) -> str:
    """Strip accents, so Duchêne and Duchene compare equal."""
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def words(s: str) -> list[str]:
    s = s.lower().replace("’", "'")
    return re.findall(r"[a-z0-9']+", s)


def blocks(transcript: str) -> list[tuple[str, list[str]]]:
    """(HH:MM:SS, words) for each speaker block."""
    parts = re.split(r"^\*\*SPEAKER_\d+\*\* \[(\d\d:\d\d:\d\d)\]\s*$", transcript, flags=re.MULTILINE)
    return [(parts[i], words(parts[i + 1])) for i in range(1, len(parts) - 1, 2)]


def find_block(bl, quote: str) -> str | None:
    q = words(quote)
    if not q:
        return None
    for time, w in bl:
        for i in range(len(w) - len(q) + 1):
            if w[i:i + len(q)] == q:
                return time
    return None


def secs(t: str) -> int:
    h, m, s = (int(x) for x in t.split(":"))
    return h * 3600 + m * 60 + s


def extract(path: Path) -> dict | None:
    try:
        outer = json.loads(path.read_text())
    except json.JSONDecodeError:
        return None  # empty or partial: a check still running, or one that failed
    text = outer.get("result", "") if isinstance(outer, dict) and "result" in outer else json.dumps(outer)
    for block in reversed(re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)):
        try:
            return json.loads(block)
        except json.JSONDecodeError:
            pass
    dec = json.JSONDecoder()
    for i, ch in enumerate(text):
        if ch == "{":
            try:
                return dec.raw_decode(text[i:])[0]
            except json.JSONDecodeError:
                continue
    return None


def clean_body(s: str) -> str:
    s = re.sub(r"^#{1,6}\s+", "", s, flags=re.MULTILINE)          # headings
    s = re.sub(r"<[^>]+>", "", s)                          # HTML
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)         # links
    return s.strip()


def main() -> None:
    (WORK / "final").mkdir(exist_ok=True)
    log = []
    for f in sorted((WORK / "checked").glob("*.json")):
        eid = f.stem
        if not f.stat().st_size:
            continue
        got = extract(f)
        art = (got or {}).get("article")
        if not art:
            log.append(f"{eid}\tNO ARTICLE\tcheck output unparseable or empty")
            continue
        src = (WORK / "in" / f"{eid}.md").read_text()
        _notes, transcript = src.split("## Transcript", 1)
        bl = blocks(transcript)
        starts = sorted({t for t, _ in bl}, key=secs)
        haystack = fold(src).lower()

        quotes = []
        for q in art.get("quotes", []):
            where = find_block(bl, q.get("text", ""))
            if not where:
                log.append(f"{eid}\tquote dropped\tnot verbatim: {q.get('text', '')[:80]}")
                continue
            if where != q.get("time"):
                log.append(f"{eid}\tquote time\t{q.get('time')} -> {where}")
            quotes.append({**q, "time": where})
        art["quotes"] = quotes

        merged: dict[str, list[str]] = {}
        for h in art.get("highlights", []):
            t = h.get("time", "")
            if not re.fullmatch(r"\d\d:\d\d:\d\d", t) or not starts:
                log.append(f"{eid}\thighlight dropped\tbad time {t!r}")
                continue
            snapped = max((s for s in starts if secs(s) <= secs(t)), key=secs, default=starts[0])
            if snapped != t:
                log.append(f"{eid}\thighlight time\t{t} -> {snapped}")
            merged.setdefault(snapped, []).append(h.get("topic", "").strip())
        art["highlights"] = [{"time": t, "topic": "; ".join(dict.fromkeys(v))}
                             for t, v in sorted(merged.items(), key=lambda kv: secs(kv[0]))]

        people = []
        heard = set(words(fold(src)))
        for p in art.get("people", []):
            name = p.get("name", "").strip()
            toks = [t for t in re.split(r"[\s-]+", fold(name).lower()) if len(t) > 2]
            # The transcript mishears names ("Duchesne" for Duchêne), so a close match counts.
            if name in HOSTS or (toks and all(
                    t in haystack or any(SequenceMatcher(None, t, w).ratio() >= 0.8 for w in heard)
                    for t in toks)):
                people.append(p)
            else:
                log.append(f"{eid}\tperson dropped\t{name} not in show notes or transcript")
        art["people"] = people

        for s in art.get("sections", []):
            s["body"] = clean_body(s.get("body", ""))
        for fq in art.get("faq", []):
            fq["a"] = clean_body(fq.get("a", ""))
        if len(art.get("description", "")) > 160:
            art["description"] = art["description"][:157].rsplit(" ", 1)[0] + "…"
            log.append(f"{eid}\tdescription trimmed\t")
        text = json.dumps(art).lower()
        for b in BANNED:
            if b in text:
                log.append(f"{eid}\tbanned phrase\t{b}")
        (WORK / "final" / f"{eid}.json").write_text(json.dumps(art, indent=1, ensure_ascii=False))
    (WORK / "validation.tsv").write_text("episode\tcheck\tdetail\n" + "\n".join(log) + "\n")
    n = len(list((WORK / "final").glob("*.json")))
    print(f"{n} articles validated; {len(log)} fixes logged in {WORK / 'validation.tsv'}")


if __name__ == "__main__":
    main()
