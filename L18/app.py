#! .venv/scripts/python

from flask import Flask, render_template
from datetime import datetime

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.DevelopmentConfig')
#     return app

# app = create_app()

app = Flask(__name__)
# app.config.from_object('config.DevelopmentConfig')


@app.route('/index')
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/time')
def time_out():
    return datetime.now().isoformat()

@app.route('/test')
def test():
    navigation = [{'link':'/', 'name':'Главная страница'},
    {'link':'about', 'name':'О сайте'},
    {'link':'time', 'name':'Время'}]
    return render_template('test.html', navigation = navigation)


if __name__ == '__main__':
    app.run()