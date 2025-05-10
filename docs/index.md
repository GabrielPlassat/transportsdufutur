---
layout: home
title: Accueil
---

<header>
  <h1>Transports du Futur</h1>
  <p>Exploration des mobilités de demain</p>
</header>


<input type="text" id="search-box" placeholder="Rechercher un article..." style="width:100%;padding:0.5rem;margin-bottom:1.5rem;" />

<ul id="search-results" class="post-list"></ul>

<script src="https://unpkg.com/lunr/lunr.js"></script>
<script>
  let posts = [];

  fetch("{{ '/search.json' | relative_url }}")
    .then(res => res.json())
    .then(data => {
      posts = data;
      const idx = lunr(function () {
        this.ref('url');
        this.field('title');
        this.field('content');
        data.forEach(doc => this.add(doc));
      });

      document.getElementById('search-box').addEventListener('input', function () {
        const query = this.value;
        const results = idx.search(query);
        const list = document.getElementById('search-results');
        list.innerHTML = '';
        results.forEach(result => {
          const post = posts.find(p => p.url === result.ref);
          const item = document.createElement('li');
          item.innerHTML = `<a href="${post.url}">${post.title}</a>`;
          list.appendChild(item);
        });
      });
    });
</script>

<ul class="post-list">
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%d/%m/%Y" }}</span>
    </li>
  {% endfor %}
</ul>
