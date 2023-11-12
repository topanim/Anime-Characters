from django.http import HttpResponse, JsonResponse

from characters.models_dir import AnimeModel
from characters.models_dir.UserModel import UserModel
from characters.dataclasses.responses import Body, Status


def test(request):

    for i in AnimeModel.objects.all():
        print(AnimeModel.name)
        print(AnimeModel.description)
        print(AnimeModel.banner)

    return JsonResponse(
            data=Body.USER_ALREADY_EXISTS,
            status=Status.CONFLICT
        )

