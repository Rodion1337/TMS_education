from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.views.decorators.cache import cache_page

app_name = 'HW23'
urlpatterns = [
    path('', views.index, name='index'),
    path('game/', cache_page(60, cache='caches_files')(views.game_views), name = 'games',),
    path('game/<slug:game_slug>', cache_page(20, cache='caches_files')(views.game_detail), name = 'game_views',),
    path('category/', cache_page(60*5, cache='caches_files')(views.category_views), name = 'categories',),
    path('category/<str:category>', cache_page(60*5, cache='caches_files')(views.category_views), name = 'categories',),
    path('game/<slug:game_slug>/comment', views.CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-upd',),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-del',),
]
