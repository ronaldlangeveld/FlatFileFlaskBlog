# Flat File Flask Blog

Last updated: 13 January 2018

I'm busy creating my own blog / cms with Flask.

My goal is to have it super basic and simple, very much with the likes of Pico or Jekyll, but with as little dependencies as possible, other than Flask and Python, so you can modify it as you wish as it is open source.

FFFB should:

 - Not contain a database.
 - Have no admin
 -	Be able to update easily through git push / pull without breaking the site.
 -	Make use of Jinja to simplify templating
 -	Post new content by only uploading .md files to your server (Markdown)

Basically, imagine a blog / cms using [Flasks "micro" philosophy](http://flask.pocoo.org/docs/0.12/foreword/#what-does-micro-mean).

## Getting started
### Run locally
1. `export FLASK_APP=server.py`
2. `export FLASK_DEBUG=1`
3. `flask run`

## Requirements
* `pip install markdown2`
* `pip install Flask-Markdown`

## Writing a blog
### Setting parameters
To make use of the title, author and date tags, you must set them at the top of your `blog.md` file in order to parse them correctly. The parameter syntax must be exactly as follows:

``` 
<!-- VARS
##title: Your title ./title
##author: Author name ./author
##date: Date ./date
##slug: your-slug-like-this ./slug
./VARS -->
```

These parameters are called in the templating engine through `{{ post.title }}`, `{{ post.date }}` or `{{ post.author }}`.
