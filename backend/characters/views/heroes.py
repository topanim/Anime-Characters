from random import shuffle

from django.core import serializers
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from characters.utils.responses import Body, Status
from characters.forms.HeroForm import HeroForm
from characters.models_dir import HeroModel, AnimeModel


@csrf_exempt
def create_hero(request):
    if request.method == 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    body = request.POST
    files = request.FILES

    form = HeroForm(body, files)

    if not form.is_valid():
        return JsonResponse(
            data=Body.INVALID_FORM_BODY,
            status=Status.INVALID
        )

    form.save(commit=True)

    return JsonResponse(
        data=Body.CREATED,
        status=Status.OK
    )


@csrf_exempt
def get_heroes(request):
    if request.method != 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    body = request.GET
    page = body.get('page')
    q = body.get('q')

    if not page:
        page = 1

    if q:
        heroes = HeroModel.objects.filter(name__contains=q)
    else:
        heroes = list(HeroModel.objects.all())
        shuffle(heroes)

    paginator = Paginator(heroes, 9)

    data = paginator.get_page(page)
    data_json = serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


@csrf_exempt
def get_hero(request, id):
    if request.method != 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    data = HeroModel.objects.filter(pk=id).first()

    if not data:
        return JsonResponse(
            data=Body.NOT_FOUND,
            status=Status.NOT_FOUND
        )
    data_json = serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


@csrf_exempt
def delete_all_heroes(request):
    if request.method != 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    HeroModel.objects.all().delete()

    return JsonResponse(
        data=Body.DELETED,
        status=Status.DELETED
    )


@csrf_exempt
def get_hero_image_url(request, id):
    if request.method != 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    hero = HeroModel.objects.filter(pk=id).first()
    if not hero:
        return JsonResponse(
            data=Body.NOT_FOUND,
            status=Status.NOT_FOUND
        )

    return JsonResponse(
        data={
            'url': hero.image.url
        },
        status=Status.OK
    )
