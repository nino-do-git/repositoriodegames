# 🎮 Pygame Showcase (Django)

Uma plataforma completa para armazenar, exibir e divulgar jogos digitais desenvolvidos com Python e Pygame, construída com Django.

---

## ✨ Funcionalidades

- Vitrine de Jogos com destaque  
- Página de detalhes com screenshots e download  
- Busca por nome ou gênero  
- Submissão de jogos com upload de arquivos  
- Contador de downloads  
- Painel administrativo com Django Admin  
- Interface moderna estilo dark  

---

## 🏗️ Arquitetura

REPOSITORIODEGAMES/

.venv/

myproject/
  main/
    migrations/
    models.py
    views.py
    admin.py
    apps.py
    urls.py

  myproject/
    settings.py
    urls.py
    asgi.py
    wsgi.py

  templates/
  static/
  media/

db.sqlite3  
manage.py  
requirements.txt  

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
- Use filtros para buscar

Detalhes:
- Clique em um jogo
- Veja descrição e download

Submissão:
- Envie título, descrição e arquivos
- Gerencie via admin

---

## 🔧 Tecnologias Utilizadas

Backend:
- Python 3.10+
- Django 4+
- SQLite

Frontend:
- Django Templates
- HTML/CSS

---

## 📂 Uploads

/media/
  games/
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