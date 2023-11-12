from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver


@receiver(pre_delete)
def delete_anime_banner(sender, instance, **kwargs):
    image = instance.banner
    image.delete()


@receiver(pre_delete)
def delete_user_icon(sender, instance, **kwargs):
    image = instance.icon
    image.delete()


@receiver(pre_delete)
def delete_hero_image(sender, instance, **kwargs):
    image = instance.image
    image.delete()
