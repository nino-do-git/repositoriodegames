# 🎮 Pygame Showcase (Django)

Uma plataforma completa para armazenar, exibir e divulgar jogos digitais desenvolvidos com Python e Pygame, construída com Django.

---

## ✨ Funcionalidades

- Vitrine de Jogos com destaque  
- Página de detalhes com screenshots, instruções e download  
- Filtro de jogos por categoria/gênero  
- Submissão de jogos com upload de arquivos e thumbnail  
- Link para código-fonte e versões de Python/Pygame do jogo  
- Contador de downloads  
- Exclusão de jogos diretamente pela interface  
- Painel administrativo com Django Admin  
- Interface moderna estilo dark  

---

## 🏗️ Arquitetura

REPOSITORIODEGAMES/

venv/

myproject/
  main/
    migrations/
    static/
      main/
        css/
          index.css
          game.css
          game_detail.css
          create_game.css
        icons/
          favicon.svg
        js/
          game-modal.js
    admin.py
    apps.py
    forms.py
    models.py
    urls.py
    utils.py
    views.py

  myproject/
    settings.py
    urls.py
    asgi.py
    wsgi.py

  templates/
    index.html
    game.html
    game_detail.html
    create_game.html

  media/
    downloads/
    imagens/
    thumbnails/

  db.sqlite3
  manage.py

requirements.txt
README.md

---

## 🔗 Rotas

/             → Lista de jogos (biblioteca)  
/add/         → Adicionar novo jogo  
/<slug>/      → Detalhes do jogo  
/<slug>/delete/   → Excluir jogo  
/<slug>/download/ → Download do arquivo do jogo  

---

## 🚀 Como Executar

1. Criar ambiente virtual

python -m venv venv

Linux/Mac:
source venv/bin/activate

Windows:
venv\Scripts\activate

---

2. Instalar dependências

pip install -r requirements.txt

---

3. Aplicar migrações

python manage.py migrate

---

4. Criar usuário admin

python manage.py createsuperuser

---

5. Rodar o servidor

python manage.py runserver

Acesse:

http://127.0.0.1:8000  
http://127.0.0.1:8000/admin  

---

## 📋 Como Usar

Explorar Jogos:
- Veja jogos na página inicial
- Use os botões de categoria para filtrar

Detalhes:
- Clique em um jogo
- Veja descrição, instruções, screenshots e faça download

Submissão:
- Acesse /add/ para cadastrar um jogo
- Informe título, descrição, desenvolvedor, gênero, plataforma
- Faça upload de thumbnail, screenshots e arquivo de download
- Gerencie via admin em /admin/

---

## 🔧 Tecnologias Utilizadas

Backend:
- Python 3.10+
- Django 5.2
- SQLite

Frontend:
- Django Templates
- HTML/CSS (por página)
- JavaScript (modal de imagens)

---

## 📂 Uploads

/media/
  downloads/
  imagens/
  thumbnails/

Configuração no settings.py:

MEDIA_URL = '/media/'  
MEDIA_ROOT = BASE_DIR / 'media'  

---

## 📝 Notas

- SQLite usado por padrão  
- Em produção:
  - Usar PostgreSQL  
  - DEBUG = False  
  - Configurar armazenamento (S3, etc)  

---

## 🎯 Roadmap Futuro

- Sistema de login  
- Comentários e avaliações  
- Favoritos  
- Tags  
- API REST  
- Rodar jogos no navegador  

---

Feito com 💜 para a comunidade Python e Pygame!
