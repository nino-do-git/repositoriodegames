from datetime import datetime
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .forms import GameForm
from .models import Game
from difflib import SequenceMatcher
from main.utils import categorias, ensure_sample_games
import os
import uuid

def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})

def game_page(request):
    jogos = Game.objects.all()
    pesquisa = ''
    valida_lis = []
    if request.method == 'POST':
        pesquisa = request.POST.get('q')
        
        for i in jogos:
            if pesquisa.lower() in i.title.lower():
                valida_lis.append(i)
                
        for i in jogos:
            if SequenceMatcher(None, pesquisa.lower(), i.title.lower()).ratio() > 0.5 and i not in valida_lis:
                valida_lis.append(i)
    
    return render(request, 'game.html', {'games': valida_lis}) 

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