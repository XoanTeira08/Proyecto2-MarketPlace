from django import forms
from django.forms import ModelForm
from .models import Shop,ReviewShop

class ShopForm(ModelForm):
    class Meta:
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
    
class ReviewShopForm(ModelForm):
    class Meta:
        model= ReviewShop
        fields= ['review', 'score']

    
    labels= {
        'review': 'Escribe tu reseña',
        'score': 'Calificacion',
    }


    widgets= {
        'review': forms.Textarea(attrs={'class': 'form-control'}),
        'score': forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 5})),
    }