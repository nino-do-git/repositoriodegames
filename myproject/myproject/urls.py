from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import add_game, delete_game, feature_game, game_detail, game_page, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('game/', game_page, name='game'),
    path('game/add/', add_game, name='add_game'),
    path('game/<slug:slug>/feature/', feature_game, name='feature_game'),
    path('game/<slug:slug>/delete/', delete_game, name='delete_game'),
    path('game/<slug:slug>/', game_detail, name='game_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
