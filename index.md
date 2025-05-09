---
layout: home
title: Accueil
---

Bienvenue sur mon blog restauré !

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.permalink }}">{{ post.title }}</a>
      <span> — {{ post.date | date: "%d/%m/%Y" }}</span>
    </li>
  {% endfor %}
</ul>
