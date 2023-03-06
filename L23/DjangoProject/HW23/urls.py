from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'HW23'
urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game_views, name = 'games'),
    path('game/<slug:game_slug>', views.game_detail, name = 'game_views'),
    path('category/', views.category_views, name = 'categories'),
    path('category/<str:category>', views.category_views, name = 'categories'),
    path('game/<slug:game_slug>/comment', views.CommentCreateView.as_view(), name='comment-add'),
    path('game/<int:comment_id>/comment_upd', views.CommentUpdateView.as_view(), name='comment-upd'),
    path('game/<int:comment_id>/comment_del', views.CommentDeleteView.as_view(), name='comment-del'),
]
