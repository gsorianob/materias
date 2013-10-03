# encoding: utf-8
from django.db import models
from django.utils.translation import ugettext as _


# class Subject(models.Model):
#     name = models.CharField(max_length=50, null=False, blank=False, unique=True, verbose_name=_('Name'))
#     description = models.TextField(blank=True, verbose_name=_('Description'))
#
#
# class ClassDay(models.Model):
#     date = models.DateField(null=True, default=None, verbose_name=_('Date'))
#     subjects = models.ManyToManyField(Subject, blank=True, verbose_name=_('Subjects'))
#
#
