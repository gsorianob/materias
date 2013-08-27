# encoding: utf-8
# from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response
from calendario.forms import SetupForm


# @login_required
def setup(request):
    form = SetupForm(initial={'semanas':16, 'clases':2})
    c = {'form': form}
    c.update(csrf(request))
    return render_to_response('setup.html', c)


# @login_required
def create(request):
    if request.method == "POST":
        form = SetupForm(request.POST)
        if form.is_valid():
            return render_to_response('create.html', {'semanas': range(16), 'clases': range(2)})
        else:
            c = {'form': form}
            c.update(csrf(request))
            return render_to_response('setup.html', c)
    else:
        raise Http404
