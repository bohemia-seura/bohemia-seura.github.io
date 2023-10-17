# Návod pro administraci stránek

## Přidání nové události
Otevřete [soubor událostí "events.yml"](https://github.com/bohemia-seura/bohemia-seura.github.io/blob/main/_data/events.yml) a přidejte další položku v seznamu. 

### date
Datum ve formátu YYYY-MM-DD (například 2023-11-25)

### name
Jméno události. V podseznamu označte jazyk jména události "cs", "sk" nebo "fi".

### place 
Místo konání události.

### categories
Seznam kategorií, pod které je událost zařazená. Platné názvy musí odpovídat názvům souborů s koncovkou ".md" ve [složce událostí "_events"](https://github.com/bohemia-seura/bohemia-seura.github.io/tree/main/_events) (například drakiada, sportovni_den ...).

## Přidání nové kategorie události

### Stránka kategorie události
Založte nový soubor s koncovkou ".md" pro novou kategorii události ve [složce událostí "_events"](https://github.com/bohemia-seura/bohemia-seura.github.io/tree/main/_events). Hlavičku souboru vytvořte podle už existujících událostí. Poté založte prázdné soubory se stejným názvem ve složkách [českých](https://github.com/bohemia-seura/bohemia-seura.github.io/tree/main/_i18n/cs/event_data), [slovenských](https://github.com/bohemia-seura/bohemia-seura.github.io/tree/main/_i18n/sk/event_data) a [finských](https://github.com/bohemia-seura/bohemia-seura.github.io/tree/main/_i18n/fi/event_data) překladů stránek událostí "event_data". Zde je možné napsat doprovodný text k nové kategorii události. Pokud zůstane soubor prázdný, zobrazí se jen kalendář a fotogalerie.

### Složka fotografií
Založte novou složku ve [složce fotografií "photos"](https://github.com/bohemia-seura/bohemia-seura.github.io/tree/main/photos) se stejným názvem, který jste použili v hlavičce souboru nové kategorie události. Fotografie přidávejte podle návodu pro přidávání nových fotografií.

### Název kategorie a jeho překlady
V souborech [českých](https://github.com/bohemia-seura/bohemia-seura.github.io/blob/main/_i18n/cs.yml), [slovenských](https://github.com/bohemia-seura/bohemia-seura.github.io/blob/main/_i18n/sk.yml) a [finských](https://github.com/bohemia-seura/bohemia-seura.github.io/blob/main/_i18n/fi.yml) názvů přidejte položku v seznamu "events" odpovídající jménu stránky nové kategorie události.

# Photo gallery
Upload photos (".png",".jpg",".jpeg" any size) and thumbnails (".jpg" 200x200 px) to the same folder. In the page header specify "image_path" variable (e.g. "image_path: /photos/sportovni_den/") and for each image its name (image.image) and title (image.title). The thumbnails can be generated with irfanView batch processing and are expected to have the same name as the image + "_t" and extension ".jpg". Configuration file is "irfanView_thumbs.ini" and the name pattern is "$N_t".


# Chirpy Starter [![Gem Version](https://img.shields.io/gem/v/jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy) [![GitHub license](https://img.shields.io/github/license/cotes2020/chirpy-starter.svg?color=blue)][mit]

When installing the [**Chirpy**][chirpy] theme through [RubyGems.org][gem], Jekyll can only read files in the folders `/_data`, `/_layouts`, `/_includes`, `/_sass` and `/assets`, as well as a small part of options of the `/_config.yml` file from the theme's gem. If you have ever installed this theme gem, you can use the command `bundle info --path jekyll-theme-chirpy` to locate these files.

The Jekyll team claims that this is to leave the ball in the user’s court, but this also results in users not being able to enjoy the out-of-the-box experience when using feature-rich themes.

To fully use all the features of **Chirpy**, you need to copy the other critical files from the theme's gem to your Jekyll site. The following is a list of targets:

```shell
.
├── _config.yml
├── _plugins
├── _tabs
└── index.html
```

To save you time, and also in case you lose some files while copying, we extract those files/configurations of the latest version of the **Chirpy** theme and the [CD][CD] workflow to here, so that you can start writing in minutes.

## Prerequisites

Follow the instructions in the [Jekyll Docs](https://jekyllrb.com/docs/installation/) to complete the installation of the basic environment. [Git](https://git-scm.com/) also needs to be installed.

## Installation

Sign in to GitHub and [**use this template**][use-template] to generate a brand new repository and name it `USERNAME.github.io`, where `USERNAME` represents your GitHub username.

Then clone it to your local machine and run:

```
$ bundle
```

## Usage

Please see the [theme's docs](https://github.com/cotes2020/jekyll-theme-chirpy#documentation).

## License

This work is published under [MIT][mit] License.

[gem]: https://rubygems.org/gems/jekyll-theme-chirpy
[chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy/
[use-template]: https://github.com/cotes2020/chirpy-starter/generate
[CD]: https://en.wikipedia.org/wiki/Continuous_deployment
[mit]: https://github.com/cotes2020/chirpy-starter/blob/master/LICENSE
