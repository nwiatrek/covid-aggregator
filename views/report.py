# facebook/views/profile.py

from flask import Blueprint, render_template
import requests

report = Blueprint('report', __name__)


@report.route('/report', methods=['GET'])
def do_stuff():
    return get_report_by_country("USA", get_all_reports()).json()


def get_all_reports():
    r = requests.get('https://covid19-server.chrismichael.now.sh/api/v1/AllReports')
    return r.json()


def get_report_by_country(country, reports):
    print(reports.items())
    for countryReport in reports[0]["table"]:
        print(countryReport)
        if countryReport.Country == country:
            return countryReport
