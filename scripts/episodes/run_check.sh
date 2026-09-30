#!/bin/bash
# Claude (Opus 5.5, high effort) fact-checks every draft against its transcript.
#   OPUS=/path/to/launcher run_check.sh [ID …]      default: every draft
# OPUS is a headless Claude Code launcher for Bedrock's Claude Opus 5.5 taking
# [--effort E] [--tools T] [--budget USD] [--cwd DIR] PROMPT_FILE and printing Claude Code's JSON.
# A checked file that already exists is kept; delete it to check again.
set -euo pipefail
cd "$(dirname "$0")"
OPUS="${OPUS:?set OPUS to the Claude launcher}"
JOBS="${JOBS:-8}"
mkdir -p work/checkin work/checked
if [ $# -eq 0 ]; then
  for d in work/draft/*.json; do set -- "$@" "$(basename "$d" .md.json)"; done
fi
for id in "$@"; do
  { cat prompts/check.md; printf '\n\n# THE EPISODE\n\n'; cat "work/in/$id.md";
    printf '\n\n# THE DRAFT\n\n'; cat "work/draft/$id.md.json"; } > "work/checkin/$id.md"
done
printf '%s\n' "$@" | xargs -P "$JOBS" -I{} bash -c '
  [ -s "work/checked/{}.json" ] && exit 0
  "$0" --effort high --tools "" --budget 3 --cwd "$PWD" "work/checkin/{}.md" \
    > "work/checked/{}.json" 2> "work/checked/{}.err" && echo "ok   {}" || echo "FAIL {}"' "$OPUS"
