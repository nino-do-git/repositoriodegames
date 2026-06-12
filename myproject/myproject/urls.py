from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from main.views import add_game, delete_game, download_game, edit_game, feature_game, game_detail, game_page, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    path('home/', index, name='index'),
    path('biblioteca/', game_page, name='game'),
    path('adicionarjogo/', add_game, name='add_game'),
    path('biblioteca/<slug:slug>/feature/', feature_game, name='feature_game'),
    path('biblioteca/<slug:slug>/delete/', delete_game, name='delete_game'),
    path('biblioteca/<slug:slug>/edit/', edit_game, name='edit_game'),
    path('biblioteca/<slug:slug>/download/', download_game, name='download_game'),
    path('biblioteca/<slug:slug>/', game_detail, name='game_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
