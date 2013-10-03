# -*- coding: utf-8 -*-
from datetime import datetime
from django.conf.urls import patterns, url
from django.views.generic import FormView
from calendario.forms import SetupForm

urlpatterns = patterns('calendario',
   url(r'^$', FormView.as_view(template_name='setup.html', form_class=SetupForm, initial={'semanas': 16, 'fecha_de_inicio': datetime.today()}), name='setup'),
   url(r'^create/$', 'views.create',  name='create'),
)
