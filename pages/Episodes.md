---
title: Episodes
layout: page
description: Every episode of the MicroBinfie podcast on microbial bioinformatics and public health, with a written overview of each and a link to listen on SoundCloud.
---

Every episode of the podcast, newest first. Each title opens a written overview of the
episode — who was on, what was discussed, timestamps you can jump to — and each has a link to
listen on SoundCloud. New episodes appear on
[SoundCloud](https://soundcloud.com/microbinfie/tracks) first.

{% assign episodes = site.posts | where_exp: "p", "p.episode" %}
{% assign by_year = episodes | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for year in by_year %}
## {{ year.name }}

{% for p in year.items %}
- **[{{ p.title }}]({{ p.url | relative_url }})** · {{ p.date | date: "%-d %B %Y" }}<br>{{ p.description | default: p.excerpt | strip_html | strip_newlines | replace: "|", "&#124;" }} [Listen on SoundCloud]({{ p.link }})
{% endfor %}
{% endfor %}
