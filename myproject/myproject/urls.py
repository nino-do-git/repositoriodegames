from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import add_game, game_page, index, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('game/', game_page, name='game'),
    path('game/add/', add_game, name='add_game'),
    path('search/', search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)