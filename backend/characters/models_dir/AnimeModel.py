import os

from django.db import models
from django.db.models.signals import post_delete, pre_delete

from characters.models_dir.UserModel import UserModel
from characters.signals.delete import delete_anime_banner
from characters.validators.file_type import FileExtensionValidator


class AnimeModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    banner = models.ImageField(upload_to='anime/banners/', validators=[FileExtensionValidator(('png', 'jpg', 'jpeg'))])
    liked_by_users = models.ManyToManyField(UserModel, related_name='liked_anime')

    class Meta:
        app_label = 'characters'


pre_delete.connect(delete_anime_banner, AnimeModel)
