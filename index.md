---
layout: page
title : Dustin Ingram
---

## About
I'm Dustin (aka [@di](https://github.com/di/)), a software engineer at
[PromptWorks](http://www.promptworks.com/) and director of our office in
Austin, TX. I'm also the co-founder of the design &amp; build firm [Wiota
Co.](http://wiota.co) and have a master's degree in [Computer
Science](http://cs.drexel.edu) from [Drexel University](http://drexel.edu).

## Newest tech articles
<ul class="posts">
  {% assign combined = "" | split: "" %}
  {% for post in site.posts %}
    {% assign combined = combined | push: post %}
  {% endfor %}
  {% for external in site.data.external %}
    {% assign combined = combined | push: external %}
  {% endfor %}
  {% assign sorted = (combined | sort: 'date') | reverse %}

  {% for post in sorted limit:5 %}
    {% include post_blob.html post=post %}
  {% endfor %}
</ul>

[See all articles...](/categories)
