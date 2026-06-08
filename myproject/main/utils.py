import os
import uuid
from difflib import SequenceMatcher

def name_changer_downloads(instance, filename):
    ext = os.path.splitext(filename)[1]
    unique_name = f"{uuid.uuid4().hex}{ext}"
    return os.path.join("downloads", unique_name)

def name_changer_thumbnails(instance, filename):
    ext = os.path.splitext(filename)[1]
    unique_name = f"{uuid.uuid4().hex}{ext}"
    return os.path.join("thumbnails", unique_name)

def name_changer_imagens(instance, filename):
    ext = os.path.splitext(filename)[1]
    unique_name = f"{uuid.uuid4().hex}{ext}"
    return os.path.join("imagens", unique_name)

categorias = [
    'plataforma',
    'arcade',
    'corrida',
    'luta',
    'tiro',
    'aventura',
    'rpg',
    'estrategia',
    'puzzle',
    'labirinto',
    'survival',
    'roguelike',
    'tower_defense',
    'simulacao',
    'esporte',
    'cartas',
    'tabuleiro',
    'quiz',
    'idle',
    'clicker',
    'ritmo',
    'stealth',
    'metroidvania',
    'hack_and_slash',
    'bullet_hell',
    'endless_runner',
    'snake',
    'breakout',
    'pong',
    'space_shooter'
]

def ensure_sample_games():
    """Cria alguns jogos de exemplo caso o banco esteja vazio."""
    from datetime import datetime
    from django.utils.text import slugify
    from .models import Game
    
    if Game.objects.count() == 0:
        now = datetime.now()
        samples = [
            {'title': 'Space Invaders', 'genre': 'arcade', 'platform': 'PC'},
            {'title': 'Super Platformer', 'genre': 'plataforma', 'platform': 'PC'},
            {'title': 'Racing Fury', 'genre': 'corrida', 'platform': 'PC'},
        ]
        for s in samples:
            Game.objects.create(
                title=s['title'],
                slug=slugify(s['title']),
                short_description=s['title'],
                description=s['title'],
                developer='Unknown',
                genre=s['genre'],
                platform=s['platform'],
                python_version='3.10',
                pygame_version='2.1',
                download_url='',
                source_code_url='',
                instructions='',
                featured='no',
                download_count='0',
                created_at=now,
                updated_at=now,
            )


def get_game_titles(category=None):
    from .models import Game
    
    qs = Game.objects.all()
    if category:
        qs = qs.filter(genre__iexact=category)
    return list(qs.values_list('title', flat=True))
