from django.urls import path
from .views import index, lol_views, render_bboard

urlpatterns = [
    path('', index),
    path('<int:lol>/', lol_views),
    path('render_bboard/', render_bboard)
]