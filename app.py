from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.errorhandler(requests.exceptions.RequestException)
def handle_request_exception(e):
    return jsonify({"error": "could not make request, please see an admin"}), 500

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/local-hospital-capacity', methods=['GET'])
def get_cap():
    responses = requests.get('https://covid19-server.chrismichael.now.sh/api/v1/AggregatedFacilityCapacityCounty').json()['data'][0]['table']
    tx_response = []
    for response in responses:
        if response['State'] == 'TX' and response['CountyName'] == 'Bexar':
            tx_response = response
    if not tx_response:
        return jsonify({"error": "no info found for Bexar County TX"}), 500
    return jsonify(tx_response), 200


if __name__ == '__main__':
    app.run()
