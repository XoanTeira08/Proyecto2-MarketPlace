from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre de la categoria',
            'descripcion': 'Descripcion de la categoria',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }


