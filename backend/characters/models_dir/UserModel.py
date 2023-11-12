from django.db import models
from django.db.models.signals import pre_delete

# from characters.signals.delete import delete_user_icon


class UserModel(models.Model):
    username = models.CharField(max_length=15, unique=True, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=150, null=False)
    icon = models.ImageField(upload_to='users/icons/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'characters'


# pre_delete.connect(delete_user_icon, UserModel)
