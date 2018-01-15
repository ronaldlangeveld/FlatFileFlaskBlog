import markdown2
from flask import Markup
import os

class PostsParser():
	'''
	Initiates parsing of all the posts.
	'''
	def __init__(self):
		self.posts = []

		for post in os.listdir("posts/"):
			# Loops over all posts and stores html in posts[]
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

		title = params[(params.find("##title: ")+9):params.find(" ./title")]
		author = params[(params.find("##author: ")+10):params.find(" ./author")]
		date = params[(params.find("##date: ")+8):params.find(" ./date")]
		slug = params[(params.find("##slug: ")+8):params.find(" ./slug")]

		return title, author, date, slug