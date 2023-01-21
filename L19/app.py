#! .venv/bin/python

from flask import Flask, render_template, request
from datetime import datetime
from requests import get
from L13_3 import Validator
import config

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = config.DevelopmentConfig.DEBUG
    return app

app = create_app()

navigation = [{'link':'/', 'name':'Главная страница'},
    {'link':'about', 'name':'О сайте'},
    {'link':'time_out', 'name':'Время'},
    {'link':'kanye_west','name':'цитата Kanye West'},
    {'link': 'register','name': 'Регистрация'}]

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', navigation = navigation)

@app.route('/time_out')
def time_out():
    return render_template('time.html', navigation = navigation, time = datetime.now().isoformat())

@app.route('/about')
def about():
    return render_template('about.html', navigation = navigation)


@app.route('/kanye_west')
def kanye_west():
    number_quote = int(request.args.get('number', 1)) #получение данных по ключу
    if number_quote < 1: #валидация входных
        number_quote = 1
    quote = set([get('https://api.kanye.rest').json()['quote'] for i in range(number_quote)]) #генерация списка цитат с очисткой от повторов
    
    return render_template('kanye_west.html', navigation = navigation, quote = quote)


@app.route('/register', methods=['GET', 'POST'])
def register():
    user = dict(request.form)
    if bool(user):
        validation = Validator(user['login'], user['password'], user['email'])
        validation_out = "Спасибо за регистрацию" if (validation.validate_email() and validation.validate_login() and validation.validate_password()) else "error"
        print(user)
    else:
        validation_out = 'Введите данные для регистрации'
        print(user)
    return render_template('register.html', validation_out = validation_out)

if __name__ == '__main__':
    app.run()