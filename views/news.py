# facebook/views/profile.py

from flask import Blueprint, render_template

news = Blueprint('news', __name__)

@news.route('/news')
def timeline():
    # Do some stuff
    return 'hello news'
