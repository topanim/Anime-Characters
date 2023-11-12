from django import forms

from characters.models_dir.AnimeModel import AnimeModel


class AnimeForm(forms.ModelForm):
    class Meta:
        model = AnimeModel
        fields = ('name', 'description', 'banner')
