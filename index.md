---
layout: default
title : Dustin Ingram
---

## About
I'm Dustin (aka [@di](https://github.com/di/)), a software engineer at
[PromptWorks](http://www.promptworks.com/) and director of our office in
Austin, TX. I'm also a member of the [Python Packaging
Authority](https://github.com/pypa), organizer for the
[PyTexas](https://pytexas.org) conference and have a master's degree in
Computer Science from [Drexel University](http://drexel.edu).

## Writing
<ul>
  {% assign combined = "" | split: "" %}
  {% for post in site.categories['articles'] %}
    {% assign combined = combined | push: post %}
  {% endfor %}
  {% for external in site.data.external %}
    {% assign combined = combined | push: external %}
  {% endfor %}
  {% assign sorted = combined | sort: 'date' | reverse %}

  {% for post in sorted limit:4 %}
    {% include post_blob.html post=post %}
  {% endfor %}
  <li>
    <a href="/writing">See more...</a>
  </li>
</ul>


## Speaking
<ul>
  {% assign combined = "" | split: "" %}
  {% for talk in site.categories['talks'] %}
    {% assign combined = combined | push: talk %}
  {% endfor %}
  {% for talk in site.data.talks %}
    {% assign combined = combined | push: talk %}
  {% endfor %}
  {% assign sorted = combined | sort: 'date' | reverse %}

  {% for talk in sorted limit:4 %}
  <li>
  {% if talk.url %}
    <a href="{{ talk.url }}">{{ talk.title }}</a><br>
  {% else %}
    <a href="{{ talk.slides_url }}">{{ talk.title }}</a><br>
  {% endif %}
    <small>
      <a href="{{ talk.venue_url }}">{{ talk.venue }}</a>, {{ talk.location }}, {{ talk.date | date : "%B %Y" }}
      {% if talk.video_url %}
      (<a href="{{ video_url }}">video</a>)
      {% endif %}
    </small>
  </li>
  {% endfor %}
  <li>
    <a href="/speaking">See more...</a>
  </li>
</ul>

## Github
You can follow me on Github [here](https://github.com/di).