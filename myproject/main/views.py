from datetime import datetime
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .forms import GameForm
from .models import Game
from main.utils import categorias, search_games, ensure_sample_games
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
    from django.db.models.query import QuerySet
    
    q = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    # Se o banco estiver vazio, popula alguns jogos de exemplo para pesquisa
    ensure_sample_games()

    # Todos os jogos da biblioteca (filtrados por categoria se selecionada)
    all_games_qs = Game.objects.all()
    if category:
        all_games_qs = all_games_qs.filter(genre__iexact=category)

    # lista de nomes para passar ao search_games
    nomes_jogos = list(all_games_qs.values_list('title', flat=True))

    # Se há pesquisa, aplica search_games; senão, mostra todos
    if q:
        matches = search_games(q, nomes_jogos)
        games_list = []
        for title in matches:
            obj = all_games_qs.filter(title__iexact=title).first()
            if obj:
                games_list.append(obj)
        games = games_list
    else:
        games = all_games_qs

    results_count = games.count() if isinstance(games, QuerySet) else len(games)

    categories = categorias

    return render(request, 'search.html', {
        'all_games': all_games_qs,
        'games': games,
        'query': q,
        'categories': categories,
        'selected_category': category,
        'results_count': results_count,
    })