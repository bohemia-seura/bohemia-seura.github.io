---
title: Sportovní den
layout: default
date: 2021-06-25 15:50:00 +0200
categories: [akce]
tags: [cz] # TAG names should always be lowercase
images:
  - image_path: /photos/sportovni_den/SportovniDen2021-001.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-002.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-003.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-004.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-005.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-006.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-007.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-008.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-009.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-010.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-011.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-012.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-013.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-014.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-015.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-016.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-017.jpeg
    title: Sportovní den  
  - image_path: /photos/sportovni_den/SportovniDen2021-018.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-019.jpeg
    title: Sportovní den
  - image_path: /photos/sportovni_den/SportovniDen2021-020.jpeg
    title: Sportovní den
---

text

<ul class="photo-gallery">
  {% for image in page.images %}
    <li><img src="{{ image.image_path }}" alt="{{ image.title}}"/></li>
  {% endfor %}
</ul>