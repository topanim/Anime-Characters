from django.db import models
from django.db.models.signals import pre_delete

from characters.models_dir.AnimeModel import AnimeModel
from characters.models_dir.UserModel import UserModel
# from characters.signals.delete import delete_hero_image
from characters.validators.file_type import FileExtensionValidator


class HeroModel(models.Model):
    name = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to='heroes/images/', null=False, validators=[FileExtensionValidator(('png',))])
    anime = models.ForeignKey(AnimeModel, null=False, on_delete=models.CASCADE)

    top = models.CharField(max_length=4, null=False)
    top_color = models.CharField(max_length=7, null=False)
    bottom = models.CharField(max_length=4, null=False)
    bottom_color = models.CharField(max_length=7, null=False)

    liked_by_users = models.ManyToManyField(UserModel, related_name='liked_heroes')

    class Meta:
        app_label = 'characters'


# pre_delete.connect(delete_hero_image, HeroModel)
