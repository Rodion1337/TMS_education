from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<slug:game_slug>', views.game_views, name = 'game_views'),
    path('category/<str:category>', views.category_views, name = 'categories')
]
