from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import anime, heroes
from .views.anime import create_anime, delete_all_anime, get_anime_all, get_anime
from .views.heroes import create_hero, get_heroes, get_hero
from .views.test import test
from .views.auth import sign_up, login

urlpatterns = [
    path('test/', test),
    path('auth/register', csrf_exempt(sign_up)),
    path('auth/login', csrf_exempt(login)),

    path('anime/create', csrf_exempt(create_anime)),
    path('anime/all', csrf_exempt(get_anime_all)),
    path('anime/<int:id>', csrf_exempt(get_anime)),

    path('hero/create', csrf_exempt(create_hero)),
    path('hero/all', csrf_exempt(get_heroes)),
    path('hero/<int:id>', csrf_exempt(get_hero)),

    path('delete_all/anime/', csrf_exempt(delete_all_anime))
]