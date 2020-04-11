import requests


class Report:
    def __init__(self, state):
        self._url = "https://covid19-server.chrismichael.now.sh/api/v1/CasesInAllUSStates"
        self.state = state

    def get_all_reports(self):
        try:
            r = requests.get(self._url)
            return r.json()
        except:
            return "Internal Server Error: Failure calling downstream", 500

    def get_report_by_country(self, reports):
        try:
            if self.state == "":
                return reports, 200
            for stateReport in reports['data'][0]['table']:
                if stateReport['USAState'] == self.state:
                    return stateReport, 200
            return "Didn't find any data for state: " + self.state, 404
        except:
            return "Internal Server Error: Unmarshalling error ", 500
