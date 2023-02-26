from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'HW23'
urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game_views, name = 'games'),
    path('game/<slug:game_slug>', views.game_views, name = 'game_views'),
    path('category/', views.category_views, name = 'categories'),
    path('category/<str:category>', views.category_views, name = 'categories'),
    
]
