from flask import Flask

app = Flask(__name__)
from flask import Flask
from views.news import news

app = Flask(__name__)
app.register_blueprint(news)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
