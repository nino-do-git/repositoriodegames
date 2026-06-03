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
    short_description = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    developer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES)
    platform = models.CharField(max_length=200)
    python_version = models.CharField(max_length=200)
    pygame_version = models.CharField(max_length=200)
    
    thumbnail = models.ImageField(upload_to=name_changer_thumbnails, blank=True, null=True)
    screenshots = models.ImageField(upload_to=name_changer_imagens, blank=True, null=True)
    download_file = models.FileField(
    upload_to=name_changer_downloads,
    blank=True,
    null=True
    )
    
    download_url = models.URLField(max_length=200)
    source_code_url = models.URLField(max_length=200)
    instructions = models.TextField(max_length=200)
    featured = models.CharField(max_length=200)
    download_count = models.CharField(max_length=200)
    created_at = models.DateTimeField(max_length=200)
    updated_at = models.DateTimeField(max_length=200)
