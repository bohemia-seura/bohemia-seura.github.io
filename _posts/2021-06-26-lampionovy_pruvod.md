---
title: Lampionový průvod
layout: default
date: 2021-06-26 15:50:00 +0200
categories: [akce]
tags: [cz] # TAG names should always be lowercase
images:
  - image_path: /photos/lampionovy_pruvod/LampionovyPruvod2021-001.jpeg
    title: Lampionový průvod
  - image_path: /photos/lampionovy_pruvod/LampionovyPruvod2021-002.jpeg
    title: Lampionový průvod
  - image_path: /photos/lampionovy_pruvod/LampionovyPruvod2021-003.jpeg
    title: Lampionový průvod
  - image_path: /photos/lampionovy_pruvod/LampionovyPruvod2021-004.jpeg
    title: Lampionový průvod
  - image_path: /photos/lampionovy_pruvod/LampionovyPruvod2021-005.jpeg
    title: Lampionový průvod
---

text

<ul class="photo-gallery">
  {% for image in page.images %}
    <li><img src="{{ image.image_path }}" alt="{{ image.title}}"/></li>
  {% endfor %}
</ul>