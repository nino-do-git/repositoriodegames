from django.shortcuts import render
from .models import Game
from django.http import HttpResponse

def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})

def game_page(request):
    games = Game.objects.all()
    return render(request, 'game.html', {'games': games})