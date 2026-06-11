from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_page, name='game'),
    path('add/', views.add_game, name='add_game'),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
    path('<slug:slug>/delete/', views.delete_game, name='delete_game'),
]
