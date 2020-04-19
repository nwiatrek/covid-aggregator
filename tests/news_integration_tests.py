import unittest
import requests
from news.news import *


class TestNews(unittest.TestCase):
    url = "http://0.0.0.0:5000/news"
    valid_location = {
        "location": "US-TX"
    }
    invalid = {
        "location": "Texass"
    }
    us_not_valid = {
        "location": "US-djfkalsdfkasdf"
    }

    def test_external_news_returns_values(self):
        news = News('US-TX')
        response = news.get_news()
        self.assertTrue(len(response) > 0)

    def test_external_news_invalid_returns_nothing(self):
        news = News('US-QQ')
        response = news.get_news()
        self.assertTrue(len(response) == 0)

    def test_get_news_report_200(self):
        r = requests.get(self.url, params=self.valid_location)
        self.assertEqual(r.status_code, 200)

    def test_get_news_no_location_gives_error(self):
        r = requests.get(self.url)
        self.assertEqual(r.status_code, 500)
        self.assertEqual(b'No location given', r.content)

    def test_bad_param_gives_error(self):
        r = requests.get(self.url, params=self.invalid)
        self.assertEqual(b'Only US supported at the moment', r.content)
        self.assertEqual(r.status_code, 500)

    def test_us_invalid_gives_iso_error(self):
        r = requests.get(self.url, params=self.us_not_valid)
        self.assertEqual(b'invalid format please look at ISO 3166-1 alpha-2', r.content)
        self.assertEqual(r.status_code, 500)


if __name__ == '__main__':
    unittest.main()
