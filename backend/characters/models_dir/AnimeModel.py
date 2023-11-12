from django.db import models

from characters.models_dir.UserModel import UserModel


class AnimeModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    banner = models.ImageField(upload_to='anime/banners/')
    liked_by_users = models.ManyToManyField(UserModel, related_name='liked_anime')

    class Meta:
        app_label = 'characters'
