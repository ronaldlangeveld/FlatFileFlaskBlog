
<!-- VARS
##title: Getting Started with FFFB ./title
##author: Ronald ./author
##date: 2018/01/16 ./date
##image: welcome.gif ./image
./VARS -->

<hr>

It's highly recommended that you run this in a python virtual environment.

Clone this project into your dirctory of choice.

## Requirements
* `pip install flask`
* `pip install markdown2`
* `pip install Flask-Markdown`

Alternativaly
* `pip install -r requirements.txt`

### Run locally
1. `export FLASK_APP=server.py`
2. `export FLASK_DEBUG=1`
3. `flask run`


## Writing a blog
### Setting parameters
To make use of the title, author and date tags, you must set them at the top of your `blog.md` file in order to parse them correctly. The parameter syntax must be exactly as follows:

<div class="row">
<div class="col-6">

<img style="width: 50vw" src="/static/img/blogtags.png">
</div>
</div>

And see, you can simply add HTML within your .MD files and your images will display!

These parameters are called in the templating engine through `{{ post.title }}`, `{{ post.slug }}`, `{{ post.date }}` or `{{ post.author }}`.