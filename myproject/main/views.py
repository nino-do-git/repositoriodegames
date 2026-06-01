from datetime import datetime
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .forms import GameForm
from .models import Game
import os
import uuid

def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})

def game_page(request):
    games = Game.objects.all()
    return render(request, 'game.html', {'games': games})


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.slug = slugify(game.title)
            now = datetime.now()
            game.created_at = now
            game.updated_at = now
            game.save()
            return redirect('game')
    else:
        form = GameForm()

    return render(request, 'create_game.html', {'form': form})