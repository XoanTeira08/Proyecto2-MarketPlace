from django.urls import path, include   
from . import views

app_name="products"

urlpatterns = [
    path('crearProducto/<slug:slug>/', views.ProductCreateView.as_view(), name="productCreate"),
    path('detalleProducto/<slug:slug>/', views.ProductDetailView.as_view(), name="productDetail"),
    path('crearResena/<str:nombre_producto>/', views.reviewCreateView.as_view(), name="reviewCreate"),
    path('<slug:categoria_slug>/', views.ProductListView.as_view(), name="productList"),
    path('editarProducto/<slug:slug>/', views.ProductUpdateView.as_view(), name="productUpdate"),
    path('eliminarProducto/<slug:slug>/', views.ProductDeleteView.as_view(), name="productDelete"),
    path('paypal/', include('paypal.standard.ipn.urls')),
]