---
layout: page
title : Writing
---

I occasionally write technical articles for my own website. Sometimes I
write for other venues instead. These articles vary widely from short "Today I
Learned" type posts, to long-form technical explanations. Often, my articles
double as the early drafts for [my speaking](/speaking).

Some of my recent writing:

<ul>
  {% assign combined = "" | split: "" %}
  {% for post in site.posts %}
    {% assign combined = combined | push: post %}
  {% endfor %}
  {% for external in site.data.external %}
    {% assign combined = combined | push: external %}
  {% endfor %}
  {% assign sorted = combined | sort: 'date' | reverse %}
  {% assign full = true %}
  {% for post in sorted %}
    {% include post_blob.html %}
  {% endfor %}
</ul>
