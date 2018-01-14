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
		print post['slug']

		if post['slug'] == slug + '\n':
			return post['content']

	return "404"


#
# Utils
#

class PostsParser():
	def __init__(self):
		self.posts = []

		# Loops over all posts and stores html in posts[]
		for post in os.listdir("posts/"):
			if post.endswith('.md'):
				path = "posts/" + post
				html = markdown2.markdown_path(path)
				title, author, date, slug = self.getVars(html)
				self.posts.append({
					'title':title,
					'author':author,
					'date':date,
					'slug':slug,
					'content':html
					})

	def getVars(self, html):
		'''
		Parses the html to get the variables.
		@input markdown to html string
		@returns title, author and date
		'''
		begin = html.find("<!-- VARS")
		end = html.find("./VARS -->")
		params = html[begin+10:end]

		title = params[(params.find("##title: ")+9):params.find("\n")]
		author = params[(params.find("##author: ")+10):params.find("\n")]
		author = params[(params.find("##: ")+10):params.find("\n")]
		date = params[(params.find("##date: ")+8):params.find("\n")]
		slug = params[(params.find("##slug: ")+8):]

		return title, author, date, slug


