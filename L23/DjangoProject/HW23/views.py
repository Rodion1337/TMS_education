from django.shortcuts import render
from .models import games, categories
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request: HttpRequest):
    sorted_game = request.GET.get('sort', 'None')
    sorted_order = {
        'None': games.objects.all(),
        'price': games.objects.order_by('price'),
        'name': games.objects.order_by('name'),
    }
    games_sorted = sorted_order.get(sorted_game).all()
    categories_sorted = list(categories.objects.all())
    return render(request, 'index.html', context={'games': games_sorted, "categories": categories_sorted})

def game_views(request, game_slug = None):
    if game_slug != None:
        game_view = games.objects.get(slug = game_slug)
        return render(request, 'game.html', context={'game': game_view,})
    else:
        games_view = games.objects.all()
        return render(request, 'games.html', context={'games' : games_view,})

def category_views(request, category = None):
    if category != None:
        category = categories.objects.get(title = category)   
        games_view = games.objects.filter(category = category.id)
        return render(request, 'games.html', context={'games' : games_view,})
    else:
        games_view = games.objects.all()
        return render(request, 'games.html', context={'games' : games_view,})


