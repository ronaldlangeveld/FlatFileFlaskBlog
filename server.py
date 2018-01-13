import os
from flask import Flask
from flask import render_template
from flask import Markup
from jinja2 import Template
import markdown2
import os

app = Flask(__name__)

# template_dir = os.path.abspath('templates/')
# app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def main():
    return render_template('index.html')


# @app.route("/post")
# def main():
#     return render_template('index.html')


@app.route("/posts")
def blog():

	posts = []

	#
	# Loops over all posts and stores html in posts[]
	#
	for post in os.listdir("posts/"):
		posts.append(markdown2.markdown_path("posts/" + post))

	return render_template('posts.html', posts=posts)