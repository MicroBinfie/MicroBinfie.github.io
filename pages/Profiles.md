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
      <!-- image of this profile will be at /assets/images/first_last.jpg -->
      <img src="/assets/images/{{ person.first }}_{{ person.last }}.jpg" alt="{{ person.first }} {{ person.last }}" />
    </li>
  {% endfor %}
</ul>

