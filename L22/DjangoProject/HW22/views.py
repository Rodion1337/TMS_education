from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from requests import request

# Create your views here.
def skills(request):
    skills = {'soft_skills':{'общительность':'5',
                             'усидчивость':'5',
                             'самоорганизованность':'4',
                             'решение конфликтов':'5',
                             'работа в команде':'5',
                             'адаптируемость':'4'},
              'hard_skills':{'python':'4',
                             'flask':'3',
                             'Django':'3',
                             'Jinja2':'3',
                             'Excel':'4',
                             '1c':'5'}}
    return render(request, 'skills.html', context = skills)

def about(request):
    return HttpResponse('Hello world!')

def index(request):
    return HttpResponse('Hello world!')