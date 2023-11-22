from django.shortcuts import render
from .models import Product, Reviews
from .forms import ReviewForm
from categorias.models import Categoria
from shops.models import Shop
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        categoria_slug = self.kwargs['categoria_slug']
        categoria = Categoria.objects.get(slug=categoria_slug)
        return Product.objects.filter(categoria=categoria)

class ProductCreateView(generic.CreateView):
    model = Product
    template_name = 'productCreate.html'
    fields = ['name', 'description', 'price', 'category', 'imagen', 'shop']

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        messages.success(self.request, 'Producto agregado con exito')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('categorias:categoryList')
    
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'productDetail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object  
        reviews = Reviews.objects.filter(product=product) 
        context['shop'] = self.object.shop
        context['reviews'] = reviews
        return context
    
   

class reviewCreateView(generic.CreateView):
    model = Reviews
    template_name = 'review.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super(reviewCreateView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['nombre_producto'])
        print(context['product'])
        return context
    
    def form_valid(self, form):
        form.instance.product= Product.objects.get(slug=self.kwargs['nombre_producto'])
        form.instance.user= self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('categorias:categoryList')

class reviewListView(generic.ListView):
    model = Reviews
    template_name = 'productDetail.html'
    context_object_name = 'reviews'

class ProductUpdateView (generic.UpdateView):
    model = Product
    template_name = 'productUpdate.html'
    fields = ['name', 'description', 'price', 'category', 'imagen']

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        messages.success(self.request, 'Producto editado con exito')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('categorias:categoryList')
    
class ProductDeleteView (generic.DeleteView):
    model = Product
    template_name = 'productDelete.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('categorias:categoryList')
    
def paypal(request):
    paypal_dict = {
        "business": "id@bussiness.example.com",
        "amount": "1.00",
        "currency_code": "USD",
        "item_name": "name of the item",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('payment_done')),
        "cancel_return": request.build_absolute_uri(reverse('payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, 'categories.html', context)

