from django.db import models
from datetime import datetime


class Game(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    developer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    python_version = models.CharField(max_length=200)
    pygame_version = models.CharField(max_length=200)
    # thumbnail = ''
    # screenshots = ''
    # download_file = ''
    download_url = models.URLField(max_length=200)
    source_code_url = models.URLField(max_length=200)
    instructions = models.TextField(max_length=200)
    featured = models.CharField(max_length=200)
    download_count = models.CharField(max_length=200)
    created_at = models.DateTimeField(max_length=200)
    updated_at = models.DateTimeField(max_length=200)
