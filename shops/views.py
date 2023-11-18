from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from .models import Shop
from .forms import ShopForm
# Create your views here.

class ShopCreateView(generic.CreateView):
    model = Shop
    template_name = 'shopCreate.html'
    fields = ['name', 'imagen']
    form_class = ShopForm
    
    def form_valid(self, form):
        shop = form.save(commit=False)
        shop.user = self.request.user
        shop.save()
        messages.success(self.request, 'Tienda agregada con exito')
        return super().form_valid(form)
    
    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('main:home')

class ShopDetailView(generic.DetailView):
    model = Shop
    template_name = 'shopDetail.html'
    context_object_name = 'shop'
