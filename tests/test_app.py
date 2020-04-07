import pytest
import mock
import requests
import app
from unittest import TestCase


class TestApp(TestCase):
    @classmethod
    def setUpClass(cls):
        app.app.testing = True
        cls.client = app.app.test_client()


class TestGetHospitalCapacity(TestApp):
    route = '/local-hospital-capacity'

    @mock.patch('app.requests.get')
    def test_get_hospital_capacity__raises_http_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError
        response = self.client.get(self.route)
        assert response.status_code == 500
        assert response.json == {"error": "could not make request, please see an admin"}

    @mock.patch('app.requests.get')
    def test_get_hospital_capacity__raises_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError
        response = self.client.get(self.route)
        assert response.status_code == 500
        assert response.json == {"error": "could not make request, please see an admin"}

    @mock.patch('app.requests.get')
    def test_get_hospital_capacity__raises_timeout_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        response = self.client.get(self.route)
        assert response.status_code == 500
        assert response.json == {"error": "could not make request, please see an admin"}

    @mock.patch('app.requests.get')
    def test_get_hospital_capacity__no_bexar_county_in_response(self, mock_get):
        mock_blob = mock.Mock()
        mock_blob.json.return_value = {"data": [{"table": [{'State': 'Fake', "CountyName": 'NotBexar'},
                                                          {'State': 'TX', 'CountyName': 'Travis'}]}]}
        mock_get.return_value = mock_blob
        response = self.client.get(self.route)
        assert response.status_code == 500
        assert response.json == {"error": "no info found for Bexar County TX"}

    @mock.patch('app.requests.get')
    def test_get_hospital_capacity__success_response(self, mock_get):
        mock_blob = mock.Mock()
        mock_blob.json.return_value = {"data": [{"table": [{'State': 'Fake', "CountyName": 'NotBexar'},
                                                          {'State': 'TX', 'CountyName': 'Bexar'}]}]}
        mock_get.return_value = mock_blob
        response = self.client.get(self.route)
        assert response.status_code == 200
        assert response.json == {'State': 'TX', 'CountyName': 'Bexar'}
