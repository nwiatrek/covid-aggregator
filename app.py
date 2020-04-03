from flask import Flask
from views.news import news
from views.report import report

app = Flask(__name__)
app.register_blueprint(news)
app.register_blueprint(report)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
