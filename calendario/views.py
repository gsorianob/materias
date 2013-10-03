# encoding: utf-8
# from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response
import itertools
from calendario.forms import SetupForm


# @login_required
# def setup(request):
#     form = SetupForm(initial={'semanas': 16, 'fecha_de_inicio': datetime.today()})
#     c = {'form': form}
#     c.update(csrf(request))
#     return render_to_response('setup.html', c)


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
            # agrego los días de clase si los tildaron en el form.
            form.cleaned_data['lunes'] and dias_de_clase.append(0)
            form.cleaned_data['martes'] and dias_de_clase.append(1)
            form.cleaned_data['miercoles'] and dias_de_clase.append(2)
            form.cleaned_data['jueves'] and dias_de_clase.append(3)
            form.cleaned_data['viernes'] and dias_de_clase.append(4)
            form.cleaned_data['sabado'] and dias_de_clase.append(5)

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
