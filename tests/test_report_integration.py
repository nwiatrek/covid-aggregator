import unittest
import requests
from unittest import TestCase
import app


class TestReportIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.app.testing = True
        cls.client = app.app.test_client()

    url = "http://0.0.0.:5000/state-report"
    texasParams = {
        "state": "Texas"
    }
    notFoundParams = {
        "state": "Texass"
    }

    def test_get_Texas_report_200(self):
        r = self.client.get(self.url + '?state=Texas')
        assert r.is_json == True
        assert r.json['USAState'] == 'Texas'
        assert r.status_code == 200

    def test_get_all_report_200(self):
        r = self.client.get(self.url)
        activeCases = r.json['data'][0]['table'][0]['ActiveCases']
        activeCases = activeCases.replace(',', '')
        assert r.status_code == 200
        # Active Cases should stay above 500000 for the foreseeable future
        self.assertTrue(int(activeCases) > 500000)

    def test_get_state_report_404(self):
        r = self.client.get(self.url + '?state=Texass')
        assert r.data == b'Didn\'t find any data for state: Texass'
        assert r.status_code == 404
