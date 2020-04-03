# facebook/views/profile.py

from flask import Blueprint, render_template
import requests

report = Blueprint('report', __name__)


@report.route('/report', methods=['GET'])
def get_all_reports():
    r = requests.get('https://covid19-server.chrismichael.now.sh/api/v1/AllReports')
    return r.json()

