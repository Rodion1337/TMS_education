from django.shortcuts import render
from requests import request, get
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@require_http_methods(["GET", "POST"])
def kanye_west(request):
    number_quote = int(request.GET.get('number', 1)) #получение данных по ключу
    if number_quote < 1: #валидация входных
        number_quote = 1
    quotes = set([get('https://api.kanye.rest').json()['quote'] for i in range(number_quote)]) #генерация списка цитат с очисткой от повторов
    print('quote lol')
    print(quotes)
    print (number_quote)
    return render(request, 'kanye_west.html', {'quote' : quotes})

def index(request):
    return HttpResponse(r'hello world')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def factorial(request):
    try:
        number_factorial = abs(int(request.GET.get('number', 1))) #получение данных по ключу
    except Exception:
        number_factorial = 1
        
    factorial = 1
    for i in range(1, number_factorial + 1):
        factorial *= i
    
    # return render(request, 'factorial.html', {'factorial' : factorial, 'number_factorial':number_factorial })

    if request.method == 'GET':
        back = json.dumps({"number": number_factorial, "factorial": factorial})
        return HttpResponse(back)
    if request.method =='POST':
        return HttpResponse(r'you need use GET')