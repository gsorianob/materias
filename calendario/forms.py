# -*- coding: utf-8 -*-
from django import forms


class SetupForm(forms.Form):
    semanas = forms.IntegerField(min_value=1, max_value=40, required=True, label="Semanas")
    clases = forms.IntegerField(min_value=1, max_value=5, required=True, label="Clases por semana")
    # mostrar días
    # elegir la fecha de la primer clase

