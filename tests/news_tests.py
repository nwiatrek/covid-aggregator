import unittest
from news.news import *
import random, string


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

    def test_remove_none_heat(self):
        news = [{'heat': 1}, {'heat': 2}, {'heat': None}]
        remove_none_heat(news)
        self.assertEqual(2, len(remove_none_heat(news)))

    def test_remove_none_heat_in_larger_objects(self):
        news = [{"heat": 104,
                 "tags": [
                     "US-TX"
                 ],
                 "type": "article",
                 "webUrl": "https://www.houstonchronicle.com/news/houston-texas/houston/article/Coronavirus-live-update-First-cases-reported-in-15148941.php",
                 "ampWebUrl": "https://www.houstonchronicle.com/news/houston-texas/houston/amp/Coronavirus-live-update-First-cases-reported-in-15148941.php",
                 "cdnAmpWebUrl": "https://www-houstonchronicle-com.cdn.ampproject.org/c/s/www.houstonchronicle.com/news/houston-texas/houston/amp/Coronavirus-live-update-First-cases-reported-in-15148941.php",
                 "publishedDateTime": "2020-03-19T11:26:00-07:00",
                 "updatedDateTime": None}, {'heat': 2}, {'heat': None}]
        remove_none_heat(news)
        self.assertEqual(2, len(remove_none_heat(news)))

    def test_location_none(self):
        with self.assertRaisesRegex(Exception, 'No location given'):
            verify_location(None)

    def test_location_not_us(self):
        with self.assertRaisesRegex(Exception, 'Only US supported at the moment'):
            verify_location('not us')

    def test_location_not_valid_iso(self):
        for i in range(10):
            location = 'US'
            if i % 2 == 0:
                location += '-'
                location += random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + \
                            random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
            if i % 2 != 0:
                location += random.choice(string.ascii_letters)

            with self.assertRaisesRegex(Exception, 'invalid format please look at ISO 3166-1 alpha-2'):
                verify_location(location)


if __name__ == '__main__':
    unittest.main()
