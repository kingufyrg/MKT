from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template


def hola(request):
    return HttpResponse("Hola Mundo")


def raiz(request):
    return HttpResponse("Hola Mundo")


def fecha_actual(request):
    # ahora = datetime.datetime.now()
    # html = "<html><body><h1>Fecha:</h1><h3>%s<h/3></body></html>" % ahora
    # return HttpResponse(html)
    # ahora = datetime.datetime.now()
    # t = Template("<html><body>Hoy es {{ fecha_actual }}.</body></html>")
    # html = t.render(Context({'fecha_actual': ahora}))
    # return HttpResponse(html)
    ahora = datetime.datetime.now()
    return render(request, 'templates_test/fecha_actual.html', {'fecha_actual': ahora})


def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=horas)
    return render(request, 'templates_test/horas_adelante.html', {'hora_siguiente': dt, 'horas': horas})

