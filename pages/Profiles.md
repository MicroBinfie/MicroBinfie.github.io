---
title:  Profiles
layout: page
lightbox: true
---

<ul>
  <li> test test test </li>
  {% for person in site.profiles %}
    <li>
      {{ person.title }} {{ person.first }} {{ person.last }}
    </li>
  {% endfor %}
</ul>

