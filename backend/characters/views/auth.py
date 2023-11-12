import hashlib

from django.http import JsonResponse
from characters.dataclasses.responses import Body, Status
from characters.forms.UserForm import UserForm

from characters.models_dir.UserModel import UserModel


def sign_up(request):
    if request.method == 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    body = request.POST
    form = UserForm(body)

    if not form.is_valid():
        return JsonResponse(
            data=Body.INVALID_FORM_BODY,
            status=Status.INVALID
        )

    user = form.save(commit=False)

    if check_if_user_exists(user.email):
        return JsonResponse(
            data=Body.USER_ALREADY_EXISTS,
            status=Status.CONFLICT
        )

    user.password = make_password(user.password)
    user.save()

    return JsonResponse(
        data=add_user_data(Body.AUTHORIZED_TRUE, body),
        status=Status.OK
    )


def login(request):
    body = request.GET
    user = auth(body)

    if user:
        return JsonResponse(
            data=add_user_data(Body.AUTHORIZED_TRUE, body),
            status=Status.OK
        )
    else:
        return JsonResponse(
            data=Body.AUTHORIZED_FALSE,
            status=Status.BAD_REQUEST
        )


def check_if_user_exists(email) -> UserModel or None:
    try:
        user = UserModel.objects.get(email=email)
        return user
    except:
        return None


def auth(obj) -> bool:
    username = obj.get('username')
    password = obj.get('password')

    if not (username and password):
        return False

    password = make_password(password)
    user = UserModel.objects.filter(username=username).first()

    if user and password == user.password:
        return True
    return False


def make_password(password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password


def add_user_data(response, body):
    response['user'] = {
        'username': body.get('username'),
        'password': body.get('password')
    }

    return response
