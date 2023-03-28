from django.shortcuts import render, get_object_or_404
from .models import Games, Categories, Comments, User
from django.http import HttpResponse, HttpRequest
from .forms_app import UserCommentForm, GuestCommentForm
from django.db.models import Avg
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from requests import request
from datetime import datetime, timedelta
from json import dumps, loads
from django.core.serializers import serialize
from .tasks import logger_task

# Create your views here.
def index(request: HttpRequest):
    logger_task.delay(str(f'{request.user} | {request.path}'))
    sorted_game = request.GET.get('sort', 'None')
    sorted_order = {
        'None': Games.objects.all(),
        'price': Games.objects.order_by('price'),
        'name': Games.objects.order_by('name'),
    }
    games_sorted = sorted_order.get(sorted_game).all()
    categories_sorted = list(Categories.objects.all())
    return render(request, 'index.html', context={'games': games_sorted, "categories": categories_sorted})


def game_views(request):
    sorted_game = request.GET.get('sort', 'None')
    sorted_order = {
        'None': Games.objects.all(),
        'price': Games.objects.order_by('price'),
        'name': Games.objects.order_by('name'),
    }
    games_view = sorted_order.get(sorted_game)
    logger_task.delay(str(f'{request.user} | {request.path}'))
    return render(request, 'games.html', context={'games' : games_view,})

def category_views(request, category = None):
    
    sorted_game = request.GET.get('sort', 'None')
    sorted_order = {
        'None': Games.objects.all(),
        'price': Games.objects.order_by('price'),
        'name': Games.objects.order_by('name'),
    }
    logger_task.delay(str(f'{request.user} | {request.path} | ?sort={sorted_game} |')
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
    logger_task.delay(str(f'{request.user} | {request.path}'))
    if request.COOKIES.get(game_slug):
        cookie = loads(request.COOKIES.get(game_slug))
        cookie = loads(request.COOKIES.get(game_slug))
        last_visited = cookie['last_visited']
        amount_visited = cookie['amount_visited']
    else:
        last_visited = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        amount_visited = 1
    comment_all = Comments.objects.order_by('create_date').filter(game_id = game_odj.id, is_active = True)
    comment_user = comment_all.filter(author_id = user_id)
    comments_other = comment_all.exclude(author_id = user_id)
    context = {'game': game_odj, 'comments_other': comments_other, 'comment_user': comment_user,'last_visited':last_visited,'amount_visited':amount_visited}
    response = render(request, 'game.html', context)
    visit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    amount_visited += 1
    response.set_cookie(game_slug, value=dumps({'last_visited':visit_time, 'amount_visited':amount_visited}), max_age=timedelta(days=20))
    response.set_cookie(game_slug, value=dumps({'last_visited':visit_time, 'amount_visited':amount_visited}), max_age=timedelta(days=20))
    return response

class CommentCreateView(CreateView):
    model = Comments
    template_name = 'comment.html'
    form_class = UserCommentForm
    # success_url = reverse_lazy('HW23:games')
    
    
    
    def form_valid(self, form):
        from .tasks import censored_comment_form
        from .tasks import censored_comment_form
        form.instance.game = Games.objects.get(slug=self.kwargs['game_slug'])
        form.instance.author = self.request.user
        self.object = form.save()
        serialize_odj = serialize('json', [self.object])
        # print('serialize_odj', serialize_odj)
        censored_comment_form.delay(serialize_odj)
        self.object = form.save()
        serialize_odj = serialize('json', [self.object])
        # print('serialize_odj', serialize_odj)
        censored_comment_form.delay(serialize_odj)
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comments
    form_class = UserCommentForm 
    template_name = 'comment_upd.html'
    
class CommentDeleteView(DeleteView):
    model = Comments
    template_name = 'comment_del.html'
    success_url = reverse_lazy('HW23:games')