from django.shortcuts import render
from .models import Games, Categories
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request: HttpRequest):
    sorted_game = request.GET.get('sort', 'None')
    sorted_order = {
        'None': Games.objects.all(),
        'price': Games.objects.order_by('price'),
        'name': Games.objects.order_by('name'),
    }
    games_sorted = sorted_order.get(sorted_game).all()
    categories_sorted = list(Categories.objects.all())
    return render(request, 'index.html', context={'games': games_sorted, "categories": categories_sorted})

def game_views(request, game_slug = None):
    if game_slug != None:
        game_view = Games.objects.get(slug = game_slug)
        return render(request, 'game.html', context={'game': game_view,})
    else:
        games_view = Games.objects.all()
        return render(request, 'games.html', context={'games' : games_view,})

def category_views(request, category = None):
    
    sorted_game = request.GET.get('sort', 'None')
    sorted_order = {
        'None': Games.objects.all(),
        'price': Games.objects.order_by('price'),
        'name': Games.objects.order_by('name'),
    }

    if category != None:
        games_view = sorted_order.get(sorted_game).filter(category = Categories.objects.get(title = category).id)
        return render(request, 'games.html', context={'games' : games_view,})
    else:
        games_view = sorted_order.get(sorted_game).all()
        return render(request, 'games.html', context={'games' : games_view,})



