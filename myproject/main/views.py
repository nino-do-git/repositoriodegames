from django.shortcuts import render
from .models import Game

def index(request):
    all_notes = Game.objects.all()
    return render(request, 'game.html', {'games': all_notes})