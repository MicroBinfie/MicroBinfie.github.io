---
title:  Profiles
layout: page
lightbox: true
---

# Guests

<ul>
  {% for person in site.profiles %}
    <li>
      {{ person.title }} {{ person.first }} {{ person.last }}
    </li>
  {% endfor %}
</ul>

