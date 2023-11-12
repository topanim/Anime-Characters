from random import shuffle

from django.core import serializers
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, Http404

from characters.dataclasses.responses import Body, Status
from characters.forms.HeroForm import HeroForm
from characters.models_dir import HeroModel, AnimeModel


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


def get_hero(request, id):
    if request.method != 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    data = HeroModel.objects.filter(pk=id)

    if not data.first():
        return JsonResponse(
            data=Body.NOT_FOUND,
            status=Status.NOT_FOUND
        )
    data_json = serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')
