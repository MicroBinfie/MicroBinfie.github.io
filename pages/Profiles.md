---
title:  Profiles
layout: page
lightbox: true
---

<ul>
  {% for person in site.data.profiles %}
    <li>
      {{ person.title }} {{ person.first }} {{ person.last }}
      <br />
      ![Image of {{ person.first }} {{ person.last }}](/assets/images/{{ person.first }}_{{ person.last }}.jpg)
    </li>
  {% endfor %}
</ul>

