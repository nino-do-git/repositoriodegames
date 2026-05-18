from django.contrib import admin
from django.urls import path
from main.views import index, game_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('game/', game_page, name='game'),
]