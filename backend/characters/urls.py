from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import anime, heroes
from .views.anime import create_anime, delete_all_anime, get_anime_all, get_anime
from .views.heroes import create_hero, get_heroes, get_hero, delete_all_heroes, get_hero_image_url
from .views.test import test
from .views.auth import sign_up, login

urlpatterns = [
    path('test/', test),
    path('auth/register', sign_up),
    path('auth/login', login),

    path('anime/create', create_anime),
    path('anime/all', get_anime_all),
    path('anime/<int:id>', get_anime),
    path('anime/delete_all/', delete_all_anime),

    path('hero/create', create_hero),
    path('hero/all', get_heroes),
    path('hero/<int:id>', get_hero),
    path('hero/delete_all/', delete_all_heroes),
    path('hero/image/<int:id>', get_hero_image_url)
]