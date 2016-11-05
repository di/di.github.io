---
layout: page
title : All Posts
---

## All categories
<ul class="tag_box inline">
{% for category in site.categories %}
  <li>
    <a href="#{{ category[0] }}-ref">
      <span class="catname">{{ category[0] | join: "/" }}</span>
      <span>({{ category[1].size }} total)</span>
    </a>
  </li>
{% endfor %}
</ul>

{% for category in site.categories %}
<h2 id="{{ category[0] }}-ref">{{ category[0] | join: "/" }}</h2>
<ul class="posts">
{% for post in category[1] %}
  <li><a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
{{ post.description }}
{% endfor %}
</ul>
{% endfor %}
