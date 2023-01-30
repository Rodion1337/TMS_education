from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(requset):
    return HttpResponse('Hello world!')

def about(requset):
    return HttpResponse('Hello world!')