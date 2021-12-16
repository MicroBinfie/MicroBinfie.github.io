---
title:  Profiles
layout: page
lightbox: true
---

<ul>
  {% for person in site.data.profiles %}
    <li>
      {{ person.title }} {{ person.first }} {{ person.last }}
    </li>
  {% endfor %}
</ul>

