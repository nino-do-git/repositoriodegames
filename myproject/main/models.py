from django.db import models
from datetime import datetime
from .utils import (
    categorias,
    name_changer_downloads,
    name_changer_imagens,
    name_changer_thumbnails,
)

GENRE_CHOICES = [
    (genre, genre.replace('_', ' ').title())
    for genre in categorias
]

class Game(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    short_description = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    developer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES)
    platform = models.CharField(max_length=200)
    python_version = models.CharField(max_length=200, blank=True)
    pygame_version = models.CharField(max_length=200, blank=True)

    thumbnail = models.ImageField(upload_to=name_changer_thumbnails, blank=True, null=True)
    screenshots = models.ImageField(upload_to=name_changer_imagens, blank=True, null=True)
    download_file = models.FileField(upload_to=name_changer_downloads, blank=True, null=True)

    download_url = models.URLField(max_length=200, blank=True)
    source_code_url = models.URLField(max_length=200, blank=True)
    instructions = models.TextField(blank=True)
    featured = models.CharField(max_length=200, blank=True, default='')
    download_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(max_length=200)
    updated_at = models.DateTimeField(max_length=200)
