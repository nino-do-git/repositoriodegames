from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_page, name='game'),
    path('add/', views.add_game, name='add_game'),
]
