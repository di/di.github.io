---
layout: default
title : Dustin Ingram
---

## About
I'm Dustin (aka [@di](https://github.com/di/)), a Developer Advocate at Google,
focused on supporting the Python community on the Google Cloud Platform. I'm
also a member of the [Python Packaging Authority](https://github.com/pypa),
maintainer of [PyPI](https://pypi.org), organizer for the
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
  {% assign n_unpublished = sorted | where: "publish",false| size %}
  {% assign n_talks = 4 | plus: n_unpublished %}

  {% for talk in sorted limit:n_talks %}
    {% include talk_blob.html %}
  {% endfor %}
  <li>
    <a href="/speaking">See more...</a>
  </li>
</ul>
