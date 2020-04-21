import unittest
import requests
from news.news import *
import app


class TestNews(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.app.testing = True
        cls.client = app.app.test_client()

    url = "/news"
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
        r = self.client.get(self.url+'?location=US-TX')
        self.assertEqual(r.status_code, 200)

    def test_get_news_no_location_gives_error(self):
        r = self.client.get(self.url)
        assert r.status_code == 500
        assert r.data == b'No location given'

    def test_bad_param_gives_error(self):
        r = self.client.get(self.url + '?location=asdfdsafsd')
        assert r.data == b'Only US supported at the moment'
        assert r.status_code == 500

    def test_us_invalid_gives_iso_error(self):
        r = self.client.get(self.url + '?location=US-TXQQ')
        assert r.data == b'invalid format please look at ISO 3166-1 alpha-2'
        assert r.status_code == 500


if __name__ == '__main__':
    unittest.main()
