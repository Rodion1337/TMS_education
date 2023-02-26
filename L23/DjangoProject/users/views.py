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


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


def register(request):
    """
    Представлении регистрации
    """
    if request.method == 'POST':                                        #получение тип запрос с фронта + проверка
        form = UserCreationForm(request.POST)                           #??? для чего UserCreationForm
        if form.is_valid():                                             #проверка чего-то...
            form.save()                                                 #что-то сохранилось но не понятно что и куда
            username = form.cleaned_data.get('username')                #???
            messages.success(request, f'Создан аккаунт {username}!')    #сообщение юзеру что он красавчик
            return redirect(reverse('index'))                      #возврат на исходную точку
    else:
        form = UserCreationForm()                                       #
    return render(request, 'users/register.html', {'form': form})       


def login_view(request):
    """
    Представление входа в аккаунт,так же перенаправление.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        next_url = request.POST.get('next') # необходимо для перенаправление на ресурс
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
    """
    Представление разлогирования
    """
    logout(request)
    return redirect('shop:index')