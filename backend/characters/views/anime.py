from random import shuffle

from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse

from characters.dataclasses.responses import Body, Status
from characters.forms.AnimeForm import AnimeForm
from characters.models_dir import AnimeModel


def create_anime(request):
    if request.method == 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    body = request.POST
    files = request.FILES

    form = AnimeForm(body, files)
    if form.is_valid():
        form.save(commit=True)

        return JsonResponse(
            data=Body.CREATED,
            status=Status.OK
        )

    return JsonResponse(
        data=Body.INVALID_FORM_BODY,
        status=Status.INVALID
    )


def get_anime_all(request):
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
        heroes = AnimeModel.objects.filter(name__contains=q)
    else:
        heroes = list(AnimeModel.objects.all())
        shuffle(heroes)

    paginator = Paginator(heroes, 9)

    data = paginator.get_page(page)
    data_json = serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def get_anime(request, id):
    if request.method != 'GET':
        return JsonResponse(
            data=Body.BAD_REQUEST,
            status=Status.BAD_REQUEST
        )

    data = AnimeModel.objects.filter(pk=id)

    if not data.first():
        return JsonResponse(
            data=Body.NOT_FOUND,
            status=Status.NOT_FOUND
        )

    data_json = serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')


def delete_all_anime(request):
    AnimeModel.objects.all().delete()
    return JsonResponse(
        data=Body.DELETED,
        status=Status.DELETED
    )
