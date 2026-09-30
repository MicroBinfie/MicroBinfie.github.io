#!/bin/bash
# GPT-6 Astra (high effort) drafts each episode page as JSON, one call per transcript.
#   run_write.sh                     every input in work/in
#   MODEL=grok run_write.sh IN.md …  named inputs on another model (OpenAI's biology filter
#                                    refuses some public-health episodes outright)
# BEDROCK points at bedrock.py from the togl-essential:bedrock-models skill.
set -euo pipefail
cd "$(dirname "$0")"
BEDROCK="${BEDROCK:-bedrock.py}"
MODEL="${MODEL:-astra}"
[ $# -gt 0 ] || set -- work/in/*.md
"$BEDROCK" map -m "$MODEL" --effort high -j 8 --max-tokens 32000 --label "site-episode-$MODEL" \
  -o work/draft --suffix .json -p "$(cat prompts/write.md)" "$@"
