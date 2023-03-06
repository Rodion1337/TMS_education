from django.shortcuts import render, get_object_or_404
from .models import Games, Categories, Comments, User
from django.http import HttpResponse, HttpRequest
from .forms_app import UserCommentForm, GuestCommentForm
from django.db.models import Avg
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from requests import request

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

@login_required(login_url='users:login')
def game_detail(request, game_slug):
    game_odj = get_object_or_404(Games, slug = game_slug)
    user_id = request.user.id
    if Comments.objects.filter(game_id = game_odj.id, author_id = user_id).count == 1:
        comment_user = Comments.objects.filter(game_id = game_odj.id, author_id = user_id)[0]
    else:
        comment_user = []
    comments_other = Comments.objects.order_by('create_date').filter(game_id = game_odj.id, is_active = True).exclude(author_id = user_id)
    context = {'game': game_odj, 'comments_other': comments_other, 'comment_user': comment_user,}
    return render(request, 'game.html', context)

class CommentCreateView(CreateView):
    model = Comments
    template_name = 'comment.html'
    form_class = UserCommentForm
    # success_url = reverse_lazy('HW23:games')
    
    def form_valid(self, form):
        form.instance.game = Games.objects.get(slug=self.kwargs['game_slug'])
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comments
    form_class = UserCommentForm 
    template_name = 'comment.html'
    
class CommentDeleteView(DeleteView):
    model = Comments
    template_name = 'comment.html'
    success_url = reverse_lazy('HW23:games')