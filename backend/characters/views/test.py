from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from characters.models_dir import AnimeModel
from characters.models_dir.UserModel import UserModel
from characters.utils.responses import Body, Status


@csrf_exempt
def test(request):
    for i in AnimeModel.objects.all():
        print(AnimeModel.name)
        print(AnimeModel.description)
        print(AnimeModel.banner)

    return JsonResponse(
        data=Body.USER_ALREADY_EXISTS,
        status=Status.CONFLICT
    )
