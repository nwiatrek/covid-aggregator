import unittest
from news.news import *


class TestNews(unittest.TestCase):
    def test_get_news_returns_values(self):
        news = News('US-TX')
        response = news.get_news()
        self.assertTrue(len(response) > 0)

    def test_get_news_invalid_returns_nothing(self):
        news = News('US-QQ')
        response = news.get_news()
        self.assertTrue(len(response) == 0)


if __name__ == '__main__':
    unittest.main()
