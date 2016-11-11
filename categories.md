---
layout: page
title : All Posts
---

## All categories
<ul class="tag_box inline">
{% assign combined = "" | split: "" %}
{% for category in site.categories %}
  {% assign combined = combined | push: category %}
{% endfor %}
{% for category in site.data %}
  {% assign combined = combined | push: category %}
{% endfor %}
{% assign sorted = combined | sort %}

{% for category in sorted %}
  <li>
    <a href="#{{ category[0] }}-ref">
      <span class="catname">{{ category[0] | join: "/" }}</span>
      <span>({{ category[1].size }} total)</span>
    </a>
  </li>
{% endfor %}

</ul>

{% for category in sorted %}
<h2 id="{{ category[0] }}-ref">{{ category[0] | join: "/" }}</h2>
<ul class="posts">
{% for post in category[1] %}
  {% include post_blob.html post=post %}
{% endfor %}
</ul>
{% endfor %}
