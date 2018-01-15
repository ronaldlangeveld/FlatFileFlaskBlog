import os
from flask import Flask
from flask import render_template
from jinja2 import Template
import os
from utils import PostsParser

app = Flask(__name__)

# template_dir = os.path.abspath('templates/')
# app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/posts")
def blog():
	posts_objects = PostsParser()
	posts = posts_objects.posts

	return render_template('posts.html', posts=posts)

@app.route('/posts/<slug>')
def single_blog(slug):
	'''
	Shows individual post
	TODO: normal 404 if not found
	TODO: create template for single-post
	TODO: remove '\n from parsing?'
	'''
	posts_objects = PostsParser()
	posts = posts_objects.posts

	for post in posts:
		if post['slug'] == slug:
			return post['content']

	return "404"
