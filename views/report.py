# facebook/views/profile.py

from flask import Blueprint, make_response, jsonify, request
import requests

report = Blueprint('report', __name__)


@report.route('/report', methods=['GET'])
def do_stuff():
    state = request.args.get('state')
    print(state)
    return get_report_by_country(state, get_all_reports())


def get_all_reports():
    r = requests.get('https://covid19-server.chrismichael.now.sh/api/v1/CasesInAllUSStates')
    return r.json()


def get_report_by_country(state, reports):
    print(reports.items())
    if state is None:
        return reports
    for stateReport in reports['data'][0]['table']:
        if stateReport['USAState'] == state:
            return stateReport
    return custom_error("Didn't find any data for state: " + state, 404)


def custom_error(message, status_code):
    return make_response(jsonify(message), status_code)
