---
title:  Episodes
layout: page
---

_Note_: This specific page is updated.... rarely.
Please check [our soundcloud](https://soundcloud.com/microbinfie/tracks) for the latest.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>

