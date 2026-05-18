from django.shortcuts import render
from .models import Game
from django.http import HttpResponse

def index(request):
    all_games = Game.objects.all()
    for game in all_games:
        print(game.title)
    return HttpResponse("Olá mundo! Este é o app notes de DevLife do Insper.")

def game_page(request):
    games = Game.objects.all()
    return render(request, 'game.html', {'games': games})