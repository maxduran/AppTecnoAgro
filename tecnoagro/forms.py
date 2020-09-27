from django import forms
from django.forms import ModelForm
from .models import Consulta, Usuario


class Usuarioconsulta(ModelForm):
    class Meta:
        model = Consulta
        fields = ['nombre','email','mensaje']


class Usuarioform(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','email','telefono','direccion']