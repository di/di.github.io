---
layout: default
title : Dustin Ingram
---

## About
I'm Dustin (aka [@di](https://github.com/di/)), an engineer on Google's Open
Source Security Team, focused on on improving the security of open-source
software that Google (and the rest of the world) relies on. I'm also a director of the [Python Software
Foundation](https://www.python.org/psf/), and maintainer of
[PyPI](https://pypi.org).

## Writing
<ul>
  {% assign combined = "" | split: "" %}
  {% for post in site.categories['articles'] %}
    {% assign combined = combined | push: post %}
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
