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
  {% assign talks = site.data.talks | sort: 'date' | reverse %}
  {% for talk in talks %}
  <li>
    <div>
      {{ talk.venue }}
      ({{ talk.date | date : "%B %d, %Y" }})
      {% if talk.slides %}
        (<a href="{{ talk.slides }}">slides</a>)
      {% endif %}
      {% if talk.video %}
        (<a href="{{ talk.video }}">video</a>)
      {% endif %}
    </div>
    {% if talk.url %}
    <a href="{{ talk.url }}">
    {% endif %}
    <div>{{ talk.title }}</div>
    {% if talk.url %}
    </a>
    {% endif %}
    <br/>
  </li>
  {% endfor %}
</ul>
