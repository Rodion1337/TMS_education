from .views import *
from django.urls import path

urlpatterns = [
    path('games/', api_games),
    path('games2/', GetGameInfoView.as_view()),
    path('comments/', api_comments),
    path('category/', api_categories),
]
