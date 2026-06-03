from datetime import datetime
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .forms import GameForm
from .models import Game
from main.utils import categorias
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

def search(request):
    from django.db.models import Q

    q = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    games = Game.objects.all()
    if q:
        games = games.filter(title__icontains=q)
    if category:
        games = games.filter(genre__iexact=category)

    categories = categorias

    return render(request, 'search.html', {
        'games': games,
        'query': q,
        'categories': categories,
        'selected_category': category,
    })