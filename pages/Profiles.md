---
title:  Profiles
layout: page
lightbox: true
---

# Guests

<ul>
  {% for person in data.profiles %}
    <li>
      {{ data.title }} {{ data.first }} {{ data.last }}
    </li>
  {% endfor %}
</ul>

