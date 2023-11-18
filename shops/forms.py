from django import forms
from django.forms import ModelForm
from .models import Shop

class ShopForm(ModelForm):
    model= Shop
    fields= ['name', 'imagen']
    labels= {
        'name': 'Dale un nombre a la tienda',
        'imagen': 'Imagen del producto',
    }
    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }