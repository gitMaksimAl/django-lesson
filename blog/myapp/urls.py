from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('game', views.game, name="game1"),
    path('game/2', views.game2, name="game2"),
    path('game/3', views.game3, name="game3"),
]
