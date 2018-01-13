import os
from flask import Flask, render_template
from jinja2 import Template
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
    return render_template('posts.html')