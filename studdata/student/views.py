
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request): # request - це посилання на клас HttpRequest, вона містить інформацыю про запити
    return HttpResponse("Сторінка додатку student.") # повертає HTML сторінку з її вмістом

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статї по категоріям</h1><p>id: {cat_id}</p>")  # повертає HTML сторінку з її вмістом

def categories_by_slug (request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статї по категоріям</h1><p>id: {cat_slug}</p>")

def archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h1>Арфів показав</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена</h1>")