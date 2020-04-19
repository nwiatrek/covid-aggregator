import requests
import re


class News:
    def __init__(self, location):
        self._url = "https://api.smartable.ai/coronavirus/news/"
        self._key = "a4fc1055a8084d228b58ae887e9df5aa"
        self.location = location

    def get_news(self):
        params = {'Subscription-key': self._key}
        response = requests.get(self._url + self.location, params)
        if response.ok:
            return sort_by_heat(response.json())
        else:
            return []


def verify_location(location):
    if location is None:
        raise Exception("No location given")
    if 'US' not in location:
        raise Exception('Only US supported at the moment')
    regex = re.compile('[A-Za-z]{2,3}-[A-Za-z]{2,3}\Z')
    if regex.match(location) is None:
        raise Exception('invalid format please look at ISO 3166-1 alpha-2')


def sort_by_heat(data):
    """order by most relevant (heat given from api)"""
    news = data.get('news')
    remove_unwanted_keys(news)
    return sorted(remove_none_heat(news), key=lambda x: x['heat'], reverse=True)


def remove_unwanted_keys(data):
    """Removes categories, images, tags"""
    for news in data:
        news.pop('categories', None)
        news.pop('images', None)
        news.pop('tags', None)


def remove_none_heat(data):
    return list(filter(lambda x: x['heat'] is not None, data))
