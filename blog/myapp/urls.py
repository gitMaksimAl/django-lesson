from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('game', views.game, name="game1"),
    path('game/statistic', views.game_statistic, name="game1_stats"),
    path('game/2', views.game2, name="game2"),
    path('game/3', views.game3, name="game3"),
    path('authors', views.all_authors_names, name="all_authors"),
]
