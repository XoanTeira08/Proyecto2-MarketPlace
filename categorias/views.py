from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Categoria
from django.views import generic

# Create your views here.
class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = 'categories.html'
    context_object_name = 'categorias'

class CategoriaDetailView(generic.DetailView):
    model = Categoria
    template_name = 'categoryDetail.html'
    context_object_name = 'categoria'

class CategoriaCreateView(generic.CreateView):
    model = Categoria
    template_name = 'categoryCreate.html'
    fields = ['nombre', 'descripcion']

    def form_valid(self, form):
        categoria = form.save(commit=False)
        categoria.save()
        messages.success(self.request, 'Categoria creada con exito')
        return redirect('categorias')

class CategoriaUpdateView(generic.UpdateView):
    model = Categoria
    template_name = 'categoryUpdate.html'
    fields = ['nombre', 'descripcion']

    def form_valid(self, form):
        categoria = form.save(commit=False)
        categoria.save()
        messages.success(self.request, 'Categoria actualizada con exito')
        return redirect('categorias')

class CategoriaDeleteView(generic.DeleteView):
    model = Categoria
    template_name = 'categoryDelete.html'
    context_object_name = 'categoria'
    success_url = '/categorias/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Categoria eliminada con exito')
        return super(CategoriaDeleteView, self).delete(request, *args, **kwargs)
