---
title:  Profiles
layout: page
lightbox: true
---

{% assign sortedPerson = site.data.profiles | sort: 'last' %}
<ul>
  {% for person in sortedPerson %}
  <!-- image of this profile will be at /assets/images/first_last.jpg -->
  {% assign imgPath = "/assets/images/" | append: person.first | append: "_" | append: person.last | append: ".jpg" | replace: " ", "" %}
    <li>
      {{ person.title }} {{ person.first }} {{ person.last }}
      <br />
      {{ imgPath }} <br />
      <img src="{{ imgPath }}" alt="{{ person.first }} {{ person.last }}" />
    </li>
  {% endfor %}
</ul>

