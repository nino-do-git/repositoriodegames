from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .forms import GameForm
from .models import Game
from difflib import SequenceMatcher
from main.utils import categorias, ensure_sample_games
import os
import uuid

def index(request):
    featured_games = Game.objects.filter(featured='sim')
    return render(request, 'index.html', {'featured_games': featured_games})

def game_page(request):
    jogos = Game.objects.all()
    pesquisa = ''

    # Lê a categoria ativa da querystring (?categoria=roguelike)
    categoria_ativa = request.GET.get('categoria', '')

    # Filtra o queryset pela categoria antes de aplicar a busca
    if categoria_ativa:
        jogos = jogos.filter(genre__iexact=categoria_ativa)

    if request.method == 'POST':
        pesquisa = request.POST.get('q', '')
        valida_lis = []
        for i in jogos:
            if pesquisa.lower() in i.title.lower():
                valida_lis.append(i)
        for i in jogos:
            if SequenceMatcher(None, pesquisa.lower(), i.title.lower()).ratio() > 0.5 and i not in valida_lis:
                valida_lis.append(i)
        games = valida_lis
    else:
        games = list(jogos)

    # Prepara lista de (slug, label) para o template renderizar os botões
    categorias_display = [(c, c.replace('_', ' ').title()) for c in categorias]

    return render(request, 'game.html', {
        'games': games,
        'query': pesquisa,
        'categorias': categorias_display,
        'categoria_ativa': categoria_ativa,
    })

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game_detail.html', {'game': game})


def feature_game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        game.featured = 'sim'
        game.save()
        return redirect('game_detail', slug=slug)
    return redirect('game_detail', slug=slug)


def delete_game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        game.delete()
        return redirect('game')
    return redirect('game_detail', slug=slug)


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.slug = slugify(game.title)
            game.download_count = '0'
            now = datetime.now()
            game.created_at = now
            game.updated_at = now
            game.save()
            return redirect('game')
    else:
        form = GameForm()

    return render(request, 'create_game.html', {'form': form})
