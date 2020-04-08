from flask import Flask, request
from views.news import news
from report.report import *

app = Flask(__name__)
app.register_blueprint(news)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/state-report', methods=['GET'])
def get_state_report():
    state = request.args.get('state')
    if state is None:
        state = ""
    report = Report(state)
    return report.get_report_by_country(report.get_all_reports())


if __name__ == '__main__':
    app.run()
