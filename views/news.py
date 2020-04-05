# facebook/views/profile.py

from flask import Blueprint, request, jsonify
from news.news import News
news = Blueprint('news', __name__)

@news.route('/news')
def timeline():
    location = request.args.get('location')
    news = News(location)
    return jsonify(news.get_news())
