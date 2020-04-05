import requests
from operator import itemgetter

class News():
    def __init__(self, location):
        self._url = "https://api.smartable.ai/coronavirus/news/"
        self._key = "a4fc1055a8084d228b58ae887e9df5aa"
        self.location = location

    def get_news(self):
        params = {'Subscription-key': self._key}
        response = requests.get(self._url + self.location, params)
        return sort_by_heat(response.json())


def verify_location(location):
    pass


def sort_by_heat(data):
    news = data.get('news')
    remove_unwanted_keys(news)
    return sorted(remove_none_heat(news), key=lambda x: x['heat'], reverse=True)


def remove_unwanted_keys(data):
    for news in data:
        news.pop('categories', None)
        news.pop('images', None)
        news.pop('tags', None)


def remove_none_heat(data):
    return list(filter(lambda x: x['heat'] is not None, data))
