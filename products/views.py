from django.shortcuts import render
from .models import Product
from categorias.models import Categoria
from django.views import generic

# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        categoria_slug = self.kwargs['categoria_slug']
        categoria = Categoria.objects.get(slug=categoria_slug)
        return Product.objects.filter(categoria=categoria)

