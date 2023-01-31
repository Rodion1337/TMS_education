from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, request
# from requests import request

# Create your views here.
def index(requset):
    print('index run')
    return render(request, 'index.html', {})

def about(requset):
    return HttpResponse('Hello world!')