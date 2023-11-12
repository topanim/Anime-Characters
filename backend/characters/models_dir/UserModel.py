from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=15, unique=True, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=150, null=False)
    icon = models.ImageField(upload_to='users/icons/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'characters'
