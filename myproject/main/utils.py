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

def search_games(pesquisa_input, nomes_jogos):
    valida_lis = []
    for i in nomes_jogos:
        if pesquisa_input.lower() in i.lower():
            valida_lis.append(i)
            
    for i in nomes_jogos:
        if SequenceMatcher(None, pesquisa_input.lower(), i.lower()).ratio() > 0.5 and i not in valida_lis:
            valida_lis.append(i)
            
    return valida_lis
