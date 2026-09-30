# Episode pages

One page per episode: a written overview made from the episode's transcript, the player, and
the original show notes. The pages exist for listeners, search engines and AI assistants, so each
names the organisms, tools, methods and people actually discussed, with timestamps that open the
episode at that moment.

| Step | Script | What it does |
|---|---|---|
| 1 | `build_inputs.py` | Reads the SoundCloud feed, matches each episode to its transcript and its existing post, writes one brief per episode |
| 2 | `run_write.sh` | GPT-6 Astra (high effort, Amazon Bedrock) drafts each page as JSON from the transcript |
| 3 | `run_check.sh` | Claude Opus 5.5 (high effort) fact-checks every draft against the transcript and corrects it |
| 4 | `validate.py` | Mechanical checks: quotes verbatim in the transcript, timestamps on real speaker blocks, people named in the episode, no stray Markdown |
| 5 | `render.py` | Writes the posts: existing posts keep their URL and original show notes (read from `origin/main`), missing episodes get new posts |
| 6 | `../check_site.py` | After `jekyll build`: no unrendered Markdown, no broken links, valid JSON-LD, one page per episode, all listed on the Episodes page and in `llms.txt` |

The transcripts come from the `microbinfie-book` pipeline (Whisper large-v3 with speaker
diarisation and a domain-vocabulary pass) and are not kept here:

```bash
python scripts/episodes/build_inputs.py --transcripts ../microbinfie-book/data/transcripts \
  --manifest ../microbinfie-book/data/manifest.json
BEDROCK=/path/to/bedrock.py bash scripts/episodes/run_write.sh
OPUS=/path/to/opus-launcher bash scripts/episodes/run_check.sh
python scripts/episodes/validate.py && python scripts/episodes/render.py
bundle exec jekyll build && python scripts/check_site.py _site scripts/episodes/work/episodes.json
```

Every step skips work already done, so a new episode needs only its transcript and a re-run.
An episode without a transcript still gets a page with its show notes and player.
`work/` keeps the drafts, the checked versions and `validation.tsv` (every mechanical fix);
the briefs, which embed whole transcripts, are not committed.
