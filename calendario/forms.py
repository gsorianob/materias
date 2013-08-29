# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import DateField, DateInput


class DateFieldWithCalendar(DateField):
    input_formats = ['%d-%m-%Y', '%d/%m/%Y']
    widget = DateInput(attrs={'class': 'datepicker'}, format='%d-%m-%Y')


class SetupForm(forms.Form):
    semanas = forms.IntegerField(min_value=1, max_value=40, required=True, label="Semanas",
                                 validators=[MinValueValidator(1), MaxValueValidator(40)])
    fecha_de_inicio = DateFieldWithCalendar(label="Fecha de inicio", required=True)
    lunes = forms.BooleanField(label="Lunes", required=False)
    martes = forms.BooleanField(label="Martes", required=False)
    miercoles = forms.BooleanField(label="Miércoles", required=False)
    jueves = forms.BooleanField(label="Jueves", required=False)
    viernes = forms.BooleanField(label="Viernes", required=False)
    sabado = forms.BooleanField(label="Sábado", required=False)

