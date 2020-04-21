import unittest
import requests
import app

class TestReportIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.app.testing = True
        cls.client = app.app.test_client()
    url = "/local-hospital-capacity"

    def test_get_hospital_capacity__raises_http_error(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert response.json['CountyName'] == 'Bexar'
