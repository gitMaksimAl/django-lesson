from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('about/', views.about, name="about"),
    path('game/statistic', views.game_statistic, name="game1_stats"),
    path('game/', views.choice_game, name="game"),
    path('authors/', views.all_authors_names, name="all_authors"),
    path('posts/<int:pk>', views.get_post, name="post"),
    path('authors/new/', views.add_author, name="new_author"),
    path('posts/new/', views.add_post, name="new_post"),
]
