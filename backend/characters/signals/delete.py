from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

from characters.models_dir.HeroModel import HeroModel
from characters.models_dir.UserModel import UserModel
from characters.models_dir.AnimeModel import AnimeModel


@receiver(pre_delete, sender=AnimeModel)
def delete_anime_banner(instance, **kwargs):
    banner = instance.banner
    banner.delete()


@receiver(pre_delete, sender=UserModel)
def delete_user_icon(instance, **kwargs):
    icon = instance.icon
    icon.delete()


@receiver(pre_delete, sender=HeroModel)
def delete_hero_image(instance, **kwargs):
    image = instance.image
    image.delete()
