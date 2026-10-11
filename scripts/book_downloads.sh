#!/bin/bash
# How many times each book file has been downloaded, per GitHub release (exact, server-side).
# The book page links to release assets for this reason. Needs the GitHub CLI (gh).
#   bash scripts/book_downloads.sh
set -euo pipefail
gh api repos/MicroBinfie/MicroBinfie.github.io/releases --paginate \
  --jq '.[] | select(.tag_name | startswith("book-")) | .tag_name as $t
        | .assets[] | select(.name | endswith(".txt") and startswith("SHA") | not)
        | "\($t)\t\(.download_count)\t\(.name)"' \
  | sort | awk -F'\t' 'BEGIN { print "release\tdownloads\tfile" } { print; n += $2 } END { print "total\t" n }' \
  | column -t -s$'\t'
# Google Analytics has the rest: the 'book_download' event (with a 'format' parameter) for every
# format including the EPUB and the web edition, plus where readers came from.
