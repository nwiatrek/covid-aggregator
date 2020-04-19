import unittest
import requests


class TestReportIntegration(unittest.TestCase):
    url = "http://0.0.0.0:5000/local-hospital-capacity"

    def test_get_hospital_capacity__raises_http_error(self):
        response = requests.get(self.url)
        print(response.json())
        assert response.status_code == 200
        assert response.json()['CountyName'] == 'Bexar'
