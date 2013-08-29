# encoding: utf-8
# from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response
import itertools
from calendario.forms import SetupForm


# @login_required
def setup(request):
    form = SetupForm(initial={'semanas': 16, 'fecha_de_inicio': datetime.today()})
    c = {'form': form}
    c.update(csrf(request))
    return render_to_response('setup.html', c)


def agregar_dia_si_es_verdadero(lista, numero_de_dia, agregar):
    if agregar:
        lista.append(numero_de_dia)


def agrupar_clases_por_semana(clases, cantidad):
    clases_de_la_semana = tuple(itertools.islice(clases, cantidad))
    while clases_de_la_semana:
        yield clases_de_la_semana
        clases_de_la_semana = tuple(itertools.islice(clases, cantidad))


# @login_required
def create(request):
    if request.method == "POST":
        form = SetupForm(request.POST)
        if form.is_valid():
            semanas = form.cleaned_data['semanas']
            fecha_de_inicio = form.cleaned_data['fecha_de_inicio']
            lunes_de_esa_semana = fecha_de_inicio + timedelta(days=-fecha_de_inicio.weekday())

            dias_de_clase = []
            agregar_dia_si_es_verdadero(dias_de_clase, 0, form.cleaned_data['lunes'])
            agregar_dia_si_es_verdadero(dias_de_clase, 1, form.cleaned_data['martes'])
            agregar_dia_si_es_verdadero(dias_de_clase, 2, form.cleaned_data['miercoles'])
            agregar_dia_si_es_verdadero(dias_de_clase, 3, form.cleaned_data['jueves'])
            agregar_dia_si_es_verdadero(dias_de_clase, 4, form.cleaned_data['viernes'])
            agregar_dia_si_es_verdadero(dias_de_clase, 5, form.cleaned_data['sabado'])

            clases = (lunes_de_esa_semana + timedelta(s*7+d) for s in xrange(semanas) for d in dias_de_clase)
            clases_por_semana = len(dias_de_clase)
            clases = agrupar_clases_por_semana(clases, clases_por_semana)

            return render_to_response('create.html', {'clases': clases, 'clases_por_semana': clases_por_semana})
        else:
            c = {'form': form}
            c.update(csrf(request))
            return render_to_response('setup.html', c)
    else:
        raise Http404
