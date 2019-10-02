import sys
import glob

from jinja2 import Template

# resize images first:
#
# $ mogrify -geometry x500 *.png
#
# use like:
#
# $ python generate_slides.py assets/images/DIRECTORY > _posts/talks/YYYY-MM-DD-title.mkdn

asset_dir = sys.argv[1]

slides = range(1, len(glob.glob(asset_dir + '/*.png')) + 1)

template = Template("""---
layout : post
category : talks
title : 'TITLE'
tags : []
publish : false
description : 'DESCRIPTION'
---

##### This is a text version of a talk I gave at LOCATION.

<div class="slides">
<table>
  {% for i in slides %}
  <tr><td><a href="#{{ i }}"><img id="{{ i }}" class="slide" src="/{{ asset_dir }}/{{ i }}.png"></a></td><td>
    <p>

    </p>
  </td></tr>
  {%- endfor %}
</table>
</div>""")

result = template.render(asset_dir=asset_dir.rstrip('/'), slides=slides)

print(result)
