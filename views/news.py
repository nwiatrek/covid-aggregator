# facebook/views/profile.py

from flask import Blueprint, request, jsonify, Response
from news.news import *
news = Blueprint('news', __name__)

@news.route('/news')
def timeline():
    try:
        location = request.args.get('location')
        print(location)
        verify_location(location)
        news = News(location)
        return jsonify(news.get_news())
    except Exception as ex:
        return Response(status=500, response=str(ex))
