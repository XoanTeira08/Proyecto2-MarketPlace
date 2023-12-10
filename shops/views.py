from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from .models import Shop, ReviewShop
from .forms import ShopForm, ReviewShopForm
from django.db import models
# Create your views here.
class ShopListView(generic.ListView):
    model = Shop
    template_name = 'shopList.html'
    context_object_name = 'shops'

    def get_queryset(self):
        return Shop.objects.all()
class ShopCreateView(generic.CreateView):
    model = Shop
    template_name = 'shopCreate.html'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop = self.object  
        reviews = ReviewShop.objects.filter(shop=shop) 
        context['reviewShop'] = reviews
        return context
    
class reviewShopCreateView(generic.CreateView):
    model = ReviewShop
    template_name = 'reviewShop.html'
    form_class = ReviewShopForm

    def get_context_data(self, **kwargs):
        context = super(reviewShopCreateView, self).get_context_data(**kwargs)
        context['shop'] = Shop.objects.get(slug=self.kwargs['nombre_tienda'])
        return context
    
    def form_valid(self, form):
        form.instance.user= self.request.user
        form.instance.shop= Shop.objects.get(slug=self.kwargs['nombre_tienda'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('main:home')

class reviewShopListView(generic.ListView):
    model = ReviewShop
    template_name = 'shopDetail.html'
    context_object_name = 'reviewShop'

class ShopAdminView(generic.DetailView):
    model = Shop
    template_name = 'shopAdmin.html'
    context_object_name = 'shop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop = self.object  
        reviews = ReviewShop.objects.filter(shop=shop) 
        context['reviewShop'] = reviews
        return context
    