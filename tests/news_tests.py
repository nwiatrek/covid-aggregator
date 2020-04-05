import unittest
from news.news import *


class TestNews(unittest.TestCase):
    def test_remove_unwanted_keys_removes_image(self):
        news = [{"images": [
        {
          "url": "https://dmn-dallas-news-prod.cdn.arcpublishing.com/resizer/0-hViRoIQMHcDOYg7gHSIpnJWlE=/1200x630/smart/filters:no_upscale()/arc-anglerfish-arc2-prod-dmn.s3.amazonaws.com/public/ZUJTE6EABJFS5NBHZHI7XHWW2A.JPG",
          "width": 1024,
          "height": 630,
          "title": "Coronavirus brings temporary reprieve for second death row inmate in Texas",
          "attribution": ''
        }
      ], }]
        remove_unwanted_keys(news)
        self.assertEqual([{}], news)

    def test_remove_unwanted_keys_removes_categories(self):
        news = [{"categories": ['news']}]
        remove_unwanted_keys(news)
        self.assertEqual([{}], news)

    def test_remove_unwanted_keys_removes_tags(self):
        news = [{"tags": None}]
        remove_unwanted_keys(news)
        self.assertEqual([{}], news)


if __name__ == '__main__':
    unittest.main()
