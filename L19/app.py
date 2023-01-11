#! .venv/scripts/python

from flask import Flask, render_template
from datetime import datetime
from flask import request
import requests

def create_app():
    app = Flask(__name__)
    # app.config.from_object('config.DevelopmentConfig')
    return app

app = create_app()

navigation = [{'link':'/', 'name':'Главная страница'},
    {'link':'about', 'name':'О сайте'},
    {'link':'time', 'name':'Время'},
    {'link':'kanye_west','name':'цитата Kanye West'}]

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', navigation = navigation)

@app.route('/time')
def time_out():
    return render_template('time.html', navigation = navigation, time = datetime.now().isoformat())

@app.route('/about')
def about():
    return render_template('about.html', navigation = navigation)


@app.route('/kanye_west', methods=['GET'])
def kanye_west():
    number_quote = int(request.args.get('number', 1)) #получение данных по ключу
    if number_quote < 1: #валидация входных
        number_quote = 1
    quote = set([(requests.get('https://api.kanye.rest').json())['quote'] for i in range(number_quote)]) #генерация списка цитат с очисткой от повторов
    return render_template('kanye_west.html', navigation = navigation, quote = quote)


if __name__ == '__main__':
    app.run()