from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'title',
            'short_description',
            'description',
            'developer',
            'genre',
            'platform',
            'python_version',
            'pygame_version',
            'thumbnail',
            'screenshots',
            'download_file',
            'download_url',
            'source_code_url',
            'instructions',
            'featured',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'instructions': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
