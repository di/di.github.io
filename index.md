---
layout: default
title : Dustin Ingram
---

## About
I'm Dustin (aka [@di](https://github.com/di/)), a software engineer at
[PromptWorks](http://www.promptworks.com/) and director of our office in
Austin, TX. I'm also a member of the [Python Packaging
Authority](https://github.com/pypa) and have a master's degree in Computer
Science from [Drexel University](http://drexel.edu).

## Writing
<ul>
  {% assign combined = "" | split: "" %}
  {% for post in site.posts %}
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
  {% assign talks = site.data.talks | sort: 'date' | reverse %}
  {% for talk in talks limit:4 %}
  <li>
    <a href="{{ talk.url }}">
      {{ talk.venue }}: {{ talk.title }}
    </a>
  </li>
  {% endfor %}
  <li>
    <a href="/speaking">See more...</a>
  </li>
</ul>

## Github
You can follow me on Github [here](https://github.com/di).
