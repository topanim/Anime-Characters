from django.http import HttpResponse, JsonResponse
from characters.models_dir.UserModel import UserModel
from characters.dataclasses.responses import Body, Status


def test(request):

    UserModel.objects.all().delete()

    return JsonResponse(
            data=Body.USER_ALREADY_EXISTS,
            status=Status.CONFLICT
        )

