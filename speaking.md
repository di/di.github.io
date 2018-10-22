---
layout: page
title : Speaking
---

I like to speak about Python and software development, but more generally I'm
interested in revealing little-known features of a language, explaining
hard-to-grasp concepts in simple terms, or using common tools in new and
unexpected ways. In-depth discussion of some of these topics can be found in
[my writing](/writing).

A sample of my recent talks:

<ul>
  {% assign combined = "" | split: "" %}
  {% for talk in site.categories['talks'] %}
    {% assign combined = combined | push: talk %}
  {% endfor %}
  {% for talk in site.data.talks %}
    {% assign combined = combined | push: talk %}
  {% endfor %}
  {% assign sorted = combined | sort: 'date' | reverse %}

  {% for talk in sorted %}
    {% include talk_blob.html %}
  {% endfor %}
</ul>
