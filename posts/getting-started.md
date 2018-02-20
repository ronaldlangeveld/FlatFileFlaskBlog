
<!-- VARS
##title: Getting Started with FFFB ./title
##author: Ronald ./author
##date: 2018/01/16 ./date
<<<<<<< HEAD:posts/getting-started.md
=======
##slug: getting-started ./slug
>>>>>>> 8a57f23301c17a327f1c4003f5c1286ff7bba205:posts/gettingstarted.md
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

<img style="width: 50vw" src="/static/img/blogtags2.png">
</div>
</div>



And see, you can simply add HTML within your .MD files and your images will display!


These parameters are called in the templating engine through `{{ post.title }}`, `{{ post.slug }}`, `{{ post.date }}`, `{{ post.image }}` or `{{ post.author }}`. 

#### Setting a featured image
To set a featured image you place your-picture.jpg in the `/static/featured-images/` folder. In your vars section you set `image` tag to `your-picture.jpg` and now you can call this image url with `{{ post.image }}`

#### Setting the slug
The slug of the blogs are now initialized by the filename of the post. So make sure these are meaningfull and unique. `/post/` will be prepended to your slug.



## Production

There's multiple ways you can deploy your flask blog.

[Heroku](https://progblog.io/How-to-deploy-a-Flask-App-to-Heroku/)

[Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)

[PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/)