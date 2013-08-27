# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('calendario',
   url(r'^$', 'views.setup',  name='setup'),
   url(r'^create/$', 'views.create',  name='create'),
)
