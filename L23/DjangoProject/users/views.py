from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse

# Create your views here.

from django.forms import *


class LoginForm(Form):                                              #создание заполняемых полей при регистрации
    username = CharField()
    password = CharField(widget=PasswordInput)


def register(request):
    if request.method == 'POST':                                    #проверка типа обращения
        form = UserCreationForm(request.POST)                       #получение данных
        if form.is_valid():                                         #проверка валидности
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect(reverse('HW23:index'))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':                                    #проверка типа обращения
        form = LoginForm(request.POST)                              #получение данных
        print(form)
        next_url = request.POST.get('next')
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(next_url)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('HW23:index')