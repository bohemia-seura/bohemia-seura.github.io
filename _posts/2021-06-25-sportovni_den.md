---
title: Sportovní den
layout: default
date: 2021-06-25 15:50:00 +0200
categories: [akce]
tags: [cz] # TAG names should always be lowercase
image_path: /photos/sportovni_den/
images:
  - image: SportovniDen2021-001.jpeg
    title: Sportovní den
  - image: SportovniDen2021-002.jpeg
    title: Sportovní den
  - image: SportovniDen2021-003.jpeg
    title: Sportovní den
  - image: SportovniDen2021-004.jpeg
    title: Sportovní den
  - image: SportovniDen2021-005.jpeg
    title: Sportovní den
  - image: SportovniDen2021-006.jpeg
    title: Sportovní den
  - image: SportovniDen2021-007.jpeg
    title: Sportovní den
  - image: SportovniDen2021-008.jpeg
    title: Sportovní den
  - image: SportovniDen2021-009.jpeg
    title: Sportovní den
  - image: SportovniDen2021-010.jpeg
    title: Sportovní den
  - image: SportovniDen2021-011.jpeg
    title: Sportovní den
  - image: SportovniDen2021-012.jpeg
    title: Sportovní den
  - image: SportovniDen2021-013.jpeg
    title: Sportovní den
  - image: SportovniDen2021-014.jpeg
    title: Sportovní den
  - image: SportovniDen2021-015.jpeg
    title: Sportovní den
  - image: SportovniDen2021-016.jpeg
    title: Sportovní den
  - image: SportovniDen2021-017.jpeg
    title: Sportovní den  
  - image: SportovniDen2021-018.jpeg
    title: Sportovní den
  - image: SportovniDen2021-019.jpeg
    title: Sportovní den
  - image: SportovniDen2021-020.jpeg
    title: Sportovní den
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sollicitudin mauris nec suscipit accumsan. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Phasellus quis neque luctus, placerat nisi ac, dignissim enim. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam pulvinar dui non nulla egestas, id ultricies nisi posuere. Suspendisse ultrices velit elit, scelerisque tempus nibh dapibus et. Cras blandit sapien in nulla mattis eleifend. Etiam fringilla sapien in ligula consequat auctor. Duis convallis lorem id nibh tincidunt finibus.

Proin id tempus lectus. Nullam blandit lobortis augue, id scelerisque neque tincidunt sed. Etiam vel neque sit amet nulla efficitur facilisis in eget tellus. Cras consequat, lorem et consequat dictum, justo eros aliquam orci, quis blandit est nulla sed lorem. Mauris hendrerit gravida quam a mattis. Sed vel tortor vel orci venenatis ullamcorper id vel ex. Nullam cursus turpis sit amet dui sodales, et tincidunt dui scelerisque. Sed vel feugiat erat. Cras sed sollicitudin nunc. Nunc bibendum nibh est, in ultricies nisl auctor eu. Nunc vestibulum magna dignissim mi consequat, eget semper quam luctus. Sed ornare malesuada sem, porttitor malesuada nisl venenatis eu. Mauris arcu libero, varius vitae sem ut, condimentum fermentum eros. Integer non eros ex.

Nunc quis dolor faucibus, gravida justo ut, cursus mi. Aenean nec placerat libero, non aliquet mauris. Donec ac varius lacus. Nullam sed lacinia sem. Sed consequat metus non purus volutpat placerat. Curabitur a odio orci. Vestibulum in urna consequat, posuere erat a, pretium purus. Pellentesque pretium nibh eu nulla mollis tincidunt. Pellentesque iaculis fermentum magna, interdum gravida sem aliquam at. Pellentesque ut malesuada risus, mattis pretium velit. Aenean sed tellus quis diam tempor venenatis. Phasellus at ipsum feugiat, elementum nisi vel, convallis massa. Quisque justo mauris, elementum at faucibus eu, suscipit eu quam. Duis in lorem eget mi euismod porta. Ut aliquam felis magna, in sollicitudin tellus pellentesque non.

Pellentesque maximus ante ut vehicula molestie. Sed non neque lobortis, finibus ligula a, gravida nisi. Duis at fermentum felis, vitae fringilla velit. Quisque pretium augue augue, a tincidunt purus suscipit in. Donec et sem lobortis, consectetur odio id, tempor libero. Quisque consectetur massa finibus diam tincidunt tempor sit amet eget arcu. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum dignissim odio sit amet commodo tincidunt. Nunc hendrerit imperdiet vehicula.

Sed iaculis ornare dignissim. Duis efficitur vestibulum hendrerit. Integer cursus ex eget mauris ornare congue. Donec nec commodo est. Nulla eget tortor neque. Etiam consequat ultricies tempor. Integer tempor venenatis tincidunt. Nulla in nibh luctus, cursus erat vel, tristique justo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Fusce vehicula placerat imperdiet. Suspendisse lacus ex, porta sed feugiat nec, blandit ac nisl. Curabitur vestibulum mi in turpis tincidunt finibus. Maecenas orci dolor, scelerisque ac maximus id, pulvinar nec dui. Proin vitae urna ut tellus vulputate egestas. 

<div class ="image-gallery">
{% for image in page.images %}
    {% assign thumb = image.image | replace: '.jpg', '_t.jpg' %}
    {% assign thumb = thumb | replace: '.png', '_t.jpg' %}
    {% assign thumb = thumb | replace: '.jpeg', '_t.jpg' %}
    <div class="box">
    <a href="{{ page.image_path }}{{ image.image }}">
      <img src="{{ page.image_path }}{{ thumb }}" alt="{{ image.title}}"  class="img-gallery" />
     </a>
    </div>
 {% endfor %}
</div>