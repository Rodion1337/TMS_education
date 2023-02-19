from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bd

# Create your views here.

lol = 'пусто'

def index(request):
    return HttpResponse(f'hello world {lol}')

def lol_views(request, lol):
    return HttpResponse(f'hello world {lol}')

def render_bboard(request):
    template = loader.get_template('index.html')
    bbs = Bd.objects.order_by('-publisher')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))