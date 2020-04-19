import unittest
import requests


class TestReportIntegration(unittest.TestCase):
    url = "http://0.0.0.0:5000/state-report"
    texasParams = {
        "state": "Texas"
    }
    notFoundParams = {
        "state": "Texass"
    }

    def test_get_Texas_report_200(self):
        r = requests.get(self.url, params=self.texasParams)
        print(r)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['USAState'], "Texas")

    def test_get_all_report_200(self):
        r = requests.get(self.url)
        activeCases = r.json()['data'][0]['table'][0]['ActiveCases']
        activeCases = activeCases.replace(',', '')
        self.assertEqual(r.status_code, 200)
        # Active Cases should stay above 500000 for the foreseeable future
        self.assertTrue(int(activeCases) > 500000)

    def test_get_state_report_404(self):
        r = requests.get(self.url, params=self.notFoundParams)
        responseCheck = b'Didn\'t find any data for state: Texass'
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.content, responseCheck)