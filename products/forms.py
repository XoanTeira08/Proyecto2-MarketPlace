from django import forms
from django.forms import ModelForm
from .models import Product, Reviews
from categorias.models import Categoria

class ProductsForm(ModelForm):
    model= Product
    fields= ['name', 'description', 'price', 'category', 'imagen']
    labels= {
        'name': 'Nombre del producto',
        'description': 'Descripcion del producto',
        'price': 'Precio del producto',
        'category': 'Categoria del producto',
        'imagen': 'Imagen del producto',
    }
    widgets= {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'price': forms.NumberInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'imagen': forms.FileInput(attrs={'class': 'form-control'}),
    }

class ReviewForm(ModelForm):
    class Meta:
        model= Reviews
        fields= ['review', 'score']

    
    labels= {
        'review': 'Escribe tu reseña',
        'score': 'Calificacion',
    }


    widgets= {
        'review': forms.Textarea(attrs={'class': 'form-control'}),
        'score': forms.IntegerField( widget=forms.NumberInput( attrs={'min': 1, 'max': 5})),
    }