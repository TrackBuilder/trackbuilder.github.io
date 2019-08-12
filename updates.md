---
layout: collection
title:  "Wekkly progress updates"
---
<ul>
  {% for update in site.updates %}
    <li>
      <a href="{{ update.url }}">{{ update.post_time }}</a>
      - {{ update.title }}
    </li>
  {% endfor %}
</ul>