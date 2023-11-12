from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views.test import test
from .views.auth import sign_up, login

urlpatterns = [
    path('test/', test),
    path('auth/register', csrf_exempt(sign_up)),
    path('auth/login', csrf_exempt(login)),
]