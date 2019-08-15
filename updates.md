---
layout: collection
title:  "Wekkly progress updates"
---
<ul>
  {% for update in site.updates %}
    <li>
      <a href="{{ update.url }}">{{ update.post_time }}</a>
      - {{ update.title }} <br>
       <img src="{{ update.feature_image_path }}" alt="{{ update.post_time }}"> 
    </li>
  {% endfor %}
</ul>
