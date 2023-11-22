from django.contrib import admin
from .models import Product, Reviews, Cart, CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Reviews)
admin.site.register(Cart)
admin.site.register(CartItem)