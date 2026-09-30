You are writing the web page for ONE episode of the MicroBinfie podcast, a podcast about
microbial bioinformatics and public health, hosted by Lee Katz, Andrew Page and Nabil-Fareed
Alikhan. The page must let somebody who has not heard the episode understand what was discussed,
and must be accurate enough that the people on it would be happy with it. It will be read by
people searching the web and by AI assistants answering questions, so it should be specific:
name the organisms, tools, methods, datasets, papers and numbers that were actually discussed.

The attached file gives the episode's title, date, SoundCloud link and show notes, then the
machine transcript. The transcript is split into speaker blocks, each starting with a label
(SPEAKER_00, SPEAKER_01 …, per episode, not resolved to names) and a timestamp [HH:MM:SS]. Tool
names and personal names are sometimes misheard.

Rules — the page is rejected if it breaks any of them:
1. Everything must come from the transcript or the show notes. Do not add facts you know from
   elsewhere, even true ones, and do not speculate about what was "probably" meant.
2. Spell people's names as the show notes give them; the hosts are Lee Katz, Andrew Page and
   Nabil-Fareed Alikhan. Name a speaker only where the transcript or show notes make it clear who
   is talking (an introduction, a host addressing a guest by name). Otherwise write "one of the
   hosts", "the guest", or "a panellist". Never guess.
3. Quotes must be copied word for word from a single speaker block — they are checked by
   machine. Tidy nothing inside a quote except capitalisation and punctuation.
4. Every timestamp must be the [HH:MM:SS] of the speaker block where that moment starts. Blocks
   can be long; give each highlight a different timestamp, and if one block covers several
   topics, list it once with its first topic.
7. Affiliations only as stated in this episode's transcript or show notes; leave empty otherwise.
5. British English. Plain, specific, readable prose — no hype, no "delve", "game-changer",
   "unlock", "in today's fast-paced world", "key takeaways". Markdown only for emphasis and
   lists inside a section body; no headings inside bodies, no HTML, no links.
6. Scale to the episode: a one-minute trailer gets a short page; a long interview gets 600–1000
   words across the sections.

Output ONLY this JSON:

{"episode": "<the episode id from the header>",
 "headline": "<a descriptive page title, at most 70 characters, not starting with the podcast name>",
 "description": "<one or two sentences for search results, at most 155 characters>",
 "summary": "<a 2–4 sentence overview paragraph: who, what, why it matters>",
 "people": [{"name": "<as in show notes>", "role": "host|guest|panellist|mentioned", "affiliation": "<only if stated, else empty>"}],
 "sections": [{"heading": "<short, specific>", "body": "<1–3 paragraphs>"}],
 "highlights": [{"time": "HH:MM:SS", "topic": "<what is discussed from here, one line>"}],
 "quotes": [{"text": "<verbatim>", "time": "HH:MM:SS", "speaker": "<name only if certain, else 'a guest' / 'one of the hosts'>"}],
 "tools": ["<named software, databases, instruments and named methods only — not generic activities like 'genome sequencing'>"],
 "topics": ["<5–10 lowercase subject keywords>"],
 "faq": [{"q": "<a question a listener might search for>", "a": "<answered from the episode, 1–3 sentences>"}]}

Give 3–6 sections, 5–12 highlights, 0–3 quotes, 3–5 FAQ entries (fewer for very short episodes).
