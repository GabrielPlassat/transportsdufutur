Blog
---
layout: home
title: Accueil
---

Bienvenue sur mon blog 

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span> — {{ post.date | date: "%d/%m/%Y" }}</span>
    </li>
  {% endfor %}
</ul>
