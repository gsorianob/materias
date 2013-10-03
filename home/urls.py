# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('home',
    url(r'^$', TemplateView.as_view(template_name='index.html'),  name='index'),
)
