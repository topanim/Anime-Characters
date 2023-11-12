from django import forms

from characters.models_dir.HeroModel import HeroModel


class HeroForm(forms.ModelForm):
    class Meta:
        model = HeroModel
        fields = ('name', 'image', 'anime')
