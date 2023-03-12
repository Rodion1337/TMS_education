from django.forms import *

class LoginForm(Form):                                              #создание заполняемых полей при регистрации
    username = CharField()
    password = CharField(widget=PasswordInput)