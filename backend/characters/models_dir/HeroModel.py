from django.db import models

from characters.models_dir.AnimeModel import AnimeModel
from characters.models_dir.UserModel import UserModel


class HeroModel(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='heroes/images/')
    anime = models.ForeignKey(AnimeModel, on_delete=models.CASCADE)
    liked_by_users = models.ManyToManyField(UserModel, related_name='liked_heroes')

    class Meta:
        app_label = 'characters'
