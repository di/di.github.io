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
  {% if talk.venue %}
  <li>
  {% if talk.url %}
    <a href="{{ talk.url }}">{{ talk.title }}</a><br>
  {% elsif talk.video_url %}
    <a href="{{ talk.video_url }}">{{ talk.title }}</a><br>
  {% elsif talk.slides_url %}
    <a href="{{ talk.slides_url }}">{{ talk.title }}</a><br>
  {% else %}
    {{ talk.title }}<br>
  {% endif %}
    <small>
      <a href="{{ talk.venue_url }}">{{ talk.venue }}</a>,
      {% if talk.location %} {{ talk.location }}, {% endif %}
      {{ talk.date | date : "%B %Y" }}
      {% if talk.slides_url %}
      (<a href="{{ talk.slides_url }}">slides</a>)
      {% endif %}
      {% if talk.description %}
      <br>
      {{ talk.description }}
      {% endif %}
    </small>
    <br><br>
  </li>
  {% endif %}
  {% endfor %}
</ul>
